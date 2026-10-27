# Small marginals for one fixed public matrix

The public matrix is sampled once and reused across records. This page gives an explicit probability bound for the event that all required four-coordinate marginals of a box product are statistically close to independent uniform field elements. On that event, the same matrix works for every translation of the box. That last property handles conditioning on the first rejection check, whose effect is to translate a smaller box by a secret-dependent amount. The matrix-exception bound is tiny at the displayed parameter shapes.

The [boundary statistic](boundary_statistic.md) uses two-coordinate marginals for its mean. The [concentration argument](concentration.md) uses four-coordinate marginals for its second moment. Neither argument assumes that the complete product vector is uniform: its entropy may be insufficient for that stronger assertion.

## 1. Notation and statement

Let $`q`$ be an odd prime, let $`n\ge 2`$ be a power of two, and put

```math
R_q=\mathbb F_q[X]/(X^n+1),\qquad
A\leftarrow\mathrm{Unif}(R_q^{k\times\ell}),\qquad
D=kn,\qquad M=\ell n.
```

A polynomial is represented by its coefficients of degrees $`0,\ldots,n-1`$. An output position is a pair $`(b,j)`$, where $`0\le b\lt k`$ is a module row and $`0\le j\lt n`$ is a coefficient index. Flattening this position gives index $`bn+j`$.

Fix sets $`\mathcal S_1,\ldots,\mathcal S_M\subseteq\mathbb F_q`$, each of cardinality $`L`$, where $`1\le L\le q`$. Let $`Z`$ be uniform on their product. Thus its coefficients are independent and uniform on their respective sets. These sets are fixed independently of $`A`$. Intervals are the application of interest, but the proof does not require them.

For distributions on a finite set, use the convention

```math
\mathrm{TV}(P,Q)=\frac12\sum_x|P(x)-Q(x)|.
```

For a set $`I`$ of $`r`$ distinct output positions, define

```math
\delta_I(A)=
\mathrm{TV}\!\left(
\mathcal L((AZ)_I),\mathrm{Unif}(\mathbb F_q^r)
\right),
\qquad
J_r=\frac{q^r-1}{q-1}.
```

Here $`1\le r\le D`$. The integer $`J_r`$ is the number of one-dimensional subspaces of $`\mathbb F_q^r`$.

### Theorem 1 — A fixed matrix controls all small marginals

For every fixed set $`I`$ of $`r`$ output positions,

```math
\mathbb E_A\bigl[\delta_I(A)^2\bigr]
\le
\frac{q^rJ_r}{4L^{\ell\lceil n/r\rceil}}.
```

Consequently, for every $`\varepsilon>0`$, define

```math
\zeta_r(\varepsilon)=
\min\!\left\{
1,\;
\binom Dr\frac{q^rJ_r}
{4\varepsilon^2L^{\ell\lceil n/r\rceil}}
\right\}.
```

With probability at least $`1-\zeta_r(\varepsilon)`$ over the single draw of $`A`$, the following holds simultaneously for every set $`I`$ of at most $`r`$ output positions and every translation $`\boldsymbol b\in R_q^\ell`$:

```math
\mathrm{TV}\!\left(
\mathcal L((A(Z+\boldsymbol b))_I),
\mathrm{Unif}(\mathbb F_q^{|I|})
\right)
\le\varepsilon.
```

The translation may depend on the matrix, challenge, or secrets. The assertion is pointwise in the translation once $`A`$ satisfies the stated event. It does not assert simultaneous control of every possible choice of the base sets $`\mathcal S_i`$.

### When the bound is informative

The guarantee is useful when $`\zeta_r(\varepsilon)`$ is small. Its definition permits the value one, so a near-universal statement about matrices requires the actual parameters. For an asymptotic family indexed by a security parameter $`\lambda`$, a sufficient condition for negligible four-coordinate exception probability is

```math
\ell\lceil n/4\rceil\log_2 L
-\log_2\!\left(
\frac{\binom D4 q^4J_4}{4\varepsilon^2}
\right)
=\omega(\log\lambda).
```

The notation $`\omega(\log\lambda)`$ means that the ratio to $`\log\lambda`$ tends to infinity. If $`q,D,\varepsilon^{-1}`$ are polynomially bounded in $`\lambda`$, it suffices that $`\ell\lceil n/4\rceil\log_2L=\omega(\log\lambda)`$. The finite theorem and its numerical table retain their explicit exception probabilities without requiring an asymptotic interpretation.

## 2. The coefficient pairing and the negacyclic signs

Write $`[f]_0`$ for the constant coefficient of $`f\in R_q`$. The element $`X`$ is invertible, and

