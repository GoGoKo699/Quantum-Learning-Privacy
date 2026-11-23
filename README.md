# Quantum Learning Privacy

**How much can quantum training reports help when privacy must protect a retained reference?** The answer depends on the reference dimension, even when every learner receives examples from the same source.

Each example supplies a fair public label and one native quantum specimen. The unknown classifier is a signed Pauli operator on $`n`$ qubits. Write $`d=2^n`$ for the specimen dimension and $`k`$ for the dimension of a reference that may be entangled with a private input.

| Privacy and control | Optimal training specimens at fixed error or prediction advantage |
|---|---:|
| Reference dimension $`1\leq k\leq d`$, predetermined quantum reports and collective decoding | $`\Theta(dk\log d/\varepsilon^2)`$ |
| Same reference bound, predetermined classical reports | $`\Theta(d^2\log d/\varepsilon^2)`$ |
| Unrestricted reference, classical feedback and arbitrary learner quantum memory | $`\Theta(d^2/\varepsilon^2)`$ |

These orders hold uniformly for $`0<\varepsilon\leq1`$. They apply both to identifying the signed Pauli and to predicting the label of one fresh clean specimen. At fixed encoder schedules the quantum sample advantage has order $`d/k`$. The ordinary local-privacy separation is the $`k=1`$ case. With unrestricted reference privacy, a classical adaptive tournament attains the same optimum as a learner with quantum memory. For intermediate $`k`$, the exact adaptive rate remains open.

The [reference-secure proof](science/reference-secure-privacy.md) connects privacy to a bound on the total information a report can retain across Pauli directions. A short unitary list matches the predetermined-encoder bound. A measurement on the trained memory converts a successful clean-test predictor into a bounded-success identifier, even when the prediction would have consumed the memory.

## Read the science

Start with the [source, privacy definition and principal theorems](science/model.md). The proof route is:

| To inspect | Read |
|---|---|
| Reference-secure privacy, matching sample laws and prediction from consumable memory | [Reference-secure learning](science/reference-secure-privacy.md) |
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

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**. The [Watrous bridge](learning/WATROUS_BRIDGE.md) selects the relevant sections, translates notation and develops the steps from those foundations to this project's private-report learning problem. Worked examples distinguish a released classical record from an averaged quantum state and show how an entangled reference changes a privacy calculation.

The [30-milestone map](learning/MILESTONES.md) has **14 background/preliminaries milestones** and **16 narrative/innovation milestones**. It moves from one specimen and one measurement to adaptive classical reports, collective quantum reports, the matched identification bounds and their physical limits. Each milestone states an understanding target, earlier dependencies, a conceptual connection and source pointers. The [learning entrypoint](learning/README.md) connects the bridge, map and specialist proofs.

## Reproduce the finite checks

From the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

The deterministic checks cover private-report information budgets, compressed Pauli moments, and the signed predictor measurement. They supplement the written proofs. They do not certify a randomly sampled list as private for every input or establish an efficient collective decoder.

## Scope

The result concerns independent one-specimen releases and a clean deployment test. Privacy holds at each public label and encoder choice and includes every released flag. With feedback, local encoders can depend on the learner’s preceding classical record. The learning model supplies fresh client randomness and counts each training specimen once.

The sample costs grow exponentially in $`n`$. Dense randomizer setup and collective decoding can also require exponential computation. The ordinary-privacy tensor-Pauli implementation uses a fixed good list and gives the separate upper bound $`O_\varepsilon(d(\log d)^7)`$.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
