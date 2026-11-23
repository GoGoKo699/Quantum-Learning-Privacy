#!/usr/bin/env python3
"""Deterministic finite checks for reference-secure private learning.

The frame average uses a finite exact second moment. The Werner check uses
Choi order to certify the analytical finite example, not sampled input states.
"""
from __future__ import annotations

import itertools
import json
import math

import numpy as np


ATOL = 2e-10
I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def rounded(value: float) -> float:
    return round(float(value), 9)


def swap(dimension: int) -> np.ndarray:
    permutation = np.arange(dimension**2).reshape(dimension, dimension).T.ravel()
    return np.eye(dimension**2)[permutation]


def apply_channel(kraus: np.ndarray, matrix: np.ndarray) -> np.ndarray:
    return sum(operator @ matrix @ operator.conj().T for operator in kraus)


def exact_frame_orbits(paulis: np.ndarray) -> list[tuple[float, np.ndarray]]:
    """An exact Pauli covariance twirl on two qubits.

    The local cycles and optional swap average each weight separately. CNOT
    sends 4 of 6 weight-one Paulis to weight two and 4 of 9 in the reverse
    direction. Using it with probability 9/10 makes either input weight map
    to the uniform output weight law (6/15, 9/15). A final uniform Pauli
    removes cross terms between different Pauli coordinates.
    """
    cycle = (I - 1j * (X + Y + Z)) / 2
    powers = (I, cycle, cycle @ cycle)
    local = [
        np.kron(left, right) for left, right in itertools.product(powers, repeat=2)
    ]
    axes = np.asarray([s @ u for s in (np.eye(4), swap(2)) for u in local])
    after = (paulis[:, None] @ axes[None, :]).reshape(-1, 4, 4)
    cnot = np.eye(4)[[0, 1, 3, 2]]
    return [
        (weight, (after[:, None] @ (gate @ axes)[None, :]).reshape(-1, 4, 4))
        for weight, gate in ((1 / 10, np.eye(4)), (9 / 10, cnot))
    ]


def damping_kraus() -> np.ndarray:
    """Four-level amplitude damping with three distinct decay probabilities."""
    losses = [0.26, 0.44, 0.14]
    coherent = np.diag(np.sqrt([1, *(1 - loss for loss in losses)]))
    jumps = []
    for level, loss in enumerate(losses, start=1):
        jump = np.zeros((4, 4))
        jump[0, level] = math.sqrt(loss)
        jumps.append(jump)
    return np.asarray([coherent, *jumps])


def pure_probe_outputs(kraus: np.ndarray, frames: np.ndarray) -> np.ndarray:
    rank = frames.shape[-1]
    vectors = np.einsum("koi,nir->nkor", kraus, frames)
    vectors = vectors.reshape(len(frames), len(kraus), -1)
    return np.einsum("nki,nkj->nij", vectors, vectors.conj()) / rank


