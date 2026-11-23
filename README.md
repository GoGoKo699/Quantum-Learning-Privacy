# Quantum Learning Privacy

**How much does quantum memory help when a private training report can be measured together with an entangled reference?**

The task is to learn a hidden signed Pauli classifier from native $`n`$-qubit examples. Each owner privatizes one specimen and releases a classical or quantum report. Training labels are public, and the privacy condition includes every released flag.

Let $`d=2^n`$ and let $`r`$ be the largest dimension of the external reference protected by the privacy guarantee. At fixed positive privacy $`\varepsilon`$ and fixed bounded identification error, the same source gives the following costs.

| Encoder choices | Reference privacy | Classical reports | Quantum reports |
|---|---|---:|---:|
| Fixed before receiving reports | $`1\le r\le d`$ | $`\Theta_\varepsilon(d^2\log d)`$ | $`\Theta_\varepsilon(dr\log d)`$ |
| Classical feedback | Arbitrary reference dimension | $`\Theta_\varepsilon(d^2)`$ | $`\Theta_\varepsilon(d^2)`$ |

At $`r=1`$ the guarantee is ordinary input-state local privacy. With fixed encoders, protecting an $`r`$-dimensional reference reduces the quantum sample advantage to a factor of order $`d/r`$. Under unrestricted reference privacy, classical feedback attains the quadratic cost even when the learner can retain quantum reports and measure them jointly. The same feedback cost applies to a fixed positive advantage on a fresh clean test specimen. The optimal feedback cost for intermediate $`r`$ remains open.

The [reference-secure proof](science/reference-secure-learning.md) bounds the information available in one report and gives a matching construction with short random-unitary lists. The [related-work account](references/related-work.md) gives the privacy definition and the sources of the randomization and discrimination tools.

## Read the science

Start with the [source, privacy definition and principal theorems](science/model.md). The proof route is:

| To inspect | Read |
|---|---|
| Reference privacy, matched product bounds and the feedback endpoint | [Reference-secure learning](science/reference-secure-learning.md) |
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

The deterministic checks address private-effect constants, reverse-divergence budgets, actual-record likelihoods, finite matrix inequalities, and the reference-dependent Pauli information budget. They supplement the written proofs. They do not certify a randomly sampled list as private for every input or establish an efficient collective decoder.

## Scope

Training uses independent native specimens and fresh local encoders. Feedback chooses the next encoder through a classical record. The privacy reference belongs to the channel's guarantee, and the learner's report memory can be arbitrarily large. Reused hidden encoder keys, coherent feedback into encoders, and joint access to raw specimens are outside the model.

Dense randomizer setup and collective decoding can also require exponential computation. For ordinary input-state privacy, an exact tensor-Pauli local implementation gives the separate upper bound $`O_\varepsilon(d(\log d)^7)`$ with a fixed good setup list. These results count specimens.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
