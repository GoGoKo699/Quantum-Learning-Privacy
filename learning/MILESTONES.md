# Thirty understanding milestones

The selected educational anchor is John Watrous, [*The Theory of Quantum Information* (2018)](https://cs.uwaterloo.ca/~watrous/TQI/), abbreviated **W** below. The [Watrous bridge](WATROUS_BRIDGE.md) translates its notation and identifies the additional project-specific arguments. W uses base-two logarithms; the scientific chapters use natural logarithms. Its fidelity convention is the root fidelity used here.

The map has **14 background/preliminaries milestones and 16 narrative/innovation milestones**. The background phase connects one physical specimen, its measurement and release, and the information measures needed to formulate the full experiment. The narrative connects the private classical report budget to the quantum encoder, then tracks how a protected reference changes the specimen cost of identification and clean prediction.

The dependencies below refer only to earlier milestones. Textbook pointers locate foundations; the named project statements supply the task-specific results. The map covers the contribution's conceptual structure and load-bearing limitations, rather than every calculation in its proofs.

## Background and preliminaries

### M01 — Background: One labeled physical specimen

- **Central question:** What information does one owner actually possess and release in this learning problem?
- **Understanding target:** Distinguish the public training label, the unknown common target, and the mixed quantum specimen $`\rho_{H,Y}=(I+YH)/d`$. Explain why a density operator is a physical input rather than a free classical description of its hidden preparation.
- **Dependencies and story role:** No earlier milestone. Establishes the local object from which every subsequent operation is built.
- **Conceptual connection:** Mixed-state descriptions connect uncertainty about an individual quantum system to a statistical pattern shared by independent examples.
- **Source pointers:** W §§2.1.1–2.1.2; [model](../science/model.md), “The source.”

### M02 — Background: Measurements produce the report

- **Central question:** How does a quantum specimen become a classical outcome or a predicted label?
- **Understanding target:** Interpret a POVM effect through its Born probability and a binary test through its observable $`A=G_+-G_-`$ with $`-I\preceq A\preceq I`$. Distinguish a measurement's complete outcome from a later function of that outcome.
- **Dependencies and story role:** M01. Gives the local input-output description used by both private reporting and clean-test prediction.
- **Conceptual connection:** A classical learning transcript can choose a quantum test, while its success is still represented by one effect or observable on the fresh specimen.
- **Source pointers:** W §2.3.1, Definition 2.34; [classical reports](../science/classical-reports.md), “The source and the allowed reports” and Theorem 4.

### M03 — Background: A Pauli pattern across qubits

- **Central question:** Why is an unknown signed Pauli a concrete supervised target?
- **Understanding target:** Explain $`d=2^n`$, the signed target set of size $`2(d^2-1)`$, and the balanced eigenspaces of a nonidentity Pauli. Relate a tensor Pauli's local factor measurements to exact clean-label prediction once its sign and factors are known.
- **Dependencies and story role:** M01–M02. Connects an individual example to the full family of possible targets.
- **Conceptual connection:** Separable feature states can contain a global parity pattern; input entanglement is not required for this learning task.
- **Source pointers:** W §§2.1.1–2.1.2 and §2.3.1 for registers, states, and measurements; local Pauli construction in [model](../science/model.md), “The source,” and [implementation](../science/implementation.md), “Source and clean deployment.”

### M04 — Background: Response energy in an operator basis

- **Central question:** How can responses to many possible observables share one finite budget?
- **Understanding target:** Read the Hilbert–Schmidt inner product and the orthogonality $`\mathrm{Tr}(PQ)=d\,\mathbf1_{\{P=Q\}}`$. Explain how a Pauli expansion and Parseval's identity turn a matrix's squared norm into a sum of squared coefficients.
- **Dependencies and story role:** M02–M03. Supplies the common algebraic language of the classical budget, quantum signal calculation, and prediction list.
- **Conceptual connection:** A local measurement effect and a quantum channel have different response budgets, although both are analyzed in the same operator basis.
- **Source pointers:** W §1.1.2, Eq. (1.81), and §1.1.3; local normalizations in [classical reports](../science/classical-reports.md), Lemma 1, and [quantum reports](../science/quantum-reports.md), Section 3.

### M05 — Background: A channel includes its discarded randomness

- **Central question:** What physical map is implemented by privately choosing a unitary branch?
- **Understanding target:** Interpret a CPTP map and its Kraus representation. Distinguish the mixed-unitary channel obtained after discarding a random index from the reversible branch obtained when that index is disclosed; recognize unitality as preservation of the identity.
- **Dependencies and story role:** M01–M04. Adds physical preprocessing to the specimen-and-measurement description.
- **Conceptual connection:** The same unitary list gives different recipient views depending on which registers leave the client.
- **Source pointers:** W §§2.2.1–2.2.2, Theorem 2.22; [quantum reports](../science/quantum-reports.md), Section 2; [implementation](../science/implementation.md), “A finite private report.”

### M06 — Background: Classical flags and averaged quantum states

- **Central question:** Why can an averaged quantum state be private while its classical preparation record is not?
- **Understanding target:** Represent a public flag and a quantum system as a block-diagonal classical-quantum state. Explain the difference between retaining a flag, conditioning on it, and tracing it out, using the basis-and-outcome snapshot example.
- **Dependencies and story role:** M02 and M05. Identifies the actual released object before privacy is imposed.
- **Conceptual connection:** A density operator does not grant access to its exact preparation description; the distinction changes the likelihood ratios an observer can obtain.
- **Source pointers:** W §§2.1.1–2.1.3 and §2.2.1; [privacy registers](../science/privacy-registers.md), “A quantum shadow state and its classical description.”

### M07 — Background: All-input local privacy as matrix order

- **Central question:** What does it mean to protect one quantum input against every measurement of its report?
- **Understanding target:** Interpret positive-semidefinite order as an event-probability inequality. Start with ordinary all-input privacy, then apply the same inequality to the joint output and reference for any two input states with equal reference marginals. Keep all public flags in the comparison.
- **Dependencies and story role:** M02 and M05–M06. Turns the released-register description into the shared reporting constraint.
- **Conceptual connection:** An equal reference marginal makes the comparison test the extra information about the input supplied by the report.
- **Source pointers:** W §1.1 for positive operators, §§2.1.3 and 2.2.1 for reference systems and channels, and §2.3.1 for measurements. See the [model](../science/model.md) and the [reference-secure privacy definition](../science/reference-secure-privacy.md).

### M08 — Background: Divergence along a classical experiment

- **Central question:** How can many weak reports be compared with one common reference experiment?
- **Understanding target:** Explain the direction of classical relative entropy, its chain rule over a transcript, and data processing to a binary event. Distinguish histories averaged under the reference law from histories averaged under an unknown target law.
- **Dependencies and story role:** M01–M02 and M07. Prepares the inference tool that will make the classical converse survive adaptive measurement choices.
- **Conceptual connection:** A reference source need not be a promised target to be useful in a lower-bound argument.
- **Source pointers:** W §§5.1.1–5.1.2 and the diagonal-state specialization of §5.2.3; the transcript calculation supplied in [classical reports](../science/classical-reports.md), Lemma 2.

### M09 — Background: Root fidelity and repeated quantum evidence

- **Central question:** How is distinguishability of two quantum reports related to distinguishability of many independent copies?
- **Understanding target:** Use root fidelity $`f(\rho,\sigma)=\Vert\sqrt\rho\sqrt\sigma\Vert_1`$ without confusing it with its square. Explain its purification meaning, product multiplicativity, and averaging over matching classical blocks.
- **Dependencies and story role:** M05–M06. Supplies the metric that connects a per-report quantum signal to collective identification.
- **Conceptual connection:** Classical public flags can be processed classically while the conditional quantum states retain the distinction measured by fidelity.
- **Source pointers:** W Definition 3.11 and §3.2.2, Theorem 3.22; local uses in [quantum reports](../science/quantum-reports.md), Sections 5–6.

### M10 — Background: Quantum relative entropy with support

- **Central question:** How can a quantum report's response be bounded without assuming its matrices commute?
- **Understanding target:** Interpret quantum relative entropy, support-restricted inverse operators, and a quadratic relative-entropy bound. Explain why the reference state must cover the report's support and why whitening does not make all operators commute.
- **Dependencies and story role:** M04–M05 and M07–M08. Provides the matrix information measure needed for the quantum converse.
- **Conceptual connection:** The quantum proof converts an all-input order bound into a summed quadratic response and then into information about the hidden target.
- **Source pointers:** W §§5.2.1 and 5.2.3, Theorem 5.35; the noncommutative quadratic calculation supplied in [quantum converse](../science/quantum-converse.md), Eqs. (Q3)–(Q8).

### M11 — Background: An ensemble is an inference problem

- **Central question:** How much information must a report reveal to identify one target among many?
- **Understanding target:** Distinguish the target ensemble, its average state, accessible information, and Holevo information. Connect an identification error requirement to a classical information requirement through the locally stated general Fano inequality.
- **Dependencies and story role:** M08–M10. Connects individual report states to the learner's overall inferential goal.
- **Conceptual connection:** A bound on target information can constrain every final collective measurement without specifying its circuit.
- **Source pointers:** W §3.1.2 and §5.3.3, Theorem 5.49; the general finite-alphabet Fano step supplied in [quantum converse](../science/quantum-converse.md), “Identification and the sample lower bound.”

### M12 — Background: Symmetry distributes response

- **Central question:** How can an average over directions become useful for an unknown target?
- **Understanding target:** Explain why one-copy and two-copy averages simplify under unitary conjugation. Use the identity and the swap to describe the second moment of a Haar-random rank-$`k`$ projector. Recognize the pure-state second moment as the $`k=1`$ case. Distinguish a Haar average from the public Clifford orientation used in the encoder.
- **Dependencies and story role:** M03–M05 and M09–M11. Joins the operator basis to the symmetry tools used by both quantum arguments.
- **Conceptual connection:** Public orientation spreads a retained signal across unknown Pauli targets. The projector moment constrains how much response can survive reference-secure privacy.
- **Source pointers:** W §7.1.1 and §7.2.1, Lemma 7.24. See [quantum reports](../science/quantum-reports.md), Section 4, for the Clifford average and [reference-secure privacy](../science/reference-secure-privacy.md) for the rank projector moment.

### M13 — Background: Specimens, confidence, and physical costs

- **Central question:** What exactly is being made cheaper, and which performance promise is being compared?
- **Understanding target:** Distinguish specimen count from gate count, setup, communication, and coherent storage. Separate worst-target identification, prior-average information bounds, and expected clean-test prediction; interpret a deterministic sample cap and a fixed positive privacy parameter.
- **Dependencies and story role:** M01–M12. Adds the operational and limiting conventions needed to compare complete protocols.
- **Conceptual connection:** A statistically optimal measurement can exist even when its construction is computationally expensive.
- **Source pointers:** W §3.1.2 for ensemble inference foundations; project-specific conventions in [model](../science/model.md), “The two reporting models” and “Identification and supervised prediction,” and [implementation](../science/implementation.md), “Resources and setup.”

### M14 — Background: The complete same-source experiment

- **Central question:** Which promises must stay fixed for the classical and quantum learning costs to be comparable?
- **Understanding target:** Assemble the native source, training reports, feedback, learner memory and clean test. Distinguish the protected reference of dimension $`k`$ in the privacy definition from the retained learner memory in the inference problem. Explain the role of fresh randomness at each owner and the independent raw specimens.
- **Dependencies and story role:** M01–M13. Integrates the background into the full problem rather than adding another isolated prerequisite.
- **Conceptual connection:** The comparison concerns private classical versus private quantum reports from the same physical specimens; it does not replace classical examples by more informative quantum examples.
- **Source pointers:** W §§2.1–2.3 for the experiment's quantum registers and operations. See the [model](../science/model.md), [reference-secure model](../science/reference-secure-privacy.md), and [implementation](../science/implementation.md).

## Narrative and innovation

### M15 — Narrative: A private classical effect cannot cover every direction

- **Central question:** What local restriction does privacy impose on an unknown-Pauli learner?
- **Understanding target:** Connect the effect eigenvalue ratio to a bounded Pauli coefficient and the summed squared-response bound. Explain why a measurement tailored to one known Pauli can be useful while no private effect has a large response in all possible directions.
- **Dependencies and story role:** M04, M07, and M14. Starts the classical proof at the level of one actual report.
- **Conceptual connection:** A spectral privacy restriction becomes an operator-basis information budget without restricting the report alphabet or computation.
- **Source pointers:** W §1.1.2 and §2.3.1; [classical reports](../science/classical-reports.md), Lemma 1.

### M16 — Narrative: The common-null argument defeats classical adaptation

- **Central question:** Why does choosing each measurement after seeing earlier reports fail to remove the lower bound?
- **Understanding target:** Follow the signed likelihood identity, cancellation of the two Pauli signs in reverse relative entropy, and the chain rule under the common maximally mixed reference transcript. Explain how successful identification creates many events with constant divergence cost.
- **Dependencies and story role:** M08 and M15. Builds a local report budget into a global adaptive identification converse.
- **Conceptual connection:** The direction of the divergence controls which history distribution appears, allowing one budget to cover every adaptive classical branch.
- **Source pointers:** W §§5.1.1–5.1.2 and §5.2.3 for divergence foundations; [classical reports](../science/classical-reports.md), Lemma 2 and Theorem 3.

### M17 — Narrative: Prediction alone already requires the classical budget

- **Central question:** Could a private classical learner predict useful labels without learning the hidden Pauli?
- **Understanding target:** Express clean-test success through the learned observable's Pauli coefficient. Explain how constant expected advantage produces a bounded-size signed Pauli list and why the same reference-transcript argument charges that weaker task order $`d^2`$ specimens.
- **Dependencies and story role:** M02, M04, and M16. Transfers the converse to the supervised task without assuming prediction equals exact identification.
- **Conceptual connection:** A classifier's useful correlations provide a short list, which is enough for a lower bound even when it does not determine one target.
- **Source pointers:** W §2.3.1 and §3.1.2; the local reduction in [classical reports](../science/classical-reports.md), Theorem 4.

### M18 — Narrative: The noisy tournament matches the classical order

- **Central question:** How can a classical learner attain the lower-bound dimension dependence without paying an extra logarithmic factor?
- **Understanding target:** Explain the private randomized-response arm, its positive, negative, or zero mean, and the knockout allocation of confidence. Understand why only the true arm's path needs protection and why the shrinking number of arms offsets increasing samples per match.
- **Dependencies and story role:** M03, M13, and M15–M17. Closes the classical branch with a matching constructive frontier.
- **Conceptual connection:** A directional privacy budget can be spent adaptively on candidate comparisons, giving $`\Theta_\varepsilon(d^2)`$ specimen order.
- **Source pointers:** W §2.3.1 for the measurement description; the randomized-response mechanism, concentration argument, and cost sum supplied in [classical reports](../science/classical-reports.md), Theorem 5 and “The resulting classical frontier.”

### M19 — Narrative: A public flag and retained reference both count

- **Central question:** How can a quantum report remain private when the observer sees a public flag and holds a reference?
- **Understanding target:** Compare two joint inputs with the same reference marginal. Show how a spectral sandwich around the replacement output implies privacy block by block. Explain how a maximally entangled input exposes the missing support of a short Kraus list.
- **Dependencies and story role:** M05–M07, M09, M12, and M14. Sets the stronger guarantee for the quantum-report construction.
- **Conceptual connection:** Ordinary outputs test product directions in the Choi matrix. Protecting a larger reference also tests entangled directions.
- **Source pointers:** W §§2.1.3 and 2.2.2 for purifications and Choi representations. See [reference-secure privacy](../science/reference-secure-privacy.md) and the [one-qubit experiment](WATROUS_BRIDGE.md#a-complete-one-qubit-experiment).

### M20 — Narrative: A fixed rank-restricted randomizer can retain Pauli signal

- **Central question:** How many hidden unitary branches are enough to protect a reference of dimension $`k`$?
- **Understanding target:** Connect the Choi quadratic form on reshaped matrices of rank at most $`k`$ to the output sandwich for inputs of Schmidt rank at most $`k`$. Explain why a constant-radius net leads to an $`O(dk)`$ list and how mixing with exact replacement adjusts the privacy parameter.
- **Dependencies and story role:** M04–M05, M12–M13, and M19. Builds a report that is uniformly private after the setup list is fixed.
- **Conceptual connection:** The same list must certify protection in every allowed direction and stay short enough to retain response energy.
- **Source pointers:** W §§2.2.2 and 7.1.1 for channel and invariant-measure foundations. See [reference-secure privacy](../science/reference-secure-privacy.md) and [quantum reports](../science/quantum-reports.md), Section 3.

### M21 — Narrative: Public Clifford orientation spreads signal across target pairs

- **Central question:** How does an average signal bound become a worst-target learning guarantee?
- **Understanding target:** Explain how a short list retains total signal energy and how uniform Pauli orientation spreads it across target pairs. Check why averaging over Pauli signs cancels cross terms for distinct unsigned Paulis. Treat opposite-sign targets separately.
- **Dependencies and story role:** M12 and M19–M20. Turns the local average signal into uniform pairwise distinguishability.
- **Conceptual connection:** Public randomization can make a signal useful without supplying the private branch index that would undo privacy.
- **Source pointers:** W §7.2.1 for uniform averaging; the Clifford-specific argument supplied in [quantum reports](../science/quantum-reports.md), Section 4, Eqs. (7)–(9), and its application to the rank-restricted list in [reference-secure privacy](../science/reference-secure-privacy.md).

### M22 — Narrative: Flat output spectra strengthen a small signal

- **Central question:** Why does Hilbert–Schmidt separation suffice here to obtain a useful fidelity gap?
- **Understanding target:** Connect the bounded output eigenvalues to the Bures/root-fidelity inequality, including its factor of dimension. Average the conditional gaps over the released classical blocks and then use tensor-product multiplicativity.
- **Dependencies and story role:** M09 and M19–M21. Converts the retained response energy into repeated evidence suitable for a decoder.
- **Conceptual connection:** The same spectral flattening that establishes privacy also provides the scale needed to read the weak signal statistically.
- **Source pointers:** W Definition 3.11 and Theorem 3.22; the local bounded-spectrum inequality and its application in [quantum reports](../science/quantum-reports.md), Section 5, Eqs. (10)–(12).

### M23 — Narrative: Collective discrimination learns every signed Pauli

- **Central question:** How do pairwise fidelity gaps lead to bounded error for every target?
- **Understanding target:** Interpret the pretty-good measurement on the known privatized family and the ordered-pair fidelity error sum. Explain how predetermined randomized response replaces the quantum construction when reference protection calls for a long randomizer list.
- **Dependencies and story role:** M11, M13, M18, and M22. Completes the identification upper bound with a quantum decoder and a classical fallback.
- **Conceptual connection:** Independent weak quantum reports can be held together until one joint measurement distinguishes a growing family of targets.
- **Source pointers:** W §3.1.2 and §3.2.2 for discrimination and fidelity foundations; the imported mixed-state PGM bound in [quantum reports](../science/quantum-reports.md), Section 6, and both construction regimes in [reference-secure privacy](../science/reference-secure-privacy.md).

### M24 — Narrative: Reference protection limits one quantum report's information

- **Central question:** How does access to a larger reference tighten the privacy-imposed learning converse?
- **Understanding target:** Whiten the report on the support of the maximally mixed input's output. Compress the joint test state to a Haar-random $`k`$-dimensional subspace and use the second moment to bound target-averaged forward and reverse divergences by order $`\varepsilon^2/(dk)`$ for $`0\lt\varepsilon\le1`$.
- **Dependencies and story role:** M04, M07, M10–M12, and M19. Establishes a per-report budget for arbitrary released dimensions.
- **Conceptual connection:** A single larger-reference privacy test constrains more of the Pauli response.
- **Source pointers:** W §§5.2.1, 5.2.3, and 7.2.1. See [reference-secure privacy](../science/reference-secure-privacy.md) for the compression identity and relative-entropy bounds.

### M25 — Narrative: Predetermined encoders turn the report budget into an identification bound

- **Central question:** Why do predetermined local encoders need order $`dk\log d`$ specimens at fixed privacy?
- **Understanding target:** Use a product of single-report null states as the common comparison. Apply additivity under public conditioning and combine the resulting Holevo bound with Fano's inequality over the signed target set.
- **Dependencies and story role:** M08, M11, M13, and M24. Converts the one-report divergence into a lower bound for every collective decoder.
- **Conceptual connection:** Fixed encoders permit the same target prior at each step of the comparison. In a feedback protocol, the next encoder can depend on earlier outcomes.
- **Source pointers:** W §§5.2.3 and 5.3.3, Theorems 5.35 and 5.49. See [reference-secure privacy](../science/reference-secure-privacy.md) and the $`k=1`$ argument in [quantum converse](../science/quantum-converse.md).

### M26 — Narrative: One joint prediction test can identify a signed target

- **Central question:** How can an identification converse constrain a learner that only predicts one clean test label?
- **Understanding target:** Expand the final binary observable on memory and the clean system in the test Pauli basis. Use the operator-valued Parseval identity and squared positive parts to construct a valid identification POVM on the trained memory. Relate a fixed prediction advantage to fixed signed-target identification success.
- **Dependencies and story role:** M02–M04, M14, M17, and M25. Gives a joint-test reduction that uses one copy of the learner's memory.
- **Conceptual connection:** The binary test distributes its response among signed target effects. The bound holds even when the trained memory is consumed.
- **Source pointers:** W §§1.1.2, 2.3.1, and 3.1.2 for operator coefficients, POVMs, and discrimination. See [reference-secure privacy](../science/reference-secure-privacy.md) for the reduction.

### M27 — Narrative: Finite compilation must preserve a privacy margin

- **Central question:** How can an ideal private mixed-unitary channel become a finite physical protocol without losing pure privacy?
- **Understanding target:** Use the ordinary-privacy example to connect a strict spectral margin, a channel approximation bound and a synthesis accuracy of order $`1/d`$. For reference protection, identify the joint input directions on which a compiled encoder must preserve the margin. Distinguish an encoder error from an error in the later decoder.
- **Dependencies and story role:** M05, M07, M13, and M19–M23. Connects the statistical construction to finite operations.
- **Conceptual connection:** A small absolute channel error can matter to multiplicative privacy when output eigenvalues scale as $`1/d`$; strict slack permits a controlled conversion.
- **Source pointers:** W §1.1.3 and §§2.2.1–2.2.2 for operator-norm and channel foundations; the explicit channel-error and margin inequalities in [implementation](../science/implementation.md), “Compilation with a strict privacy margin.”

### M28 — Narrative: Cheap local branches do not make the learner efficient

- **Central question:** Which resources improve in the ordinary-privacy Pauli-list variant, and which remain expensive?
- **Understanding target:** Explain classical storage of a good Pauli list, fresh private sampling, public Clifford descriptions, direct Pauli conjugation, and clean local deployment. Account separately for setup selection and certification, output communication, coherent training storage, and collective-decoder construction.
- **Dependencies and story role:** M03, M05, M13, M23, and M27. Integrates the implementation costs into the scope of the sample advantage.
- **Conceptual connection:** Exact local Pauli gates and ordinary classical lookup avoid a free QRAM assumption, while the extra polylogarithmic specimens and expensive global steps remain charged.
- **Source pointers:** W §§2.1–2.3 for registers, channels, and measurements; [implementation](../science/implementation.md), “Exact Pauli gates,” “Source and clean deployment,” and “Resources and setup.”

### M29 — Narrative: Classical feedback and arbitrary quantum memory

- **Central question:** Does the per-report budget still constrain adaptive selection of later encoders?
- **Understanding target:** Follow reverse relative entropy from the common null, where the classical history supplies target-independent weighting. Use the tensor product of the old memory and fresh report conditional on history, then apply data processing through the learner's instrument. Explain why the resulting lower bound is of order $`dk`$ at fixed privacy.
- **Dependencies and story role:** M08, M14, M16, M24–M26. Extends the converse to classical feedback with retained quantum memory.
- **Conceptual connection:** A classical history can control the next encoder while the learner's quantum register remains available for any final joint measurement.
- **Source pointers:** W §5.2.3 for quantum relative entropy and data processing. See [reference-secure privacy](../science/reference-secure-privacy.md) for the adaptive null calculation.

### M30 — Narrative: Where quantum reports save specimens

- **Central question:** How does the reference dimension change the same-source comparison?
- **Understanding target:** State the matching predetermined-encoder order $`\Theta_\varepsilon(dk\log d)`$ for identification and clean prediction. Explain why adaptive classical randomized response attains the $`\Theta_\varepsilon(d^2)`$ full-reference optimum at $`k=d`$. State the intermediate-$`k`$ adaptive lower and upper bounds with the allowed feedback and setup assumptions.
- **Dependencies and story role:** M14, M18, M23, and M25–M29. Reassembles the project as one comparison across privacy guarantees.
- **Conceptual connection:** Private channels can preserve entanglement even under full-reference privacy, where adaptive quantum learning and the classical tournament have the same specimen order. Statistical costs and implementation costs are separate.
- **Source pointers:** [Model](../science/model.md), [reference-secure privacy](../science/reference-secure-privacy.md), [implementation](../science/implementation.md), and [related work](../references/related-work.md).
