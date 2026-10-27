# Security consequences and simulation limits

The [boundary statistic](boundary_statistic.md) identifies the coefficients of $`s_2`$ from repeated augmented transcripts. This chapter states the consequences, the computational assumption needed for a simulation obstruction, and the boundary between the full-key and compressed-key conclusions.

The statistical identification theorem, linear completion of the full algebraic key, and computational obstruction to public-key-only simulation are distinct statements. The first two follow from the proved observation law and linear algebra. The simulation conclusion additionally invokes a precisely specified hardness assumption.

## 1. The statistical input

Use the [model](model.md), with

```math
R_q=\mathbb F_q[X]/(X^n+1),\qquad
A\in R_q^{k\times\ell},\qquad
t=As_1+s_2,
```

and $`\|s_1\|_\infty,\|s_2\|_\infty\le\eta`$. Norms concern integer coefficient representatives. Assume $`2\eta<q`$, so these representatives are unique. Put $`D=kn`$ and $`M=\ell n`$.

Let $`\mathcal V_N(A,t;s_1,s_2)`$ be the joint law of $`N`$ independent first-attempt records under one fixed key, with the public information and censoring rule specified in the model. In this chapter, let $`\widehat s_2`$ denote the coefficientwise nearest-integer rounding of the real-valued estimates proved in [concentration](concentration.md). On the finite-marginal event $`\mathcal G_A`$, that result gives

```math
\Pr[\widehat s_2=s_2\mid A,s_1,s_2]\ge1-\delta
```

for the stated observation bound. This guarantee is uniform over all bounded secrets for each good fixed matrix. Writing

```math
\delta_A=\Pr_A[A\notin\mathcal G_A],
```

the unconditional success is at least $`1-\delta-\delta_A`$. The matrix exception is paid once, at key generation, rather than separately at every attempt.

The estimator uses indexed high coefficients, challenges, the first-check outcome, and the allowed residual histogram. It does not use the full public vector $`t`$. That vector is needed for the next implication.

## 2. Full-key identification and matrix rank

Suppose $`k\ge\ell`$ and the map $`A:R_q^\ell\to R_q^k`$ is injective. Over the semisimple ring below it has a left inverse $`L_A`$. Given the correct $`s_2`$ and the full public $`t`$,

```math
s_1=L_A(t-s_2)\pmod q.
```

The bounded centered lift is then the original $`s_1`$. This computation can also be performed on the explicit $`D\times M`$ coefficient matrix over $`\mathbb F_q`$; no transform oracle is needed.

