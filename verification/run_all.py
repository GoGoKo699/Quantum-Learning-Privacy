#!/usr/bin/env python3
"""Deterministic finite checks for the private-report learning proofs.

The analytical proofs remain authoritative. This program does not certify an
all-input approximate randomizer or construct a collective learning decoder.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import itertools
import json
import math
from pathlib import Path

import numpy as np

from check_quantum_budget import run_checks as check_quantum_information_budget

SEED = 20261115
ATOL = 2e-10


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def rounded(value: float) -> float:
    return round(float(value), 9)


def hermitian(matrix: np.ndarray) -> np.ndarray:
    return (matrix + matrix.conj().T) / 2


def positive_root(matrix: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eigh(hermitian(matrix))
    require(float(values.min()) >= -ATOL, "matrix is not positive semidefinite")
    return (vectors * np.sqrt(np.maximum(values, 0))) @ vectors.conj().T


def inverse_positive_root(matrix: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eigh(hermitian(matrix))
    require(float(values.min()) > 0, "matrix is not positive definite")
    return (vectors / np.sqrt(values)) @ vectors.conj().T


def paulis(n: int) -> np.ndarray:
    single = [
        np.eye(2, dtype=complex),
        np.array([[0, 1], [1, 0]], dtype=complex),
        np.array([[0, -1j], [1j, 0]], dtype=complex),
        np.diag([1, -1]).astype(complex),
    ]
    matrices = []
    for factors in itertools.product(single, repeat=n):
        matrix = factors[0]
        for factor in factors[1:]:
            matrix = np.kron(matrix, factor)
        matrices.append(matrix)
    return np.asarray(matrices[1:])


def private_povm(
    rng: np.random.Generator, d: int, epsilon: float, family: str
) -> np.ndarray:
    """Construct effects whose spectral ratio is exactly exp(epsilon).

    These are controlled finite examples, not sampled certificates for a
    separate channel's all-input privacy.
    """
    ratio = math.exp(epsilon)
    if family == "basis_randomized_response":
        gaussian = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
        unitary, _ = np.linalg.qr(gaussian)
        projectors = [
            np.outer(unitary[:, j], unitary[:, j].conj()) for j in range(d)
        ]
        return np.asarray(
            [(np.eye(d) + (ratio - 1) * p) / (d + ratio - 1) for p in projectors]
        )
    if family == "weighted_rank_one":
        count = 2 * d + 1
        vectors = rng.normal(size=(count, d)) + 1j * rng.normal(size=(count, d))
        raw = np.asarray([np.outer(v, v.conj()) for v in vectors])
        normalization = inverse_positive_root(raw.sum(axis=0))
        povm = np.asarray([normalization @ e @ normalization for e in raw])
        contrast = (ratio - 1) / (d + ratio - 1)
        effects = []
        for effect in povm:
            weight = np.trace(effect).real / d
            effects.append((1 - contrast) * weight * np.eye(d) + contrast * effect)
        return np.asarray(effects)
    raise ValueError(f"unknown POVM family: {family}")


def check_private_povms(rng: np.random.Generator) -> dict:
    dimensions = [2, 4, 8]
    epsilons = [0.05, 0.5, 1.0, 2.0]
    families = ["basis_randomized_response", "weighted_rank_one"]
    trials = 10
    cases = 0
    max_variance_ratio = 0.0
    max_kl_ratio = 0.0
    max_signal_ratio = 0.0
    max_likelihood_error = 0.0
    max_completeness_error = 0.0

    for n, d in enumerate(dimensions, start=1):
        basis = paulis(n)
        identity = np.eye(d)
        positive_sources = (identity[None, :, :] + basis) / d
        negative_sources = (identity[None, :, :] - basis) / d
        for epsilon in epsilons:
            ratio = math.exp(epsilon)
            contrast = math.tanh(epsilon / 2)
            variance_bound = math.sinh(epsilon / 2) ** 2
            kl_bound = math.sinh(epsilon) ** 2 / 4
            for family in families:
                for _ in range(trials):
                    effects = private_povm(rng, d, epsilon, family)
                    completeness_error = float(
                        np.max(np.abs(effects.sum(axis=0) - identity))
                    )
                    require(completeness_error < ATOL, "POVM does not sum to I")
                    max_completeness_error = max(
                        max_completeness_error, completeness_error
                    )
                    for effect in effects:
                        values = np.linalg.eigvalsh(hermitian(effect))
                        require(values.min() > 0, "POVM effect is not positive")
                        require(
                            values.max() / values.min() <= ratio + ATOL,
                            "effect eigenvalue ratio exceeds exp(epsilon)",
                        )

                    q = np.trace(effects, axis1=1, axis2=2).real / d
                    signal = np.einsum("zij,pji->zp", effects, basis).real / d
                    coefficients = signal / q[:, None]
                    require(
                        float(np.max(np.abs(coefficients))) <= contrast + ATOL,
                        "a Pauli coefficient exceeds tanh(epsilon/2)",
                    )
                    variance = float(np.sum(q[:, None] * coefficients**2))
                    require(
                        variance <= variance_bound + ATOL,
                        "Pauli-energy budget exceeded",
                    )

                    # Compute the target likelihoods directly by the Born rule,
                    # then compare them with the signed likelihood identity.
                    p_positive = np.einsum(
                        "zij,pji->zp", effects, positive_sources
                    ).real
                    p_negative = np.einsum(
                        "zij,pji->zp", effects, negative_sources
                    ).real
                    require(
                        p_positive.min() > 0 and p_negative.min() > 0,
                        "private target likelihood is not strictly positive",
                    )
                    likelihood_error = max(
                        float(np.max(np.abs(p_positive - q[:, None] - signal))),
                        float(np.max(np.abs(p_negative - q[:, None] + signal))),
                    )
                    require(
                        likelihood_error < ATOL, "signed Born likelihood identity failed"
                    )
                    # These are reverse KL divergences from the null I/d.
                    # Summing both signs also covers either public training label.
                    signed_kl = float(
                        np.sum(
                            q[:, None] * np.log(q[:, None] / p_positive)
                            + q[:, None] * np.log(q[:, None] / p_negative)
                        )
                    )
                    require(
                        signed_kl <= kl_bound + ATOL,
                        "summed signed reverse-KL budget exceeded",
                    )
                    max_variance_ratio = max(
                        max_variance_ratio, variance / variance_bound
                    )
                    max_kl_ratio = max(max_kl_ratio, signed_kl / kl_bound)
                    max_signal_ratio = max(
                        max_signal_ratio,
                        float(np.max(np.abs(coefficients))) / contrast,
                    )
                    max_likelihood_error = max(
                        max_likelihood_error, likelihood_error
                    )
                    cases += 1
    return {
        "cases": cases,
        "dimensions": dimensions,
        "epsilons": epsilons,
        "families": families,
        "trials_per_setting": trials,
        "maximum_pauli_energy_over_bound": rounded(max_variance_ratio),
        "maximum_signed_reverse_kl_over_bound": rounded(max_kl_ratio),
        "maximum_absolute_signal_over_bound": rounded(max_signal_ratio),
        "maximum_signed_likelihood_absolute_error": rounded(max_likelihood_error),
        "maximum_povm_completeness_absolute_error": rounded(max_completeness_error),
    }


def check_complete_snapshot() -> dict:
    """Exact qubit record counterexample; averaged quantum output is different."""
    # Pick X, Y, Z uniformly, measure that axis, and report (axis, sign).
    # On |0>, the event (Z,+) has probability 1/3; on |1>, it has probability 0.
    report_zero = [
        Fraction(1, 6),
        Fraction(1, 6),
        Fraction(1, 6),
        Fraction(1, 6),
        Fraction(1, 3),
        Fraction(0),
    ]
    report_one = [
        Fraction(1, 6),
        Fraction(1, 6),
        Fraction(1, 6),
        Fraction(1, 6),
        Fraction(0),
        Fraction(1, 3),
    ]
    require(sum(report_zero) == sum(report_one) == 1, "snapshot law not normalized")
    require(
        report_zero[4] > 0 and report_one[4] == 0,
        "complete snapshot should fail every finite pure-LDP ratio",
    )

    # Prepare the measured eigenstate and average over the entire classical
    # record. The resulting qubit channel is rho -> (I + rho)/3.
    axes = paulis(1)
    identity = np.eye(2)
    sources = [(identity + sign * axis) / 2 for axis in axes for sign in (1, -1)]
    largest_formula_error = 0.0
    smallest_domination_eigenvalue = math.inf
    averaged = []
    for rho in sources:
        actual = np.zeros((2, 2), dtype=complex)
        for axis in axes:
            for sign in (1, -1):
                projector = (identity + sign * axis) / 2
                probability = np.trace(projector @ rho).real / 3
                actual += probability * projector
        formula = (identity + rho) / 3
        largest_formula_error = max(
            largest_formula_error, float(np.max(np.abs(actual - formula)))
        )
        require(
            np.max(np.abs(actual - formula)) < ATOL,
            "averaged preparation channel formula failed",
        )
        averaged.append(actual)
    for first in averaged:
        for second in averaged:
            lower = float(np.linalg.eigvalsh(2 * second - first).min())
            smallest_domination_eigenvalue = min(
                smallest_domination_eigenvalue, lower
            )
            require(lower >= -ATOL, "finite averaged-output domination check failed")
    return {
        "complete_record_event": "axis=Z, sign=+",
        "event_probability_on_zero": str(report_zero[4]),
        "event_probability_on_one": str(report_one[4]),
        "complete_record_pure_ldp_epsilon": "infinite",
        "averaged_quantum_channel": "(I + rho)/3",
        "averaged_quantum_output_spectral_interval": ["1/3", "2/3"],
        "averaged_quantum_channel_pure_ldp_epsilon": "log(2)",
        "finite_input_states_checked": len(sources),
        "finite_ordered_input_pairs_checked": len(sources) ** 2,
        "maximum_channel_formula_absolute_error": rounded(largest_formula_error),
        "minimum_domination_eigenvalue": rounded(smallest_domination_eigenvalue),
    }


def check_tournament_costs() -> dict:
    dimensions = [2, 4, 8, 16, 32, 256]
    epsilons = [0.1, 0.5, 1.0, 2.0]
    failures = [0.01, 0.1, 0.4]
    cases = 0
    maximum_cost_ratio = 0.0
    maximum_sum_failure_over_delta = 0.0
    for d in dimensions:
        count = 2 * (d * d - 1)
        padded = 1 << (count - 1).bit_length()
        rounds = padded.bit_length() - 1
        require(count <= padded < 2 * count, "invalid tournament padding")
        for epsilon in epsilons:
            contrast = math.tanh(epsilon / 2)
            for delta in failures:
                exact_cost = 0
                summed_failure_bound = 0.0
                for round_number in range(1, rounds + 1):
                    samples_per_arm = math.ceil(
                        8
                        / contrast**2
                        * math.log(2 ** (round_number + 1) / delta)
                    )
                    active_arms = padded // 2 ** (round_number - 1)
                    exact_cost += active_arms * samples_per_arm
                    local_failure = 2 * math.exp(
                        -samples_per_arm * contrast**2 / 8
                    )
                    require(
                        local_failure <= delta / 2**round_number + ATOL,
                        "chosen tournament sample count misses its Hoeffding bound",
                    )
                    summed_failure_bound += local_failure
                displayed_bound = padded * (
                    2
                    + 8
                    / contrast**2
                    * (6 * math.log(2) + 2 * math.log(1 / delta))
                )
                require(
                    exact_cost <= displayed_bound + ATOL,
                    "tournament ceiling cost exceeds displayed bound",
                )
                require(
                    summed_failure_bound <= delta + ATOL,
                    "path-wise analytic failure bounds exceed delta",
                )
                maximum_cost_ratio = max(
                    maximum_cost_ratio, exact_cost / displayed_bound
                )
                maximum_sum_failure_over_delta = max(
                    maximum_sum_failure_over_delta, summed_failure_bound / delta
                )
                cases += 1
    return {
        "cases": cases,
        "dimensions": dimensions,
        "epsilons": epsilons,
        "target_failures": failures,
        "maximum_exact_cost_over_displayed_bound": rounded(maximum_cost_ratio),
        "maximum_sum_of_analytic_failure_bounds_over_delta": rounded(
            maximum_sum_failure_over_delta
        ),
        "stochastic_success_simulation": False,
    }


def bounded_state(
    rng: np.random.Generator, d: int, eta: float
) -> np.ndarray:
    gaussian = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    direction = hermitian(gaussian)
    direction -= np.trace(direction).real * np.eye(d) / d
    scale = float(np.max(np.abs(np.linalg.eigvalsh(direction))))
    require(scale > 0, "degenerate random traceless direction")
    direction /= scale
    return (np.eye(d) + eta * direction) / d


def root_fidelity(first: np.ndarray, second: np.ndarray) -> float:
    root = positive_root(first)
    middle = hermitian(root @ second @ root)
    return float(np.trace(positive_root(middle)).real)


def check_bures_bound(rng: np.random.Generator) -> dict:
    dimensions = [2, 3, 4, 8]
    etas = [0.05, 0.4, 0.8]
    trials = 20
    cases = 0
    largest_ratio = 0.0
    smallest_margin = math.inf
    for d in dimensions:
        for eta in etas:
            spectral_bound = (1 + eta) / d
            for _ in range(trials):
                first = bounded_state(rng, d, eta)
                second = bounded_state(rng, d, eta)
                for state in (first, second):
                    values = np.linalg.eigvalsh(state)
                    require(
                        values.min() > 0
                        and values.max() <= spectral_bound + ATOL
                        and abs(np.trace(state).real - 1) < ATOL,
                        "generated state misses its stated spectral band",
                    )
                fidelity = root_fidelity(first, second)
                lhs = 1 - fidelity
                difference_squared = float(
                    np.trace((first - second).conj().T @ (first - second)).real
                )
                rhs = d * difference_squared / (8 * (1 + eta))
                margin = lhs - rhs
                require(
                    margin >= -ATOL,
                    "bounded-spectrum Bures/root-fidelity inequality failed",
                )
                if lhs > ATOL:
                    largest_ratio = max(largest_ratio, rhs / lhs)
                smallest_margin = min(smallest_margin, margin)
                cases += 1
    maximally_mixed = np.eye(4) / 4
    require(
        abs(root_fidelity(maximally_mixed, maximally_mixed) - 1) < ATOL,
        "equal-state fidelity is not one",
    )
    return {
        "cases": cases,
        "dimensions": dimensions,
        "etas": etas,
        "trials_per_setting": trials,
        "maximum_rhs_over_fidelity_gap": rounded(largest_ratio),
        "minimum_fidelity_gap_minus_rhs": rounded(smallest_margin),
        "equal_state_endpoint_checked": True,
    }


def run() -> dict:
    rng = np.random.default_rng(SEED)
    return {
        "schema_version": 1,
        "seed": SEED,
        "rounding_decimal_places": 9,
        "private_povm_bounds": check_private_povms(rng),
        "complete_snapshot_and_averaged_state": check_complete_snapshot(),
        "tournament_costs": check_tournament_costs(),
        "bounded_spectrum_bures_bound": check_bures_bound(rng),
        "noncommuting_quantum_information_budget": check_quantum_information_budget(),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--write-expected",
        action="store_true",
        help="replace expected_results.json after an intentional reviewed update",
    )
    args = parser.parse_args()
    results = run()
    expected_path = Path(__file__).with_name("expected_results.json")
    if args.write_expected:
        expected_path.write_text(
            json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        print(f"Wrote {expected_path.name}")
        return
    expected = json.loads(expected_path.read_text(encoding="utf-8"))
    require(
        results == expected,
        "deterministic rounded results differ from expected_results.json; "
        "inspect the change before updating the expected file",
    )
    print(json.dumps({"status": "passed", "results": results}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