```math
X^{-j}=-X^{n-j}\quad(1\le j\lt n),
\qquad
[X^{-j}f]_0=f_j\quad(0\le j\lt n).
```

The second identity incorporates the minus sign from $`X^n=-1`$. In particular, the bilinear pairing

```math
\langle a,f\rangle_0=[af]_0
```

is nondegenerate: if $`[af]_0=0`$ for every $`a\in R_q`$, choosing $`a=X^{-j}`$ shows that every coefficient of $`f`$ is zero.

This pairing will turn a relation among selected output coordinates into a polynomial annihilator. It avoids an implicit transpose convention: the polynomial representing a coefficient functional uses the negative exponents $`X^{-j}`$, with the signs shown above.

## 3. Two elementary linear-algebra facts

### Lemma 2 — Rank of sparse negacyclic multiplication

If a nonzero polynomial $`v\in R_q`$ has $`s`$ nonzero coefficients, multiplication by $`v`$ has rank at least $`\lceil n/s\rceil`$ over $`\mathbb F_q`$.

**Proof.** The multiplication matrix has no zero column: its $`j`$th column represents $`X^jv`$, which is nonzero because $`X`$ is a unit. Every row is a signed cyclic rearrangement of the coefficients of $`v`$, so has exactly $`s`$ nonzero entries.

Choose a basis consisting of $`t`$ rows of the matrix. The union of their supports must cover all $`n`$ columns. Otherwise every linear combination of those basis rows would vanish in a missing column, contradicting the fact that the full column is nonzero. Thus $`ts\ge n`$, proving the claim. $`\square`$

This argument holds over the finite field itself. It does not require the polynomial modulus to split, a Fourier transform, or a characteristic-zero uncertainty inequality.

### Lemma 3 — A product box meets a subspace in few points

Let $`E\subseteq\mathbb F_q^M`$ be a linear subspace of dimension $`t`$, and let $`Z'`$ be an independent copy of $`Z`$. Then

```math
\Pr[Z-Z'\in E]\le L^{-(M-t)}.
```

**Proof.** There are $`t`$ coordinate positions whose projection is injective on $`E`$: choose pivot coordinates in a basis matrix. For any fixed value $`Z=z`$, this projection is also injective on the affine space $`z-E`$. At most $`L^t`$ points of the product support of $`Z'`$ can lie in that affine space, because each of the selected coordinates has only $`L`$ possible values. The product support has $`L^M`$ equally likely points. The bound holds for every $`z`$ and hence after averaging over it. $`\square`$

## 4. Collision proof of Theorem 1

Let $`\Delta=Z-Z'`$. For a fixed difference $`\Delta`$, the map

```math
\mathcal C_\Delta:
\mathbb F_q^{k\ell n}\longrightarrow\mathbb F_q^r,
\qquad
A\longmapsto(A\Delta)_I
```

is linear. If its rank is $`\rho(\Delta)`$, uniformity of the coefficients of $`A`$ gives

```math
\Pr_A[(A\Delta)_I=0]=q^{-\rho(\Delta)}.
```

### Bounding deficient-rank differences

Suppose $`\rho(\Delta)\lt r`$. There is a nonzero vector $`\lambda\in\mathbb F_q^r`$ such that the corresponding linear combination of the selected output functionals is zero. Scalar multiples give the same relation, so it suffices to consider $`J_r`$ projective choices.

Fix one such relation. Among the selected output module rows, choose a row $`b`$ on which its coefficients are not all zero. Let $`I_b`$ be the coefficient indices selected in that row, and define

```math
v_\lambda=\sum_{j\in I_b}\lambda_{b,j}X^{-j}\in R_q.
```

Its monomials are distinct, including their negacyclic signs. It is therefore nonzero and has at most $`r`$ nonzero coefficients. The relation holds for every choice of the matrix entries. Varying one entry $`a\in R_q`$ of row $`b`$, while fixing the other entries to zero, gives

```math
[a\Delta_t v_\lambda]_0=0
\quad\text{for every }a\in R_q,
\qquad 1\le t\le\ell.
```

The nondegenerate pairing proves

```math
\Delta_t v_\lambda=0\qquad(1\le t\le\ell).
```

By Lemma 2, the kernel of multiplication by $`v_\lambda`$ has dimension at most $`n-\lceil n/r\rceil`$. The allowed difference vectors therefore lie in a subspace of dimension at most

```math
M-\ell\lceil n/r\rceil.
```

Lemma 3 bounds the probability of this particular projective relation by $`L^{-\ell\lceil n/r\rceil}`$. Taking the union over the relations gives

```math
\Pr_\Delta[\rho(\Delta)\lt r]
\le J_rL^{-\ell\lceil n/r\rceil}.
```

