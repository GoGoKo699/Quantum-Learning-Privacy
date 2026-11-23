# Private examples and a common quantum classifier

A data owner can hide one quantum example before releasing it, while a learner still discovers a pattern shared by many owners. The representation of that private release matters. Here the same labeled quantum source is supplied to both learners: one receives private classical reports, and the other may retain private quantum reports until a collective measurement.

The resulting sample separation survives every fixed positive local-privacy level as the number of qubits grows. It does not rely on replacing classical examples with more informative quantum examples. It compares two ways of releasing the same native quantum data under the same privacy definition.

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

This is ordinary input-state QLDP. The [reference-secure extension](reference-secure-learning.md) compares $`(\Lambda\otimes\mathrm{id}_R)(\rho_{AR})\preceq e^\varepsilon(\Lambda\otimes\mathrm{id}_R)(\sigma_{AR})`$ for every joint input pair with $`\rho_R=\sigma_R`$. The guarantee can bound $`\dim R`$ by $`r`$ or allow all references. The training distribution stays the same. With independent product inputs, the one-record Loewner inequality remains valid after tensoring the other fixed reports and applying a collective measurement. Learning the common target from many different owners is compatible with local protection of each owner's individual example.

## Reporting and feedback

Each owner accesses one raw specimen, uses fresh local ancillas and private randomness, and makes one private release. Raw specimens and client quantum memories do not persist between records. Correlated hidden keys shared between owners are outside both models.

| Resource | Classical reports | Quantum reports used here |
|---|---|---|
| Local access | One raw specimen | One raw specimen |
| Local privacy | Conditional on public information and the actual classical report | Same condition for the quantum report and every released flag |
| Released register | Any classical report alphabet | A quantum system and public flags |
| Choice of local mechanism | Fixed schedule or classical feedback | Fixed schedule or classical feedback obtained from instruments on the learner's report memory |
| Retained learner memory | Unlimited classical memory | Privatized quantum systems and classical flags |
| Final processing | Arbitrary classical computation and a test POVM | Arbitrary collective measurement and computation |

The classical lower bound therefore covers more than a fixed noise channel followed by measurement. It allows the learner to design and adapt its private measurement itself. The coherent upper bound uses a noninteractive product encoder. The [product converse](quantum-converse.md) establishes its optimal ordinary-privacy identification order. The reference-secure extension allows classical outcomes from instruments on previous reports to select the next encoder. Conditional on the target and classical history, fresh reports factor from the current quantum memory.

Sample budgets are deterministic upper caps. A learner stopping early can be padded with input-independent reports. Bounds on expected stopping time under the target sources alone are not asserted.

## Identification and supervised prediction

In **identification**, the learner outputs the signed Pauli $`\widehat H`$. Upper bounds below control the maximum error over all targets. The product-quantum converse uses a uniform prior, which also bounds any worst-target guarantee.

In **clean-test prediction**, training ends before one fresh, unprivatized specimen $`\rho_{H,Y}`$ arrives with its label hidden. The learner predicts $`Y`$. A classical training transcript may specify any binary test POVM. A learner retaining quantum reports may measure them together with the test specimen. A constant advantage $`\beta\in(0,1/2)`$ means success at least $`1/2+\beta`$ for every target, averaged over training and test randomness. Privacy of the training reports is the constraint; a constant-accuracy claim for privatized test specimens is not made.

Identification with error $`\delta`$ gives clean-test success at least $`1-\delta`$: on correct identification, a local Pauli measurement is exact. The reverse implication is not assumed. The classical prediction converse is proved directly using a bounded-size list extracted from the learned test observable.

## Principal results

For fixed positive privacy and fixed target error or clean-test advantage, the [reference-secure results](reference-secure-learning.md) give the following orders.

| Privacy and task | Reporting model | Specimens |
|---|---|---:|
| Reference dimension at most $`r`$, identification | Product quantum reports | $`\Theta_{\varepsilon,\delta}(dr\log d)`$ |
| Any reference bound, identification | Noninteractive classical reports | $`\Theta_{\varepsilon,\delta}(d^2\log d)`$ |
| Unrestricted reference, identification | Classical feedback with arbitrary quantum report memory | $`\Theta_{\varepsilon,\delta}(d^2)`$ |
| Unrestricted reference, clean-test prediction | Classical feedback with arbitrary quantum report memory | $`\Theta_{\varepsilon,\beta}(d^2)`$ |

Under ordinary privacy, for fixed $`\varepsilon>0`$, identification error $`\delta\in(0,1/2)`$, and clean-test advantage $`\beta\in(0,1/2)`$, the baseline results are:

| Task and reporting model | Required and sufficient training specimens | Authoritative proof |
|---|---:|---|
| Identification, arbitrary adaptive private classical reports | $`\Theta_{\varepsilon,\delta}(d^2)`$ | [Classical reports](classical-reports.md) |
| Constant clean-test advantage, private classical reports | $`\Theta_{\varepsilon,\beta}(d^2)`$ | [Prediction converse and noisy tournament](classical-reports.md) |
| Identification, noninteractive private quantum product encoders | $`\Theta_{\varepsilon,\delta}(d\log d)`$ | [Coherent construction](quantum-reports.md), [quantum converse](quantum-converse.md) |
| Identification with an exact tensor-Pauli local implementation and a fixed good setup list | $`O_{\varepsilon,\delta}(d(\log d)^7)`$ | [Pauli implementation](implementation.md) |

The ordinary-privacy product construction also predicts clean test labels at the same sample order. Its ordinary-privacy converse concerns target identification. For $`n`$ qubits, the principal identification orders are $`\Theta(n2^n)`$ and $`\Theta(4^n)`$ at fixed privacy and confidence. Both grow exponentially in $`n`$; their ratio is exponential as well.

The fixed-privacy limit matters: $`\varepsilon`$ is held independent of $`d`$. The randomizer construction requires sufficiently large $`d`$, with its actual list length $`K\le d^2/2`$. The reference-secure result gives the matching feedback endpoint under unrestricted reference privacy. Intermediate reference dimensions with feedback remain open.

## Why the representation matters

A private classical effect has a bounded total squared response across the $`d^2-1`$ unknown Pauli directions. Following the adaptive protocol under a common maximally mixed reference source turns this local restriction into a $`d^2`$ sample lower bound. A private quantum report can keep many small noncommuting responses together. An operator-randomizing channel with only order $`d`$ Kraus unitaries retains enough total response energy, and a public random Clifford orientation shares that energy among all targets. A collective decoder combines the weak reports.

Approximate randomization and the general discrimination tools are established ingredients. The operational result is the same-source, same-privacy comparison, including the adaptive classical converse. [Interpretation](interpretation.md) connects the bounds and states their physical limits. [Implementation](implementation.md) accounts for randomizer setup, gates, randomness, communication, storage, and decoding. These are sample-complexity laws; no total runtime advantage is inferred.

## Reading route

Read [classical reports](classical-reports.md) for the private-effect information budget and tournament, [coherent reports](quantum-reports.md) for the construction, [the quantum converse](quantum-converse.md) for its product-encoder optimum, [reference-secure learning](reference-secure-learning.md) for the dependence on reference dimension and classical feedback, and [privacy registers](privacy-registers.md) for the released-record distinction. The [verification guide](../verification/README.md) separates finite checks from the analytical statements.
