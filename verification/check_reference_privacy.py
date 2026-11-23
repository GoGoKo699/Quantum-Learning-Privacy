#!/usr/bin/env python3
"""Finite checks for reference-private reports and signed-target extraction."""
from __future__ import annotations

from collections import deque
from functools import reduce
from itertools import product
import json
import math

import numpy as np

from check_quantum_budget import ATOL, hermitian, require, rounded


def pauli_basis(n: int) -> np.ndarray:
    single = (
        np.eye(2, dtype=complex),
        np.array([[0, 1], [1, 0]], dtype=complex),
        np.array([[0, -1j], [1j, 0]], dtype=complex),
        np.diag([1, -1]).astype(complex),
    )
    return np.asarray([reduce(np.kron, factors) for factors in product(single, repeat=n)])


def clifford_representatives(basis: np.ndarray) -> np.ndarray:
    """Enumerate phase-free Clifford actions with one unitary per Pauli coset."""
    identity = basis[0]
    actions = []
    for label, pauli in enumerate(basis[1:], start=1):
        # Rotation by a Pauli fixes commuting labels and adds its label
        # (bitwise XOR in the I,X,Y,Z encoding) to anticommuting labels.
        action = tuple(
            index if np.allclose(pauli @ other, other @ pauli) else index ^ label
            for index, other in enumerate(basis)
        )
        actions.append((action, (identity + 1j * pauli) / math.sqrt(2)))

    first = tuple(range(len(basis)))
    representatives = {first: identity}
    unexplored = deque([first])
    while unexplored:
        action = unexplored.popleft()
        unitary = representatives[action]
        for generator, rotation in actions:
            composed = tuple(generator[index] for index in action)
            if composed not in representatives:
                representatives[composed] = rotation @ unitary
                unexplored.append(composed)
    return np.asarray(list(representatives.values()))


def check_compression_moment() -> dict:
    cases = []
    maximum_error = 0.0
    for n, expected_cosets in ((1, 6), (2, 720)):
        basis = pauli_basis(n)
        d = basis.shape[-1]
        representatives = clifford_representatives(basis)
        require(len(representatives) == expected_cosets, "incomplete Clifford enumeration")
        # Left multiplication by every Pauli runs through each coset.
        unitaries = (basis[:, None] @ representatives[None, :]).reshape(-1, d, d)
        labels = np.arange(d**2).reshape(d, d)
        swap = np.eye(d**2)[labels.T.ravel()]
        for k in range(1, d + 1):
            frames = unitaries[..., :k]
            projectors = frames @ frames.conj().transpose(0, 2, 1)
            observed = np.einsum("aij,akl->ikjl", projectors, projectors).reshape(d**2, d**2)
            observed /= len(projectors)
            a = k * (d * k - 1) / (d * (d**2 - 1))
            b = k * (d - k) / (d * (d**2 - 1))
            expected = a * np.eye(d**2) + b * swap
            error = float(np.max(np.abs(observed - expected)))
            require(error < ATOL, "Clifford projection tensor moment failed")

            compressed = np.einsum("aij,pil,alm->apjm", frames.conj(), basis[1:], frames)
            gram = np.einsum("apij,aqji->pq", compressed, compressed)
            gram /= len(frames) * k
            gamma = (d * k - 1) / (d**2 - 1)
            response_error = float(np.max(np.abs(gram - gamma * np.eye(d**2 - 1))))
            require(response_error < ATOL, "compressed Pauli Gram normalization failed")
            maximum_error = max(maximum_error, error, response_error)
            cases.append({"input_dimension": d, "reference_dimension": k, "gamma": rounded(gamma)})
    return {
        "cases": cases,
        "ensemble_sizes": [24, 11520],
        "maximum_tensor_or_response_error": rounded(maximum_error),
    }


def clean_test_probability(
    observable: np.ndarray, state: np.ndarray, signed_pauli: np.ndarray
) -> float:
    d = signed_pauli.shape[0]
    identity = np.eye(observable.shape[0])
    probability = 0.0
    for label in (-1, 1):
        test_state = (np.eye(d) + label * signed_pauli) / d
        effect = (identity + label * observable) / 2
        probability += float(np.trace(effect @ np.kron(state, test_state)).real) / 2
    return probability