### From collisions to total variation

For fixed $`A`$, let $`P_A`$ denote the law of $`(AZ)_I`$ and define its collision probability by $`\mathrm{CP}(P_A)=\sum_xP_A(x)^2`$. Independence of $`Z,Z'`$ gives

```math
\begin{aligned}
\mathbb E_A\mathrm{CP}(P_A)
&=\mathbb E_\Delta q^{-\rho(\Delta)}\\
&\le q^{-r}+J_rL^{-\ell\lceil n/r\rceil}.
\end{aligned}
```

The bound uses collision probability $`q^{-r}`$ on full-rank differences and the upper bound $`1`$ on the exceptional differences. Cauchy–Schwarz gives the normalization

```math
\mathrm{TV}(P_A,U)^2
\le\frac{q^r}{4}\sum_x(P_A(x)-q^{-r})^2
=\frac{q^r}{4}\bigl(\mathrm{CP}(P_A)-q^{-r}\bigr),
```

where $`U`$ is uniform on $`\mathbb F_q^r`$. Taking expectations proves the first assertion of Theorem 1.

Markov's inequality bounds the probability that a specified $`\delta_I(A)`$ exceeds $`\varepsilon`$ by its second-moment bound divided by $`\varepsilon^2`$. A union bound over the $`\binom Dr`$ sets of size $`r`$ gives $`\zeta_r(\varepsilon)`$. Every smaller set can be extended to one of size $`r`$, and total variation cannot increase under projection.

Finally, for every fixed $`A`$ and $`\boldsymbol b`$,

```math
(A(Z+\boldsymbol b))_I=(AZ)_I+(A\boldsymbol b)_I.
```

Translation is a bijection that preserves uniform measure. Thus the translated marginal has **exactly the same** total variation distance as the untranslated marginal. This proves the simultaneous all-translations assertion without an additional union bound. $`\square`$

## 5. Conditioning on the first check

