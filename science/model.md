# Private examples and a common quantum classifier

A data owner can hide one quantum example before releasing it, while a learner still discovers a pattern shared by many owners. The representation of that private release matters. Here the same labeled quantum source is supplied to both learners: one receives private classical reports, and the other may retain private quantum reports until a collective measurement.

With ordinary local privacy the two ways of releasing these examples have different sample costs. [Reference-secure privacy](reference-secure-privacy.md) adds a retained reference to the privacy comparison and quantifies how the separation changes as its dimension grows.

## The source

Let $`n\ge1`$, $`d=2^n`$, and let $`\mathcal P_*`$ contain one Hermitian representative of each nonidentity $`n`$-qubit Pauli operator. Its members obey

```math
P^2=I,\qquad \mathrm{Tr}P=0,\qquad
\mathrm{Tr}(PQ)=d\,\mathbf 1_{\{P=Q\}}.
```

There are $`d^2-1`$ such representatives. The unknown target is a signed Pauli

```math
H\in\mathcal H=\{\pm P:P\in\mathcal P_*\},\qquad
L=|\mathcal H|=2(d^2-1).
```

Each training example consists of an independent fair, public label $`Y\in\{+1,-1\}`$ and one quantum specimen

```math
\rho_{H,Y}=\frac{I+YH}{d}.
```

The examples are independent conditional on the common target. The state is uniform on the $`Y`$ eigenspace of $`H`$. If the target is known, measuring its local Pauli factors and multiplying the outcomes recovers the label perfectly. Every feature state is separable across its $`n`$ qubits.

