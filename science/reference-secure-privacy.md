# The sample cost of protecting a quantum reference

The same signed-Pauli learning problem can require more training specimens when local privacy protects against a retained quantum reference. A collective learner that fixes its encoders in advance needs order $`dk\log d/\varepsilon^2`$ specimens when the protected reference has dimension $`k`$. With unrestricted reference protection and classical feedback, the cost is order $`d^2/\varepsilon^2`$. A classical reporting protocol attains that rate even against learners with unrestricted quantum memory.

The reference is part of the privacy test for an encoder. The learning experiment still supplies the same independent specimens and public labels. Thus changing $`k`$ changes the protection required of each encoder while leaving the supervised source and deployment test fixed.

## Model and results

Use the [signed-Pauli source](model.md). Set $`d=2^n`$, $`\mathcal P_*=\mathcal P_n\setminus\{I\}`$, $`M=d^2-1`$, and $`\mathcal H=\{\pm P:P\in\mathcal P_*\}`$. The uniform signed target $`H`$ has $`L=2M`$ possible values. Its training specimen at public label $`y\in\{\pm1\}`$ is $`\rho_{H,y}=(I+yH)/d`$. The fresh independent test specimen has the same form with its label hidden.

A local channel $`\Lambda`$ is $`\varepsilon`$-private for reference dimension $`k`$ if, for every $`R`$ with $`\dim R\le k`$ and every pair $`\rho_{RS},\sigma_{RS}`$ with $`\rho_R=\sigma_R`$,

```math
(\mathrm{id}_R\otimes\Lambda)(\rho_{RS})
\preceq e^\varepsilon(\mathrm{id}_R\otimes\Lambda)(\sigma_{RS}).
```

