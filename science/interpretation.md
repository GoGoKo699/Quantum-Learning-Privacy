# Local privacy and collective learning

The hidden target is a pattern shared by many examples. Local privacy protects one owner's quantum example from any measurement on that owner's released report. It does not require the population-level pattern to remain unknowable after many independent owners contribute.

This project asks how the form of that release changes the learning cost. Both learners start with the same labeled quantum specimens, and both local mechanisms must obey the same all-input-state privacy inequality. The classical learner can optimize and adapt its private measurements. The quantum construction uses a predetermined local channel, retains its quantum outputs, and measures them together.

## Two information budgets

A classical private report is a POVM outcome. Privacy bounds the ratio between the largest and smallest eigenvalues of every nonzero effect. Pauli orthogonality then gives a bounded sum of squared responses over all $`d^2-1`$ possible directions. A mechanism can focus on one direction, but it cannot respond strongly to all of them. The reverse-relative-entropy argument evaluates every adaptive choice under one common reference transcript, so changing the next measurement after each report does not remove the bound.

The matching tournament illustrates how a classical learner spends that budget. It privately tests candidate Paulis, keeps the winners, and allocates increasingly reliable comparisons to the shrinking set. Only a constant total cost per initial candidate is needed, so the upper bound has order $`d^2`$ rather than an extra factor of $`\log d`$.

A quantum report retains a matrix of small responses instead of choosing one classical record. An operator-randomizing channel hides every individual input, yet a channel with order $`d`$ Kraus unitaries cannot erase all of its Pauli response energy. Public Clifford randomization distributes that surviving energy uniformly among the unknown targets without disclosing the private Kraus index. A collective measurement combines the weak responses from many reports. The [noninteractive converse](quantum-converse.md) shows that each such report carries only order $`1/d`$ target information at fixed privacy; learning one of order $`d^2`$ targets therefore needs order $`d\log d`$ reports.

The quantitative distinction is between the budget in a classical private effect and the information retained by a private quantum channel. The randomizer and discrimination tools themselves are established ingredients.

## What the exponential separation means

For $`n`$ qubits and fixed positive privacy and bounded error, the identification costs are

```math
N_{\mathrm C}=\Theta(4^n),\qquad
N_{\mathrm Q,prod}=\Theta(n2^n).
```

The quantum product-encoder cost is optimal in its stated class. The classical converse permits adaptive encoders and unlimited classical computation. The same quantum protocol learns a clean-test classifier, while any private classical learner attaining fixed positive clean-test advantage still needs order $`4^n`$ training specimens. The [prediction-to-identification measurement](reference-secure-privacy.md) gives the matching product-encoder lower bound for prediction, including a consumable quantum model.

The comparison is statistical. Both costs are exponential in the number of qubits. Generic randomizer setup and collective decoding can also be expensive. The exact Pauli implementation reduces the per-report quantum gates at a larger polylogarithmic sample cost; it does not supply an efficient decoder or efficiently certified setup.

## Relation to the entanglement-breaking privacy boundary

[Bhalerao, Nuradha, and Leditzky](https://arxiv.org/abs/2609.13418v1) prove that every $`d`$-input $`\varepsilon`$-QLDP channel is entanglement-breaking when

```math
\varepsilon\le\log\frac d{d-1}.
```

They also show that learning from entanglement-breaking outputs with quantum memory can be simulated by measuring raw inputs individually and storing classical information. That simulation need not preserve the privacy of the classical latent measurement record; the theorem here compares optimized private classical reports themselves.

The universal entanglement-breaking threshold shrinks with dimension. The present separation holds at every fixed positive $`\varepsilon`$ for sufficiently large $`d`$, and so does not contradict it. It supplies an operational surviving advantage in that regime. Non-entanglement-breaking behavior alone would not have proved such a learning advantage.

The original short-list construction alone does not determine the sharp transition as $`\varepsilon`$ decreases with $`d`$. Its actual list length and the condition $`K\le d^2/2`$ remain part of the finite theorem. The reference-secure chapter gives uniform small-privacy scaling by mixing a constant-distortion list with exact replacement.

## Privacy and physical scope

Ordinary privacy covers all unassisted input states and measurements of the actual release. Reference-secure privacy also covers joint measurements with a retained quantum reference and compares inputs with the same reference marginal. At fixed privacy, the [proof](reference-secure-privacy.md) bounds the average squared response per Pauli by order $`1/(dk)`$, so the cost for predetermined quantum encoders grows linearly with $`k`$. At full reference protection the adaptive classical tournament reaches the same specimen order as arbitrary retained quantum memory. The protection still concerns each owner's release. Learning the shared population target remains the task.

The source is classical data only in its labels; its features are native quantum specimens. Every feature state is separable across its qubits. In the Pauli-list implementation, each realized branch is a tensor product of Pauli gates, so individual quantum reports remain separable as well. The quantum resource is retaining reports for joint processing across examples. The randomly selected tensor-Pauli pattern can be correlated across qubits within one specimen; a product of separately chosen single-qubit private channels would be a different mechanism.

The examples, local randomization, public flags, communication, coherent storage, final measurement and clean deployment operation are accounted for in [implementation](implementation.md). Device noise, geometric routing, a uniformly efficient all-state setup certificate, and a polynomial-time collective decoder require additional work. None is assumed by the statistical result.