def log_positive(matrix: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eigh(matrix)
    require(values.min() > 0, "nonpositive report in matrix logarithm")
    return (vectors * np.log(values)) @ vectors.conj().T


def check_twirl_and_reverse_divergence() -> dict:
    d = 4
    identity = np.eye(d)
    paulis = np.asarray([
        np.kron(a, b) for a, b in itertools.product((I, X, Y, Z), repeat=2)
    ])
    kraus = damping_kraus()
    completeness = sum(k.conj().T @ k for k in kraus)
    require(
        np.max(np.abs(completeness - identity)) < ATOL,
        "amplitude-damping branch is not trace preserving",
    )

    # The report is 3/4 replacement plus 1/4 amplitude damping. Use its
    # analytically valid complete-order certificate to also test the privacy
    # budget on every finite probe, without inferring privacy from probes.
    replacement = np.diag([1, 2, 3, 4]) / 10
    mixture = 1 / 4
    null = (1 - mixture) * replacement + mixture * apply_channel(kraus, identity / d)
    null_inverse = np.linalg.inv(null)
    nonunitality = np.linalg.norm(d * null - identity)
    require(nonunitality > 1e-3, "reference report became maximally mixed")
    replacer_choi = np.kron(replacement, identity / d)
    damping_choi = pure_probe_outputs(kraus, identity[None])[0]
    inverse_root = np.diag(1 / np.sqrt(np.diag(replacer_choi)))
    whitened_choi = inverse_root @ damping_choi @ inverse_root
    # The weighted Choi Kraus vectors have disjoint computational supports.
    # Their squared norms therefore give the complete-order constant exactly.
    replacement_inverse = np.linalg.inv(replacement)
    damping_ratio = max(np.trace(k.conj().T @ replacement_inverse @ k) for k in kraus)
    require(
        abs(np.linalg.eigvalsh(whitened_choi).max() - damping_ratio) < ATOL,
        "Choi order constant differs from the orthogonal Kraus formula",
    )
    upper = (1 - mixture) + mixture * damping_ratio
    privacy_ratio = upper / (1 - mixture)
    privacy_bound = (privacy_ratio - 1) * (1 - 1 / privacy_ratio)

    signals = [mixture * apply_channel(kraus, p) / d for p in paulis[1:]]
    pauli_budget = sum(np.trace(a @ null_inverse @ a).real for a in signals)
    frame_orbits = exact_frame_orbits(paulis)
    cases = []
    for r in range(1, d + 1):
        reference = np.eye(r) / r
        baseline = np.kron(null, reference)
        baseline_inverse = np.kron(null_inverse, r * np.eye(r))
        weighted_quadratic = 0.0
        maximum_quadratic = 0.0
        for weight, unitaries in frame_orbits:
            output = (
                (1 - mixture) * np.kron(replacement, reference)
                + mixture * pure_probe_outputs(kraus, unitaries[:, :, :r])
            )
            delta = output - baseline
            quadratics = np.einsum("nij,nji->n", delta @ baseline_inverse, delta).real
            weighted_quadratic += weight * np.mean(quadratics)
            maximum_quadratic = max(maximum_quadratic, float(quadratics.max()))
        predicted = (d * r - 1) * pauli_budget / (d**2 - 1)
        require(
            abs(weighted_quadratic - predicted) < ATOL,
            "compressed Choi twirl factor failed",
        )
        require(
            maximum_quadratic <= privacy_bound + ATOL,
            "private probe quadratic bound failed",
        )
        cases.append({
            "reference_rank": r,
            "finite_frame_average": rounded(weighted_quadratic),
            "predicted_average": rounded(predicted),
            "maximum_probe_quadratic": rounded(maximum_quadratic),
        })

    maximum_reverse_ratio = 0.0
    maximum_commutator = 0.0
    log_null = log_positive(null)
    for signal in signals:
        base_quadratic = np.trace(signal @ null_inverse @ signal).real
        for sign in (-1, 1):
            report = null + sign * signal
            require(
                np.linalg.eigvalsh(report - null / privacy_ratio).min() >= -ATOL,
                "signed report violates certified lower order bound",
            )
            reverse_relative_entropy = np.trace(null @ (log_null - log_positive(report))).real
            reverse_quadratic = np.trace(signal @ np.linalg.solve(report, signal)).real
            require(
                -ATOL <= reverse_relative_entropy <= reverse_quadratic + ATOL,
                "reverse relative entropy exceeds reverse quadratic",
            )
            require(
                reverse_quadratic <= privacy_ratio * base_quadratic + ATOL,
                "inverse order does not bound reverse quadratic",
            )
            maximum_reverse_ratio = max(
                maximum_reverse_ratio, reverse_relative_entropy / base_quadratic
            )
            maximum_commutator = max(
                maximum_commutator, np.linalg.norm(null @ report - report @ null)
            )
    require(
        maximum_commutator > 1e-3,
        "reverse divergence example lacks noncommuting reports",
    )
    return {
        "input_dimension": d,
        "frames_per_rank": sum(len(orbit) for _, orbit in frame_orbits),
        "pauli_quadratic_budget": rounded(pauli_budget),
        "complete_order_privacy_ratio": rounded(privacy_ratio),
        "probe_quadratic_bound": rounded(privacy_bound),
        "maximum_relative_entropy_over_baseline_quadratic": rounded(maximum_reverse_ratio),
        "maximum_reference_report_commutator_norm": rounded(maximum_commutator),
        "nonunitality_frobenius_norm": rounded(nonunitality),
        "compressed_choi_cases": cases,
    }


def check_werner_choi() -> dict:
    dimension = 5
    contrast = 1 / 4
    identity = np.eye(dimension**2)
    normalization = dimension**2 - contrast * dimension
    choi = (identity - contrast * swap(dimension)) / normalization
    axes = choi.reshape((dimension,) * 4)
    for bra, ket in ((0, 2), (1, 3)):
        marginal = np.trace(axes, axis1=bra, axis2=ket)
        require(
            np.max(np.abs(marginal - np.eye(dimension) / dimension)) < ATOL,
            "Werner Choi marginal is not maximally mixed",
        )

    depolarizing_choi = identity / dimension**2
    lower = dimension**2 * (1 - contrast) / normalization
    upper = dimension**2 * (1 + contrast) / normalization
    require(
        np.linalg.eigvalsh(choi - lower * depolarizing_choi).min() >= -ATOL,
        "Werner lower complete-positive order comparison failed",
    )
    require(
        np.linalg.eigvalsh(upper * depolarizing_choi - choi).min() >= -ATOL,
        "Werner upper complete-positive order comparison failed",
    )
    transposed = axes.transpose(0, 3, 2, 1).reshape(dimension**2, dimension**2)
    minimum = np.linalg.eigvalsh(transposed).min()
    prediction = (1 - contrast * dimension) / normalization
    require(
        minimum < -ATOL and abs(minimum - prediction) < ATOL,
        "Werner partial transpose is not negative as predicted",
    )
    return {
        "dimension": dimension,
        "werner_contrast": contrast,
        "lower_depolarizing_multiplier": rounded(lower),
        "upper_depolarizing_multiplier": rounded(upper),
        "complete_reference_privacy_epsilon": rounded(math.log(upper / lower)),
        "minimum_partial_transpose_eigenvalue": rounded(minimum),
    }


def run_checks() -> dict:
    return {
        "schema_version": 1,
        "absolute_tolerance": ATOL,
        "exact_twirl_and_reverse_divergence": check_twirl_and_reverse_divergence(),
        "reference_private_werner_choi": check_werner_choi(),
    }


if __name__ == "__main__":
    print(json.dumps({"status": "passed", "results": run_checks()}, indent=2, sort_keys=True))
