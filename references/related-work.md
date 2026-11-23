# Related work and contribution boundaries

The comparison concerns the same supplied quantum examples on both sides: a public balanced label $`y`$, a feature specimen $`(I+yH)/d`$, and an unknown signed nonidentity Pauli $`H`$, where $`d=2^n`$. Each specimen is privatized before collection. The distinction is whether the released private output remains quantum or is converted immediately to a classical report. All-input local privacy is imposed on each mechanism, conditional on its public information.

The result is a sample-complexity separation at fixed positive privacy as dimension grows. It is not a claim that quantum advantage under local privacy is new, and it does not establish an efficient collective decoder or a hardware crossover. The precise theorem domains and resource charges are in the scientific account.

## The source and quantum-memory comparison are inherited

The public project [Quantum Learning with Label Noise](https://github.com/GoGoKo699/Quantum-Learning-Label-Noise/tree/f305698454964e101311b3a337efe49c71808cff) uses exactly this signed-Pauli supervised source and a clean future prediction task. Its [model](https://github.com/GoGoKo699/Quantum-Learning-Label-Noise/blob/f305698454964e101311b3a337efe49c71808cff/science/model.md) makes public annotations, native specimen access and consumable quantum models explicit. Its [collective-statistics result](https://github.com/GoGoKo699/Quantum-Learning-Label-Noise/blob/f305698454964e101311b3a337efe49c71808cff/science/collective_statistics.md) gives order $`n/\gamma^2`$ examples under annotation contrast $`\gamma`$; its [individual-measurement converse](https://github.com/GoGoKo699/Quantum-Learning-Label-Noise/blob/f305698454964e101311b3a337efe49c71808cff/science/individual_measurements.md) gives order $`d/\gamma^2`$ as a necessary cost when quantum memory does not persist between examples.

That source, its Pauli second-moment identities, and its separation of sample complexity from computational efficiency are not new contributions here. Annotation corruption in that project is not a universal privacy condition. In particular, choosing a contrast in those formulas does not optimize over private quantum or classical mechanisms.

[Chen, Cotler, Huang and Li](bibliography.md#cchl2021) establish the general quantum-memory learning separation and learning-tree framework. Here the classical converse adds the spectrum restriction on every private POVM effect and a reverse-relative-entropy argument valid under adaptive classical feedback. The quantum construction instead combines an established approximate randomizer with public Clifford symmetrization and a retained-signal calculation. These mechanisms establish the additional privacy-constrained comparison.

## Private measurements and coherent-example learning

[Angrisani and Kashefi](bibliography.md#ak2025), using the numbering in arXiv:2203.03591v2, prove the equivalence between private measurements and quantum statistical queries in Theorems 4.1–4.2. Proposition 5.1 gives private parity learning from coherent quantum examples using private measurements and classical communication.

These results already establish compatibility of local privacy and quantum learning advantage. Their parity comparison changes the example access relative to classical examples. The present experiment fixes one native quantum source for both competitors and compares private quantum outputs with all adaptive private classical reports. Its collective learner retains quantum specimens after privatization; it is not a private-measurement/QSQ learner.

## Quantum advantage in private hypothesis testing already exists

[Nam, Park, Lee and Bae](bibliography.md#nplb2026), Sections III–VII of arXiv:2501.10152v4, compare optimized classical and quantum local mechanisms for hypothesis testing on classical samples. They establish advantages in error exponents for specified distributions and small alphabets using nonorthogonal states followed by depolarization.

The present result concerns growing-dimensional native quantum data, an unknown Pauli among order $`d^2`$ targets, and specimen complexity against adaptive classical privatization. Its significance rests on this asymptotic same-source comparison, not on being the first private quantum advantage.

## Generic utility, specified observables, and released records

[Nuradha, Bhalerao and Leditzky](bibliography.md#nbl2026) optimize generic state utility in Theorem 7 and specified-observable estimation in Propositions 8–12 of arXiv:2602.10510v1. Their fixed-observable mechanisms can depend on the observable. Here the target Pauli is unknown when a specimen is privatized.

Section IV-B1 and Eq. (23) distinguish another relevant object: an averaged measure-and-prepare quantum channel. A released classical snapshot description, including its random basis information, is a different output channel. Privacy of the averaged quantum state does not alone certify privacy of that richer record. The present model includes every accessible flag in the released output and checks privacy conditional on the public Clifford. This interface distinction is separate from an estimation-error calculation.

## The entanglement-breaking threshold is a different regime

[Bhalerao, Nuradha and Leditzky](bibliography.md#bnl2026), Theorem III.1 of arXiv:2609.13418v1, show that every input-dimension-$`d`$ QLDP channel is entanglement-breaking when $`\varepsilon\leq\log[d/(d-1)]`$. Their Theorem V.1 simulates binary quantum-memory learning through an entanglement-breaking channel by single-copy measurements of the raw inputs and classical storage.

Here $`\varepsilon>0`$ is fixed before $`d`$ grows; that threshold shrinks with dimension. The separation does not contradict their theorem or establish the transition near its boundary. Their simulation also does not assert that the simulated raw-input measurement itself satisfies the same privacy constraint.

## Approximate randomization supplies the private channel

[Hayden, Leung, Shor and Winter](bibliography.md#hlsw2004) established short random-unitary approximations to complete randomization. [Aubrun](bibliography.md#aubrun2009), Theorem 1 of arXiv:0805.2900v2, supplies an operator-norm randomizer with $`K=O(d/\eta^2)`$ Haar unitaries. His Theorem 2 supplies $`K=O(d(\log d)^6/\eta^2)`$ for isotropic ensembles, including tensor Paulis.

These are imported existence theorems. This project supplies their supervised-learning use: a lower bound on surviving Pauli energy, its distribution across all target pairs by public Clifford randomization, and a resulting fidelity separation. The $`O_\varepsilon(d\log d)`$ specimen bound uses arbitrary-unitary randomizers. The Pauli alternative has a larger polylogarithmic factor; neither good-list existence nor low per-use gate cost implies efficient setup certification or decoding.

## The discrimination and Clifford tools are standard

The conversion from a pairwise root-fidelity gap to a logarithmic-in-ensemble-size copy overhead uses established mixed-state discrimination. [Montanaro](bibliography.md#montanaro2019), Theorem 1 and Lemma 3, provides a direct worst-case PGM statement. [Cheng et al.](bibliography.md#cheng2025), Theorem 11 and Appendix J in arXiv:2403.17868v2, gives the prior-weighted fidelity bound used in the related source project. Root fidelity here is $`\Vert\sqrt{\rho}\sqrt{\sigma}\Vert_1`$; it is the square root of sources that use squared fidelity.

Uniform Clifford selection is also established; [Koenig and Smolin](bibliography.md#ks2014) give an explicit polynomial-operation indexing and selection algorithm. No new Clifford sampler or PGM implementation algorithm is claimed.

The matching noninteractive quantum identification converse uses standard Haar second moments, the order-two Petz relative-entropy bound, Holevo information and Fano's inequality. Their exact calculation with all-input local privacy gives the task-specific per-report information budget in [the converse](../science/quantum-converse.md). It does not replace the correlated ensemble mean by a product or extend the product-encoder bound to adaptive quantum encoders. [Watrous](bibliography.md#watrous2018) supplies the standard quantum-information foundations.

## Privacy with an external quantum reference

[Li, Guan and Ying](bibliography.md#lgy2026), Definition 3 and Section V of arXiv:2611.25775v1, compare outputs on joint inputs with the same reference marginal and relate that privacy condition to Choi and replacement-channel order. The [learning theorem](../science/reference-secure-learning.md) uses this condition with an explicit reference dimension and arbitrary report registers. The averaged probe converts the privacy guarantee into a Pauli information budget and a matching specimen law. The quantum-memory feedback argument extends the original classical reverse-divergence proof to a learner retaining quantum reports.

[Aubrun](bibliography.md#aubrun2009) supplies the constant-net precedent for ordinary operator randomization. [Lancien and Winter](bibliography.md#lw2024) place low-Kraus channel approximation in a broader setting. The construction here controls the relative order against a bounded reference and uses the surviving Pauli response to recover a classifier. Haar concentration from [Meckes](bibliography.md#meckes2019) supplies the fixed-probe estimate.

## What remains outside the conclusion

Raw collective preprocessing before local privatization, hidden correlated keys, and uncounted released randomness change the experiment. The feedback theorem permits classical control over successive fresh encoders. The optimum for intermediate reference dimensions with feedback remains open. Public labels, expensive randomizer descriptions, coherent training storage, and the collective measurement remain part of the stated resource account.
