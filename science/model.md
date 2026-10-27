# Repeated shuffled residues

A shuffle removes the correspondence between an internal value and its original coordinate. It preserves the number of occurrences of every value. This project studies whether those counts remain correlated with other, indexed information from the same signing attempt.

The observation is a histogram of rounding remainders. The indexed information is the commitment's high part and the public challenge. A small asymmetry in the rounding rule creates a correlation whose average identifies a coefficient of the fixed secret. The [boundary calculation](boundary_statistic.md), [fixed-matrix theorem](fixed_matrix.md), and [concentration bound](concentration.md) establish this statement without assuming that the entire commitment is statistically uniform.

## Algebra and parameters

Let $`q`$ be an odd prime and $`n\ge2`$ a power of two. Set

```math
R=\mathbb Z[X]/(X^n+1),
\qquad
R_q=\mathbb F_q[X]/(X^n+1).
```

Coefficient vectors use the basis $`1,X,\ldots,X^{n-1}`$. Multiplication is negacyclic: $`X^n=-1`$. Integer coefficient bounds refer to the sampled integer representatives before reduction modulo $`q`$.

Fix positive module ranks $`k,\ell`$, with $`D=kn\ge4`$ and $`M=\ell n`$. Draw the public matrix once:

```math
A\leftarrow U(R_q^{k\times\ell}).
```

The secrets $`s_1\in R^\ell`$ and $`s_2\in R^k`$ have coefficients in $`\{-\eta,\ldots,\eta\}`$, where $`\eta\ge1`$. The statistical result holds for every such pair on the same good-matrix event. The full public key used for the security consequence is

```math
(A,t),\qquad t=As_1+s_2\pmod q.
```

Choose an even $`\alpha`$ and an integer $`p\ge2`$ such that

```math
q=p\alpha+1,\qquad a=\alpha/2.
```

The challenge set $`\mathcal B_\tau`$ consists of polynomials with exactly $`\tau`$ nonzero coefficients, each independently signed, for $`1\le\tau\le n`$. Put $`\beta=\eta\tau`$ and assume $`\beta<a`$. The nonce bound $`\gamma_1`$ is an integer satisfying

```math
\gamma_1>\beta,\qquad
L=2(\gamma_1-\beta)-1\ge1,\qquad
2\gamma_1\le q.
```

The last condition makes each coefficient interval a set of distinct field residues. In particular, $`L\le q`$, as required by the fixed-matrix theorem.

| Symbol | Meaning |
|---|---|
| $`n`$ | Polynomial degree |
| $`k,\ell`$ | Output and input module ranks |
| $`D=kn,\ M=\ell n`$ | Output and input coefficient dimensions |
| $`q=p\alpha+1`$ | Field modulus and rounding relation |
| $`a=\alpha/2=\gamma_2`$ | Low-part endpoint |
| $`\eta,\tau,\beta=\eta\tau`$ | Secret bound, challenge weight, product bound |
| $`\gamma_1`$ | Nonce coefficient bound |
| $`L=2(\gamma_1-\beta)-1`$ | Interior box size after the first check |
| $`\varepsilon`$ | Small-marginal total variation tolerance |
| $`\delta`$ | Conditional statistical failure target |

## The rounding convention

For a residue $`x\in\mathbb F_q`$, let $`H(x)`$ and $`L_\alpha(x)`$ be the high and low parts defined by the ML-DSA decomposition convention. To specify the convention completely, take $`x^+\in\{0,\ldots,q-1\}`$, let $`r`$ be its representative modulo $`\alpha`$ in $`(-a,a]`$, and set

```math
(H(x),L_\alpha(x))=
\begin{cases}
(0,r-1),&x^+-r=q-1,\\
((x^+-r)/\alpha,r),&\text{otherwise}.
\end{cases}
```

Thus $`H(x)\in\{0,\ldots,p-1\}`$, $`L_\alpha(x)\in[-a,a]`$, and

```math
x=\alpha H(x)+L_\alpha(x)\pmod q.
```

We write $`L`$ without a subscript only for the box size, and $`L_\alpha`$ for the low-part function. The zero high bin contains $`\alpha+1`$ residues. The low value $`-a`$ has one preimage; every other low value has $`p`$. These exceptional endpoints drive the calculation.

