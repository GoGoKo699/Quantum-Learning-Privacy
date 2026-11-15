# Coherent private reports

The quantum learner retains the privatized specimens until a collective
identification measurement. The local mechanism is an approximate randomizer,
rather than a depolarizing channel. A public random Clifford orientation makes
its surviving information useful for every target Pauli.

All logarithms below are natural. We write

```math
f(\rho,\sigma)=\Vert\sqrt\rho\sqrt\sigma\Vert_1
```

for **root fidelity**. Some references call its square the fidelity. The
identification error in this chapter is a maximum over targets, rather than
only a uniform-prior average.

## 1. A finite statement

Let $`d=2^n`$, let $`\mathcal P_n`$ contain one Hermitian representative of
every $`n`$-qubit Pauli, including $`I`$, and put

```math
\mathcal H=\{\pm P:P\in\mathcal P_n\setminus\{I\}\},
\qquad L=|\mathcal H|=2(d^2-1).
```

Fix $`0\lt \eta\lt 1`$ and a list of $`K`$ unitaries defining

```math
\Phi(X)=\frac1K\sum_{j=1}^K U_j XU_j^\dagger.
```

Assume the following **all-state operator-randomization guarantee**:

**Equation (1).**

```math
\frac{1-\eta}{d}I\ \le\ \Phi(\rho)\ \le\
\frac{1+\eta}{d}I
\qquad\text{for every density operator }\rho.
```

Assume also $`K\le d^2/2`$. The channel in Section 2 below is
$`\varepsilon_\eta`$-QLDP, where

```math
\varepsilon_\eta=\ln\frac{1+\eta}{1-\eta}.
```

From independently privatized labeled specimens it identifies every
$`H\in\mathcal H`$ with error at most $`\delta\in(0,1)`$ whenever

**Equation (2).**

```math
N\ \ge\
\left\lceil
8(1+\eta)K\ln\frac{L(L-1)}{\delta}
\right\rceil.
```

The decoder is the pretty good measurement on the known family of
privatized states. Equation (2) is an information-theoretic measurement
bound; it supplies no efficient circuit for that decoder.

## 2. The actual released report is private

Let $`\mathcal C_n`$ be the finite Clifford group modulo global phases. For
each specimen independently, choose $`C\in\mathcal C_n`$ uniformly. Apply

```math
\Psi_C=\mathrm{Ad}_{C^\dagger}\circ\Phi\circ
\mathrm{Ad}_C,
\qquad \mathrm{Ad}_C(X)=CXC^\dagger,
```

and release both the classical value $`C`$ and the quantum system. Thus the
one-specimen channel, conditional on the already-public label, is

**Equation (3).**

```math
\Lambda(\rho)=\frac1{|\mathcal C_n|}
\sum_{C\in\mathcal C_n}|C\rangle\langle C|\otimes\Psi_C(\rho).
```

The private random index $`j`$ selecting $`U_j`$ is discarded and is not in
the report. The list of unitaries can be public. Releasing its sampled index
would give a different channel and would invalidate this privacy argument.

By (1), for every $`C`$ and every pair of input states,

```math
\Psi_C(\rho)
\le\frac{1+\eta}{d}I
\le\frac{1+\eta}{1-\eta}\Psi_C(\sigma).
```

The same Loewner inequality holds block by block in (3). Consequently

```math
\Lambda(\rho)\le e^{\varepsilon_\eta}\Lambda(\sigma)
```

for the **actual classical-quantum report**, including its public flag.
This proves ordinary QLDP against every final measurement, even if the
learner combines the report with its other independent privatized systems.
It does not establish reference-extended privacy for an input entangled
with an unrestricted external system.

For the supervised source in the [model](model.md), include the fair public
label $`y`$ as another classical register. The one-specimen state under
target $`H`$ is

```math
\Sigma_H=
\frac1{2|\mathcal C_n|}
\sum_{y=\pm1}\sum_C
|y,C\rangle\langle y,C|\otimes\tau_{H,y,C},
```

where

**Equation (4).**

```math
\tau_{H,y,C}
=\frac{I+yC^\dagger\Phi(CHC^\dagger)C}{d}.
```

Privacy concerns the quantum input conditional on $`y`$. The label's
privacy is not asserted. Conditional on $`H`$, independently generated and
privatized specimens have joint state $`\Sigma_H^{\otimes N}`$.

## 3. A low-Kraus randomizer retains a total signal budget

The normalized Pauli operators $`R/\sqrt d`$ form an orthonormal
Hilbert-Schmidt basis of all complex $`d\times d`$ matrices. Define the
squared Hilbert-Schmidt norm of the channel as a linear superoperator by

```math
S_\Phi=
\sum_{R\in\mathcal P_n}\frac{\Vert\Phi(R)\Vert_2^2}{d}.
```

For unitary conjugation superoperators,

