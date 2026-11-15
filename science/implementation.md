# Implementation and resource account

The separation counts native quantum training specimens. It assumes no state-loading oracle, preparation inverse, QRAM, efficient collective decoder, or free setup. Pauli preprocessing below has exact inexpensive per-report gates in the ideal finite-gate model; selecting a good short list and decoding its outputs remain separate costs.

## A finite private report

Let $`d=2^n`$. Fix a public list of $`K`$ unitaries for which

```math
\Phi(X)=\frac1K\sum_{i=1}^{K}U_iXU_i^\dagger,\qquad
\frac{1-\eta_0}{d}I\preceq\Phi(\rho)
\preceq\frac{1+\eta_0}{d}I
```

for every input state, with $`0\lt \eta_0\lt \tanh(\varepsilon/2)`$.

For every specimen, draw a fresh private uniform index $`i`$ and an independent public uniform Clifford $`C`$. Apply $`C^\dagger U_iC`$, then release its quantum output, $`C`$, and the public label $`Y`$. Averaging the hidden index realizes

```math
\Lambda(\rho)=\mathbb E_C\,|C\rangle\langle C|
\otimes C^\dagger\Phi(C\rho C^\dagger)C.
```

The private index is not released: that would expose an invertible unitary branch. Fresh independent indices are part of the protocol; marginal privacy does not justify reusing one hidden index across records. The good list is public, reusable setup, not a secret key. Choose $`K`$ to be a power of two above the sufficient theorem bound, at constant-factor cost, for exact sampling with $`\log_2K`$ private bits. Exact rejection sampling handles general $`K`$.

### Exact Pauli gates

Aubrun's isotropic-ensemble theorem supplies good tensor-Pauli lists of length

```math
K=O\!\left(d(\log d)^6/\eta_0^2\right).
```

This is $`d`$ times the sixth power of $`\log d`$. It yields the $`O_\varepsilon(d(\log d)^7)`$ specimen upper bound at fixed privacy.

Store each Pauli by $`2n`$ binary $`X/Z`$ coordinates. Clifford conjugation preserves tensor Paulis, so compute $`C^\dagger U_iC`$ classically and apply it directly. Executing $`C`$ and $`C^\dagger`$ on the record is unnecessary; global phases do not affect the channel.

The list occupies $`2Kn`$ classical bits, up to indexing overhead. Its address is classical: use an ordinary classical lookup or charge a linear scan. Symplectic matrix multiplication computes the conjugation in $`O(n^2)`$ bit operations. Applying the selected Pauli uses at most $`2n`$ $`X/Z`$ gates. A public Clifford descriptor occupies $`O(n^2)`$ bits; the explicit Koenig–Smolin sampler/indexer uses $`O(n^3)`$ classical operations. No table is queried in coherent superposition.

### Source and clean deployment

Every preparation of $`\rho_{H,Y}=(I+YH)/d`$ is charged. The learner receives no coherent source access or inverse. A source holding secret $`H`$ can map it to a single-qubit $`Z`$ by a Clifford, prepare the required eigenstate with $`n-1`$ maximally mixed qubits, and apply the inverse Clifford. This uses $`O(n)`$ Clifford gates with unrestricted connectivity and fresh classical randomness for mixed factors. It is a source construction, not information given to the learner. Geometry and routing add their actual costs.

After identification, store the signed-Pauli description in $`O(n)`$ bits. On a fresh clean specimen, measure its Pauli factors and multiply their outcomes with the known sign, using $`O(n)`$ basis changes and measurements. Correct identification gives exact prediction for the ideal clean source. The theorem does not assert constant accuracy on privatized test data.

## Resources and setup

| Resource | Short dense-unitary list | Tensor-Pauli list |
| --- | --- | --- |
| List length at fixed $`\eta_0`$ | $`O_{\eta_0}(d)`$ | $`O_{\eta_0}(d(\log d)^6)`$ |
| Setup storage | All matrices or compiled circuits | $`2Kn`$ classical Pauli bits |
| Quantum work per report | Selected dense circuit with Clifford conjugation | At most $`2n`$ $`X/Z`$ gates after classical conjugation |
| Public record per specimen | $`Y`$ and $`O(n^2)`$ Clifford bits | $`Y`$ and $`O(n^2)`$ Clifford bits |
| Fresh private randomness | $`\log K`$ bits for power-of-two $`K`$ | $`\log K`$ bits for power-of-two $`K`$ |
| Quantum report | $`n`$ qubits | $`n`$ qubits |
| Direct storage for $`N`$ reports | $`Nn`$ coherent data qubits, plus flags | $`Nn`$ coherent data qubits, plus flags |
| Identification samples | $`O_\varepsilon(d\log d)`$ | $`O_\varepsilon(d(\log d)^7)`$ |
| Setup and decoder time | No efficient bound established | Cheap report gates; no efficient setup, certification or decoder bound established |

Generic dense unitaries are expensive. A conservative finite synthesis decomposes each into $`O(d^2\mathrm{poly}(n))`$ continuous elementary gates, then approximates single-qubit factors over a finite universal set. All $`K`$ compiled circuits must be stored. The sample advantage is not an end-to-end runtime advantage.