This order gives the probability ratio bound for every joint measurement on the reference and the complete release. The label and public choices condition the local mechanism. All flags produced by it remain in the release for the privacy comparison. At $`k=1`$ this is ordinary all-input-state QLDP. The unrestricted-reference definition is the equal-marginal comparison in [Li, Guan and Ying, Section V and Theorem 3](https://arxiv.org/html/2611.25775v1). The unrestricted rate below uses dimension-$`d`$ comparisons for its lower bound and an all-reference construction for its upper bound.

The learner can store arbitrary private quantum reports and perform any joint decoding. In the **predetermined** model, encoders are fixed conditional on external public coins and labels. Each owner operates separately with fresh private randomness and local ancillas. In the **classical-feedback** model, a learner instrument can produce classical history used to choose the next encoder. Each new specimen is independent of learner memory conditional on the target and label. The models exclude coherent feedback to owners, cross-record hidden keys, and joint access to multiple raw specimens. The count $`N`$ caps specimens on every branch. To handle early stopping, pad the run with input-independent releases.

For fixed identification error $`\delta\in(0,1)`$ or fixed clean-test advantage $`\beta\in(0,1/2)`$, the orders below hold as $`d`$ grows, uniformly over $`1\le k\le d`$ and $`0<\varepsilon\le1`$. Constants may depend on the fixed error or advantage. The upper bounds hold for every target. The lower bounds use a uniform target and also apply to worst-target guarantees.

| Encoder access and required privacy | Identification and one clean-test prediction |
|---|---|
| Predetermined encoders, reference dimension $`1\le k\le d`$ | $`\Theta(dk\log d/\varepsilon^2)`$ |
| Classical feedback, unrestricted reference | $`\Theta(d^2/\varepsilon^2)`$ |
| Classical feedback, dimension $`k\le d`$ | $`\Omega(dk/\varepsilon^2)`$, with adaptive upper bound $`O(\min\{dk\log d,d^2\}/\varepsilon^2)`$ |

The first line includes the matching prediction converse at $`k=1`$. At unrestricted reference dimension, classical reporting matches the general quantum learner's adaptive specimen cost. The optimal adaptive rate for intermediate $`k`$ is unresolved. The same dimension orders hold at any fixed finite positive $`\varepsilon`$, with constants depending on $`\varepsilon`$.

## 1. The information budget of a protected reference

Fix a local encoder and put $`\tau=\Lambda(I/d)`$ and $`A_P=\Lambda(P)/d`$. All inverses are on the support of $`\tau`$. The ordinary $`k=1`$ comparisons show that every output has this support and each training output $`\omega_{H,y}=\Lambda(\rho_{H,y})`$ obeys $`e^{-\varepsilon}\tau\preceq\omega_{H,y}\preceq e^\varepsilon\tau`$.

Let $`W:\mathbb C^k\to\mathbb C^d`$ be a Haar-uniform isometry. Compare the state $`k^{-1/2}\sum_{a=1}^k|Wa\rangle|a\rangle`$ with the product $`I/d\otimes I_k/k`$. Both reference marginals are $`I_k/k`$. Put $`B_P=\tau^{-1/2}A_P\tau^{-1/2}`$. Expanding the entangled state's projector in the Pauli basis gives the whitened difference

```math
C_W=\sum_{P\in\mathcal P_*}B_P\otimes(W^\dagger P W)^{\mathsf T}.
```

The encoded entangled state is $`(\tau^{1/2}\otimes I_k)(I+C_W)(\tau^{1/2}\otimes I_k)/k`$. The two orders of the privacy comparison give $`e^{-\varepsilon}I\preceq I+C_W\preceq e^\varepsilon I`$. Hence

```math
\mathrm{Tr}[(\tau\otimes I_k/k)C_W^2]\le (e^\varepsilon-1)^2.
```

For the Haar moment, write $`\Pi=WW^\dagger`$ and let $`F`$ exchange two $`d`$-dimensional systems. The twirl is $`\mathbb E\Pi^{\otimes 2}=a I+b F`$, with

```math
a=\frac{k(dk-1)}{d(d^2-1)},\qquad b=\frac{k(d-k)}{d(d^2-1)}.
```

The trace and the trace against $`F`$ give $`k^2`$ and $`k`$, determining the coefficients. In $`\mathbb E\mathrm{Tr}(P\Pi Q\Pi)`$, the term with $`b`$ vanishes for traceless Paulis. Thus

```math
\mathbb E_W\,\frac{\mathrm{Tr}[(W^\dagger PW)(W^\dagger QW)]}{k}
=\mathbf 1_{\{P=Q\}}\frac{dk-1}{d^2-1}.
```

Transposition only reverses the product inside this trace. Expanding the squared difference, averaging, and using $`\mathrm{Tr}(\tau B_P^2)=\mathrm{Tr}(A_P\tau^{-1}A_P)`$ gives

```math
\boxed{\quad
\frac1M\sum_{P\in\mathcal P_*}\mathrm{Tr}(A_P\tau^{-1}A_P)
\le\frac{(e^\varepsilon-1)^2}{dk-1}.
\quad}
```

At $`k=1`$ this recovers the [ordinary-privacy budget](quantum-converse.md). At $`k=d`$ the denominator is $`d^2-1`$, because the Choi comparison sees the full Pauli basis in one operator. The bound holds independent of the dimension and commutativity of the report.

Write $`\omega_{H,y}-\tau=\pm A_P`$. The [Petz second-moment bound](quantum-converse.md#one-report-support-and-a-quadratic-information-budget) $`D(\omega\Vert\sigma)\le\mathrm{Tr}[(\omega-\sigma)\sigma^{-1}(\omega-\sigma)]`$ follows from scalar Jensen in the eigenbases of the two states. Applying it in both directions and using $`\omega_{H,y}^{-1}\preceq e^\varepsilon\tau^{-1}`$ yields

```math
D(\omega_{H,y}\Vert\tau)\le\mathrm{Tr}(A_P\tau^{-1}A_P),\qquad
D(\tau\Vert\omega_{H,y})\le e^\varepsilon\mathrm{Tr}(A_P\tau^{-1}A_P).
```

## 2. Identification and prediction with predetermined encoders

Condition on all public inputs, whose distribution is independent of the target. The target-dependent reports form a product, while their target average generally does not. Let $`\tau_j`$ be the $`j`$th encoder's output at $`I/d`$. If $`\omega_h^{(N)}`$ is the report state for target $`h`$ and $`\bar\omega^{(N)}`$ its uniform average, the relative-entropy decomposition gives

```math
\frac1L\sum_h D\!\left(\omega_h^{(N)}\,\middle\Vert\,\bigotimes_j\tau_j\right)
=\chi(H:Q^N)+D\!\left(\bar\omega^{(N)}\,\middle\Vert\,\bigotimes_j\tau_j\right).
```

By additivity on products, the forward entropy estimate, and the uniform Pauli budget, the Holevo information is at most $`N(e^\varepsilon-1)^2/(dk-1)`$. This remains true after averaging over public inputs. If a final measurement identifies $`H`$ with probability at least $`s`$, data processing and Fano's inequality give

```math
N\ge\frac{dk-1}{(e^\varepsilon-1)^2}\,[s\log L-\log 2].
```

A one-test predictor is equally constrained. Let $`\sigma_h`$ be its final training memory before receiving the independent clean test, with classical records included as registers. Represent prediction by a Hermitian binary observable $`B=F_+-F_-`$ on memory and test. Then $`-I\preceq B\preceq I`$. Expand it as $`B=\sum_{P\in\mathcal P_n} B'_P\otimes P`$, where $`B'_P=\mathrm{Tr}_S[B(I\otimes P)]/d`$ is Hermitian by cyclicity on the test factor. Tracing $`B^2\preceq I`$ over the test gives

```math
\sum_{P\in\mathcal P_n}(B'_P)^2
=\frac1d\mathrm{Tr}_S(B^2)\preceq I .
```

For signed $`h=\pm P`$, put $`B'_h=\pm B'_P`$ and define $`E_h=((B'_h)_+)^2`$, using the positive spectral part. For an unsigned $`P`$, the two effects sum to $`(B'_P)^2`$, so adjoining a failure effect makes a POVM on training memory alone. Its average correct-identification probability is at least

```math
\frac1L\sum_h\mathrm{Tr}(\sigma_h E_h)
\ge
\left[\frac1L\sum_h\mathrm{Tr}\big(\sigma_h(B'_h)_+\big)\right]^2
\ge 4\beta^2 .
```

The first step uses scalar Jensen in each spectral decomposition and then in the uniform target average. The second uses $`2\beta=L^{-1}\sum_h\mathrm{Tr}(\sigma_h B'_h)`$ when the predictor's average advantage is $`\beta`$, as follows by expanding the two test-label states in the success probability. The reduction permits arbitrary training states and can consume the memory. It uses no test specimen and makes no gate-efficiency claim. Substituting $`s=4\beta^2`$ in the information bound yields the prediction converse, including ordinary privacy at $`k=1`$.

## 3. Matching predetermined reports

### A short list that protects dimension $`k`$

Let $`R_*(X)=\mathrm{Tr}(X)I/d`$. Use the vectorization $`\mathrm{vec}(U)=(U\otimes I)\sum_a|a,a\rangle`$ and the corresponding unnormalized Choi matrix. The Choi matrix of $`R_*`$ is $`I/d`$. For an absolute constant $`C`$, a list of $`K=\lceil Cdk\rceil`$ Haar unitaries can be fixed so that its channel $`\Phi=K^{-1}\sum_i\mathrm{Ad}_{U_i}`$ satisfies

```math
\frac{1-\eta_0}{d}\Vert v\Vert ^2
\le \langle v|J_\Phi|v\rangle
\le\frac{1+\eta_0}{d}\Vert v\Vert ^2
\qquad\text{for all }v\text{ of Schmidt rank at most }k,
\qquad \eta_0=\frac12.
```

To see existence, identify $`v=\mathrm{vec}(X)`$ and define

```math
T(X)=K^{-1/2}\big(\sqrt d\,\mathrm{Tr}(U_i^\dagger X)\big)_{i=1}^K .
```

For fixed $`\Vert X\Vert _2=1`$, the unscaled components $`\sqrt d\,\mathrm{Tr}(U_i^\dagger X)`$ have mean zero, second absolute moment one by Haar orthogonality, and uniformly sub-Gaussian real and imaginary parts. The corresponding real functions on $`U(d)`$ have Lipschitz constant $`\sqrt d`$ in the Hilbert–Schmidt metric. The Haar log-Sobolev constant of order $`1/d`$ compensates for this factor. See [Meckes, Theorems 5.16–5.17](https://case.edu/artsci/math/mwmeckes/elizabeth/Haar_book.pdf). The squared absolute values are uniformly subexponential. Bernstein's inequality gives probability at most $`2e^{-cK}`$ of a deviation of $`\Vert T(X)\Vert _2^2`$ from one by more than $`1/8`$, with an absolute $`c>0`$.

The Frobenius unit sphere of rank-at-most-$`k`$ matrices has a $`1/32`$-net of size $`\exp(O(dk))`$. In a singular value decomposition $`X=U\Sigma V^\dagger`$, cover each of the two isometries in operator norm and the vector of singular values in Euclidean norm, to accuracy $`1/96`$. The isometry nets follow by volume packing in the operator-norm unit ball of real dimension $`2dk`$, with centers on the isometries. The product net gives the asserted Frobenius accuracy because $`\Vert \Sigma\Vert _2=1`$. A union bound makes the fixed-point deviation estimate hold simultaneously on the net at $`K\ge Cdk`$.

Let $`S`$ be the supremum of $`\Vert T(X)\Vert _2`$ over the rank-at-most-$`k`$ Frobenius unit sphere. The difference between $`X`$ and its nearest net point has rank at most $`2k`$. Split its singular values into two rank-at-most-$`k`$ pieces whose Frobenius norms sum to at most $`\sqrt2/32`$. The triangle inequality gives

```math
S\le\frac{\sqrt{9/8}}{1-\sqrt 2/32},\qquad
\Vert T(X)\Vert _2\ge \sqrt{7/8}-(\sqrt 2/32)S .
```

These imply $`\Vert T(X)\Vert _2^2\in[1/2,3/2]`$, and $`\Vert T(X)\Vert _2^2=d\langle v|J_\Phi|v\rangle`$. This extends the rank-one randomization principle of [Aubrun, Theorem 1](https://arxiv.org/abs/0805.2900) to rank-constrained quadratic tests. The probabilistic argument establishes that a fixed good list exists. The privacy guarantee requires such a list. A probability of drawing a bad list cannot be charged to the decoder's error.

Write any pure input over $`S R`$ as $`|\psi\rangle=(I\otimes A)\sum_a|a,a\rangle`$. For $`\dim R\le k`$, pulling an output test vector back by $`I\otimes A^\dagger`$ gives Schmidt rank at most $`k`$. The Choi inequality therefore yields

```math
(1-\eta_0)\frac{I}{d}\otimes\psi_R
\preceq(\Phi\otimes\mathrm{id}_R)(\psi)
\preceq(1+\eta_0)\frac{I}{d}\otimes\psi_R .
```

Linearity gives the same sandwich for mixed inputs. Set $`q=\tanh(\varepsilon/2)`$ and use $`\Phi_q=q\Phi+(1-q)R_*`$. Its sandwich has distortion $`q\eta_0`$, so the ratio for equal-marginal pairs is bounded by $`(1+q\eta_0)/(1-q\eta_0)\le e^\varepsilon`$. Calibrating by replacement keeps the short-list length independent of $`\varepsilon`$ and charges the lost signal in the sample count.

### Public orientation and decoding

Choose an independent uniform Clifford, rotate the input before applying $`\Phi_q`$, and rotate the output back as in the [ordinary private mechanism](quantum-reports.md#2-the-actual-released-report-is-private). Release the Clifford flag with the system. Each flag block satisfies the reference-aware sandwich, so releasing it preserves the guarantee. Discard the sampled list index and the replacement coin.

When $`K\le d^2/2`$, the list channel $`\Phi`$ has mean normalized squared Pauli response at least $`1/(2K)`$ by the [sum of squared unitary overlaps](quantum-reports.md#3-a-low-kraus-randomizer-retains-a-total-signal-budget). Replacement annihilates traceless Paulis, so the mean response of $`\Phi_q`$ is at least $`q^2/(2K)`$. Clifford conjugation makes the response uniform over Pauli directions. Random Clifford signs cancel mixed products for distinct unsigned Paulis. Consequently, every distinct target pair has mean squared output-state Hilbert–Schmidt distance at least $`q^2/(dK)`$, with a larger bound for opposite signs of the same Pauli. The output spectra are bounded above by $`(1+\eta_0)/d`$. The [root-fidelity inequality](quantum-reports.md#5-bounded-output-spectra-convert-signal-into-fidelity-separation) then bounds pairwise root fidelity by $`1-q^2/[8(1+\eta_0)K]`$ for actual reports with flags and labels. Tensor products and the [worst-target pretty good measurement](quantum-reports.md#6-an-explicit-statistical-decoder-with-worst-target-error-control) give failure at most $`\delta`$ with

```math
N\ge
\left\lceil
\frac{8(1+\eta_0)K}{q^2}\log\frac{L(L-1)}{\delta}
\right\rceil .
```

The list branch uses a fresh private choice among $`K`$ dense unitaries. Replacement uses a maximally mixed $`n`$-qubit preparation, for example by discarding the specimen and using $`n`$ independent bits to select a basis state. Public list storage, gate synthesis, and implementation of the collective measurement are separate resources. The proof specifies a statistically attaining measurement.

If $`K>d^2/2`$, then $`d^2=O(dk)`$ since $`K=\lceil Cdk\rceil`$. Use predetermined randomized response on every unsigned Pauli, sampling each one $`O(q^{-2}\log(M/\delta))`$ times. The true Pauli has mean $`+q`$ or $`-q`$, while every other Pauli has mean zero. Hoeffding's inequality and a union bound give the target and its sign from the largest absolute empirical mean with probability at least $`1-\delta`$. The next section establishes the identical privacy guarantee against every reference. Both constructions attain any fixed clean-test advantage below $`1/2`$ by identifying with sufficiently small fixed failure and measuring the estimated Pauli.

## 4. Classical feedback and quantum learner memory

Keep the actual classical history as a separate register of the learner's memory. For fixed target $`h`$, compare complete target and null training experiments. The target supplies specimen $`\rho_{h,y}`$ each round. The null supplies $`I/d`$ with the same label law and learner operations. At fixed preceding history $`z`$ and current label $`y`$, the new release in the null is $`\tau_{z,y}`$ and the target release is $`\omega_{h,z,y}`$. Each is in a product with its experiment's prior conditional quantum memory. The two conditional memories may differ.

For states block diagonal over a classical history, relative entropy is the classical relative entropy of the histories plus the null-weighted quantum conditional relative entropies. Before the next learner instrument, adding the independent release raises that relative entropy by exactly $`\mathbb E_{0,z,y}D(\tau_{z,y}\Vert\omega_{h,z,y})`$ by tensor-product additivity. The same instrument acts under both hypotheses, so data processing can only decrease the divergence. Starting with identical memories gives

```math
D(\sigma_0\Vert\sigma_h)
\le \sum_{j=1}^N\mathbb E_{0,z,y}
D(\tau_{j,z,y}\Vert\omega_{h,j,z,y}).
```

The right-hand side is weighted under the null, whose history is independent of the target. Averaging over signed targets and using Section 1 gives mean divergence at most $`Ne^\varepsilon(e^\varepsilon-1)^2/(dk-1)`$. The same conditional calculation uses integrals for measurable classical histories with densities relative to a dominating measure.

Pinsker's inequality and Jensen give

```math
\frac1L\sum_h\frac12\Vert \sigma_h-\sigma_0\Vert _1
\le
\sqrt{\frac{N e^\varepsilon(e^\varepsilon-1)^2}{2(dk-1)}} .
```

With the null memory, average identification succeeds with probability at most $`1/L`$. Pairing that memory with a clean test under the signed prior gives chance prediction because both label-conditioned test states average to $`I/d`$. For each $`h,y`$, tensoring the same test state to the two memories leaves their trace distance unchanged. The displayed bound consequently controls both identification gain above $`1/L`$ and clean prediction gain above chance. This yields $`\Omega(dk/\varepsilon^2)`$ for either fixed performance goal and $`\Omega(d^2/\varepsilon^2)`$ at the unrestricted endpoint.

### The classical tournament protects every reference

Every all-input-state private POVM release retains its privacy parameter for a reference of any dimension. For each outcome effect $`E_a`$, ordinary privacy gives $`\lambda_{\max}(E_a)\le e^\varepsilon\lambda_{\min}(E_a)`$. The subnormalized conditional reference operator in block $`a`$ lies between $`\lambda_{\min}(E_a)\rho_R`$ and $`\lambda_{\max}(E_a)\rho_R`$. Using this interval for both equal-marginal inputs proves the required blockwise order. This is the stability of classical-output channels described in [Li, Guan and Ying, Section V-B](https://arxiv.org/html/2611.25775v1).

In particular, the [private noisy tournament](classical-reports.md#a-private-noisy-tournament-attains-the-classical-order) with binary effects $`[I+qwyQ]/2`$, for arm $`Q`$, label $`y`$, and release $`w`$, protects arbitrary references conditional on each actual history. It uses $`O(d^2/\varepsilon^2)`$ specimens at fixed target error. This matches the unrestricted-reference converse with an ordinary classical learner. At $`\varepsilon=0`$, the dimension-one comparison alone forces reports to be independent of their specimen, so neither task gains from training.

### Predetermined classical reports under the same guarantee

Every predetermined classical encoder that satisfies the ordinary privacy inequality also satisfies unrestricted reference privacy, by the effect bounds above. The product converse in Section 2 with $`k=d`$ therefore applies to every classical schedule, even when the specified reference cap is smaller. The fixed randomized-response schedule in Section 3 attains the resulting order $`d^2\log d/\varepsilon^2`$ for $`0<\varepsilon\leq1`$ and fixed identification error. The predictor-to-identifier reduction gives the same lower order for fixed clean-test advantage, and identification supplies the matching prediction strategy. At any fixed finite positive privacy level the same dimension dependence follows from the displayed constants. The quantum and classical predetermined costs therefore differ by a factor of order $`d/k`$ under the same reference bound.

## 5. What the reference changes

A short unital randomizer with fewer than $`d^2`$ Kraus operators can satisfy ordinary privacy and still have infinite privacy parameter against an unrestricted reference. Its Choi matrix has a kernel, while $`I/d^2`$ is the full-support output of the comparison product state. The maximally entangled and product inputs have the same reference marginal $`I/d`$. The event projecting onto the kernel has positive probability on the product input and zero probability on the maximally entangled input. This is the support obstruction of [Li, Guan and Ying, Theorem 4 and Appendix A-C](https://arxiv.org/html/2611.25775v1) applied to the original randomizer and to each released Clifford block. The sample law applies to all valid encoders, including replacements for that randomizer.

[Wang, Sadeghi and Shi, Sections 3–4](https://arxiv.org/html/2601.19126v1) study an entropy constraint on bipartite inputs, product channels on both parts, and local measurements. The reference test here keeps one part untouched and permits joint measurements. [Bhalerao, Nuradha and Leditzky](https://arxiv.org/abs/2609.13418) show that ordinary QLDP is entanglement breaking at $`\varepsilon\le\log(d/(d-1))`$ and apply that observation to other learning tasks. The reference-aware budget here also applies at fixed positive privacy as dimension grows. The [label-noise antecedent](https://github.com/GoGoKo699/Quantum-Learning-Label-Noise/blob/f305698454964e101311b3a337efe49c71808cff/science/collective_statistics.md) has the same clean-test task and a prediction lower bound for scalar training contrast. The reduction in Section 2 applies to arbitrary encoded training states.
