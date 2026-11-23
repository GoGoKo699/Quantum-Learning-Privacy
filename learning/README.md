# Learn private quantum learning

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**. The [source-to-project bridge](WATROUS_BRIDGE.md) identifies selective textbook locations, translates notation, and develops one complete qubit experiment before connecting the foundations to the proofs.

The same labeled quantum specimen can be released as a private classical report or a private quantum report. How much training data does each learner need, and how does that answer change when privacy must also protect correlations with a reference? The result tracks both reference size and the timing of reporting decisions.

| Reading goal | Route |
|---|---|
| Understand what is supplied and protected | [Scientific model](../science/model.md), then the [qubit experiment](WATROUS_BRIDGE.md#a-complete-one-qubit-experiment) |
| Translate the selected book into project notation | [Reading map and convention dictionary](WATROUS_BRIDGE.md#selective-reading-map) |
| Follow the complete conceptual dependencies | [30 milestones](MILESTONES.md) with 14 background milestones and 16 narrative milestones |
| Understand why the released register matters | [Privacy registers](../science/privacy-registers.md) |
| Read the ordinary-privacy proof | [Classical reports](../science/classical-reports.md), [quantum reports](../science/quantum-reports.md), and [quantum converse](../science/quantum-converse.md) |
| Follow the reference-size and feedback results | [Reference-secure learning](../science/reference-secure-learning.md) |
| Assess the resource meaning and limits | [Interpretation](../science/interpretation.md) and [implementation](../science/implementation.md) |

The bridge connects Watrous's foundations to imported research ingredients such as approximate randomization and quantitative state discrimination, and to the private-response and learning arguments proved in this project.

At fixed positive privacy and fixed identification error, the product-report specimen costs are $`\Theta_\varepsilon(dr\log d)`$ for quantum reports with reference dimension at most $`r`$ and $`\Theta_\varepsilon(d^2\log d)`$ for classical reports. With unrestricted reference privacy and classical feedback, identification and clean-test prediction at fixed advantage both cost $`\Theta_\varepsilon(d^2)`$. The learner may retain report quantum memory and use it to produce classical feedback. Clean prediction uses a fresh unprivatized test specimen.