The full-key convention occurs in [SUCRE, Section 2.5 and Figure 3](https://eprint.iacr.org/2026/2248). There the recovered vectors and public data form the algebraic signing key. The legitimate signing computation is consequently available with that key. A signature-security consequence also uses the scheme's stated correctness and signing-time contract, and charges the cost of obtaining the augmented transcripts.

### Proposition 1: injectivity probability

Assume $`q\equiv1\pmod{2n}`$. The polynomial $`X^n+1`$ has $`n`$ distinct roots in $`\mathbb F_q`$, and the Chinese remainder isomorphism gives

```math
R_q\cong\prod_{\nu=1}^{n}\mathbb F_q.
```

For uniform $`A`$, its images $`A_\nu\in\mathbb F_q^{k\times\ell}`$ are independent uniform matrices. Therefore

**(S1)**

```math
\Pr[A\text{ is injective}]
=\left(\prod_{j=0}^{\ell-1}(1-q^{j-k})\right)^n.
```

In particular,

**(S2)**

```math
\delta_{\rm rk}:=\Pr[A\text{ is not injective}]
\le n\sum_{j=0}^{\ell-1}q^{j-k}
<\frac{nq^{\ell-k}}{q-1}.
```

**Proof.** Expose the columns of a uniform field matrix in order. Conditional on $`j`$ independent columns, their span contains $`q^j`$ of the $`q^k`$ possible next columns. This gives the product for one factor. The Chinese remainder map is a bijection, so it sends uniform ring entries to independent uniform factor entries. Injectivity requires full column rank in every factor, proving (S1). A union bound and $`1-\prod_j(1-a_j)\le\sum_j a_j`$ give (S2). $`\square`$

More generally, for a squarefree factorization $`X^n+1=\prod_\nu f_\nu`$ with $`d_\nu=\deg f_\nu`$, replace (S1) by

```math
\prod_\nu\prod_{j=0}^{\ell-1}
\left(1-q^{d_\nu(j-k)}\right).
```

For odd $`q`$ and power-of-two $`n`$, squarefreeness holds because the characteristic does not divide $`n`$. The split case covers the parameter sets here. If $`k<\ell`$, this injectivity argument is unavailable, while the separate $`s_2`$ identification theorem still applies.

At $`q=8380417`$ and $`n=256`$, (S2) gives:

| Parameter shape | $`(k,\ell)`$ | Upper bound on $`\delta_{\rm rk}`$ |
|---|---:|---:|
| 44 | $`(4,4)`$ | $`3.05475\times10^{-5}`$ |
| 65 | $`(6,5)`$ | $`3.64510\times10^{-12}`$ |
| 87 | $`(8,7)`$ | $`3.64510\times10^{-12}`$ |

These are small concrete failure probabilities. They need not be negligible in every asymptotic family: $`n/(q-1)`$ can be inverse polynomial when $`q`$ is polynomially bounded.

### Corollary 2: full-key identification

Under the statistical theorem and the full-key convention,

**(S3)**

```math
\Pr[(\widehat s_1,\widehat s_2)=(s_1,s_2)]
\ge1-\delta-\delta_A-\delta_{\rm rk}.
```

No independence between the matrix events is required. If the actual joint key-and-view law is within total variation $`\xi_N`$ of the ideal law, subtract $`\xi_N`$ as well. That approximation must cover the repeated joint experiment; an unspecified approximation for one sample is insufficient.

## 3. A publicly verifiable search problem

An indistinguishability test must operate without the original secret. Define

**(S4)**

```math
\mathcal W_\eta(A,t)=
\left\{(u,v):
Au+v=t,\quad
\|u\|_\infty\le\eta,\quad
\|v\|_\infty\le\eta
\right\},
```

where $`u\in R_q^\ell`$ and $`v\in R_q^k`$. Membership is publicly decidable by the ring equation and coefficient bounds. The bounded-witness search problem asks for **any** member of this set under the stated public-key distribution, rather than equality with the key generator's original draw.

Let $`\mathsf E_N`$ be the identification estimator followed by linear completion and public validation. It first rejects records outside the public format, coefficient ranges, challenge set, or allowed censoring patterns; this keeps its resource bound valid on simulated inputs as well. It returns $`\bot`$ on an invalid candidate, an inconsistent equation, or a noninjective matrix. On genuine views it returns a valid bounded witness with the probability in (S3). Thus

**(S5)**

```math
\mathsf D(A,t,V)
=
\mathbf1\{\mathsf E_N(A,t,V)\in\mathcal W_\eta(A,t)\}
```

is a public, efficiently decidable event. A different bounded witness also counts as success for the defined search problem.

## 4. Repeated-transcript simulation

A public-key-only simulator $`\mathsf{Sim}_N`$ receives $`(A,t)`$ and public parameters and produces $`N`$ proposed first-attempt records. It may be stateful and correlate its outputs. It receives no witness, trapdoor, or genuine secret-dependent transcripts, and cannot change the supplied public key. Algorithms in this chapter are classical; a corollary for quantum simulators requires the corresponding quantum bounded-witness assumption.

Let $`\varepsilon_{\rm BW}(T)`$ be the maximum success probability of a time-$`T`$ algorithm solving (S4) under the key distribution. Include any independently available classical random oracle in this experiment.

### Theorem 3: simulation implies bounded-witness search

If $`\mathsf{Sim}_N`$ runs in time $`T_{\rm sim}`$ and $`\mathsf E_N`$ in time $`T_{\rm ext}`$, the public test (S5) has distinguishing advantage at least

**(S6)**

```math
1-\delta-\delta_A-\delta_{\rm rk}
-\varepsilon_{\rm BW}(T_{\rm sim}+T_{\rm ext})
```

between genuine and simulated repeated views. Subtract an additional $`\xi_N`$ under the source approximation following (S3).

**Proof.** On genuine views, public validation succeeds with probability at least the first four terms of (S6). On simulated views, the composition

```math
\mathsf E_N(A,t,\mathsf{Sim}_N(A,t))
```

is a bounded-witness search algorithm with the displayed total time. Its success is at most $`\varepsilon_{\rm BW}(T_{\rm sim}+T_{\rm ext})`$. Subtract the two acceptance probabilities. $`\square`$

This is a computational obstruction. An unbounded simulator can find a witness and generate genuine views. A simulator supplied with a witness or an appropriate key-generation trapdoor is outside the premise.

For an asymptotic consequence, $`N`$ and total processing must be polynomial in the security parameter. The observation bound has this property under the stated parameter scaling, including a non-negligible $`p_z`$. It is not polynomial in $`\log q`$ for arbitrary exponentially large $`q`$.

### Connection to a bounded-secret Module-LWE decision assumption

Consider the decision problem

**(S7)**

```math
(A,As_1+s_2)
\quad\text{versus}\quad
(A,U),\qquad U\leftarrow U(R_q^k),
```

with the exact secret and error distributions specified and supported coefficientwise in $`[-\eta,\eta]`$. For every fixed $`A`$, at most $`(2\eta+1)^{M+D}`$ different vectors $`t`$ can arise from bounded pairs. Therefore

**(S8)**

```math
\Pr_U[\mathcal W_\eta(A,U)\ne\varnothing]
\le
\rho_{\rm wit}:=
\min\left\{1,\frac{(2\eta+1)^{M+D}}{q^D}\right\}.
```

A bounded-witness solver with real-instance success $`p_{\rm BW}`$, followed by public validation, distinguishes (S7) with advantage at least $`p_{\rm BW}-\rho_{\rm wit}`$. Thus the corresponding bounded-secret decisional Module-LWE assumption implies bounded-witness search hardness whenever the support bound is negligible.

The base-two logarithms of the untruncated support bounds for 44, 65, and 87 are approximately $`-18795.25`$, $`-26399.33`$, and $`-38184.91`$. These are counting bounds, not measured security levels. The implication uses the stated bounded-secret and error laws; it does not assert a parameter-preserving worst-case reduction or silently change to a uniform-secret assumption.

## 5. The one-transcript definition and composition

The corrected [SUCRE Definition 5](https://eprint.iacr.org/2026/2248) gives a distinguisher the public key and one real or simulated transcript, averaging over a newly generated keypair. It omits the signing key.

The cited analysis requires more: [Devevey et al., Section 4.2, Definition 10 of the current ePrint](https://eprint.iacr.org/2023/245.pdf) supplies the witness to the distinguisher, while keeping it unavailable to the simulator, and quantifies over valid statement-witness pairs. The original version has the same condition as Definition 7. The requirement is also reproduced in [Fallahpour's thesis, Definition 29](https://pouriafallahpour.github.io/Thesis-with-acknowledgements.pdf).

This condition has a direct role in a hybrid proof. When replacing one record among many, a reduction receiving the witness can generate all remaining real records under the same key. A one-record bound $`\epsilon`$ then gives a $`N\epsilon`$ repeated-record bound. The public-key-only definition does not provide that ability.

Consequently, Theorem 3 also obstructs a negligible-error witness-robust one-record simulator when $`N`$ is polynomial, the success lower bound in (S3) is non-negligible, and bounded-witness search is hard. This conclusion concerns the full augmented view, independently of the particular local sampler analyzed elsewhere.

A simple example illustrates the logical distinction. Let a hidden fair sign $`S`$ determine conditionally independent observations with

```math
\Pr[X_i=S\mid S]=\frac12+\epsilon.
```

One observation is marginally fair, but

```math
\mathbb E[X_1X_2]=4\epsilon^2.
```

Independent fair-sign simulation loses this repeated correlation. The example explains why matching a one-record marginal is insufficient. The lattice simulation theorem is stronger: it uses public witness validation to cover correlated public-key-only simulators as well.

The source comparison identifies a missing hypothesis in the cited composition route. The [sampler-marginal result](sampler_marginal.md) separately addresses the stated one-sample comparison distribution. A falsified premise does not itself falsify every conditional implication using that premise. The established claims are the statistical identification result, the conditional simulation obstruction, and the definition mismatch. They do not rule out every alternative security theorem under a different observation model or assumption.

## 6. Fresh messages, first attempts, and resource costs

The mathematical source supplies independent uniform challenges. In the classical random-oracle formulation $`c=\mathcal O(m\mathbin\|h)`$, the same first-attempt law follows when messages have distinct unambiguously encoded prefixes and no earlier oracle query uses the next prefix. Here $`m`$ is the message, $`\mathcal O`$ is the challenge oracle, and $`H`$ continues to denote the high-part function. Lazy sampling supplies a challenge independent of that nonce and all previous records.

Equal commitments under different message prefixes do not reuse the same input. Coinciding challenge values do not invalidate independence either: independent uniform draws may coincide. Retaining only first attempts avoids the further within-message dependence caused by retries.

If messages are compressed to independent uniform $`\kappa`$-bit prefixes, distinct messages do not guarantee distinct prefixes. The analysis must then include

**(S9)**

```math
\Pr[\text{prefix collision}]
\le\frac{N(N-1)}{2^{\kappa+1}}.
```

For $`N\le2^{61}`$, this is at most $`2^{-135}`$ at $`\kappa=256`$ and $`2^{-391}`$ at $`\kappa=512`$, conditional on that prefix model. Matrix expansion, deterministic nonce derivation, finite counters, and other seeded mechanisms require their actual source and domain-separation assumptions. A theorem for uniform $`A`$ is not automatically a statistical theorem for every fixed finite seed family.

The theorem is first a statement about an observable first-attempt source. To obtain these observations from completed signing requests, the interface must expose the first record with its attempt boundary and retain it regardless of later outcomes. A bounded-attempt interface can return the first record even when it ultimately reports failure. For a run-until-success interface, one also uses its stated termination and runtime guarantee. [Devevey et al.](https://eprint.iacr.org/2023/245) treat the distinction between bounded and unbounded abort loops explicitly.

With one first record retained per request, $`N`$ records require $`N`$ signing requests. If a complete request has expected cost $`C_{\rm sign}`$, obtaining the observations costs $`N C_{\rm sign}`$, including all unused later attempts. The processing costs below are additional to that source cost.

### Exact integer processing and storage

The statistic can be represented exactly, so identifying a small mean does not require an uncharged real-arithmetic operation. On a first-check-passing record, write

**(S10)**

```math
\mathsf{num}_{b,j}
=
(qF-DpS_1)
\sum_{i=0}^{n-1}C(c)_{i,j}
\left(q\mathbf1_{\{h_{bn+i}=0\}}-(\alpha+1)\right).
```

Set this numerator to zero on a first-check rejection. Since $`\mu=pS_1/q`$ and $`p_0=(\alpha+1)/q`$, the observed quantity is exactly $`Q_{b,j}=\mathsf{num}_{b,j}/q^2`$. With $`R=\tau D\beta`$ from the [concentration proof](concentration.md),

```math
|\mathsf{num}_{b,j}|\le q^2R.
```

Every signed sum of $`N`$ numerators can therefore be represented with

**(S11)**

```math
b_{\rm acc}
=
\left\lceil\log_2(2Nq^2R+1)\right\rceil
```

bits. The histogram weight can be formed by scanning the $`D`$ observed residues or a sparse histogram with at most $`D`$ nonzero entries. Direct accumulation of all coefficient statistics uses $`O(ND\tau)`$ integer operations. Charging each conservatively at schoolbook cost gives $`O(ND\tau b_{\rm acc}^2)`$ bit operations.

There are $`D`$ accumulators, using $`O(Db_{\rm acc})`$ bits. One-record input buffers require $`O(D\log q+\tau\log n)`$ bits when the challenge is stored by its signed support. The explicit public module matrix itself uses $`O(k\ell n\log q)`$ bits. No storage of the complete sequence of records is needed.

Let $`\mathsf{sum}_{b,j}`$ be the accumulated integer numerator. Before nearest-integer rounding, the real-valued estimate is the exact rational expression

**(S12)**

```math
\widetilde s_{b,j}
=
-\frac{2\,\mathsf{sum}_{b,j}(2\gamma_1)^M}
{NqL^M\tau}.
```

Its numerator and denominator have bit lengths at most

**(S13)**

```math
b_{\rm fin}
=
O\!\left(
b_{\rm acc}
+M\log_2(2\gamma_1)
+\log_2(Nq\tau)
\right).
```

The common integer powers can be formed with $`O(\log(M+1))`$ schoolbook multiplications at this length. The $`D`$ final nearest-integer decisions can use exact integer division and remainder comparisons. A conservative total for these operations is $`O((D+\log(M+1))b_{\rm fin}^2)`$ bit operations and $`O(Db_{\rm acc}+b_{\rm fin})`$ working bits, apart from the input and matrix storage.

For full-key completion, Gaussian elimination on the explicit $`D\times M`$ coefficient matrix costs $`O(DM^2)`$ field operations when $`D\ge M`$ and uses $`O(DM\log q)`$ bits of matrix storage. Standard modular arithmetic makes this polynomial bit cost; even charging $`O((\log q)^3)`$ per field operation, including inversion, gives the conservative bound $`O(DM^2(\log q)^3)`$. The source work, accumulation, exact rescaling, and linear algebra are all separate charges.

The sufficient observation counts $`2^{57}`$, $`2^{61}`$, and $`2^{59}`$ are large analytical bounds in the ideal model. They are not observed device traces, practical feasibility measurements, or complete bit-operation security estimates. No operational implementation experiment is used here.

## 7. Compressed verification keys and physical observations

For a compressed key, write its hidden low part abstractly as

```math
t=2^{d_{\rm pk}}t_1+t_0.
```

Even if the same observation theorem identifies $`s_2`$, the public equation becomes

```math
As_1=2^{d_{\rm pk}}t_1+t_0-s_2,
```

with compression exponent $`d_{\rm pk}`$ and unknown $`t_0`$. The linear completion from Section 2 is therefore unavailable as stated. Disclosure of $`s_2`$ remains a meaningful consequence of the specified observations; full-key recovery or forgery for the compressed interface needs an additional argument.

The observation resource is also substantive. [SUCRE's Theorem 3 proof](https://eprint.iacr.org/2026/2248) introduces a scheme returning the high coefficients and permuted norm-check values. Its Definition 10 and Figure 1 include declared public outputs. This supports the mathematical augmented view. It does not establish that an arbitrary physical device gives an observer an exact histogram, reliable attempt boundaries, and noiseless indexed high coefficients.

The supported scope is: repeated augmented views identify $`s_2`$; full public $`t`$ and matrix injectivity extend the result to the algebraic key; and a computationally indistinguishable public-key-only simulator for those repeated views would solve the stated bounded-witness problem. Ordinary ML-DSA without added observations, narrower noisy physical interfaces, and compressed-key full forgery remain separate questions.

## Reading onward

The [related-work account](../references/RELATED_WORK.md) compares this model with earlier shuffled-nonce and rejected-response results. The [scientific entrypoint](README.md) places the chapter after the statistical and concentration proofs.