```math
\langle\mathrm{Ad}_{U_i},
\mathrm{Ad}_{U_j}\rangle_{\mathrm{HS(super)}}
=|\mathrm{Tr}(U_i^\dagger U_j)|^2.
```

Therefore

**Equation (5).**

```math
S_\Phi=
\frac1{K^2}\sum_{i,j=1}^K
|\mathrm{Tr}(U_i^\dagger U_j)|^2
\ \ge\ \frac{d^2}{K}.
```

Every summand is nonnegative; the diagonal terms alone give the inequality.
Repeated unitaries in the list cause no problem. Unitality gives
$`\Phi(I)=I`$, so the identity contributes exactly one to $`S_\Phi`$.
It follows that

**Equation (6).**

```math
\mu_\Phi:={\mathbb E}_{R\in\mathcal P_n\setminus\{I\}}
\frac{\Vert\Phi(R)\Vert_2^2}{d}
=\frac{S_\Phi-1}{d^2-1}
\ge\frac{d^2/K-1}{d^2-1}
\ge\frac1{2K}.
```

The final inequality uses $`K\le d^2/2`$. This condition is part of the
finite theorem, not an assumption to suppress in a small-privacy limit.

Equation (6) is an average over Pauli directions. A fixed randomizer may
erase some particular directions entirely. The public Clifford in (3)
is what turns the average into a uniform pair-separation guarantee.

## 4. Public orientation separates every pair of targets

Clifford conjugation sends a fixed nonidentity Pauli to a uniformly random
signed nonidentity Pauli. Thus, for every signed target $`H`$,

```math
\mathbb E_C\frac{\Vert\Phi(CHC^\dagger)\Vert_2^2}{d}=\mu_\Phi.
```

For two targets $`H,G`$ that are not equal up to sign, the mixed inner
product averages to zero:

**Equation (7).**

```math
\mathbb E_C\mathrm{Tr}
\big[\Phi(CHC^\dagger)\Phi(CGC^\dagger)\big]=0.
```

To see this directly, write a uniform Clifford as a symplectic coset
representative followed by an independent uniform Pauli. Conjugation by
that Pauli multiplies $`H`$ and $`G`$ by their respective binary symplectic
characters. Their unsigned labels are distinct nonzero vectors over
$`\mathbb F_2`$, hence linearly independent. The two signs are therefore
independent and their product has mean zero, also after conditioning on
the coset representative. Linearity of $`\Phi`$ proves (7). This argument
applies whether $`H`$ and $`G`$ commute or anticommute.

Combining (6) and (7), distinct targets satisfy

**Equation (8).**

```math
\mathbb E_C\big\Vert
\Phi(CHC^\dagger)-\Phi(CGC^\dagger)
\big\Vert_2^2
\ge\frac dK.
```

If $`G=-H`$, the left side is instead $`4d\mu_\Phi\ge2d/K`$, so (8)
still holds. In (4), conjugation by the same $`C^\dagger`$ and the sign
$`y`$ do not affect the Hilbert-Schmidt distance. Dividing (8) by $`d^2`$
gives

**Equation (9).**

```math
\mathbb E_C
\Vert\tau_{H,y,C}-\tau_{G,y,C}\Vert_2^2
\ge\frac1{dK}.
```

## 5. Bounded output spectra convert signal into fidelity separation

We use the following elementary inequality. If density operators
$`\rho,\sigma`$ obey $`\Vert\rho\Vert_\infty,\Vert\sigma\Vert_\infty\le a`$, then

**Equation (10).**

```math
1-f(\rho,\sigma)
\ge\frac{\Vert\rho-\sigma\Vert_2^2}{8a}.
```

Indeed, choose a unitary $`V`$ attaining Uhlmann's root-fidelity
variational formula, so for $`A=\sqrt\rho`$ and $`B=\sqrt\sigma V`$,

```math
\VertA-B\Vert_2^2=2-2f(\rho,\sigma).
```

The identity

```math
AA^\dagger-BB^\dagger
=(A-B)A^\dagger+B(A^\dagger-B^\dagger)
```

and the Schatten-norm product inequality give

```math
\Vert\rho-\sigma\Vert_2
\le(\VertA\Vert_\infty+\VertB\Vert_\infty)\VertA-B\Vert_2
\le2\sqrt a\sqrt{2-2f(\rho,\sigma)},
```

which proves (10).

All the states in (4) have operator norm at most $`(1+\eta)/d`$, by (1).
Root fidelity of block-diagonal states with the same classical block
probabilities is the corresponding average of block root fidelities.
Applying (9) and (10) therefore yields, uniformly over distinct targets,

**Equation (11).**

```math
1-f(\Sigma_H,\Sigma_G)
\ge\frac{d}{8(1+\eta)}
\mathbb E_{y,C}
\Vert\tau_{H,y,C}-\tau_{G,y,C}\Vert_2^2
\ge\frac1{8(1+\eta)K}.
```

Write $`\gamma=1/[8(1+\eta)K]`$. Tensor-product multiplicativity gives