Use the [model's notation](model.md): the nonce coefficients are independent uniform integers in $`(-\gamma_1,\gamma_1]`$, the secret coefficients have magnitude at most $`\eta`$, and the signed challenge has weight $`\tau`$. Put $`\beta=\eta\tau\lt \gamma_1`$ and let

```math
P_z=\{\|y+cs_1\|_\infty\lt \gamma_1-\beta\},\qquad
L=2(\gamma_1-\beta)-1.
```

Assume $`L\le q`$, as in all parameter shapes considered here. Every coefficient of $`cs_1`$ lies in $`[-\beta,\beta]`$. For any fixed challenge and secret, the accepted integer values of $`z=y+cs_1`$ in each coordinate are precisely

```math
\{-\gamma_1+\beta+1,\ldots,\gamma_1-\beta-1\}.
```

Shifting this interval by the negative of a coefficient of $`cs_1`$ keeps it inside the original nonce interval. It contains exactly $`L`$ values. Consequently,

```math
p_z:=\Pr(P_z\mid c,s_1)
=\left(\frac{L}{2\gamma_1}\right)^M,
\qquad
\mathcal L(y\mid P_z,c,s_1)=\mathcal L(Z-cs_1),
```

where $`Z`$ is uniform on the centered product box just displayed. This is an equality of integer distributions before reduction modulo $`q`$. The bound $`L\le q`$ makes the coefficients of the smaller box distinct residues, as required by Theorem 1.

In particular, $`p_z`$ is independent of the challenge and secrets. A matrix satisfying Theorem 1 for this one base box controls the output conditional on $`P_z`$ for **every** challenge and secret. No assertion of independence after an arbitrary rejection event is being made; the argument uses this specific translated-box identity.

## 6. Four-coordinate bounds at the stated parameter shapes

For the common values $`q=8380417`$, $`n=256`$, and $`\varepsilon=2^{-128}`$, the bound in Theorem 1 gives the following values. The parameter shapes are those in SUCRE's Table 2; the numerical probabilities here are derived from this page's theorem, not measurements. [SUCRE]

| Shape | $`(k,\ell)`$ | $`\gamma_1`$ | $`\beta`$ | $`L`$ | $`\log_2\zeta_4(2^{-128})`$, rounded |
|---|---:|---:|---:|---:|---:|---:|
| 44 | $`(4,4)`$ | $`2^{17}`$ | 78 | 261987 | $`-4157.3820`$ |
| 65 | $`(6,5)`$ | $`2^{19}`$ | 196 | 1048183 | $`-5947.0876`$ |
| 87 | $`(8,7)`$ | $`2^{19}`$ | 120 | 1048335 | $`-8505.4505`$ |

The calculation uses

```math
\begin{aligned}
\log_2\zeta_4(\varepsilon)
={}&\log_2\binom D4+4\log_2q
+\log_2(1+q+q^2+q^3)\\
&-\ell\lceil n/4\rceil\log_2L
-2-2\log_2\varepsilon,
\end{aligned}
```

since the expression inside the minimum defining $`\zeta_4`$ is below one in these cases. Conservative consequences are $`\zeta_4\lt 2^{-4157}`$, $`2^{-5947}`$, and $`2^{-8505}`$, respectively.

These are probabilities over a uniform module matrix. A short-seed matrix expansion is a different literal distribution and requires the model for its expander stated in [security scope](security_scope.md). The result does not assert that an arbitrary seeded matrix family satisfies the same statistical bound.

## Appendix: sharper one- and two-coordinate bounds

The generic four-coordinate theorem is the load-bearing result. The smaller projections admit stronger bounds that also check the factors of $`q`$ and $`1/4`$ in the collision argument.

### One coordinate

For a single output coordinate and any nonzero difference $`\Delta`$, that coordinate of $`A\Delta`$ is a nonzero linear functional of the relevant row of $`A`$. Indeed, the constant-coefficient pairing detects every nonzero polynomial component of $`\Delta`$. The exceptional event $`\Delta=0`$ has probability $`L^{-M}`$. Therefore

```math
\mathbb E_A\mathrm{CP}(P_A)
=q^{-1}+(1-q^{-1})L^{-M},
\qquad
\mathbb E_A\delta_I(A)^2
\le\frac{q-1}{4L^M}.
```

### Two coordinates in different module rows

For $`\Delta\ne0`$, the two nonzero linear functionals involve independent matrix rows. Their joint collision probability is exactly $`q^{-2}`$. Hence

```math
\mathbb E_A\mathrm{CP}(P_A)
=q^{-2}+(1-q^{-2})L^{-M},
\qquad
\mathbb E_A\delta_I(A)^2
\le\frac{q^2-1}{4L^M}.
```

### Two coordinates in one module row

Suppose the coefficient indices differ by $`d`$ modulo $`n`$, with $`0\lt d\lt n`$. Set

```math
g=\gcd(n,d),\qquad
e_d=\#\{\lambda\in\mathbb F_q:\lambda^{n/g}=-1\}.
```

First separate the event $`\Delta=0`$, which gives rank zero. For a nonzero difference, rank one occurs precisely when all $`\ell`$ polynomial components lie in the same eigenspace of multiplication by $`X^d`$. This follows directly from the relation

```math
(\lambda_1X^{-i}+\lambda_2X^{-j})\Delta_t=0
```

and the fact that neither coefficient can be zero for a relation between two nonzero functionals. Multiplication by a monomial removes the negative exponents without changing the equation's kernel.

The signed permutation $`X^d`$ has $`g`$ coordinate cycles of length $`n/g`$. Because $`n`$ is a power of two, $`d/g`$ is odd, and the product of signs on each cycle is $`-1`$. An eigenvalue must satisfy $`\lambda^{n/g}=-1`$. For every such eigenvalue, choosing one coordinate on each cycle determines all others, so the eigenspace has dimension $`g`$.

Lemma 3 and a union bound consequently give

```math
\Pr[\Delta\ne0\text{ and rank one}]
\le e_dL^{-\ell(n-g)}.
```

This bound concerns nonzero differences. If $`e_d=0`$, rank one is impossible but the zero difference must still be counted. Keeping the two cases separate yields

```math
\mathbb E_A\delta_I(A)^2
\le\frac14\left(
(q^2-1)L^{-M}
+(q-1)e_dL^{-\ell(n-g)}
\right).
```

Since $`g\le n/2`$ and $`e_d\le n`$, a convenient uniform bound for all pairs is

```math
\mathbb E_A\delta_I(A)^2
\le\frac14\left(q^2L^{-M}+qnL^{-M/2}\right).
```

The same Markov, union, projection, and translation arguments apply. The proof does not replace any finite-field eigenspace by a complex eigenspace.

## Source and scope

[SUCRE] Sonia Belaïd et al., *ML-DSA masking sweetened with SUCRE: Shuffle-and-Unmask Countermeasure for REjection sampling*, TCHES 2026(1), corrected [ePrint 2026/2248](https://eprint.iacr.org/2026/2248), especially Section 2.5 and Table 2. The source supplies the parameter model; the finite-marginal bounds above are the mathematical argument developed in this project.

The theorem is an information-theoretic statement about a fixed uniform matrix and a fresh product-box source. It supplies the small-marginal premise used in [concentration](concentration.md). It does not by itself claim a signature forgery, physical side-channel feasibility, or full-vector pseudorandomness.
