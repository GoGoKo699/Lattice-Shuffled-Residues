# Scientific overview

Shuffling changes the order of an internal vector while preserving its multiset of values. The scientific question is whether the remaining counts can be combined with indexed information from the same attempt and repeated observations under one secret.

Here the anonymous data are low-part rounding residuals. The indexed data are commitment high bits and a signed sparse challenge. A rounding endpoint produces an exact scalar correlation; challenge symmetry turns that correlation into a linear secret mean. The central proof task is to justify the required moments for one random public matrix that stays fixed throughout the observation sequence.

## The argument

| Step | Question answered | Result |
|---|---|---|
| [1. Model](model.md) | What is observed, and what changes after the first check? | The conditional nonce is exactly uniform on a translated product box. Fresh first attempts supply independent records in the stated random-oracle model. |
| [2. Boundary statistic](boundary_statistic.md) | How can an anonymous count reveal an indexed coefficient? | One extra rounding preimage gives a scalar covariance. Averaging against the challenge yields a known multiple of a coefficient of $`s_2`$. |
| [3. Fixed public matrix](fixed_matrix.md) | Does the calculation survive matrix reuse and conditioning? | Sparse multiplication rank and a collision argument control every required small marginal for the same matrix and every translation. |
| [4. Concentration](concentration.md) | How many records are sufficient? | Exact fourth moments, transfer errors, and Bernstein's inequality give simultaneous integer identification with explicit failure terms. |
| [5. Security scope](security_scope.md) | What follows about public-key simulation? | Full-key completion and public witness validation turn repeated-view simulation into bounded-witness search, with explicit costs and rank exceptions. |
| [6. Replacement marginal](sampler_marginal.md) | Does the source's particular one-view replacement even match a scalar marginal? | Its zero-high probability has an exact deficit. Sampling from the correct conditional preimage fiber repairs this isolated issue. |

## Three distributions to keep distinct

The **genuine fixed-key distribution** samples a public matrix once, fixes bounded secrets, and draws fresh nonces and challenges. It is the distribution to which the identification theorem applies.

The **independent-coordinate comparison distribution** replaces the commitment coordinates by independent uniform field elements for the purpose of computing moments. It is an analytical intermediate. The small-marginal theorem bounds the difference between these moments and the genuine ones without replacing the entire output distribution.

The **source's replacement distribution** is the specific sampler in corrected SUCRE Figure 7 and Definition 11. Its dummy secret and high-bit sampling rule are the subject of the separate marginal calculation. The main statistical theorem does not depend on this sampler.

## Main quantitative statement

Use the notation of the model and let

```math
\theta=\frac{p_z\tau}{2q},
\qquad R=\tau D\beta.
```

There is an observable record statistic $`Q_{b,j}`$ with $`|Q_{b,j}|\le R`$. On the same good-matrix event for every bounded pair of secrets,

```math
\left|\mathbb E Q_{b,j}+\theta(s_{2,b})_j\right|
\le p_z\tau D\beta\varepsilon.
```

The concentration chapter gives an explicit uniform second-moment bound $`V`$. If

```math
D\beta\varepsilon\le\frac1{16q},
\qquad
t_*=\frac{\theta}{4},
\qquad
N\ge
\frac{2V+(4/3)Rt_*}{t_*^2}
\ln\frac{2D}{\delta},
```

then the estimates

```math
\widehat s_{b,j}
=-\frac1{\theta N}\sum_{a=1}^N Q^{(a)}_{b,j}
```

are simultaneously within $`3/8`$ of their integer targets except with probability at most $`\delta+\zeta_4(\varepsilon)`$. The failure probability includes the one-time draw of the matrix. The same good matrix works for all bounded secrets and all challenge-dependent translations; the theorem does not assume simultaneous control of arbitrary base boxes chosen after seeing the matrix.

For a full verification key and an injective matrix, the recovered $`s_2`$ determines $`s_1`$ by linear algebra. The relevant simulation obstruction concerns any public-key-only simulator for the **joint collection** of repeated views, including stateful simulators that correlate their outputs. It is conditional on a precisely stated bounded-witness hardness assumption at the total resource budget.

## Rejection and centering

The selected residual values lie in the rejected boundary band. A positive selected count therefore forces low-part rejection. An accepted first-check-passing attempt has weighted count $`F=0`$, so its centered contribution is $`F-D\mu=-D\mu`$. Such records remain in the statistic. Only first-check failures contribute zero by definition.

This distinction prevents a change of sampling law from being hidden inside the calculation. The analysis records first attempts and does not condition on eventual rejection.

## Interpretation and limits

The theorem demonstrates persistent correlation in a defined enlarged leakage view. The quantitative sufficient counts are very large. Physical acquisition, trace noise, partial observation, and a standard compressed verification key require additional arguments. The [security chapter](security_scope.md) accounts for signer cost, statistical processing, exact arithmetic, storage, and the rank exception; it also separates a missing proof hypothesis from a false hardness premise.

The [related-work account](../references/RELATED_WORK.md) credits prior shuffled-information inference and explains the remaining comparison limits. The [verification guide](../verification/README.md) connects each finite calculation to the analytical claim it checks.