The collective decoder accesses privatized reports only. The direct pretty-good-measurement construction uses $`Nn`$ coherent data qubits and can require additional workspace. Its matrices, precision and compiled gate count may be enormous. Every finite instance is a finite POVM approximable by a finite circuit to fixed error, but no efficient decoder follows. Public flags are ordinary classical inputs to its construction.

The randomizer results establish a good fixed list's existence. A random setup list that might fail all-state randomization cannot simply be called pure $`\varepsilon`$-private. The theorem uses selected nonuniform good-list setup; no efficient uniformly certified generator is established.

Strict margin permits finite certification in principle. For unit vectors with $`\Vert\psi-\varphi\Vert_2\le r`$, trace contraction implies

```math
\Vert\Phi(|\psi\rangle\langle\psi|)
-\Phi(|\varphi\rangle\langle\varphi|)\Vert_\infty\le2r.
```

A sufficiently fine finite pure-state net and certified eigenvalue intervals therefore certify a global bound with slack. A net resolving an $`O(1/d)`$ absolute spectral margin already has size exponential in $`d`$; list search may cost still more. These costs are not free preprocessing.

The rates concern fixed positive $`\varepsilon`$ and sufficiently large $`d`$. The actual list must meet $`K\le d^2/2`$ where the upper-bound proof uses that inequality. A small finite demonstration does not establish this asymptotic crossover.

## Compilation with a strict privacy margin

Set

```math
\eta_*=\tanh(\varepsilon/2),\qquad m=\eta_*-\eta_0>0.
```

If an actual CPTP implementation obeys

```math
\Vert\widetilde\Phi-\Phi\Vert_\diamond\le\kappa\le m/(2d),
```

then trace norm dominates operator norm and

```math
\frac{1-\eta_0-d\kappa}{d}I
\preceq\widetilde\Phi(\rho)
\preceq\frac{1+\eta_0+d\kappa}{d}I.
```

Consequently,

```math
\widetilde\Phi(\rho)
\preceq
\frac{1+\eta_0+d\kappa}{1-\eta_0-d\kappa}
\,\widetilde\Phi(\sigma)
\preceq e^\varepsilon\widetilde\Phi(\sigma).
```

This remains pure privacy. For a dense list, compile each $`U_i`$ to a unitary $`V_i`$, up to global phase, with

```math
\VertU_i-V_i\Vert_\infty\le\delta\le m/(4d).
```

The unitary-channel bound gives

```math
\left\Vert\frac1K\sum_i\mathrm{Ad}_{V_i}
-\frac1K\sum_i\mathrm{Ad}_{U_i}\right\Vert_\diamond
\le2\delta.
```

The actual mixed-unitary implementation is exactly CPTP and unital, still with a list of length $`K`$. Apply the learning proof directly to that actual channel: its low-list-rank trace identity and its flattening bound both remain valid. There is no uncharged infinite-precision unitary oracle.

Absolute channel accuracy $`O(m/d)`$ can be exponentially small in $`n`$. Its logarithm is $`O(n+\log(1/m))`$, which enters finite synthesis. The Pauli implementation avoids this synthesis approximation in the ideal $`X/Z`$ model. A physical device must establish its actual channel bound; average gate fidelity alone does not establish this all-input condition.

Approximation of the final collective POVM changes identification error. Every subsequent CPTP map preserves the privacy already established for the reports. Decoder compilation precision and costs remain charged.

## Product records and quantum references

The guarantee is ordinary one-record privacy,

```math
\Lambda(\rho)\preceq e^\varepsilon\Lambda(\sigma),
```

conditional on the public label and all released flags. It is not inferred by discarding a flag that is actually released.

For product datasets differing only in record $`j`$, independent reports obey

```math
\begin{aligned}
&\Lambda_1(\rho_1)\otimes\cdots\otimes
\Lambda_j(\rho_j)\otimes\cdots\otimes\Lambda_N(\rho_N)\\
&\quad\preceq e^\varepsilon
\Lambda_1(\rho_1)\otimes\cdots\otimes
\Lambda_j(\sigma_j)\otimes\cdots\otimes\Lambda_N(\rho_N).
\end{aligned}
```

Tensoring unchanged positive factors preserves order, as does every collective CPTP map and measurement. Thus coherent decoding preserves the stated record-neighbor guarantee. Identifying population parameter $`H`$ is compatible with it: changing $`H`$ changes all specimens.

This argument does not prove privacy when the changed record is entangled with a retained reference or other raw records. The definition imposed no corresponding inequality on $`\Lambda\otimes\mathrm{id}_R`$ for such joint states. The source and record-neighbor extension use independent specimens; reference-secure privacy is not claimed.

## Sources

- G. Aubrun, [On almost randomizing channels with a short Kraus decomposition](https://arxiv.org/abs/0805.2900), Theorems 1–2 and Sections 2.5–2.6. Both list-existence bounds are inherited.
- R. Koenig and J. A. Smolin, [How to efficiently select an arbitrary Clifford group element](https://arxiv.org/abs/1406.2170). Explicit polynomial classical sampling/indexing.
- A. Barenco et al., [Elementary gates for quantum computation](https://arxiv.org/abs/quant-ph/9503016), and C. M. Dawson and M. A. Nielsen, [The Solovay–Kitaev algorithm](https://arxiv.org/abs/quant-ph/0505030). Finite universality and approximation are inherited; the margin inequalities specify the accuracy needed here.
