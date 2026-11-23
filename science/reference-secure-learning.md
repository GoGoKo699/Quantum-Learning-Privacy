# Learning under reference-secure local privacy

The amount of side information covered by the privacy guarantee changes the specimen cost of learning a hidden signed Pauli. With a reference of dimension at most $`r`$, noninteractive quantum reports need order $`dr\log d`$ specimens at fixed privacy and confidence. Here $`d`$ is the dimension of the specimen. Classical reports with the same noninteractive restriction need order $`d^2\log d`$ specimens, because private classical reports already protect arbitrary quantum references. Under unrestricted reference privacy, feedback reduces both costs to order $`d^2`$. That feedback law allows the learner to retain quantum reports and process them jointly.

## Model and statements

Use the [signed-Pauli source](model.md) with $`d=2^n`$, $`n\geq1`$. Write $`\mathcal P_*`$ for the $`M=d^2-1`$ nonidentity Hermitian Paulis, with $`\mathrm{Tr}(PQ)=d\mathbf 1_{P=Q}`$. The $`L=2M`$ possible targets are $`H\in\mathcal H=\{\pm P:P\in\mathcal P_*\}`$. Each fresh public fair label $`y\in\{+1,-1\}`$ comes with one specimen $`\rho_{H,y}=(I+yH)/d`$. Specimens are independent conditional on the target and labels. A local channel $`\Lambda:A\to Q`$ releases one complete report, including any flags that its output carries. Privacy is conditional on the public label and every externally chosen setting of the channel. All logarithms are natural.

For $`1\leq r\leq d`$, a channel is **$`r`$-reference-secure at level $`\varepsilon`$** if, for every reference $`R`$ of dimension at most $`r`$ and every pair of states $`\xi_{RA},\zeta_{RA}`$ with $`\xi_R=\zeta_R`$,

```math
(\mathrm{id}_R\otimes\Lambda)(\xi_{RA})
\preceq e^\varepsilon(\mathrm{id}_R\otimes\Lambda)(\zeta_{RA}).
```

Testing all effects on $`RQ`$ is equivalent to this operator inequality. Equal reference marginals mean that the reference alone contains the same information in the two privacy experiments. The case $`r=1`$ is [ordinary all-input local privacy](model.md). At $`r=d`$, the bounds below hold also when the privacy contract requires the inequality for references of arbitrary finite dimension. The actual learning experiment still supplies the learner only the private reports and public labels. The reference occurs in the channel's privacy test, never as extra training data or a limit on decoder memory.

In the **product model**, the encoder sequence is specified by the labels and independent public coins. Conditional on those variables and the fixed target, reports are independent. A collective decoder with arbitrary quantum memory is allowed. In the **classical-feedback model**, the learner can retain quantum memory and apply an arbitrary instrument between releases. Only the classical history from those instruments is sent to each fresh owner to select the next channel. The selected channel acts on the fresh single specimen using a fresh local environment, with no client–learner shared private randomness or quantum state. Consequently, conditional on the target and history, the new report is in product with the learner's preceding memory before the learner processes them together. The number of specimens is bounded on every branch. These conditions exclude an owner applying a channel jointly to a raw specimen and a quantum message from the learner.

| Reporting model | Specimens for worst-case identification |
| --- | --- |
| Quantum product reports, reference dimension at most $`r`$ | $`\Theta_\varepsilon(dr\log d)`$ |
| Classical product reports, reference dimension at most $`r`$ | $`\Theta_\varepsilon(d^2\log d)`$ |
| Classical feedback with arbitrary quantum report memory, full reference privacy | $`\Theta_\varepsilon(d^2)`$ |

The table fixes $`\varepsilon>0`$ and an identification error $`0<\delta<1/2`$. For fixed error above $`1/4`$, the same lower orders follow from the displayed divergences and the upper orders from using target error $`1/4`$. More explicitly, uniformly for $`0<\varepsilon\leq1`$ and $`0<\delta\leq1/4`$, the three orders are $`dr\varepsilon^{-2}[\log d+\log(1/\delta)]`$, $`d^2\varepsilon^{-2}[\log d+\log(1/\delta)]`$, and $`d^2\varepsilon^{-2}\log(1/\delta)`$, respectively. In the last model, any fixed positive prediction advantage on one fresh clean test specimen also has order $`d^2`$ at fixed privacy, or $`d^2/\varepsilon^2`$ for $`0<\varepsilon\leq1`$, with constants depending on the required advantage. The feedback converse at intermediate $`r`$ gives an order-$`dr`$ lower bound at fixed privacy and confidence. A matching intermediate-reference feedback rate is open here.

