# From Watrous to private quantum learning

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (Cambridge University Press, 2018)**. The [author's book page](https://cs.uwaterloo.ca/~watrous/TQI/) provides the standard-layout prepublication manuscript used for the locators below. Page numbers are the printed numbers in that manuscript, not a PDF viewer's page counter. The book is linked, not reproduced here.

The project asks whether one owner's quantum example can be locally private while many owners' examples still reveal a common classifier. Both learners receive the same native quantum data. Their difference is the register released after privatization: an arbitrary classical report, or a quantum report retained for joint processing.

Watrous supplies the language of registers, channels, measurements, distinguishability, entropy and invariant averaging. The privacy constraint and the learning bounds require additional arguments given in this repository. Approximate-randomizer and mixed-state discrimination theorems are research dependencies, identified separately below.

## The experiment in the book's language

There are $`n`$ feature qubits, with dimension $`d=2^n`$. The hidden target $`H`$ is one of the $`2(d^2-1)`$ signed nonidentity Pauli operators. An independent public sign $`Y`$ accompanies each training specimen:

```math
\rho_{H,Y}=\frac{I+YH}{d}.
```

This density operator is uniform on one eigenspace of $`H`$. For example, if $`H=Z\otimes X`$ and $`Y=+1`$, a source can select uniformly from the product eigenstates whose two local eigenvalues multiply to $`+1`$. The learner receives one specimen from that mixture, rather than a description of the selected pure preparation.

An owner applies one channel $`\Lambda`$ before release. Conditional on the public label and public information, privacy requires

```math
\Lambda(\rho)\preceq e^\varepsilon\Lambda(\sigma)
\quad\text{for every pair of input density operators }\rho,\sigma.
```

This is ordinary input-state privacy. To protect a retained reference of dimension at most $`k`$, compare the joint outputs for any two joint inputs with the same reference marginal. The protected reference is a register in the privacy test. The learner may keep an arbitrary quantum memory and raw specimens are privatized independently.

A final collective measurement may discover $`H`$ from many independent private reports. Local privacy protects one record; it does not require the common population pattern to remain hidden.

## Selective reading map

The route below follows the dependencies of this project. Completing the full textbook is unnecessary.

| Project need | Watrous locator | Connection supplied here |
|---|---|---|
| Represent a specimen and its public label | §§2.1.1–2.1.3, pp.58–71; Definition 2.5, p.62 | Treat the label as a classical block and keep track of which registers the learner receives. |
| Represent local release and discarded randomness | §§2.2.1–2.2.2, pp.72–90; Theorem 2.22 | A channel includes private ancillas and discarded environments; a released flag is an additional output. |
| Write a classical report as a POVM | §2.3.1, p.100 onward; Definition 2.34 | Input-state privacy becomes an eigenvalue-ratio constraint on every report effect. |
| Measure total response in a Pauli basis | §1.1.2, Eq.(1.81), p.15; §1.1.3, p.24 onward | Apply the operator inner product to the normalized tensor-Pauli basis; the private-effect variance calculation is local to the project. |
| Relate prediction to discrimination | §§3.1.1–3.1.2, pp.125–138; Theorem 3.4, p.128 | A learned binary test is a POVM. Identification supplies the clean measurement. The project supplies a converse from prediction even when the test acts jointly on quantum memory and the clean system. |
| Combine weak quantum reports | Definition 3.11, p.139; §3.2.2 and Theorem 3.22, p.151 | Use root fidelity, a project-specific spectral estimate, then an imported quantitative mixed-state discrimination bound. |
| Bound information in reports | §§5.1.1–5.1.2, pp.250–264; §§5.2.1–5.2.3, pp.265–282; Theorem 5.35, p.280 | Classical transcript chain rules and a quadratic quantum-response bound supply the two converses. |
| Turn information into identification cost | §5.3.3, p.294 onward; Theorem 5.49, p.299 | Combine the Holevo bound with the general finite-alphabet Fano calculation written below. |
| Average over unknown directions | §7.1.1, p.391 onward; §7.2.1 and Lemma 7.24, p.416 | Compare the two-copy pure-state moment with the rank-projector calculation used for reference protection. |

The [30 milestones](MILESTONES.md) place these foundations before the project's privacy and learning arguments. The [scientific model](../science/model.md) remains authoritative for theorem domains.

## Notation and convention dictionary

| Book convention | Convention in this project |
|---|---|
| A vector $`u`$ and the operator $`uu^*`$ | Often written $`\lvert u\rangle`$ and $`\lvert u\rangle\langle u\rvert`$. |
| $`A^*`$, $`1_{\mathcal X}`$, measurement operator $`\mu(z)`$ | $`A^\dagger`$, $`I`$, and POVM effect $`E_z`$. |
| $`\langle A,B\rangle=\mathrm{Tr}(A^*B)`$ | The same operator inner product. For Hermitian Paulis, $`\mathrm{Tr}(PQ)=d\delta_{P,Q}`$. |
| Unsubscripted operator norm $`\Vert A\Vert`$ | Written $`\Vert A\Vert_\infty`$ when contrasted with Schatten norms. $`\Vert A\Vert_2`$ is the Hilbert–Schmidt norm. |
| Fidelity $`F(\rho,\sigma)=\Vert\sqrt\rho\sqrt\sigma\Vert_1`$ | The same quantity is denoted $`f`$ when root fidelity needs emphasis. Squared fidelity is $`f^2`$. |
| Base-two logarithms in entropy and relative entropy, explicitly fixed on p.251 | Natural logarithms in the proofs here. Thus $`D_{\mathrm{nat}}=(\ln2)D_{\mathrm{book}}`$; information inequalities keep their form when every term uses the same base. |
| Entropy often denoted $`H`$ | The italic target symbol $`H`$ here also denotes a signed Pauli. Its role is fixed by context; $`h_2`$ is binary entropy with the logarithm base declared in the proof. |

The success probability for equal-prior binary discrimination is $`1/2+\Vert\rho-\sigma\Vert_1/4`$. A half-trace-distance convention would therefore put an additional factor of two in the advantage. Fidelity and distance conventions should be checked before transferring a cited bound.

## A complete one-qubit experiment

This example illustrates the registers and privacy definition. It is not a small-dimension demonstration of the asymptotic sample separation.

Let $`n=1`$, so the target set is

```math
\mathcal H=\{+X,-X,+Y,-Y,+Z,-Z\}.
```

If the target is $`H=Z`$, a public label $`y=+1`$ accompanies $`|0\rangle`$, and $`y=-1`$ accompanies $`|1\rangle`$. A learner that knows $`H`$ measures $`Z`$ on a fresh clean specimen and predicts its hidden label without error.

### A private classical report

Choose a known axis $`A\in\{X,Y,Z\}`$. Measure it, then flip the measured sign independently with probability $`1/4`$. The released sign $`z\in\{\pm1\}`$ has effects

```math
E_z=\frac12\left(I+\frac z2 A\right).
```

Each effect has eigenvalues $`3/4`$ and $`1/4`$. Hence for every pair of input states the probability ratio of any one-sign event is at most $`3`$. The report is $`\varepsilon=\log3`$ private, including inputs outside the six-target promise.

For a training specimen the exact likelihood is

```math
\Pr[z\mid H,y,A]
=\frac12\left(1+\frac{zy}{2}\frac{\mathrm{Tr}(AH)}2\right).
```

When $`A=H`$, the product $`yz`$ has mean $`1/2`$; when $`A=-H`$, its mean is $`-1/2`$; for either perpendicular axis it has mean zero. Thus the report probes a chosen direction.

The axis may itself be chosen uniformly and released. Its choice is input-independent, and the privacy bound holds separately for each axis. The full report is then $`(A,z)`$. Averaging away $`A`$ is unnecessary and would describe a different recipient's information.

### A private quantum report

Instead release the qubit after the depolarizing channel

```math
\Lambda(\rho)=\frac12\rho+\frac12\frac I2.
```

Every output has eigenvalues between $`1/4`$ and $`3/4`$, so the Loewner privacy inequality holds with the same $`\log3`$ parameter. The training output is

```math
\Lambda(\rho_{H,y})=\frac12\left(I+\frac y2 H\right).
```

It retains a weak response in the unknown target direction. The learner still has a quantum system on which later joint measurements can act. The public training label must be retained: forgetting it and averaging over $`y`$ gives $`I/2`$ for every target.

For equal public labels, root fidelity between two reports from opposite target signs is $`\sqrt{3}/2`$; between perpendicular target axes it is $`\sqrt{7/8}`$. These are explicit mixed-qubit values below one. They illustrate why many weak reports can be discriminated collectively. The large-dimension theorem uses a different randomizer whose response budget scales more favorably than depolarization.

### What changes when a reference is kept

In the reference test, the two candidate joint inputs to the report have the same marginal on the kept reference $`R`$. The classical report above keeps its $`\log 3`$ guarantee for every reference size. In each sign branch, the eigenvalue bounds on $`E_z`$ put the unnormalized reference output between $`\rho_R/4`$ and $`3\rho_R/4`$. Positivity is preserved when the measurement outcome is obtained by a partial trace.

For the quantum report, compare two different Bell states. Each has reference marginal $`I/2`$. Writing $`\Lambda_a`$ for the depolarizing channel with retention $`a`$, the output on a Bell state $`\Phi`$ is

```math
(\Lambda_a\otimes\mathrm{id})(\Phi)
=a\Phi+(1-a)\frac{I_4}{4}.
```

Measuring the projector onto the first Bell state gives event probabilities $`(1+3a)/4`$ and $`(1-a)/4`$. At the original retention $`a=1/2`$, their ratio is 5. This pair alone defeats a full-reference budget of $`\log 3`$. The ratio 5 also bounds the worst pair. For every pure two-qubit input $`\psi`$, Schmidt decomposition and Cauchy–Schwarz give $`\psi\preceq 2 I_2\otimes\rho_R`$. The inequality extends to mixed inputs, so each joint output lies between $`(1-a)I_2\otimes\rho_R/2`$ and $`(1+3a)I_2\otimes\rho_R/2`$. Choosing $`a=1/3`$ therefore restores $`\log 3`$ privacy for the full reference while retaining a weaker signal.

The retained reference here is part of the privacy test. The learner's memory is built from reports during training and appears in a different part of the argument.

### Why a hidden random choice must stay hidden

The same channel has the random-Pauli realization

```math
\Lambda(\rho)=\frac58\rho+
\frac18X\rho X+\frac18Y\rho Y+\frac18Z\rho Z.
```

Its random Pauli index is discarded. If that index were released with the output qubit, the recipient could invert the selected Pauli and recover the raw input. Equivalently, in any fixed branch an output event can distinguish two orthogonal pure inputs with positive versus zero probability. No finite all-input privacy parameter would protect that flagged release.

There is no conflict between this observation and a public independent axis in the classical protocol: each classical axis branch is already private. A quantum randomizer's reversible Kraus branch is not.

The full-dimensional [released-register example](../science/privacy-registers.md) develops the same distinction for shadow-state preparations and their classical descriptions.

## The steps the book does not supply

### Classical reports: from one effect to an adaptive transcript

Watrous's POVM framework lets the privacy condition be tested on extremal input eigenvectors. For a nonzero private effect, normalize it as $`B=E/\mathrm{Tr}E`$. The project then proves

```math
d\mathrm{Tr}(B^2)-1
\leq \sinh^2(\varepsilon/2).
```

Expanding $`B`$ in the orthogonal tensor-Pauli basis turns this into a total squared-response budget. This is a project calculation, not an extra textbook theorem.

Adaptivity is handled by evaluating every next mechanism under the same maximally mixed reference transcript. Expanding the logarithm of conditional likelihood ratios gives the classical relative-entropy chain rule. The two target signs cancel the linear term. The resulting summed reverse-relative-entropy budget yields the $`d^2`$ converse. Its matching noisy tournament is also supplied here.

See [classical reports](../science/classical-reports.md), including the bounded-list argument for clean prediction. The proof does not assume that a good predictor reveals the target.

### Quantum reports: randomization plus surviving response

The book's channel and invariant-measure language supports the calculation, but the short operator-randomizer existence theorem is imported from Aubrun. A low-Kraus-count random-unitary channel cannot erase all its Pauli energy. Public Clifford conjugation distributes that remaining energy over every pair of unknown targets while the private Kraus index stays discarded.

The project converts this average squared distance to a root-fidelity gap using the output spectral bound. A quantitative mixed-state PGM bound, imported from the research literature, then gives the identification construction. [Quantum reports](../science/quantum-reports.md) gives the complete proof; [related work](../references/related-work.md) and [bibliography](../references/bibliography.md) identify the imported statements and their versions.

### The product-encoder converse: averaging and information

Lemma 7.24 gives the two-copy identity

```math
\mathbb E_{\psi}\psi^{\otimes2}
=\frac{I+F}{d(d+1)},
```

where $`F`$ swaps the copies. Pauli orthogonality turns it into

```math
\mathbb E_\psi[
\mathrm{Tr}(P\psi)\mathrm{Tr}(Q\psi)]
=\frac{\delta_{P,Q}}{d+1}
```

for nonidentity Paulis. The project applies this to a private channel, obtaining an average target-information budget of order $`1/d`$ per report at fixed privacy.

The inequality bounding quantum relative entropy by a quadratic Petz expression is proved directly in [the quantum converse](../science/quantum-converse.md); it is not attributed to an unverified textbook theorem. The same chapter explains why Holevo information can be summed for the predetermined product encoders considered here. The reverse-null comparison below handles classical feedback with a retained quantum memory.

For completeness, the general finite-alphabet Fano step is elementary. Let $`H`$ be uniform on $`L`$ targets and let $`\widehat H`$ have error probability $`\delta`$. Introduce the binary error indicator. Conditional on an error, at most $`L-1`$ target values remain, so

```math
H(H\mid\widehat H)
\leq h_2(\delta)+\delta\log(L-1).
```

Subtracting from $`H(H)=\log L`$ gives

```math
I(H:\widehat H)
\geq(1-\delta)\log L-h_2(\delta).
```

Watrous's Holevo theorem controls the information accessible to the final measurement. The displayed general Fano form is supplied here; the book's Lemma 5.54 concerns a binary special case.

### Larger references tighten the report budget

Watrous's purification and Choi representations explain why a reference of dimension $`k`$ reveals directions associated with Schmidt rank up to $`k`$. In the [reference-secure construction](../science/reference-secure-privacy.md), an operator-spectral estimate on these directions gives a channel whose every tested output lies near replacement in positive-semidefinite order. The list of hidden unitaries has length $`O(dk)`$. The estimate requires a single good list simultaneously valid on all rank-constrained directions. Its public orientation is permitted because the same guarantee holds in each orientation.

The per-report converse tests a maximally entangled input supported on a random $`k`$-dimensional subspace against a decorrelated input with the same reference marginal. Unitary invariance reduces the projector's second moment to the identity and the swap. This is the rank-$`k`$ extension of the pure-state moment above. In the Pauli basis, the resulting budget bounds averaged target divergences by order $`\varepsilon^2/(dk)`$ for $`0\lt\varepsilon\le1`$. Positive-semidefinite order controls support during the conversion into both directions of relative entropy.

Predetermined encoders accumulate the forward budget and use Holevo and Fano to identify the signed target. When a classical history chooses the next encoder, the reverse comparison instead averages histories under the same null for every target. The fresh report joins the previously retained quantum state by a tensor product conditional on that history. The learner can then apply an arbitrary joint instrument. Relative-entropy data processing gives the adaptive lower bound without imposing a dimension bound on the learner's memory.

### Turn one prediction test into an identification measurement

Watrous's notation for POVMs gives a single binary observable $`B`$ on trained memory and a clean test system. Let $`A_P`$ be the operator on memory obtained by taking the Pauli coefficient of $`B`$ on the test system. The partial trace of $`B^2`$ gives the operator-valued Parseval inequality

```math
\sum_{P} A_P^2=\frac{\mathrm{Tr}_{\rm test}(B^2)}{d}\preceq I.
```

For a signed target $`\pm P`$, the effect $`(\pm A_P)_+^2`$ uses the squared positive part, retaining only the eigenvalues with the required sign. The effects sum to at most identity because the two signed effects for each Pauli sum to $`A_P^2`$. Completing them by a failure effect gives an identification POVM on one copy of the trained quantum memory. Clean prediction advantage $`\beta`$ gives signed identification success of at least $`4\beta^2`$ in the same worst-case or prior-average convention. This transfers the identification converses to a joint prediction test that consumes its memory.

## Reassemble the claim with its limits

At fixed positive privacy and fixed performance, the specimen cost of predetermined local encoders is $`\Theta_\varepsilon(dk\log d)`$ for signed identification and clean prediction. The order becomes $`\Theta(dk\log d/\varepsilon^2)`$, uniformly for $`0\lt\varepsilon\le1`$. At $`k=1`$ this gives the original quantum identification order and a matching quantum prediction cost. The adaptive lower bound is $`\Omega_\varepsilon(dk)`$, attained at full reference dimension $`k=d`$ by the classical noisy tournament, which remains valid for every reference dimension.

The model uses independent native specimens, public labels, one private release per specimen, fresh local randomness and a clean deployment test. Feedback in the adaptive analysis is classical. Randomizer setup, certification, synthesis, communication, coherent storage and collective decoding are separate costs. The tensor-Pauli implementation for ordinary privacy uses more specimens by a polylogarithmic factor. See [implementation](../science/implementation.md) for the resource accounting and [reference-secure privacy](../science/reference-secure-privacy.md) for the adaptive bounds at intermediate reference size.

The [milestone map](MILESTONES.md) connects these steps from one report through the full-reference comparison.
