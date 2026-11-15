# What a classical private report can learn

Each training specimen is an $`n`$-qubit state accompanied by a public training label. A client turns that one specimen into a classical report, and the learner can use every preceding report to choose the next client's measurement. The question in this chapter is how many specimens are needed when each complete report obeys local differential privacy.

The answer is quadratic in the Hilbert-space dimension at every fixed positive privacy level. This remains true for unlimited classical computation, arbitrary report alphabets, adaptive measurements, and a prediction task that asks only for a fixed advantage on a fresh clean specimen. A noisy tournament attains the same dimension dependence.

The labeled hidden-Pauli source is inherited from [Quantum-Learning-Label-Noise](https://github.com/GoGoKo699/Quantum-Learning-Label-Noise). The contribution here concerns private reports and their comparison with quantum reports. The general framework of locally private quantum measurements and its relation to quantum statistical queries is developed by [Angrisani and Kashefi, arXiv:2203.03591v2](https://arxiv.org/abs/2203.03591v2). The proofs below give the finite inequalities needed for this particular source.

## The source and the allowed reports

Set $`d=2^n`$, with $`n\geq 1`$. Choose one Hermitian phase convention for the nonidentity $`n`$-qubit Paulis and call the resulting set $`\mathcal P_*`$. Thus


```math
M=|\mathcal P_*|=d^2-1,
\qquad
\mathrm{Tr}(PQ)=d\,\mathbf 1_{\{P=Q\}}
\quad(P,Q\in\mathcal P_*\cup\{I\}).
```


The hidden target belongs to the signed set


```math
\mathcal H=\{+P,-P:P\in\mathcal P_*\},
\qquad
L=|\mathcal H|=2(d^2-1).
```


For each training specimen, a fresh public label $`Y`$ is uniform on $`\{+1,-1\}`$, and the state is


```math
\rho_{H,Y}=\frac{I+YH}{d}.
```


The specimens are independent conditional on $`H`$. Training labels are public; the true label of a test specimen is hidden.

At a preceding classical history $`h`$ and current training label $`y`$, the client may use any POVM $`E^{h,y}`$. Its outcome is the complete report sent to the learner. Any public random seed, setting, or auxiliary classical record is part of that report or of the conditioning history. The privacy requirement is


```math
\Pr[Z\in B\mid \rho,h,y]
\leq
e^\varepsilon
\Pr[Z\in B\mid \sigma,h,y]
```


for every pair of input density matrices $`\rho,\sigma`$ and every measurable report event $`B`$. We assume $`0\lt \varepsilon\lt \infty`$.

The client receives one raw specimen, uses fresh local ancillas and randomness if desired, and makes one private release. Neither raw specimens nor client quantum memories persist between records. Hidden keys correlated across records are excluded. Public randomness independent of the source can be included in the history. These conditions make each next release a one-specimen private POVM conditional on its actual classical history.

The learner may retain all classical reports and compute without restriction. It can choose each next POVM adaptively, and it can use at most $`N`$ specimens. A protocol that stops earlier can be padded with input-independent reports for the proof. No bound below is asserted merely from an expected stopping time under the promised sources.

A finite-outcome POVM is sufficient to read the argument. General measurable reports follow by taking a POVM density with respect to its trace measure and replacing sums by integrals.

## A private report has a bounded Pauli budget

Write


```math
r=e^\varepsilon,
\qquad
c=\frac{r-1}{r+1}=\tanh(\varepsilon/2),
```


and define


```math
V_\varepsilon=\frac{(r-1)^2}{4r}
=\sinh^2(\varepsilon/2),
\qquad
C_\varepsilon
=\frac{V_\varepsilon}{1-c^2}
=\frac14\sinh^2\varepsilon.
```


Consider one allowed POVM, with its history and current label fixed. For an effect $`E_z`$ of positive trace, put


```math
q_z=\frac{\mathrm{Tr}E_z}{d},
\qquad
v_P(z)=\frac{\mathrm{Tr}(E_zP)}
{\mathrm{Tr}E_z}.
```


Here $`q`$ is the report distribution when the input is $`I/d`$.

**Lemma 1 — one-report bounds.** Every private POVM satisfies


```math
|v_P(z)|\leq c
\quad(P\in\mathcal P_*),
```


and


```math
\sum_{P\in\mathcal P_*}
\mathbb E_{z\sim q}[v_P(z)^2]
\leq V_\varepsilon.
```


These bounds are uniform over the POVM and over its conditioning history.

**Proof.** Privacy applied to the largest- and smallest-eigenvalue eigenvectors of $`E_z`$ gives


```math
\lambda_{\max}(E_z)
\leq r\,\lambda_{\min}(E_z).
```


A nonzero effect therefore has strictly positive minimum eigenvalue. Every nonidentity Pauli has equally large $`+1`$ and $`-1`$ eigenspaces. The traces of $`E_z`$ on those two eigenspaces have ratio at most $`r`$. Their normalized difference is $`v_P(z)`$, proving $`|v_P(z)|\leq c`$.

For the second statement let $`F_z=E_z/q_z`$, so $`\mathrm{Tr}F_z=d`$. Pauli orthogonality gives


```math
\sum_{P\in\mathcal P_*}v_P(z)^2
=
\frac{\mathrm{Tr}F_z^2}{d}-1.
```


The right-hand side is the variance of the eigenvalues of $`F_z`$, whose mean is one. If their minimum is $`a`$, they lie in $`[a,ra]`$. The scalar inequality $`(x-a)(ra-x)\geq0`$, averaged over the eigenvalues, yields


```math
\frac{\mathrm{Tr}F_z^2}{d}-1
\leq (ra-1)(1-a)
\leq \frac{(r-1)^2}{4r}.
```


The last maximum occurs at $`a=(r+1)/(2r)`$. Average over $`z`$ to finish. $`\square`$

The lemma does not say that every Pauli signal is small. A private report can concentrate its information on a selected observable. It says that its squared signals, summed over all possible unknown Paulis, have a bounded total.

## An adaptive lower bound for identification

Introduce a reference experiment outside the target promise: every raw training specimen is $`I/d`$, and its public label is still an independent fair sign. Run exactly the same adaptive protocol. Let $`Q_0`$ be its full classical transcript law in this reference experiment, and let $`Q_H`$ be its transcript law on target $`H`$.

All relative entropies below use natural logarithms. Write


```math
\mathrm{kl}(u\Vert v)
=
u\log\frac uv+(1-u)\log\frac{1-u}{1-v}
```


for binary relative entropy.

**Lemma 2 — reverse-divergence budget.** For every $`N`$-specimen adaptive classical protocol,


```math
\sum_{H\in\mathcal H}D(Q_0\Vert Q_H)
\leq C_\varepsilon N.
```


**Proof.** Fix a history occurring in the reference experiment and fix the next public label $`y`$. For the next chosen POVM, the report laws under $`+P`$ and $`-P`$ are


```math
p_{+P}(z\mid y)=q_z[1+yv_P(z)],
\qquad
p_{-P}(z\mid y)=q_z[1-yv_P(z)].
```


Consequently


```math
\begin{aligned}
D(q\Vert p_{+P})+D(q\Vert p_{-P})
&=
\mathbb E_q[-\log(1-v_P^2)]\\
&\leq
\frac{\mathbb E_q[v_P^2]}{1-c^2}.
\end{aligned}
```


The inequality follows from
$`-\log(1-u)\leq u/(1-c^2)`$ for $`0\leq u\leq c^2`$.
Summing over $`P`$ and using Lemma 1 bounds the next-report divergence sum by $`C_\varepsilon`$. Averaging over the next public label preserves the bound.

Now apply the relative-entropy chain rule with $`Q_0`$ as the first argument. For every target, the preceding histories in that chain rule are averaged under the same reference law $`Q_0`$. Therefore the one-step sum bound applies at every adaptive history. Sum over the at most $`N`$ releases. Independent protocol randomness and the public labels have the same conditional laws in both experiments and add no divergence. $`\square`$

Using the reference law in this direction is essential to the proof: it gives a common distribution over histories for the sum over targets.

**Theorem 3 — private classical identification.** Suppose a classical protocol outputs $`\widehat H\in\mathcal H`$ and


```math
\Pr_H[\widehat H=H]\geq1-\delta
\qquad\text{for every }H\in\mathcal H,
```


where $`0\lt \delta\lt 1/2`$. Then


```math
N
\geq
\frac{L}{2C_\varepsilon}
\mathrm{kl}\!\left(\frac2L\,\middle\Vert\,1-\delta\right).
```


In particular, for every fixed $`\varepsilon>0`$ and fixed $`\delta\lt 1/2`$,


```math
N=\Omega_{\varepsilon,\delta}(d^2).
```


For fixed $`\delta`$ and $`0\lt \varepsilon\leq1`$, the displayed lower bound is $`\Omega_\delta(d^2/\varepsilon^2)`$, with a dimension-independent constant.

**Proof.** Let $`A_H=\{\widehat H=H\}`$. Their reference probabilities sum to one, so at least $`L/2`$ targets satisfy $`Q_0(A_H)\leq2/L`$. On every such target $`Q_H(A_H)\geq1-\delta`$. Because $`L\geq6`$, we have $`2/L\lt 1-\delta`$. Binary data processing, followed by monotonicity of binary relative entropy on these separated intervals, gives


```math
D(Q_0\Vert Q_H)
\geq
\mathrm{kl}\!\left(\frac2L\,\middle\Vert\,1-\delta\right).
```


Sum over those targets and use Lemma 2. For fixed $`\delta`$, the binary divergence tends to $`\log(1/\delta)>0`$ as $`d`$ grows. Also $`C_\varepsilon=\Theta(\varepsilon^2)`$ uniformly on $`0\lt \varepsilon\leq1`$. $`\square`$

This proof allows adaptive private measurements, rather than comparing only a fixed noise channel followed by measurement.

## Constant clean-test advantage already costs $`d^2`$

After training, give the learner one fresh clean state $`\rho_{H,Y}`$, with its true label hidden. A classical training transcript $`T`$ determines a binary POVM $`G^T_+,G^T_-`$ for this test. Fresh quantum ancillas, a circuit chosen from $`T`$, and prediction randomness can all be absorbed into that POVM. Define its test observable


```math
A_T=G^T_+-G^T_-,
\qquad -I\leq A_T\leq I.
```


Conditional on $`T`$, its success probability is exactly


```math
\Pr[\widehat Y=Y\mid H,T]
=
\frac12+\frac{\mathrm{Tr}(A_TH)}{2d}.
```


This formula averages over the fresh fair test label and the test measurement.

**Theorem 4 — private classical prediction.** Fix $`0\lt \beta\lt 1/2`$. Suppose that for every target $`H`$, the learner's success probability, averaged over its training transcript and the fresh test, is at least $`1/2+\beta`$. Let


```math
b_\beta=\frac{\beta}{1-\beta},
\qquad
t_{d,\beta}=\frac{2}{L\beta^2}.
```


Whenever $`t_{d,\beta}\lt b_\beta`$,


```math
N
\geq
\frac{L}{2C_\varepsilon}
\mathrm{kl}(t_{d,\beta}\Vert b_\beta).
```


Thus every fixed positive clean-test advantage requires


```math
N=\Omega_{\varepsilon,\beta}(d^2)
```


for fixed $`\varepsilon>0`$. The statement does not require the learner to identify $`H`$ explicitly.

**Proof.** Put $`a_H(T)=\mathrm{Tr}(A_TH)/d`$. The success assumption gives $`\mathbb E_H[a_H(T)]\geq2\beta`$, while $`a_H(T)\leq1`$. Hence


```math
\Pr_H[a_H(T)\geq\beta]
\geq\frac{\beta}{1-\beta}
=b_\beta.
```


For a fixed transcript define the signed Pauli list


```math
\mathcal L(T)
=
\left\{H\in\mathcal H:
\frac{\mathrm{Tr}(A_TH)}d\geq\beta
\right\}.
```


Pauli orthogonality and $`\mathrm{Tr}A_T^2/d\leq1`$ imply


```math
\sum_{P\in\mathcal P_*}
\left(\frac{\mathrm{Tr}(A_TP)}d\right)^2
\leq1.
```


At most one of $`+P,-P`$ can enter $`\mathcal L(T)`$. Consequently
$`|\mathcal L(T)|\leq\beta^{-2}`$.
The list is an analytical function of the transcript; no efficient matrix representation or enumeration algorithm is assumed.

Under the reference experiment,


```math
\sum_{H\in\mathcal H}
Q_0[H\in\mathcal L(T)]
=
\mathbb E_0|\mathcal L(T)|
\leq\beta^{-2}.
```


Therefore at least $`L/2`$ targets have reference inclusion probability at most $`t_{d,\beta}`$. Their true inclusion probabilities are at least $`b_\beta`$. Apply binary data processing to each inclusion event, sum, and use Lemma 2. $`\square`$

The test specimen in this theorem is clean. The theorem makes no constant-accuracy promise when test specimens themselves must pass through a private channel. Its purpose is to show that the classical training lower bound is already present in ordinary supervised prediction, rather than arising solely from an exact parameter-identification requirement.

## A private noisy tournament attains the classical order

The lower bound has a matching classical procedure in its dependence on dimension. It can use computation and measurement choices adaptively, just as the converse allows.

For an arm $`Q\in\mathcal H`$, measure $`Q`$ on a fresh training specimen and apply binary randomized response with contrast $`c=\tanh(\varepsilon/2)`$. Release only the randomized sign multiplied by the public training label. Equivalently, the released observation $`W\in\{+1,-1\}`$, conditional on the public label $`y`$, has POVM effects


```math
E^{Q,y}_w=\frac{I+cwyQ}{2}.
```


The maximum ratio between report probabilities on any two states is at most


```math
\frac{1+c}{1-c}=e^\varepsilon.
```


Thus the actual released observation is private. Its expectation on target $`H`$ is


```math
\mu_Q
=\mathbb E_H[W]
=
c\,\frac{\mathrm{Tr}(QH)}d
=
\begin{cases}
+c,&Q=H,\\
-c,&Q=-H,\\
0,&\text{otherwise}.
\end{cases}
```


There is exactly one arm of mean $`+c`$, separated from every competitor by a gap of at least $`c`$.

Pad the $`L`$ arms to $`L'=2^{\lceil\log_2L\rceil}\lt 2L`$ arms with input-independent mean-zero dummy arms. Pair them in a knockout bracket. At round $`r=1,\ldots,\log_2L'`$, sample every surviving arm


```math
t_r
=
\left\lceil
\frac8{c^2}
\log\frac{2^{r+1}}{\delta}
\right\rceil
```


times on fresh specimens, and advance the arm with the larger empirical mean in each match. Dummy observations can be generated without specimens; charging them as if they used specimens only enlarges the stated bound.

**Theorem 5 — private tournament.** For every $`0\lt \delta\lt 1`$, the tournament outputs $`H`$ with probability at least $`1-\delta`$ for every target $`H`$, and uses no more than


```math
N_{\mathrm{tor}}
\leq
L'
\left[
2+\frac8{c^2}
\left(6\log2+2\log\frac1\delta\right)
\right]
```


specimens. In particular, at bounded confidence,


```math
N_{\mathrm{tor}}=O_\varepsilon(d^2).
```


For $`0\lt \varepsilon\leq1`$, the bound is
$`O[d^2\varepsilon^{-2}(1+\log(1/\delta))]`$.

**Proof.** Condition on the true arm surviving until round $`r`$. Its observations have mean $`c`$, and the opposing arm's mean is at most zero. If the true arm loses, either its empirical mean is at most $`c/2`$, or its opponent's empirical mean is at least $`c/2`$. Hoeffding's inequality for signs in $`[-1,1]`$ gives loss probability at most


```math
2\exp(-t_rc^2/8)\leq\delta/2^r.
```


Only the true arm's path needs to be protected. A union bound over its rounds gives total failure at most $`\sum_{r\geq1}\delta/2^r=\delta`$.

At round $`r`$, at most $`L'/2^{r-1}`$ arms remain. Bound the ceiling in $`t_r`$ by one plus its argument and use


```math
\sum_{r\geq1}2^{-r+1}=2,
\qquad
\sum_{r\geq1}(r+1)2^{-r+1}=6
```


to obtain the sample bound. Fresh observations justify the same conditional Hoeffding bound after every adaptive selection. $`\square`$

Once the tournament has identified $`H`$, measuring $`H`$ predicts each fresh clean label exactly. Identification failure is the only error charged in that resulting prediction guarantee.

## The resulting classical frontier

For any fixed privacy level $`0\lt \varepsilon\lt \infty`$ and fixed identification failure below $`1/2`$, the worst-case specimen complexity of adaptive private classical identification is


```math
N_{\mathrm C}(d;\varepsilon)=\Theta_\varepsilon(d^2).
```


For every fixed target prediction advantage $`0\lt \beta\lt 1/2`$, the same $`\Theta_\varepsilon(d^2)`$ dimension dependence holds for expected clean-test prediction. The prediction lower bound is Theorem 4. For the upper bound, choose a fixed tournament failure $`\delta\lt 1/2-\beta`$; on successful identification the prediction is exact, and even assigning zero success on the failure event gives total success at least $`1-\delta>1/2+\beta`$.

At high privacy $`0\lt \varepsilon\leq1`$, bounded-confidence identification and fixed-advantage prediction have order $`d^2/\varepsilon^2`$, with constants depending on the fixed failure or advantage. This is a statement about specimen complexity under the stated local release model. It does not compare central differential privacy, multi-specimen client preprocessing, retained hidden cross-record keys, or quantum reports processed with persistent quantum memory.
