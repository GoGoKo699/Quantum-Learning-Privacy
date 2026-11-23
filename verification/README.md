# Finite verification

Run these checks from the repository root:

~~~bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
~~~

The recorded environment is Python 3.12.14 with NumPy 2.3.5. NumPy is the only third-party dependency; its installed version is pinned in [requirements.txt](requirements.txt). The script uses a fixed seed, checks its inequalities before reporting success, rounds diagnostic values to nine decimal places, and compares the complete result with [expected_results.json](expected_results.json).

These are finite checks of specific proof risks. They supplement the analytical arguments and do not establish their general quantifiers by simulation.

| Check | Finite scope | Risk addressed |
| --- | --- | --- |
| Private POVM bounds | 240 POVMs; dimensions 2, 4, 8; privacy levels 0.05, 0.5, 1, 2; two families with uniform and unequal outcome weights | Eigenvalue-ratio constants, Pauli normalization, complete signed likelihoods, and the factor in the reverse-relative-entropy budget |
| Complete snapshot record | An exact qubit record event, followed by six finite input states and 36 ordered pairs for the averaged quantum output | Confusing the actual classical report with the quantum state obtained after averaging and discarding that report |
| Tournament budgets | 72 settings; dimensions 2 through 256, four privacy levels, three target failures | Rounding the per-arm sample counts, bracket padding, summing the true arm's analytic failure bounds, and the displayed total-cost formula |
| Bounded-spectrum Bures inequality | 240 state pairs; dimensions 2, 3, 4, 8; three spectral bands; equal-state endpoint | Root fidelity versus squared fidelity, matrix-order normalization, and the dimension-dependent constant in the Hilbert–Schmidt bound |
| Quantum information budget | A nonunital qubit channel and its four-dimensional singular-support embedding; exact six-state projective 2-design | Haar/Pauli normalization, support inverses, noncommuting Petz bounds, and the one-report Holevo calculation |
| Compressed Pauli moment | All 24 one-qubit and all 11,520 two-qubit Clifford actions up to global phase, with every compression rank in each dimension | The two coefficients of the projector tensor moment and the resulting factor `(dk−1)/(d²−1)` |
| Prediction and signed identification | Binary test observables on input dimensions 2, 4, and 8 with pure and mixed quantum memories | Operator Parseval, POVM completeness, signed Born probabilities and the square of the prediction score |
| Reference-privacy examples | Nine transpose-depolarizing channels and a rank-three qubit random-unitary channel | Choi spectral ratio, the partial-transpose eigenvalue and an event that detects a missing Bell component |

The private POVMs are constructed by two controlled families. The first randomizes a projective measurement. The second starts with a normalized rank-one POVM of unequal trace weights and mixes each effect with its trace-weighted identity. The script checks the resulting spectral ratio and then evaluates every nonidentity Pauli in the stated dimension. Target probabilities are computed directly by the Born rule before being compared with the signed likelihood identity. Relative entropies are evaluated in the reference-to-target direction required by the adaptive proof.

For the snapshot counterexample, choose a Pauli axis uniformly and release the axis and measured sign. On the input zero state, the event “Z axis and positive sign” has probability one third; on the input one state it has probability zero. This exact event defeats every finite pure local-privacy parameter for that complete classical record. If the measured eigenstate is instead prepared and the classical record discarded, the averaged quantum channel is rho → (I + rho)/3, whose output spectra lie between one third and two thirds. These are different released objects. The all-input spectral statement follows from that channel formula; checking six states is not a numerical certificate over every input.

The tournament check evaluates the explicit Hoeffding-based bounds and the exact integer sample counts. It does not estimate a stochastic success rate or replace the proof of the adaptive tournament's success.

The Bures check generates density matrices with a controlled spectral upper bound and computes root fidelity using Hermitian eigendecompositions. It tests the inequality used in [quantum-reports.md](../science/quantum-reports.md). It does not construct the collective decoder.

The quantum information-budget check uses an amplitude-damping channel mixed with a full-rank replacement state. Its privacy follows analytically from the output spectral interval on its support; it is not inferred from sampled inputs. The six Pauli eigenstates form an exact qubit projective 2-design. The check evaluates the whitened quadratic identity, the Petz relative-entropy bound and the one-report Holevo quantity for genuinely noncommuting outputs. An isometric embedding with a zero output block checks that support-restricted inverses preserve those quantities. The independent check can also be run as `python3 verification/check_quantum_budget.py`.

The reference-privacy check enumerates the Clifford moments in two input dimensions, computes both sides of the compression identity and checks every rank, including one and full dimension. It independently computes the clean prediction probability by the Born rule and tests the positive-part measurement that extracts a signed Pauli from the retained quantum memory. The two Choi examples isolate the missing-support obstruction and show that a reference-private channel can preserve entanglement. Run these checks independently with `python3 verification/check_reference_privacy.py`.

## What these checks do not establish

The analytical arguments establish the all-input guarantees, existence of a valid randomizer list, sample bounds and limits of adaptive quantum encoding. The program checks finite instances of the identities and inequalities used in those arguments. It supplies neither a randomizer setup list nor a circuit for the collective decoder.

No randomizer privacy claim is inferred from testing random input states. In particular, a successful run is not an all-state privacy certificate for an unrelated numerical channel.

## Updating recorded results

After an intentional change, inspect the mathematical reason for every changed result. Then regenerate the expected file:

~~~bash
python3 verification/run_all.py --write-expected
python3 verification/run_all.py
~~~

The update flag replaces only verification/expected_results.json. Do not regenerate it merely to conceal a failed inequality or an unexplained discrepancy.
