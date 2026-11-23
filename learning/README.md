# Learn private quantum learning

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**. The [source-to-project bridge](WATROUS_BRIDGE.md) selects textbook sections and works through a one-qubit example where a reference changes the privacy budget.

Each owner sends one private report from a labeled quantum specimen. The learning question is how much useful information that report can retain while protecting input correlations with a reference of dimension $`k`$. The reference belongs to the privacy test. The learner's retained quantum memory is a separate register and has no dimension bound in the converse.

| Reading goal | Route |
|---|---|
| Identify the source and protected registers | [Scientific model](../science/model.md), then the [one-qubit example](WATROUS_BRIDGE.md#a-complete-one-qubit-experiment) |
| Find the quantum information foundations | [Watrous reading map](WATROUS_BRIDGE.md#selective-reading-map) |
| Follow the proof dependencies | [30 milestones](MILESTONES.md), with 14 background and 16 narrative milestones |
| See how classical reports learn the target | [Classical reports](../science/classical-reports.md) |
| See how reference protection changes quantum reports | [Reference-secure privacy](../science/reference-secure-privacy.md), building on [quantum reports](../science/quantum-reports.md) |
| Track the physical costs | [Interpretation](../science/interpretation.md) and [implementation](../science/implementation.md) |

Training and deployment use the same signed-Pauli source. Training owners release independently privatized specimens with public labels. Prediction uses one fresh clean test specimen. Predetermined local encoders need $`\Theta_\varepsilon(dk\log d)`$ specimens for either task at fixed positive privacy and fixed performance. When classical feedback can choose later encoders, the lower bound is $`\Omega_\varepsilon(dk)`$. At $`k=d`$ the classical tournament attains that order.
