# Quantum Learning Privacy

**Can quantum memory still help when every training specimen is locally private?** This project gives an exponential sample separation between classical and quantum private reports from the same labeled quantum source.

The task is to learn one hidden signed Pauli classifier from native $`n`$-qubit examples. Every owner privatizes one specimen before releasing it. Privacy holds for every possible input state and includes all public flags. Training labels are public.

Let $`d=2^n`$. At every fixed positive local-privacy level $`\varepsilon`$ and fixed bounded identification error, the sample costs are:

| Private training reports | Specimens | Allowed processing |
|---|---:|---|
| Classical | $`\Theta_\varepsilon(d^2)`$ | Arbitrary adaptive private measurements and unlimited classical computation |
| Quantum | $`\Theta_\varepsilon(d\log d)`$ | Noninteractive product encoders and arbitrary collective decoding |

The quantum upper also learns a classifier for a fresh clean specimen. Any private classical learner achieving a fixed positive clean-test advantage requires $`\Omega_\varepsilon(d^2)`$ specimens. A matching quantum lower bound is established for identification in the product-encoder model, not for prediction alone or adaptive quantum encoders.

The coherent mechanism combines a short operator-randomizing channel with a public random Clifford orientation. A stronger private-effect Pauli information budget limits classical reports. The result uses established approximate-randomization and discrimination tools; the [related-work account](references/related-work.md) explains the same-source privacy comparison and its inherited ingredients.

## Read the science

Start with the [source, privacy definition and principal theorems](science/model.md). The proof route is:

| To inspect | Read |
|---|---|
| Adaptive private classical lower bound and matching noisy tournament | [Classical reports](science/classical-reports.md) |
| Private randomizer, public flags, Clifford response and collective decoder | [Quantum reports](science/quantum-reports.md) |
| Matching noninteractive quantum identification converse | [Quantum information budget](science/quantum-converse.md) |
| Privacy of a classical snapshot versus an averaged quantum state | [Released registers](science/privacy-registers.md) |
| Randomness, setup, gates, communication, storage and finite precision | [Implementation](science/implementation.md) |
| Meaning, privacy regimes and physical boundaries | [Interpretation](science/interpretation.md) |
| Attribution and source versions | [Related work](references/related-work.md), [bibliography](references/bibliography.md) |
| Finite checks and their scope | [Verification](verification/README.md) |

[The LLM reading guide](llms.txt) maps questions to the authoritative proof files.

## Learn the project

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**. The [Watrous bridge](learning/WATROUS_BRIDGE.md) selects the relevant sections, translates notation and develops the steps from those foundations to this project's private-report learning problem. A complete small example distinguishes a released classical record from an averaged quantum state.

The [30-milestone map](learning/MILESTONES.md) has **14 background/preliminaries milestones** and **16 narrative/innovation milestones**. It moves from one specimen and one measurement to adaptive classical reports, collective quantum reports, the matched identification bounds and their physical limits. Each milestone states an understanding target, earlier dependencies, a conceptual connection and source pointers. The [learning entrypoint](learning/README.md) connects the bridge, map and specialist proofs.

## Reproduce the finite checks

From the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

The deterministic checks address private-effect constants, reverse-divergence budgets, actual-record likelihoods and finite matrix inequalities. They supplement the written proofs. They do not certify a randomly sampled list as private for every input or establish an efficient collective decoder.

## Scope

The privacy parameter is fixed as $`d`$ grows, and the selected randomizer must satisfy its all-state guarantee and finite list-length condition. The result concerns ordinary input-state QLDP, independent one-specimen privatization, and a clean deployment test. Reference-secure privacy, reused hidden encoder keys and joint preprocessing of raw specimens are outside the model.

Both principal sample costs are exponential in $`n`$. Dense randomizer setup and collective decoding can also require exponential computation. An exact tensor-Pauli local implementation gives the larger upper bound $`O_\varepsilon(d(\log d)^7)`$ with a fixed good setup list. No end-to-end runtime advantage is inferred.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
