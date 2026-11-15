#!/usr/bin/env python3
"""Deterministic finite checks of the quantum-report information budget.

The qubit channel used here is analytically private: it is a fixed full-rank
replacement channel mixed with amplitude damping.  Its spectral enclosure
certifies all-input privacy.  The six inputs are an exact projective 2-design,
not a random-state privacy test.  No randomizer or collective decoder is built.
"""
from __future__ import annotations

import json
import math

import numpy as np


ATOL = 2e-10


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def rounded(value: float) -> float:
    return round(float(value), 9)


def hermitian(matrix: np.ndarray) -> np.ndarray:
    return (matrix + matrix.conj().T) / 2


def real_trace(matrix: np.ndarray) -> float:
    value = np.trace(matrix)
    require(abs(float(value.imag)) < ATOL, "unexpected imaginary trace")
    return float(value.real)


def support_data(state: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return the support isometry, inverse, and inverse square root."""
    values, vectors = np.linalg.eigh(hermitian(state))
    require(values.min() >= -ATOL, "reference state is not positive")
    positive = values > ATOL
    basis = vectors[:, positive]
    eigenvalues = values[positive]
    inverse = (basis / eigenvalues) @ basis.conj().T
    inverse_root = (basis / np.sqrt(eigenvalues)) @ basis.conj().T
    return basis, inverse, inverse_root


def log_on_support(state: np.ndarray, basis: np.ndarray) -> np.ndarray:
    compressed = hermitian(basis.conj().T @ state @ basis)
    values, vectors = np.linalg.eigh(compressed)
    require(values.min() > 0, "state is not positive on the common support")
    logarithm = (vectors * np.log(values)) @ vectors.conj().T
    return basis @ logarithm @ basis.conj().T


def relative_entropy(
    first: np.ndarray, second: np.ndarray, basis: np.ndarray
) -> float:
    return real_trace(
        first @ (log_on_support(first, basis) - log_on_support(second, basis))
    )


def channel_kraus() -> tuple[list[np.ndarray], np.ndarray]:
    """(4/5) Tr(X) tau0 + (1/5) amplitude_damping_(2/5)(X)."""
    unitary = np.array([[1, 1j], [1j, 1]], dtype=complex) / math.sqrt(2)
    eigenvalues = [3 / 10, 7 / 10]
    replacement = unitary @ np.diag(eigenvalues) @ unitary.conj().T
    kraus = []
    for i, value in enumerate(eigenvalues):
        for j in range(2):
            ket = unitary[:, i]
            bra = np.eye(2, dtype=complex)[j]
            kraus.append(math.sqrt((4 / 5) * value) * np.outer(ket, bra))
    damping = [
        np.diag([1, math.sqrt(3 / 5)]).astype(complex),
        np.array([[0, math.sqrt(2 / 5)], [0, 0]], dtype=complex),
    ]
    kraus.extend(math.sqrt(1 / 5) * operator for operator in damping)
    return kraus, replacement


def finite_case(output_isometry: np.ndarray) -> dict:
    identity = np.eye(2, dtype=complex)
    paulis = [
        np.array([[0, 1], [1, 0]], dtype=complex),
        np.array([[0, -1j], [1j, 0]], dtype=complex),
        np.diag([1, -1]).astype(complex),
    ]
    pure_states = [(identity + sign * p) / 2 for p in paulis for sign in (-1, 1)]
    kraus, replacement = channel_kraus()
    embedded_kraus = [output_isometry @ operator for operator in kraus]

    def channel(matrix: np.ndarray) -> np.ndarray:
        return sum(operator @ matrix @ operator.conj().T for operator in embedded_kraus)

    completeness = sum(operator.conj().T @ operator for operator in embedded_kraus)
    completeness_error = float(np.max(np.abs(completeness - identity)))
    require(completeness_error < ATOL, "Kraus operators are not trace preserving")
    tau = channel(identity / 2)
    basis, inverse, inverse_root = support_data(tau)
    support = basis @ basis.conj().T
    require(basis.shape[1] == 2, "unexpected output support rank")
    require(abs(real_trace(tau) - 1) < ATOL, "reference is not normalized")

    # For EVERY input density rho, 0 <= AD(rho) <= I and
    # (3/10) I <= tau0 <= (7/10) I.  Thus on the output support
    # (6/25) I <= Lambda(rho) <= (19/25) I.  Any two outputs obey
    # Lambda(rho) <= (19/6) Lambda(sigma), including after isometric embedding.
    lower, upper = 6 / 25, 19 / 25
    ratio = upper / lower
    epsilon = math.log(ratio)
    replacement_values = np.linalg.eigvalsh(replacement)
    require(
        np.max(np.abs(replacement_values - [3 / 10, 7 / 10])) < ATOL,
        "replacement spectrum differs from its analytic certificate",
    )
    outputs = [channel(state) for state in pure_states]
    smallest_enclosure_margin = math.inf
    smallest_relative_margin = math.inf
    for output in outputs:
        compressed = hermitian(basis.conj().T @ output @ basis)
        values = np.linalg.eigvalsh(compressed)
        smallest_enclosure_margin = min(
            smallest_enclosure_margin, float(values.min() - lower), float(upper - values.max())
        )
        for difference in (ratio * tau - output, output - tau / ratio):
            minimum = float(
                np.linalg.eigvalsh(hermitian(basis.conj().T @ difference @ basis)).min()
            )
            smallest_relative_margin = min(smallest_relative_margin, minimum)
        require(
            np.max(np.abs((np.eye(tau.shape[0]) - support) @ output)) < ATOL,
            "output has leaked outside the reference support",
        )
    require(smallest_enclosure_margin >= -ATOL, "finite output misses certified enclosure")
    require(smallest_relative_margin >= -ATOL, "reference-relative domination failed")

    # Verify that this case really exercises nonunital, noncommuting matrices.
    nonunitality = float(np.linalg.norm(channel(identity) - support))
    maximum_commutator = max(float(np.linalg.norm(tau @ out - out @ tau)) for out in outputs)
    require(nonunitality > 1e-3, "test channel became unital")
    require(maximum_commutator > 1e-3, "test reports all commute with the reference")

    swap = np.array(
        [[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]], dtype=complex
    )
    second_moment = sum(np.kron(state, state) for state in pure_states) / 6
    design_error = float(np.max(np.abs(second_moment - (np.eye(4) + swap) / 6)))
    require(design_error < ATOL, "six Pauli eigenstates do not satisfy the exact 2-design moment")
    coefficients = np.asarray([[real_trace(p @ state) for p in paulis] for state in pure_states])
    covariance_error = float(np.max(np.abs(coefficients.T @ coefficients / 6 - np.eye(3) / 3)))
    require(covariance_error < ATOL, "normalized Pauli coefficient second moment failed")

    signals = [channel(p) / 2 for p in paulis]
    pauli_budget = sum(real_trace(signal @ inverse @ signal) for signal in signals)
    pure_chi_squared = []
    maximum_whitening_error = 0.0
    maximum_entropy_gap = -math.inf
    divergences = []
    for output in outputs:
        difference = output - tau
        chi_squared = real_trace(difference @ inverse @ difference)
        whitened = inverse_root @ output @ inverse_root
        whitened_difference = whitened - support
        whitened_chi_squared = real_trace(tau @ whitened_difference @ whitened_difference)
        maximum_whitening_error = max(
            maximum_whitening_error, abs(chi_squared - whitened_chi_squared)
        )
        require(chi_squared >= -ATOL, "Petz chi-squared divergence is negative")
        divergence = relative_entropy(output, tau, basis)
        order_two = math.log(real_trace(output @ output @ inverse))
        require(divergence >= -ATOL, "relative entropy is negative")
        require(divergence <= order_two + ATOL, "relative entropy exceeds Petz order-two bound")
        require(order_two <= chi_squared + ATOL, "log bound exceeds Petz chi-squared divergence")
        maximum_entropy_gap = max(maximum_entropy_gap, divergence - chi_squared)
        pure_chi_squared.append(chi_squared)
        divergences.append(divergence)
    require(maximum_whitening_error < ATOL, "noncommuting whitening identity failed")
    haar_budget_error = abs(pauli_budget - 3 * float(np.mean(pure_chi_squared)))
    require(haar_budget_error < ATOL, "Haar/Pauli quadratic budget identity failed")

    constant = (ratio - 1) ** 2
    tighter_constant = ratio + 1 / ratio - 2
    require(pauli_budget <= 3 * constant + ATOL, "Pauli budget exceeds simple privacy bound")
    require(pauli_budget <= 3 * tighter_constant + ATOL, "Pauli budget exceeds sharpened privacy bound")
    mean_error = float(np.max(np.abs(sum(outputs) / 6 - tau)))
    require(mean_error < ATOL, "uniform signed-target mean is not the reference")
    holevo = float(np.mean(divergences))
    chi_squared_average = pauli_budget / 3
    require(holevo <= chi_squared_average + ATOL, "one-report Holevo exceeds quadratic budget")
    require(holevo <= constant + ATOL, "one-report dimension-normalized information bound failed")

    return {
        "output_dimension": int(tau.shape[0]),
        "reference_support_rank": int(basis.shape[1]),
        "pure_design_states": len(pure_states),
        "analytic_output_spectral_enclosure_on_support": ["6/25", "19/25"],
        "analytic_all_input_privacy_bound": "log(19/6)",
        "privacy_certified_by_mixture_spectral_bounds": True,
        "random_all_input_certification": False,
        "maximum_kraus_completeness_error": rounded(completeness_error),
        "channel_nonunitality_frobenius_norm": rounded(nonunitality),
        "maximum_reference_report_commutator_norm": rounded(maximum_commutator),
        "minimum_finite_output_enclosure_margin": rounded(smallest_enclosure_margin),
        "minimum_finite_reference_domination_margin": rounded(smallest_relative_margin),
        "maximum_exact_design_second_moment_error": rounded(design_error),
        "maximum_pauli_coefficient_covariance_error": rounded(covariance_error),
        "maximum_noncommuting_whitening_identity_error": rounded(maximum_whitening_error),
        "haar_pauli_quadratic_budget_identity_error": rounded(haar_budget_error),
        "pauli_quadratic_budget": rounded(pauli_budget),
        "simple_budget_bound": rounded(3 * constant),
        "sharpened_budget_bound": rounded(3 * tighter_constant),
        "maximum_relative_entropy_minus_chi_squared": rounded(maximum_entropy_gap),
        "uniform_signed_target_mean_error": rounded(mean_error),
        "one_report_holevo_nats": rounded(holevo),
        "one_report_mean_petz_chi_squared": rounded(chi_squared_average),
        "epsilon_nats": rounded(epsilon),
    }


def run_checks() -> dict:
    full_rank = finite_case(np.eye(2, dtype=complex))
    embedding = np.array(
        [[1, 0], [1j, 0], [0, 1], [0, 1j]], dtype=complex
    ) / math.sqrt(2)
    embedded = finite_case(embedding)
    invariant_keys = [
        "pauli_quadratic_budget",
        "one_report_holevo_nats",
        "one_report_mean_petz_chi_squared",
        "channel_nonunitality_frobenius_norm",
        "maximum_reference_report_commutator_norm",
    ]
    for key in invariant_keys:
        require(full_rank[key] == embedded[key], f"isometric embedding changed {key}")
    return {
        "schema_version": 1,
        "rounding_decimal_places": 9,
        "absolute_tolerance": ATOL,
        "finite_cases": [full_rank, embedded],
        "singular_reference_support_checked": True,
        "isometric_invariants_checked": invariant_keys,
    }


if __name__ == "__main__":
    print(json.dumps({"status": "passed", "results": run_checks()}, indent=2, sort_keys=True))
