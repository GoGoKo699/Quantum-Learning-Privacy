# Which register is private?

Privacy is a property of the register a recipient receives. Two procedures can produce the same averaged density operator while releasing different amounts of classical information. This distinction is essential when a local experiment records its measurement setting and outcome.

## A quantum shadow state and its classical description

Consider the following one-specimen experiment in dimension $`d`$. Choose a Clifford $`U`$, apply it to the input, apply depolarizing noise with surviving signal $`s\in[0,1]`$, and measure the computational basis. Write the outcome as $`b`$.

If the recipient receives the classical pair $`(U,b)`$, its POVM effect is

```math
E_{U,b}=\frac1{|\mathcal C|}
\left[sU^\dagger|b\rangle\langle b|U+\frac{1-s}{d}I\right].
```

Choose $`\rho=U^\dagger|b\rangle\langle b|U`$ and an orthogonal pure state $`\sigma`$. The probability ratio for this one report event is

```math
\frac{\Pr_\rho[(U,b)]}{\Pr_\sigma[(U,b)]}
=\frac{s+(1-s)/d}{(1-s)/d}
=1+\frac{ds}{1-s}.
```

These are the maximum and minimum eigenvalues of the effect, so the complete classical report is $`\varepsilon`$-QLDP exactly when

```math
s\le\frac{e^\varepsilon-1}{d+e^\varepsilon-1}.
```

At $`s=1`$, one input gives positive probability to the event and the other gives zero; no finite privacy parameter protects that classical record.

Instead, suppose the sender prepares the quantum state $`U^\dagger|b\rangle\langle b|U`$ and releases only that system, discarding its classical description. The averaged channel is

```math
\mathcal M_s(\rho)
=\frac{s}{d+1}\rho+
\left(1-\frac{s}{d+1}\right)\frac Id.
```

For this quantum-state release, the optimal privacy parameter is

```math
\varepsilon_{\mathrm{state}}
=\log\left(1+\frac{ds}{d+1-s}\right).
```

In particular $`s=1`$ gives $`\varepsilon_{\mathrm{state}}=\log2`$. The quantum system does not provide its exact preparation description. A recipient cannot reconstruct that richer classical pair from one copy of the released state.

## A finite likelihood check

At $`d=4`$ and $`\varepsilon=\log(3/2)`$, the choice $`s=5/9`$ makes the averaged quantum-state channel $`\varepsilon`$-QLDP. The classical pair, however, has likelihood ratio

```math
1+\frac{4(5/9)}{1-5/9}=6,
```

whereas the permitted ratio is $`3/2`$. Protecting that actual classical pair requires $`s\le1/9`$. This is an exact calculation, rather than a numerical privacy certificate.

## How the learning construction treats flags

The [coherent report](quantum-reports.md) explicitly releases a Clifford flag $`C`$ and a randomized quantum system. Its privacy proof holds separately in every $`C`$ block, including arbitrary output measurements. The privately chosen Kraus index is discarded; disclosing it would release a reversible unitary branch and invalidate the argument.

The [reference-secure construction](reference-secure-learning.md) keeps the same flag contract and proves joint order on every Clifford block for the specified reference dimension.

The [classical converse](classical-reports.md) includes every setting or snapshot descriptor available to its learner. It therefore applies to the private classical record itself. A known observable can still be estimated efficiently by choosing a private measurement tailored to that observable; the learning problem must discover which one of many observables is relevant.

The averaged channel above appears in the private-shadow analysis of [Nuradha, Bhalerao, and Leditzky, arXiv:2602.10510v1, equation (23), Proposition 11 and Appendix I](https://arxiv.org/abs/2602.10510v1). Its quantum-state privacy guarantee must be distinguished from the privacy of a released classical snapshot description. This register comparison supplies the relevant boundary here; it makes no general claim about the other results in that work.