## A compressed Choi identity

Fix one channel and put $`\tau=\Lambda(I/d)`$ and $`A_P=\Lambda(P)/d`$. Work on the support of $`\tau`$. Ordinary local privacy follows by taking a trivial reference, and comparison to $`I/d`$ gives $`e^{-\varepsilon}\tau\preceq\Lambda(\rho)\preceq e^\varepsilon\tau`$ for every state $`\rho`$. Thus all output operators are supported there.

Let $`V:\mathbb C^r\to\mathbb C^d`$ be an isometry, with orthonormal columns $`v_i`$. Let $`\varphi_V`$ be the projector onto $`r^{-1/2}\sum_i|i\rangle_R\otimes|v_i\rangle_A`$. It has the same reference marginal as $`I_R/r\otimes I_A/d`$. Set

```math
J_V=(\mathrm{id}_R\otimes\Lambda)(\varphi_V),
\qquad T=I_R/r\otimes\tau.
```

Reference privacy in both directions gives $`e^{-\varepsilon}T\preceq J_V\preceq e^\varepsilon T`$. With $`Z=T^{-1/2}J_VT^{-1/2}`$, the eigenvalues of $`Z`$ lie in $`[e^{-\varepsilon},e^\varepsilon]`$ and $`\mathrm{Tr}(TZ)=1`$. Applying $`(Z-e^{-\varepsilon}I)(e^\varepsilon I-Z)\succeq0`$ inside a trace against $`T`$ gives

```math
\mathrm{Tr}[(J_V-T)T^{-1}(J_V-T)]
=\mathrm{Tr}[T(Z-I)^2]
\leq C_\varepsilon,
\qquad C_\varepsilon=4\sinh^2(\varepsilon/2).
```

Write $`\|X\|_\tau^2=\mathrm{Tr}(X^\dagger\tau^{-1}X)`$ and $`B_{ij}=|i\rangle\langle j|-\mathbf 1_{i=j}I/d`$, using the first $`r`$ coordinates of $`\mathbb C^d`$. Choose $`V`$ to consist of the first $`r`$ columns of a uniform Clifford $`C`$. The blocks of $`J_V-T`$ are $`\Lambda(CB_{ij}C^\dagger)/r`$. Therefore the left side of the preceding bound is

```math
\frac1r\sum_{i,j=1}^r\|\Lambda(CB_{ij}C^\dagger)\|_\tau^2.
```

For any complex traceless matrix $`B=\sum_{P\in\mathcal P_*}b_PP`$, the Pauli factor of a uniform Clifford averages away the cross terms in this squared norm. Indeed the independent sign characters of two distinct Pauli labels have product mean zero. The remaining Clifford action is transitive on the unsigned nonidentity labels, so each diagonal term averages to $`M^{-1}\sum_P\|\Lambda(P)\|_\tau^2`$. Since $`\sum_P|b_P|^2=\|B\|_2^2/d`$, with $`\|\cdot\|_2`$ the Hilbert–Schmidt norm, this proves

```math
\mathbb E_C\|\Lambda(CBC^\dagger)\|_\tau^2
=\frac{d\|B\|_2^2}{M}\sum_{P\in\mathcal P_*}\|A_P\|_\tau^2.
```

Finally $`\sum_{ij}\|B_{ij}\|_2^2=r^2-r/d`$. Averaging the compressed Choi bound therefore gives the exact identity and the resulting Pauli budget

```math
\mathbb E_C\,\mathrm{Tr}[(J_V-T)T^{-1}(J_V-T)]
=\frac{dr-1}{d^2-1}\sum_{P\in\mathcal P_*}\|A_P\|_\tau^2,
\qquad
\frac1M\sum_{P\in\mathcal P_*}\|A_P\|_\tau^2
\leq\frac{C_\varepsilon}{dr-1}.
```

At $`r=1`$ this gives the single-report budget from [the ordinary privacy converse](quantum-converse.md). At $`r=d`$ the compression is the full normalized Choi state. No factor involving the report dimension enters either case.