**Equation (12).**

```math
f(\Sigma_H^{\otimes N},\Sigma_G^{\otimes N})
\le(1-\gamma)^N\le e^{-\gamma N}.
```

## 6. An explicit statistical decoder with worst-target error control

For a finite family $`\{\omega_H:H\in\mathcal H\}`$, the unweighted
pretty good measurement is

```math
T=\sum_H\omega_H,
\qquad M_H=T^{-1/2}\omega_H T^{-1/2},
```

with the inverse on the support of $`T`$. Any missing effect on the
orthogonal complement can be assigned arbitrarily, since none of the
target states reaches it.

Montanaro's mixed-state **worst-case** PGM bound, Lemma 3 of
[*Pretty simple bounds on quantum state discrimination*,
arXiv:1908.08312v2](https://arxiv.org/abs/1908.08312), is

**Equation (13).**

```math
\max_H\bigl[1-\mathrm{Tr}(M_H\omega_H)\bigr]
\le\sum_{H\ne G}f(\omega_H,\omega_G).
```

The sum is over ordered distinct pairs. This is the stated mixed-state
result, not an average-prior bound promoted to a maximum-error claim.
It needs neither pure states nor an additional covariance argument.
The PGM and its fidelity bounds are inherited discrimination tools.

Use $`\omega_H=\Sigma_H^{\otimes N}`$. Equations (12) and (13) give

**Equation (14).**

```math
\max_H\Pr_H\{\widehat H\ne H\}
\le L(L-1)
\exp\!\left[-\frac{N}{8(1+\eta)K}\right].
```

Equation (2) follows. The classical registers in these states are already
measured flags. Because the PGM is block diagonal in the flag sequence,
it can be implemented as a quantum measurement conditioned on their
classical values. The direct protocol retains $`Nn`$ quantum output
qubits, rather than coherently storing the Clifford descriptions.

## 7. Existence, sample rates, and implementation boundaries

The approximate-randomization input is established prior work. Aubrun,
[*On almost randomizing channels with a short Kraus decomposition*,
arXiv:0805.2900v2](https://arxiv.org/abs/0805.2900), Theorem 1 proves the
existence of lists obeying (1) with

```math
K\le A_{\rm H}\,d\eta^{-2}
```

up to integer rounding and an absolute constant. The lists are obtained
from Haar unitaries. For fixed $`\varepsilon>0`$, choose any fixed
$`\eta`$ with $`\varepsilon_\eta\le\varepsilon`$; for example,
$`\eta=\tanh(\varepsilon/2)`$ in the exact-channel statement. For all
sufficiently large $`d`$, the list satisfies $`K\le d^2/2`$, and (2) gives

**Equation (15).**

```math
N=O_\varepsilon\!\left(d[\ln d+\ln(1/\delta)]\right).
```

For small fixed $`0\lt \varepsilon\le1`$, this upper bound has
$`\varepsilon^{-2}`$ dependence, subject to the stated finite
$`K\le d^2/2`$ condition. It is not a uniform separation down to
$`\varepsilon\asymp1/d`$.

Theorem 2 of the same paper applies to any isotropic unitary ensemble,
explicitly including tensor-product Pauli operators, and gives lists of
length

```math
K=O\!\left(d(\ln d)^6\eta^{-2}\right).
```

For this finite, exactly representable Pauli-list variant, (2) gives

**Equation (16).**

```math
N=O_\varepsilon\!\left(d(\ln d)^6
[\ln d+\ln(1/\delta)]\right).
```

At fixed identification error this is $`O_\varepsilon(d(\ln d)^7)`$.
The same finite condition applies; fixed $`\varepsilon`$ and large enough
$`d`$ satisfy it because $`(\ln d)^6=o(d)`$.

These existence theorems allow a **fixed good list** as public setup.
A newly sampled list whose all-state property has not been certified is
not automatically a pure-QLDP implementation: decoder failure
$`\delta`$ cannot absorb a probability of violating privacy. The list
selection, certification boundary, and finite-precision treatment must
remain explicit in any implementation.

For the Pauli variant, the list occupies $`2nK`$ classical bits, apart
from ordinary indexing. Each private branch uses $`O(n)`$ Pauli gates
after a classical random index is sampled, with ordinary classical table
lookup and no QRAM. The public Clifford needs $`O(n^2)`$ description bits
and polynomially many Clifford gates. The discarded private index
requires $`O(\log_2K)`$ random bits with an appropriate exact sampler.
The input and output each have $`n`$ qubits. A general Haar-list branch
requires dense-unitary descriptions and synthesis; its gate cost is not
polynomial in $`n`$.

Neither variant supplies an efficient collective decoder, a practical
dimension crossover, or a total-runtime advantage. The established
conclusion is the specimen-count upper bound with genuine local privacy
for the released flags and quantum systems. The
[classical-report converse](classical-reports.md) supplies the competing
fully adaptive private classical bound.