This is the decomposition in [SUCRE, Figure 2 and Lemma 5](https://eprint.iacr.org/2026/2248) and [FIPS 204](https://doi.org/10.6028/NIST.FIPS.204). The arguments below use the displayed definition, including its endpoint convention.

## One independent attempt

For a fixed matrix and fixed secrets, draw a fresh nonce and challenge:

```math
y\leftarrow U(\{-\gamma_1+1,\ldots,\gamma_1\}^{M}),
\qquad
c\leftarrow U(\mathcal B_\tau),
```

independently. Form

```math
w=Ay\pmod q,\qquad h=H(w),
\qquad z=y+cs_1,
\qquad r=L_\alpha(w-cs_2).
```

The high and low functions act coefficientwise. All coefficients of $`cs_1`$ and $`cs_2`$ have magnitude at most $`\beta`$ because each is a sum of $`\tau`$ signed secret coefficients.

Let $`P_z`$ denote the event

```math
\|z\|_\infty<\gamma_1-\beta.
```

The low-part check passes when $`\|r\|_\infty<a-\beta`$. We study an augmented observation containing the indexed $`h`$, challenge $`c`$, the first-check outcome, and the complete histogram of $`r`$ when that check is reached. A fresh uniformly random permutation of the entire $`D`$-coefficient residual vector contains exactly this histogram and additional irrelevant random order.

The theorem also covers suppression of the histogram on accepted attempts. Its statistic uses only residual values that force low-part rejection; their counts are known to be zero on an accepted attempt. This observation is proved in the [statistic chapter](boundary_statistic.md#visibility-and-rejection).

The full histogram is a substantive resource. A noisy physical trace, one probed coefficient, or a truncated early-abort trace defines a different observation model.

## Exact conditioning on the first check

For every fixed challenge and both fixed secrets,

```math
p_z:=\Pr(P_z)
=\left(\frac{L}{2\gamma_1}\right)^M.
```

Indeed, $`P_z`$ requires each coefficient of $`z`$ to lie in

```math
\mathcal I=
\{-\gamma_1+\beta+1,\ldots,\gamma_1-\beta-1\},
```

which has exactly $`L`$ elements. Translation by any coefficient of $`cs_1`$ maps this interval inside the original nonce interval, since that coefficient is bounded by $`\beta`$. Every admissible $`z`$ has one equally likely nonce preimage. Therefore, conditional on $`P_z`$ and $`c`$,

```math
y=Z-cs_1,
\qquad Z\leftarrow U(\mathcal I^M).
```

The pass probability is independent of $`c`$, so the challenge remains uniform after conditioning. The conditional nonce distribution is an exact translated product box. This is the input law used by the fixed-matrix theorem.

## First attempts and the random-oracle model

The independent challenge experiment can be obtained from the first signing attempt for each distinct fresh message in the classical random-oracle model. Use a fresh message whose oracle prefix has not previously been queried. Its commitment is computed before the first challenge query. Lazy sampling then makes that challenge independent of the nonce and uniformly distributed in $`\mathcal B_\tau`$.

Observations from later attempts of the same signing invocation are unnecessary. Restricting to first attempts avoids dependence caused by revisiting a challenge input under the same message prefix. The augmented view must identify attempt boundaries and expose the relevant commitment and check outcomes. With a direct $`c=\mathcal O(m\mathbin\|h)`$ model, where $`\mathcal O`$ is the challenge oracle and $`m`$ is a fresh message prefix, distinct prefixes give exact freshness. A separate finite message prehash contributes its usual collision event.

This is a classical observation strategy. It does not require quantum oracle queries, quantum storage, or a quantum algorithm.

## Relation to the audited source

[SUCRE's corrected ePrint](https://eprint.iacr.org/2026/2248), received September 28, 2026, explicitly uses a full verification key in Section 2.5. Its Theorem 3 introduces an enlarged signature view containing the commitment high bits and shuffled norm-check values for each attempt. Definition 11 uses frequency maps and suppresses the low-part hint when the first check fails. These are the source-level reasons for studying the observation above.

The ideal uniform matrix and independent box nonces are mathematical distributions. A short seed expanded by a fixed concrete function is not literally uniform over all matrices or nonce sequences. Instantiating the theorem for seeded algorithms requires the stated random-oracle or pseudorandomness model. The [security-scope chapter](security_scope.md) keeps this distinction, full versus compressed verification keys, and physical leakage separate.

## Reading onward

The [boundary statistic](boundary_statistic.md) first derives the observable mean under independent uniform output coordinates. The [fixed-matrix proof](fixed_matrix.md) then justifies the small marginals required by that calculation for one matrix reused across observations. The [concentration theorem](concentration.md) turns the mean into a finite-observation guarantee. No claim of full-vector uniformity is used.