## Product identification converse

For a fixed public label $`y`$ and target $`H=sP`$, the report is $`\omega_{H}=\tau+ysA_P`$. Its mean over uniform signed targets is $`\tau`$. The [Petz order-two bound](quantum-converse.md#from-the-quadratic-budget-to-relative-entropy) implies $`D(\omega_H\Vert\tau)\leq\|A_P\|_\tau^2`$, so the average report divergence to $`\tau`$ is at most $`C_\varepsilon/(dr-1)`$. Conditional on the labels and public coins, use the product of the maximally mixed input reports as the reference. Additivity across product states and the relative-entropy identity for a mixture bound the mutual information of the target and all reports by $`NC_\varepsilon/(dr-1)`$. In particular, this argument does not assume the mean of the target-conditioned product reports is itself a product. The labels and coins have the same law for every target. Data processing and Fano's inequality then give

```math
N\geq\frac{dr-1}{C_\varepsilon}
\left[\log L-h_2(\delta)-\delta\log(L-1)\right].
```

This proves the fixed-confidence lower bound. The reverse-divergence argument below also applies to product encoders and adds the $`\log(1/\delta)`$ term for higher confidence.

## Classical feedback with quantum report memory

Write $`\Omega^t_0`$ for the joint state of the learner's classical history and quantum memory after $`t`$ specimens when all specimens are $`I/d`$. The public labels still have their original law. Write $`\Omega^t_H`$ for the corresponding state under target $`H`$. Keep the classical settings and outcomes used for feedback in an orthogonal record. Work first with finite records and finite quantum registers, with arbitrary dimensions. Padding with input-independent releases handles earlier stops. For general classical records with normal channels the block formulas below use the integral form of classical conditional relative entropy.

At each history $`h`$ and next label $`y`$, compare the learner's two states immediately after it receives the fresh report, before it applies its next instrument. These states have a classical block for $`(h,y)`$, and their conditional quantum states factor into the previous memory and the fresh report. Classical block decomposition and tensor additivity of relative entropy, followed by data processing through the next instrument, give

```math
D(\Omega_0^{t+1}\Vert\Omega_H^{t+1})
\leq D(\Omega_0^t\Vert\Omega_H^t)
+\mathbb E_{h\sim0,\,y}D(\tau_{h,y}\Vert\omega_{H,h,y}).
```

The label law is the same in both experiments. If the labels are public before the run, put their entire sequence in the initial record and condition on it. The expectation over histories always uses the null experiment, so this distribution is common to all targets even when the protocol makes adaptive encoder choices. For each selected encoder, ordinary local privacy gives $`\omega_{H,h,y}\succeq e^{-\varepsilon}\tau_{h,y}`$. Apply the order-two bound in the reverse direction, using $`\omega_{H,h,y}^{-1}\preceq e^\varepsilon\tau_{h,y}^{-1}`$ on the common support. The resulting increment for target $`sP`$ is at most $`e^\varepsilon\|A_P\|_{\tau_{h,y}}^2`$. The compressed Choi budget holds uniformly for the chosen channel at every history. Summing over the steps yields

```math
\frac1L\sum_H D(\Omega_0^N\Vert\Omega_H^N)
\leq \frac{N e^\varepsilon C_\varepsilon}{dr-1}.
```

For identification, the final outcome $`\widehat H=H`$ has probability at most $`2/L`$ under the null for at least $`L/2`$ targets. On each of those targets it has probability at least $`1-\delta`$ in the target experiment. Binary data processing therefore gives

```math
N\geq\frac{dr-1}{2e^\varepsilon C_\varepsilon}
\mathrm{kl}\!\left(\frac2L\,\middle\Vert\,1-\delta\right).
```

Here $`\mathrm{kl}`$ is relative entropy between two Bernoulli distributions. Since $`L\geq6`$, this binary divergence is at least $`(2/3)\log(1/\delta)-\log 2`$, which is at least $`(1/6)\log(1/\delta)`$ for $`\delta\leq1/4`$. Together with the product converse this proves both terms of its high-confidence lower bound. At $`r=d`$ the reverse bound gives order $`d^2\log(1/\delta)`$ with privacy-dependent constants.

For prediction, give the final learner one fresh clean specimen $`\rho_{H,y}`$ with hidden fair label $`y`$. Compare training under target $`H`$ to null training, supplying the same clean test state and label distribution in both cases. The change in success probability for that target is bounded by $`\tfrac12\|\Omega_0^N-\Omega_H^N\|_1`$. This step allows a joint measurement on quantum memory and the clean test. Under null training, the mean success over uniform signed $`H`$ is exactly $`1/2`$, because the averaged clean test state is $`I/d`$ for either label. If target-experiment success is at least $`1/2+\beta`$ for every $`H`$, quantum Pinsker and Jensen imply

```math
\beta\leq\left[\frac1{2L}\sum_H D(\Omega_0^N\Vert\Omega_H^N)\right]^{1/2},
\qquad
N\geq\frac{2\beta^2(dr-1)}{e^\varepsilon C_\varepsilon}.
```

## A short randomizer with a bounded reference

Let $`\mathcal D(X)=\mathrm{Tr}(X)I/d`$. We construct a fixed list of $`K\leq\lceil c_0 dr\rceil`$ unitaries, for an absolute constant $`c_0`$, such that their equally weighted mixture $`\Phi_0`$ satisfies, for every state on $`RA`$ with $`\dim R\leq r`$,

```math
\tfrac12\xi_R\otimes I/d
\preceq (\mathrm{id}_R\otimes\Phi_0)(\xi_{RA})
\preceq \tfrac32\xi_R\otimes I/d.
```

Choose $`K`$ independent Haar unitaries. To prove the claim, take $`d\times r`$ matrices $`V`$ with $`\|V\|_\infty\leq1`$ and vectors $`\psi\in\mathbb C^{rd}`$ with $`\|\psi\|_2\leq1`$. Use the reference-first vectorization $`v=r^{-1/2}\sum_i|i\rangle\otimes V|i\rangle`$ and define the real quadratic form

```math
q(V,\psi)=\langle\psi|(\mathrm{id}_R\otimes(\Phi_0-\mathcal D))
(|v\rangle\langle v|)|\psi\rangle.
```

For fixed $`V,\psi`$, this is an average of independent centered variables. With $`\psi`$ represented by its $`d\times r`$ column matrix $`\Psi`$, an uncentered term is $`|\mathrm{Tr}(\Psi^\dagger U V)|^2/r`$. The complex linear functional of $`U`$ inside the absolute value has mean zero and Hilbert–Schmidt Lipschitz constant at most $`\|\Psi V^\dagger\|_2\leq1`$. The Haar concentration inequality on $`U(d)`$ gives real and imaginary tails of the form $`2e^{-c d t^2}`$ at deviation $`t`$. Its squared modulus divided by $`r`$ consequently has subexponential scale $`O(1/(dr))`$. The Haar mean equals the depolarizing term by unitary invariance. Bernstein's inequality gives, for some absolute $`c_1>0`$,

```math
\Pr[|q(V,\psi)|>1/(4dr)]\leq 2 e^{-c_1 K}.
```

Take $`1/32`$-nets of the two unit balls in operator norm and Euclidean norm, respectively. Each has cardinality at most $`65^{2dr}`$ by the volumetric bound for a norm ball. Let $`S=\sup_{V,\psi}|q(V,\psi)|`$ over the two balls. For fixed $`\psi`$, complex polarization bounds the sesquilinear form in $`V`$ associated with $`q`$ by $`4S\|V_1\|_\infty\|V_2\|_\infty`$. Thus replacing $`V`$ by its net point changes $`q`$ by at most $`8S/32`$. For fixed $`V`$, the Hermitian form in $`\psi`$ has operator norm at most $`S`$, giving a change at most $`2S/32`$. Hence $`S`$ is at most twice the maximum of $`|q|`$ on net pairs. For $`K=\lceil c_0dr\rceil`$ with $`c_0`$ large enough, the concentration bound and a union bound give a positive probability of $`S\leq1/(2dr)`$.

For an isometry $`V`$, the depolarizing term on $`|v\rangle\langle v|`$ is $`I_{RA}/(dr)`$. The bound on $`S`$ gives the claimed operator inequalities on every such state. For a general pure state with reference marginal $`\xi_R`$, its column matrix has a polar factorization into an isometry and a positive matrix. Equivalently, the state is obtained from some $`|v\rangle`$ by applying $`\sqrt{r\xi_R}`$ on the reference. The isometry can be completed arbitrarily on the kernel of that marginal. Congruence by the reference filter gives the desired inequalities for that pure state, because the channel acts only on $`A`$. Convex combination gives them for mixed states, and embedding covers smaller references.

The order $`dr`$ in the list is necessary for a mixed-unitary channel with finite $`r`$-reference privacy. On the isometry state its output has rank at most the list length. Comparison with the product input $`I_R/r\otimes I_A/d`$ and the unital channel's full-rank output forces rank $`dr`$. This is a list-length statement for such channels. The learning lower bound above allows arbitrary encoders and uses the stronger quadratic identity.

The concentration ingredient follows from the $`U(d)`$ log-Sobolev bound in [Meckes, Theorem 5.16](https://case.edu/artsci/math/mwmeckes/elizabeth/Haar_book.pdf) and its associated concentration inequality. [Aubrun, Theorem 1 and Lemma 4](https://arxiv.org/abs/0805.2900v2) give the corresponding unassisted Haar randomizer and constant-net method. [Lancien and Winter, *Quantum* 8, 1320 (2024), Secs. 2–3](https://doi.org/10.22331/q-2024-04-30-1320) develop general low-Kraus-rank channel approximations for unassisted outputs and discuss the rank obstruction for completely bounded approximation. The construction here controls relative operator bounds against the corresponding reference marginal. These bounds are what allow the fixed list to be used under the stated privacy contract.

## Matching constructions

Set $`\theta=\tanh(\varepsilon/2)`$ and use $`\Phi_\theta=(1-\theta)\mathcal D+\theta\Phi_0`$. Its relative bounds against $`\xi_R\otimes I/d`$ are $`1-\theta/2`$ and $`1+\theta/2`$. The ratio is at most $`e^\varepsilon`$. Conjugate each local channel by an independent uniform public Clifford and include that Clifford in the report as in [the coherent encoder](quantum-reports.md). Input and output Clifford conjugations preserve the reference guarantee, which therefore holds blockwise for the actual flagged report. The sampled private unitary index and the private choice between the two branches of $`\Phi_\theta`$ are discarded. The fixed list may be public.

To see its identification power, compute the squared Hilbert–Schmidt norm of the superoperator $`\Phi_0`$ using the Pauli basis $`\{P/\sqrt d\}`$. For its unitary list $`\{U_j\}`$ this norm is

```math
\frac{1}{K^2}\sum_{i,j}|\mathrm{Tr}(U_i^\dagger U_j)|^2\geq\frac{d^2}{K}.
```

Since $`\Phi_0`$ is unital, the identity contributes one. If $`K\leq d^2/2`$, the average of $`\|\Phi_0(P)\|_2^2/d`$ over nonidentity Paulis is at least $`1/(2K)`$. For two signed targets with distinct unsigned Paulis, Clifford averaging eliminates the cross term by the same pair of Pauli sign characters used above. Opposite targets have twice the squared-distance lower bound obtained in the distinct-Pauli case. The depolarizing admixture scales every traceless Pauli by the factor $`\theta`$ relative to $`\Phi_0`$. Thus for any distinct pair the expected squared Hilbert–Schmidt distance between their conditional output states is at least $`\theta^2/(dK)`$.

All conditional output states have operator norm at most $`(1+\theta/2)/d`$. The [root-fidelity inequality](quantum-reports.md#5-bounded-output-spectra-convert-signal-into-fidelity-separation) turns the distance bound into a root-fidelity gap of at least $`\theta^2/[8(1+\theta/2)K]`$ for every pair of complete flagged reports. The gap uses the block average over the same public labels and Cliffords. Tensor-product root fidelity and the [mixed-state worst-case pretty-good measurement bound](quantum-reports.md#6-an-explicit-statistical-decoder-with-worst-target-error-control) then give worst-case error at most $`\delta`$ with $`O(K\theta^{-2}[\log L+\log(1/\delta)])`$ specimens. The argument counts every release, including the depolarizing branch. It provides an existence guarantee for a fixed good list and a collective decoder. Dense list synthesis, exact privacy certification, finite-precision margins and efficient implementation of the decoder are separate costs.

If the chosen list length exceeds $`d^2/2`$, then $`d^2=O(dr)`$ with an absolute constant. A fixed classical schedule now supplies the same upper order. For each of the $`M`$ unsigned nonidentity Paulis, allocate $`O(\theta^{-2}\log(M/\delta))`$ specimens and use the [private binary report](classical-reports.md#a-private-noisy-tournament-attains-the-classical-order) with contrast $`\theta`$. The report mean, after multiplying by the public label, is $`+\theta`$ or $`-\theta`$ for the hidden Pauli and zero otherwise. Hoeffding bounds and a union bound give simultaneous estimation accuracy below $`\theta/2`$ with probability at least $`1-\delta`$. Pick the largest absolute empirical mean and its sign. The fixed schedule costs $`O(d^2\theta^{-2}[\log d+\log(1/\delta)])`$, which in this regime is $`O(dr\theta^{-2}[\log d+\log(1/\delta)])`$.

For the classical comparator, let a POVM effect $`E_z`$ have minimum eigenvalue $`m_z`$. Ordinary all-input privacy implies $`m_z I\preceq E_z\preceq e^\varepsilon m_z I`$ by testing its extremal eigenvectors. On any joint input $`\xi_{RA}`$, the reference operator of the released outcome block therefore satisfies

```math
m_z\xi_R\preceq\mathrm{Tr}_A[(I_R\otimes E_z)\xi_{RA}]
\preceq e^\varepsilon m_z\xi_R.
```

Partial trace in this expression is equivalently the positive measurement operation with $`\sqrt{E_z}`$ on both sides. The bound applied to two inputs with equal reference marginals proves unrestricted-reference privacy for the entire classical output. The same proof applies to POVM densities for general classical alphabets. Thus every private classical product encoder satisfies the $`r=d`$ lower bound, while the fixed schedule attains it. For classical feedback at full reference, the existing [adaptive tournament](classical-reports.md#a-private-noisy-tournament-attains-the-classical-order) uses those same reference-secure effects and needs $`O(d^2\theta^{-2}\log(1/\delta))`$ specimens for $`\delta\leq1/4`$. It gives the prediction upper bound by identifying the target with a sufficiently small constant error, then measuring the target on the clean test specimen. The converse permits more general quantum-memory decoders in both cases.

## What changes when the reference grows

With product encoders the specimen separation is of order $`d/r`$. The original adaptive classical comparator uses order $`d^2`$ specimens. Against that comparator the product quantum protocol has a smaller specimen order when $`r\log d=o(d)`$ at fixed privacy and confidence. At full reference, feedback closes the specimen gap even with unrestricted learner quantum memory and joint clean-test readout. The distinction is a consequence of the privacy input class and the permitted feedback. The reverse-divergence budget applies even to reference-secure channels that preserve entanglement. To see this, take a normalized Choi state $`J=(I-aF)/(d^2-ad)`$, where $`F`$ swaps the two $`d`$-dimensional systems, $`0<a\leq\tanh(\varepsilon/2)`$, and $`ad>1`$. Both marginals are $`I/d`$. Its minimum and maximum eigenvalues have ratio $`(1+a)/(1-a)\leq e^\varepsilon`$. The two operator bounds on $`J`$ are complete-positive order bounds on its channel relative to the depolarizing channel, so they bound any joint output above and below by multiples of $`\xi_R\otimes I/d`$. This proves unrestricted reference privacy. The partial transpose of $`F`$ is $`d`$ times a maximally entangled projector, and the corresponding eigenvalue of the partial transpose of $`J`$ is $`(1-ad)/(d^2-ad)<0`$. Hence the channel is not entanglement breaking.

[Li, Guan and Ying, arXiv:2611.25775v1, Definition 3 and Appendix A-C](https://arxiv.org/html/2611.25775v1) formulate unrestricted equal-reference-marginal privacy and use the maximally entangled versus product comparison to study Choi support. The compressed Choi learning budget and its specimen consequences above are different conclusions. [Bhalerao, Nuradha and Leditzky, arXiv:2609.13418](https://arxiv.org/abs/2609.13418) prove entanglement breaking in a dimension-dependent high-privacy regime for ordinary local privacy and study losses on other learning tasks. The law here uses reference-secure privacy at fixed $`\varepsilon`$ and addresses signed-Pauli identification and prediction. The [original related-work account](../references/related-work.md) documents the inherited supervised source, private-measurement literature and collective discrimination tools.