Only the specimen and its public training label are supplied. The learner receives no classical description of a latent pure preparation, repeat copies of that latent preparation, coherent preparation oracle, or QRAM access. This source and its clean test task are inherited from [the signed-Pauli learning problem](https://github.com/GoGoKo699/Quantum-Learning-Label-Noise/tree/f305698454964e101311b3a337efe49c71808cff); [related work](../references/related-work.md) identifies the inherited and new ingredients.

## Privacy belongs to the released register

Fix a finite privacy parameter $`\varepsilon>0`$. A one-specimen channel $`\Lambda`$ satisfies pure quantum local differential privacy, abbreviated QLDP, when

```math
\Lambda(\rho)\preceq e^\varepsilon\Lambda(\sigma)
\qquad\text{for every pair of input density operators }\rho,\sigma.
```

The order is the positive-semidefinite, or Loewner, order. Equivalently, every event obtained by measuring the released register has probability on one input at most $`e^\varepsilon`$ times its probability on any other input. Privacy is imposed over the entire input state space, including states outside the learning promise.

The label is public and is not protected. Privacy must hold conditional on that label, the preceding available classical history, and every public random choice. Any additional flag released with the quantum or classical report is included in the channel output. The private random index discarded inside a channel is not released. Averaging away a flag that the recipient actually receives cannot establish privacy of that recipient's view; [the register example](privacy-registers.md) makes the distinction explicit.

This is ordinary, unassisted-input QLDP. Its reference-secure extension compares joint inputs with the same marginal on a retained reference of dimension at most $`k`$, after the channel acts locally on the specimen. The reference changes the privacy requirement, while the training source below still supplies independent specimens. With independent product inputs, the one-record Loewner inequality remains valid after tensoring the other fixed reports and applying a collective measurement. Learning the common target from many different owners is compatible with local protection of each owner's individual example.

## The two reporting models

Each owner accesses one raw specimen, uses fresh local ancillas and private randomness, and makes one private release. Raw specimens and client quantum memories do not persist between records. Correlated hidden keys shared between owners are outside both models.

| Resource | Classical reports | Quantum reports used here |
|---|---|---|
| Local access | One raw specimen | One raw specimen |
| Local privacy | Conditional all-input-state $`\varepsilon`$-QLDP | Conditional all-input-state $`\varepsilon`$-QLDP |
| Released register | Any classical report alphabet | A quantum system and public flags |
| Choice of local mechanism | May adapt to every previous classical report | Predetermined product encoders; public randomness allowed |
| Retained learner memory | Unlimited classical memory | Privatized quantum systems and classical flags |
| Final processing | Arbitrary classical computation and a test POVM | Arbitrary collective measurement and computation |

The classical lower bound therefore covers more than a fixed noise channel followed by measurement. It allows the learner to design and adapt its private measurement itself. The coherent upper bound uses a noninteractive product encoder. A separate converse establishes its optimal identification order within that product-encoder class; it does not determine the optimum for adaptive quantum encoders.

Sample budgets are deterministic upper caps. A learner stopping early can be padded with input-independent reports. Bounds on expected stopping time under the target sources alone are not asserted.

## Identification and supervised prediction

In **identification**, the learner outputs the signed Pauli $`\widehat H`$. Upper bounds below control the maximum error over all targets. The product-quantum converse uses a uniform prior, which also bounds any worst-target guarantee.

In **clean-test prediction**, training ends before one fresh, unprivatized specimen $`\rho_{H,Y}`$ arrives with its label hidden. The learner predicts $`Y`$. A classical training transcript may specify any binary test POVM. A constant advantage $`\beta\in(0,1/2)`$ means success at least $`1/2+\beta`$ for every target, averaged over training and test randomness. Privacy of the training reports is the constraint; a constant-accuracy claim for privatized test specimens is not made.

Identification with error $`\delta`$ gives clean-test success at least $`1-\delta`$: on correct identification, a local Pauli measurement is exact. The [prediction-to-identification reduction](reference-secure-privacy.md) gives a bounded-success identifier from any fixed-advantage predictor, including a predictor with a consumable quantum model. The classical prediction converse also follows directly from a bounded-size list extracted from the learned test observable.

## Principal results

For every fixed $`\varepsilon>0`$, fixed $`\delta\in(0,1/2)`$, and fixed $`\beta\in(0,1/2)`$, as $`d=2^n`$ grows:

| Task and reporting model | Required and sufficient training specimens | Authoritative proof |
|---|---:|---|
| Identification, arbitrary adaptive private classical reports | $`\Theta_{\varepsilon,\delta}(d^2)`$ | [Classical reports](classical-reports.md) |
| Constant clean-test advantage, private classical reports | $`\Theta_{\varepsilon,\beta}(d^2)`$ | [Prediction converse and noisy tournament](classical-reports.md) |
| Identification, noninteractive private quantum product encoders | $`\Theta_{\varepsilon,\delta}(d\log d)`$ | [Coherent construction](quantum-reports.md), [quantum converse](quantum-converse.md) |
| Identification with an exact tensor-Pauli local implementation and a fixed good setup list | $`O_{\varepsilon,\delta}(d(\log d)^7)`$ | [Pauli implementation](implementation.md) |

For $`n`$ qubits under ordinary privacy, the predetermined-quantum and adaptive-classical orders are $`\Theta(n2^n)`$ and $`\Theta(4^n)`$, respectively, at fixed privacy and confidence. These orders hold for both identification and fixed-advantage clean prediction.

The [reference-secure theorem](reference-secure-privacy.md) extends the predetermined-encoder law to $`\Theta(dk\log d/\varepsilon^2)`$ for $`1\leq k\leq d`$ and $`0<\varepsilon\leq1`$. With unrestricted reference privacy, the adaptive optimum is $`\Theta(d^2/\varepsilon^2)`$ even with arbitrary retained quantum memory. The feedback chooses the next local encoder using a classical history. With predetermined encoders, classical reports instead require order $`d^2\log d/\varepsilon^2`$ under the same reference bound, since ordinary-private classical effects already protect arbitrary references.

The short-list construction in the ordinary-privacy chapter uses an actual list length $`K\leq d^2/2`$. The reference-secure proof uses a constant-distortion list and separately tunes privacy by an input-independent replacement branch. It gives uniform small-$`\varepsilon`$ scaling and leaves the optimal quantum rate with adaptive encoders open for intermediate reference dimensions.

## Why the representation matters

A private classical effect has a bounded total squared response across the $`d^2-1`$ unknown Pauli directions. Following the adaptive protocol under a common maximally mixed reference source turns this local restriction into a $`d^2`$ sample lower bound. A private quantum report can keep many small noncommuting responses together. An operator-randomizing channel with only order $`d`$ Kraus unitaries retains enough total response energy, and a public random Clifford orientation shares that energy among all targets. A collective decoder combines the weak reports.

Approximate randomization and the general discrimination tools are established ingredients. The operational result is the same-source, same-privacy comparison, including the adaptive classical converse. [Interpretation](interpretation.md) connects the bounds and states their physical limits. [Implementation](implementation.md) accounts for randomizer setup, gates, randomness, communication, storage, and decoding. These are sample-complexity laws; no total runtime advantage is inferred.

## Reading route

Read [classical reports](classical-reports.md) for the private-effect information budget and tournament, [coherent reports](quantum-reports.md) for the construction, [the quantum converse](quantum-converse.md) for its product-encoder optimum, and [privacy registers](privacy-registers.md) for the exact released-record distinction. The [verification guide](../verification/README.md) separates finite checks from the analytical statements.