def check_predictor_observable(
    observable: np.ndarray, basis: np.ndarray, states: list[np.ndarray]
) -> tuple[float, int, int]:
    d = basis.shape[-1]
    memory_dimension = observable.shape[0] // d
    block = observable.reshape(memory_dimension, d, memory_dimension, d)
    coefficients = np.einsum("aibj,pji->pab", block, basis) / d
    parseval = np.sum(coefficients @ coefficients, axis=0)
    square = (observable @ observable).reshape(
        memory_dimension, d, memory_dimension, d
    )
    expected = np.einsum("aibi->ab", square) / d
    error = float(np.max(np.abs(parseval - expected)))
    require(error < ATOL, "operator-valued Parseval failed")
    require(
        np.linalg.eigvalsh(hermitian(np.eye(memory_dimension) - expected)).min() >= -ATOL,
        "observable outside the unit-norm bound",
    )

    conclusive_effects = []
    cases = 0
    positive_cases = 0
    for pauli, coefficient in zip(basis[1:], coefficients[1:], strict=True):
        for sign in (-1, 1):
            values, vectors = np.linalg.eigh(hermitian(sign * coefficient))
            effect = (vectors * np.maximum(values, 0) ** 2) @ vectors.conj().T
            conclusive_effects.append(effect)
            for state in states:
                score = float(np.trace(state @ (sign * coefficient)).real)
                probability = clean_test_probability(observable, state, sign * pauli)
                error = max(error, abs(score - (2 * probability - 1)))
                success = float(np.trace(state @ effect).real)
                require(
                    success + ATOL >= max(0, 2 * probability - 1) ** 2,
                    "signed predictor-to-identification success bound failed",
                )
                cases += 1
                positive_cases += int(score > ATOL)
    require(error < ATOL, "signed prediction Born probabilities differ from Pauli scores")
    total = np.sum(conclusive_effects, axis=0)
    require(
        np.linalg.eigvalsh(hermitian(np.eye(memory_dimension) - total)).min() >= -ATOL,
        "signed extraction effects cannot be completed to a POVM",
    )
    return error, cases, positive_cases


def check_predictor() -> dict:
    rng = np.random.default_rng(20261123)
    total_cases = 0
    positive_cases = 0
    maximum_error = 0.0
    for n, memory_dimension in ((1, 2), (2, 3), (3, 5)):
        d = 2**n
        basis = pauli_basis(n)
        shape = (memory_dimension * d, memory_dimension * d)
        for _ in range(3):
            raw = hermitian(rng.normal(size=shape) + 1j * rng.normal(size=shape))
            observable = raw / np.max(np.abs(np.linalg.eigvalsh(raw)))
            pure = rng.normal(size=memory_dimension) + 1j * rng.normal(size=memory_dimension)
            state = np.outer(pure, pure.conj()) / np.vdot(pure, pure).real
            mixed = (state + np.eye(memory_dimension) / memory_dimension) / 2
            error, cases, positive = check_predictor_observable(observable, basis, [state, mixed])
            maximum_error = max(maximum_error, error)
            total_cases += cases
            positive_cases += positive
    return {
        "clean_test_and_identification_cases": total_cases,
        "strictly_positive_signed_score_cases": positive_cases,
        "maximum_parseval_or_born_error": rounded(maximum_error),
    }


def check_choi_examples() -> dict:
    cases = 0
    npt_cases = 0
    maximum_error = 0.0
    for d, epsilon in product((2, 4, 8), (0.25, 0.5, 1.0)):
        t = math.tanh(epsilon / 2)
        labels = np.arange(d**2).reshape(d, d)
        swap = np.eye(d**2)[labels.T.ravel()]
        choi = (np.eye(d**2) - t * swap) / (d * (d - t))
        eigenvalues = np.linalg.eigvalsh(choi)
        ratio = eigenvalues[-1] / eigenvalues[0]
        margin = abs(ratio - math.exp(epsilon))
        partial_transpose = choi.reshape(d, d, d, d).transpose(0, 3, 2, 1)
        smallest = np.linalg.eigvalsh(partial_transpose.reshape(d**2, d**2))[0]
        predicted = (1 - t * d) / (d * (d - t))
        maximum_error = max(maximum_error, margin, abs(smallest - predicted))
        require(eigenvalues[0] > 0, "transpose-depolarizing Choi must be positive")
        require(abs(np.trace(choi) - 1) < ATOL, "Choi matrix is not normalized")
        npt_cases += int(smallest < -ATOL)
        cases += 1
    require(maximum_error < ATOL, "Choi privacy ratio or partial transpose formula failed")
    require(npt_cases > 0, "finite cases missed reference-private NPT examples")

    # Equal mixing of X, Y, and Z gives the qubit channel (2 I - rho)/3
    # on density matrices. Its ordinary privacy ratio is at most two, but the
    # missing Bell component distinguishes equal-reference-marginal inputs.
    identity, *axes = pauli_basis(1)
    bell = identity.reshape(-1) / math.sqrt(2)
    images = [np.kron(axis, identity) @ bell for axis in axes]
    short_choi = sum(np.outer(image, image.conj()) for image in images) / 3
    entangled_input_probability = float(np.vdot(bell, short_choi @ bell).real)
    mixed_input_probability = float(np.vdot(bell, np.eye(4) @ bell / 4).real)
    require(abs(entangled_input_probability) < ATOL, "missing Bell component has weight")
    require(abs(mixed_input_probability - 0.25) < ATOL, "mixed reference baseline failed")
    return {
        "transpose_depolarizing_cases": cases,
        "negative_partial_transpose_cases": npt_cases,
        "maximum_spectral_identity_error": rounded(maximum_error),
        "missing_bell_event_entangled_input_probability": rounded(entangled_input_probability),
        "missing_bell_event_mixed_input_probability": rounded(mixed_input_probability),
    }


def run_checks() -> dict:
    return {
        "compressed_pauli_moment": check_compression_moment(),
        "signed_prediction_extraction": check_predictor(),
        "choi_privacy_examples": check_choi_examples(),
    }


if __name__ == "__main__":
    print(json.dumps(run_checks(), indent=2, sort_keys=True))
