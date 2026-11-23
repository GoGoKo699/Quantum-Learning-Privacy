# Thirty understanding milestones

The selected educational anchor is John Watrous, [*The Theory of Quantum Information* (2018)](https://cs.uwaterloo.ca/~watrous/TQI/), abbreviated **W** below. The [Watrous bridge](WATROUS_BRIDGE.md) translates its notation and identifies the additional project-specific arguments. W uses base-two logarithms; the scientific chapters use natural logarithms. Its fidelity convention is the root fidelity used here.

The map has **14 background/preliminaries milestones and 16 narrative/innovation milestones**. The background phase connects one physical specimen, its measurement and release, and the information measures needed to formulate the full experiment. The narrative phase joins the classical converse and tournament, the coherent construction, and the effects of protecting references and allowing feedback. This allocation gives both proof branches their prerequisites without turning the map into the textbook's table of contents.

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

- **Central question:** What does it mean to protect one quantum input, including its correlations with a reference?
- **Understanding target:** Interpret $`\Lambda(\rho)\preceq e^\varepsilon\Lambda(\sigma)`$ for every pair of ordinary input states, including states outside the learning promise. Extend the test to joint inputs with the same reference marginal and include every released flag in the order comparison.
- **Dependencies and story role:** M02 and M05–M06. Turns the released-register description into the shared reporting constraint.
- **Conceptual connection:** For classical reports, privacy becomes an eigenvalue-ratio restriction on each POVM effect. This will also bound the reference state in each released outcome block.
- **Source pointers:** W §1.1 for positive operators, §§2.1.3 and 2.2.1 for registers and channels, and §2.3.1 for measurements. See the definitions in [reference-secure learning](../science/reference-secure-learning.md) and the one-qubit example in the [bridge](WATROUS_BRIDGE.md#what-changes-when-a-reference-is-retained).

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
- **Understanding target:** Explain the purpose of uniform unitary and pure-state averages, the second moment $`\mathbb E\psi^{\otimes2}=(I+F)/[d(d+1)]`$, and Clifford conjugation of Pauli labels. Distinguish an average response from a guarantee for every target.
- **Dependencies and story role:** M03–M05 and M09–M11. Joins the operator basis to the symmetry tools used by both quantum arguments.
- **Conceptual connection:** The upper bound uses public orientation to spread a retained signal, while the converse uses a pure-state second moment to budget information.
- **Source pointers:** W §7.1.1 and §7.2.1, Lemma 7.24; local Clifford sign argument in [quantum reports](../science/quantum-reports.md), Section 4, and moment normalization in [quantum converse](../science/quantum-converse.md), Eq. (Q5).

### M13 — Background: Specimens, confidence, and physical costs

- **Central question:** What exactly is being made cheaper, and which performance promise is being compared?
- **Understanding target:** Distinguish specimen count from gate count, setup, communication, and coherent storage. Separate worst-target identification, prior-average information bounds, and expected clean-test prediction; interpret a deterministic sample cap and a fixed positive privacy parameter.
- **Dependencies and story role:** M01–M12. Adds the operational and limiting conventions needed to compare complete protocols.
- **Conceptual connection:** A statistically optimal measurement can exist even when its construction is computationally expensive.
- **Source pointers:** W §3.1.2 for ensemble inference foundations; project-specific conventions in [model](../science/model.md), “The two reporting models” and “Identification and supervised prediction,” and [implementation](../science/implementation.md), “Resources and setup.”

### M14 — Background: The complete same-source experiment

- **Central question:** Which promises must stay fixed for the classical and quantum learning costs to be comparable?
- **Understanding target:** Assemble the labeled source, reference-bound privacy test, complete released registers, retained learner memory, and clean future test. Distinguish a preset product schedule from channel choices made through classical feedback. Explain the role of public labels, independent raw records, and fresh local randomness.
- **Dependencies and story role:** M01–M13. Integrates the background into the full problem rather than adding another isolated prerequisite.
- **Conceptual connection:** Both learners receive specimens from the same physical source. The reference is part of the privacy test, and channel selection and storage belong to the learning protocol.
- **Source pointers:** W §§2.1–2.3 for the state-channel-measurement framework. See [model](../science/model.md) and [reference-secure learning](../science/reference-secure-learning.md) for the source, privacy, and feedback interfaces.

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

### M19 — Narrative: A quantum report is private in every public block

- **Central question:** How can a channel conceal every individual input while leaving its quantum output available for learning?
- **Understanding target:** Use the operator-randomization band to establish ordinary input-state privacy of the quantum system conditional on each released Clifford flag. Distinguish the public orientation from the independently sampled private Kraus index, which is discarded.
- **Dependencies and story role:** M05–M07, M12, and M14. Starts the coherent branch with an actual private release rather than a hypothetical signal.
- **Conceptual connection:** Blockwise order proves privacy of the complete recipient view while permitting later joint processing of independent reports.
- **Source pointers:** W §§2.1.1, 2.2.1–2.2.2; [quantum reports](../science/quantum-reports.md), Sections 1–2; [privacy registers](../science/privacy-registers.md), “How the learning construction treats flags.”

### M20 — Narrative: A short Kraus list must retain signal energy

- **Central question:** What prevents an approximate randomizer with few unitary branches from erasing every Pauli response?
- **Understanding target:** Relate the superoperator Hilbert–Schmidt norm to the pairwise trace overlaps of its unitary branches. Explain how the nonnegative diagonal contributions, removal of the identity direction, and $`K\le d^2/2`$ give an average surviving energy of order $`1/K`$.
- **Dependencies and story role:** M04–M05 and M19. Extracts the quantitative local signal left inside the private quantum output.
- **Conceptual connection:** Privacy flattens each output spectrum, while a short channel description limits how completely all operator directions can be suppressed.
- **Source pointers:** W §§1.1.2–1.1.3 and §2.2.2; the task-specific trace identity in [quantum reports](../science/quantum-reports.md), Section 3, Eqs. (5)–(6).

### M21 — Narrative: Public Clifford orientation protects every target pair

- **Central question:** How does an average signal bound become a worst-target learning guarantee?
- **Understanding target:** Explain uniform Pauli orientation and the independent sign averaging that cancels cross terms for distinct unsigned Paulis. Treat opposite-sign targets separately and see why the same pair-separation bound covers both commuting and anticommuting targets.
- **Dependencies and story role:** M12 and M19–M20. Turns the local average signal into uniform pairwise distinguishability.
- **Conceptual connection:** Public randomization can make a signal useful without supplying the private branch index that would undo privacy.
- **Source pointers:** W §7.2.1 for uniform averaging; the Clifford-specific argument supplied in [quantum reports](../science/quantum-reports.md), Section 4, Eqs. (7)–(9).

### M22 — Narrative: Flat output spectra strengthen a small signal

- **Central question:** Why does Hilbert–Schmidt separation suffice here to obtain a useful fidelity gap?
- **Understanding target:** Connect the bounded output eigenvalues to the Bures/root-fidelity inequality, including its factor of dimension. Average the conditional gaps over the released classical blocks and then use tensor-product multiplicativity.
- **Dependencies and story role:** M09 and M19–M21. Converts the retained response energy into repeated evidence suitable for a decoder.
- **Conceptual connection:** The same spectral flattening that establishes privacy also provides the scale needed to read the weak signal statistically.
- **Source pointers:** W Definition 3.11 and Theorem 3.22; the local bounded-spectrum inequality and its application in [quantum reports](../science/quantum-reports.md), Section 5, Eqs. (10)–(12).

### M23 — Narrative: Collective discrimination learns every signed Pauli

- **Central question:** How do pairwise fidelity gaps lead to bounded error for every target?
- **Understanding target:** Interpret the pretty-good measurement on the known privatized family, the ordered-pair fidelity error sum, and its worst-target guarantee. Explain why the public flag sequence remains classical and why the resulting copy bound is a statistical decoder statement.
- **Dependencies and story role:** M11, M13, and M22. Closes the coherent upper-bound branch with a finite identification protocol.
- **Conceptual connection:** Independent weak quantum reports can be held together until one joint measurement distinguishes a growing family of targets.
- **Source pointers:** W §3.1.2 and §3.2.2 for discrimination and fidelity foundations; the imported mixed-state PGM bound and local sample calculation in [quantum reports](../science/quantum-reports.md), Section 6.

### M24 — Narrative: Privacy also limits one quantum report's information

- **Central question:** Could a different private quantum channel hide a much larger target signal per specimen?
- **Understanding target:** Follow whitening on the reference support, the pure-state second moment, and the quadratic-to-relative-entropy step. Explain why all-input privacy bounds the signed target ensemble's Holevo information by order $`1/d`$, independently of report dimension.
- **Dependencies and story role:** M04, M07, M10–M12, and M19. Begins the converse branch for arbitrary noninteractive private quantum encoders.
- **Conceptual connection:** The Pauli second moment gives a channel information budget distinct from the classical effect budget.
- **Source pointers:** W §§5.2.1, 5.2.3, and 7.2.1, Lemma 7.24; the noncommutative derivation in [quantum converse](../science/quantum-converse.md), Eqs. (Q3)–(Q9).

### M25 — Narrative: A product reference gives the coherent identification converse

- **Central question:** Why do arbitrary collective decoding and large report spaces still require order $`d\log d`$ product-encoded specimens under ordinary privacy?
- **Understanding target:** Distinguish the correlated target-ensemble mean from the product of single-report reference states. Apply relative-entropy decomposition, tensor-product additivity, Holevo's bound, and general Fano's inequality under the stated public conditioning.
- **Dependencies and story role:** M08, M11, M13, and M24. Builds the one-report quantum budget into the global noninteractive converse.
- **Conceptual connection:** A uniform prior is legitimate after conditioning on independent public coins, but the proof does not authorize replacing a posterior after adaptive encoder feedback by that prior.
- **Source pointers:** W §5.2.3 and §5.3.3, Theorems 5.35 and 5.49; [quantum converse](../science/quantum-converse.md), Eqs. (Q10)–(Q11), Theorem Q, and the local Fano derivation.

### M26 — Narrative: A reference probe tightens the information budget

- **Central question:** Why does protecting a larger reference reduce the average Pauli information in one report?
- **Understanding target:** Compare a maximally entangled probe in a random $`r`$-dimensional input subspace with an independent input having the same reference marginal. Follow the weighted quadratic bound and see why Clifford averaging turns it into the per-specimen budget of order $`1/(dr-1)`$.
- **Dependencies and story role:** M07, M10–M12, and M24–M25. Reuses the product-information proof with the stronger one-report budget.
- **Conceptual connection:** Privacy constrains a joint channel response even though the learning source supplies the same independent labeled specimens.
- **Source pointers:** W §§2.1.3, 2.2.2, and 7.2.1 for references, channels, and unitary averaging. See the [weighted probe identity](../science/reference-secure-learning.md#a-compressed-choi-identity) and the [product converse](../science/reference-secure-learning.md#product-identification-converse).

### M27 — Narrative: A short list retains a signal under reference privacy

- **Central question:** How can a quantum report meet the stronger privacy condition and still identify every signed Pauli?
- **Understanding target:** Explain how a list of order $`dr`$ Haar unitaries gives a multiplicative order bound on all supported reference probes. Use filtering on the reference and mixing to pass to general joint inputs. Connect the list-size bound to the retained Clifford-averaged response and collective decoder.
- **Dependencies and story role:** M05, M07, M12, M19–M23, and M26. Matches the stronger lower bound with an explicit reporting and decoding mechanism given a suitable list.
- **Conceptual connection:** The dimension of the reference enters the randomizer size and hence the sample budget. Compilation requires a privacy margin at the level of the tested joint outputs.
- **Source pointers:** W §§2.2.2 and 7.2.1 for channels and symmetry. See the [bounded-reference randomizer](../science/reference-secure-learning.md#a-short-randomizer-with-a-bounded-reference) and [matching constructions](../science/reference-secure-learning.md#matching-constructions) for the list, decoder, and fallback, and [implementation](../science/implementation.md) for the original ordinary-privacy compilation analysis.

### M28 — Narrative: The matched product comparison prices the fixed schedule

- **Central question:** What does the classical comparison become when both encoders must choose their channels in advance?
- **Understanding target:** Use effect eigenvalue bounds to lift ordinary pure privacy of each classical report to an arbitrary reference. Compare a balanced schedule of private Pauli queries with the per-report information and Fano lower bound. Read $`\Theta_\varepsilon(d^2\log d)`$ versus $`\Theta_\varepsilon(dr\log d)`$ as identification rates under the same product schedule constraint.
- **Dependencies and story role:** M04, M07, M11, M15, M18, and M26–M27. Separates the effect of reference size from the effect of feedback.
- **Conceptual connection:** Ordinary classical privacy already enforces the stronger reference guarantee. The product advantage has order $`d/r`$.
- **Source pointers:** W §§2.3.1 and 5.3.3 for POVMs and information. The lift and matched product bounds are in [reference-secure learning](../science/reference-secure-learning.md).

### M29 — Narrative: Classical feedback retains a common null history

- **Central question:** How can a learner reuse quantum memory, and what is the cost when privacy protects every reference?
- **Understanding target:** Split the learner's state into a classical history and retained quantum memory. Use conditional factorization for a new report and data processing after learner instruments. Explain why reverse relative entropy gives the same null history weights for all targets. Apply the resulting bound both to identification and to a clean test, where opposite target signs give null success one-half.
- **Dependencies and story role:** M08, M10, M14, M16–M18, and M26–M28. Extends the lower bound to channel choices made through classical feedback and brings the private tournament back as a matching upper bound.
- **Conceptual connection:** The quantum memory may produce the next classical decision. Its coherent state stays on the learner's side of the reporting interface.
- **Source pointers:** W §2.3.2, Eqs. (2.258)–(2.262), and §5.2.3 for instruments and divergence. See the [feedback converse](../science/reference-secure-learning.md#classical-feedback-with-quantum-report-memory) and the [intermediate-reference regime](../science/reference-secure-learning.md#what-changes-when-the-reference-grows).

### M30 — Narrative: Reference size, feedback, and physical resources

- **Central question:** Which privacy and reporting choices determine the sample advantage?
- **Understanding target:** State the product identification laws and the unrestricted-reference feedback law for identification and fixed clean-test advantage. Explain where the ordinary-privacy result lies, what is open for intermediate references with feedback, and why setup, compilation, communication, storage, and collective decoding incur costs beyond the specimen count.
- **Dependencies and story role:** M13–M14 and M26–M29. Reassembles the experimental assumptions, proof routes, and operational consequences.
- **Conceptual connection:** A population pattern can remain learnable under record-level protection, but the reference guarantee and the allowed reporting decisions control the available sample savings.
- **Source pointers:** W §§2.2.1, 3.1.2, and 5.3.3 for channel and inference foundations. [Reference-secure learning](../science/reference-secure-learning.md), [implementation](../science/implementation.md), and [related work](../references/related-work.md) give the scope, resources, and attribution.
