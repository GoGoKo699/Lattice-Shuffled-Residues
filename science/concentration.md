# Moments and a finite-observation bound

The centered boundary statistic has a mean proportional to one fixed secret coefficient. This page proves a second-moment bound that allows the high-bit indicator and low-residue statistic to correlate at the same coordinate. It then transfers both moments to a single fixed public matrix and gives an explicit Bernstein bound for finitely many independent records.

At the three stated parameter shapes, conservative sufficient counts are $`2^{57}`$, $`2^{61}`$, and $`2^{59}`$ first-attempt records. These are analytical bounds in the [augmented transcript model](model.md). They are enormous counts, not practical trace estimates or experimental results.

## 1. Parameters and the observable centered statistic

Use

```math
R_q=\mathbb F_q[X]/(X^n+1),\qquad
A\in R_q^{k\times\ell},\qquad
D=kn,\qquad M=\ell n.
```

The matrix is drawn once and then fixed. Assume $`D\ge4`$ and use zero-based coefficient indices $`0,\ldots,D-1`$. Let

```math
q=p\alpha+1,\qquad
\alpha\text{ even},\qquad q>2\alpha,\qquad
a=\alpha/2,\qquad
\beta=\eta\tau<a.
```

Assume $`\gamma_1>\beta`$ and $`L=2(\gamma_1-\beta)-1\le q`$. Each fresh nonce $`y`$ is independently uniform in the integer coefficient box $`(-\gamma_1,\gamma_1]^M`$. The challenge $`c`$ is uniform among signed polynomials with exactly $`\tau`$ nonzero coefficients and is independent of that nonce in the first-attempt model. The fixed secrets have coefficient magnitude at most $`\eta`$.

For one record, put

```math
w=Ay,\qquad d=cs_2,\qquad
h_i=\mathrm{HighBits}_q(w_i,\alpha),\qquad
r_i=\mathrm{LowBits}_q(w_i-d_i,\alpha).
```

All $`d_i`$ are regarded as integer coefficients and satisfy $`|d_i|\le\beta`$. The [boundary count](boundary_statistic.md) uses

```math
g(r)=
\begin{cases}
j,&r=-a+j\text{ for some }1\le j\le\beta,\\
0,&\text{otherwise},
\end{cases}
\qquad
p_0=\frac{\alpha+1}{q},
\qquad f(w_i)=\mathbf1\{h_i=0\}-p_0.
```

Define the known constants

```math
S_1=\frac{\beta(\beta+1)}2,\qquad
S_2=\frac{\beta(\beta+1)(2\beta+1)}6,\qquad
\mu=\frac pqS_1,
```

and the histogram statistics

```math
F=\sum_{i=0}^{D-1}g(r_i),\qquad
F_c=F-D\mu.
```

The subscript on $`F_c`$ denotes centering. It does not mean that the challenge is used to construct the histogram.

Fix a module block $`b`$ and a secret coefficient index $`j`$. Let $`C(c)`$ be the integer negacyclic multiplication matrix of $`c`$, so $`C(c)s_{2,b}`$ is the coefficient vector of $`cs_{2,b}`$. The statistic of interest is

```math
T_{b,j}
=F_c\sum_{i=0}^{n-1}C(c)_{i,j}f(w_{bn+i}).
```

A column of $`C(c)`$ has exactly $`\tau`$ nonzero entries, each equal to $`1`$ or $`-1`$. Equivalently, after extending this column by zeros outside block $`b`$, write

```math
T=\left(\sum_{i=0}^{D-1}a_iU_i\right)
  \left(\sum_{i=0}^{D-1}V_i\right),
\quad
U_i=f(w_i),\quad V_i=g(r_i)-\mu,
\quad
a_i\in\{-1,0,1\},\quad\sum_i a_i^2=\tau.
```

### Which records contribute

Let $`P_z`$ be the event that the first check passes:

```math
P_z=\{\|y+cs_1\|_\infty<\gamma_1-\beta\},\qquad
p_z=\Pr(P_z)=\left(\frac{L}{2\gamma_1}\right)^M.
```

Define $`Q_{b,j}=0`$ when this check rejects. On **every** record for which it passes, use $`Q_{b,j}=T_{b,j}`$.

This includes accepted records. Each low value selected by $`g`$ has magnitude at least $`a-\beta`$ and would fail the low-part bound, which requires a strict inequality. Thus an accepted record has $`F=0`$, even if its residual histogram is omitted. Its centered value is therefore $`F_c=-D\mu`$, and its indexed public high bits still contribute. Assigning zero to the whole centered statistic on accepted records would change the mean and invalidate the variance calculation below.

## 2. Exact one-coordinate moments

Begin with a comparison distribution: conditional on a fixed challenge, the coordinates $`w_i`$ are independent uniform field elements. The two variables $`U_i,V_i`$ at a single coordinate are allowed to correlate.

Every selected ordinary low residue has $`p`$ preimages. The exceptional zero high bin has $`\alpha+1`$ preimages. Therefore

```math
\mathbb E U_i=\mathbb E V_i=0,\qquad
u:=\mathbb E U_i^2=p_0(1-p_0),\qquad
v:=\mathbb E V_i^2=\frac pqS_2-\mu^2.
```

The [scalar boundary identity](boundary_statistic.md) gives, with $`\xi_i=(-d_i)_+`$,

```math
\mathbb E[\mathbf1\{h_i=0\}g(r_i)]
=\frac{S_1+\xi_i}{q},\qquad
\mathbb E[\mathbf1\{h_i=0\}g(r_i)^2]
=\frac{S_2+\xi_i^2}{q}.
```

Subtracting the product of the marginal means yields

```math
m_i:=\mathbb E[U_iV_i]
=\frac{\xi_i}{q}-\frac{(p-1)S_1}{q^2},
\qquad
|m_i|\le m_*:=\frac\beta q+\frac{(p-1)S_1}{q^2}.
```

For completeness, the within-coordinate fourth moment is also explicit. Since an indicator $`H`$ satisfies $`(H-p_0)^2=(1-2p_0)H+p_0^2`$,

```math
\begin{aligned}
\kappa_i:=\mathbb E[U_i^2V_i^2]
={}&(1-2p_0)\left(
\frac{S_2+\xi_i^2}{q}
-2\mu\frac{S_1+\xi_i}{q}
+\mu^2p_0
\right)+p_0^2v.
\end{aligned}
```

The uniform estimate needed later is simpler:

```math
0\le\kappa_i\le v.
```

It follows from $`|U_i|\le1`$ and $`\mathbb E V_i^2=v`$. It makes no independence assumption within a coordinate.

## 3. Exact second moment and a challenge-uniform bound

Set $`M_a=\sum_i a_im_i`$. Independence of distinct coordinate pairs gives $`\mathbb E T=M_a`$. In the expansion

```math
\mathbb E T^2
=\sum_{i,i',j,j'}a_i a_{i'}
\mathbb E[U_iU_{i'}V_jV_{j'}],
```

every term containing a singleton coordinate vanishes: that coordinate contributes a centered variable independent of the rest. The surviving index patterns are exactly the following.

| Index pattern | Total contribution |
|---|---|
| All four indices coincide | $`\sum_i a_i^2\kappa_i`$ |
| The two $`U`$ indices coincide, and the two $`V`$ indices coincide at a different coordinate | $`\tau(D-1)uv`$ |
| Two distinct coordinates each contain one $`U`$ and one $`V`$ | $`2\sum_{i\ne i'}a_i a_{i'}m_im_{i'}`$ |

The last sum is ordered. Its factor of two corresponds to the two ways to pair a $`U`$ with a $`V`$. Consequently,

```math
\boxed{
\mathbb E T^2
=\tau Duv+2M_a^2
+\sum_i a_i^2(\kappa_i-uv-2m_i^2).
}
```

Equivalently,

```math
\mathbb E T^2
=\tau(D-1)uv+\sum_i a_i^2\kappa_i
+2M_a^2-2\sum_i a_i^2m_i^2.
```

Using $`\sum_i a_i^2=\tau`$, $`\kappa_i\le v`$, and $`|M_a|\le\tau m_*`$ proves the uniform bound

```math
\boxed{
\mathbb E T^2\le
B:=\tau\bigl((D-1)u+1\bigr)v+2\tau^2m_*^2.
}
```

For a fixed challenge, subtraction of $`M_a^2`$ also gives

```math
\mathrm{Var}(T\mid c)
\le\tau\bigl((D-1)u+1\bigr)v+\tau^2m_*^2.
```

For random challenges, the bound used in the sequel is the **second-moment** bound $`B`$. It holds for every challenge and therefore also after averaging over them. Averaging only the conditional variances would omit $`\mathrm{Var}_c(\mathbb E[T\mid c])`$.

The pointwise range is

```math
|T|\le R:=\tau D\beta.
```

Indeed, $`|U_i|\le1`$, and $`|V_i|\le\beta`$ because $`g`$ takes values in $`[0,\beta]`$ and $`\mu`$ is its mean.

## 4. Averaging the challenge

The coefficients $`a_i`$ and shifts $`d_i`$ both depend on $`c`$; they must not be treated as independent. The needed calculation instead uses the exact symmetry $`c\mapsto-c`$. For a fixed block and coefficient,

```math
\mathbb E_c\!\left[
C(c)_{i,j}(-(cs_{2,b})_i)_+
\right]
=-\frac12\mathbb E_c\!\left[
C(c)_{i,j}(cs_{2,b})_i
\right].
```

This follows by pairing $`c`$ with $`-c`$ and using $`(-x)_+-(x)_+=-x`$. Uniform independent signs on the weight-$`\tau`$ support imply zero mixed second moments for distinct challenge coefficients and second moment $`\tau/n`$ for each individual coefficient. With the negacyclic signs included,

```math
\mathbb E_c[C(c)^{\mathsf T}C(c)]=\tau I_n,
\qquad
\mathbb E_c[C(c)_{i,j}]=0.
```

Thus the constant term in $`m_i`$ averages to zero and the comparison mean is

```math
\mathbb E T_{b,j}=-\frac{\tau}{2q}(s_{2,b})_j.
```

The [boundary-statistic page](boundary_statistic.md) derives this mean directly. Here it is combined with a variance bound that remains valid under the same challenge mixture.

## 5. Transfer to a fixed matrix

Assume $`A`$ satisfies the four-coordinate conclusion of [Theorem 1 in the fixed-matrix argument](fixed_matrix.md) with error $`\varepsilon`$ for the interior box of side $`L`$. That event has probability at least $`1-\zeta_4(\varepsilon)`$ over the single uniform matrix draw.

Conditional on $`P_z`$, the nonce is exactly $`Z-cs_1`$. The all-translations clause therefore applies simultaneously to every challenge and both fixed secrets. Applying the coordinate functions defining $`U_i,V_i`$ cannot increase total variation.

Each summand $`U_iV_j`$ of the mean uses at most two coordinates. Its range has length at most $`\beta`$. To check this constant, note that the product of the intervals $`[-p_0,1-p_0]`$ and $`[-\mu,\beta-\mu]`$ has range length at most $`\beta`$: its extrema occur at corners, and the difference of the relevant corners is one of $`p_0\beta`$, $`(1-p_0)\beta`$, $`\mu`$, or $`\beta-\mu`$. The assertion remains true if the two indices coincide.

For a function with range length $`K`$, changing its input law by total variation at most $`\varepsilon`$ changes its expectation by at most $`K\varepsilon`$. There are $`\tau D`$ nonzero summands, so, uniformly in the fixed challenge,

```math
\left|\mathbb E[T\mid P_z,c,A]-M_a\right|
\le\tau D\beta\varepsilon.
```

Every term in $`T^2`$ involves at most four distinct coordinates. Its absolute value is at most $`\beta^2`$, hence its range length is at most $`2\beta^2`$. At most $`\tau^2D^2`$ terms have nonzero coefficient. Therefore

```math
\mathbb E[T^2\mid P_z,c,A]
\le B+2\tau^2D^2\beta^2\varepsilon.
```

Both conclusions are uniform in the challenge, so they can be averaged over it. The probability $`p_z`$ is challenge-independent. With $`Q=\mathbf1[P_z]T`$, define

```math
\theta=\frac{p_z\tau}{2q},\qquad
V=p_z\left(B+2\tau^2D^2\beta^2\varepsilon\right),
\qquad R=\tau D\beta.
```

Then for every secret coefficient $`s_j`$—with its block index suppressed—

```math
\boxed{
\begin{aligned}
\mathbb E[Q_j\mid A]&=-\theta s_j+e_j,
&|e_j|&\le p_z\tau D\beta\varepsilon,\\
\mathrm{Var}(Q_j\mid A)&\le\mathbb E[Q_j^2\mid A]\le V,
&|Q_j|&\le R.
\end{aligned}
}
```

These are bounds on the actual conditional distribution for that fixed matrix. The argument does not replace an entire sequence of records by independent uniform product vectors or assume that the full vector $`Ay`$ is uniform.

## 6. A simultaneous finite-observation theorem

Let $`N`$ denote the number of independent **first-attempt records**, counting first-check rejections as zero-valued records and retaining accepted first-check-passing records as described above. Independence is conditional on the fixed matrix and secrets. The [model](model.md) states the fresh-message and nonce conditions under which these are the relevant records.

For each of the $`D`$ secret coefficients, let $`\overline Q_j`$ be the mean of its $`N`$ observed statistics and put

```math
\widehat s_j=-\frac{\overline Q_j}{\theta}.
```

### Theorem 2 — Finite-observation identification

Assume $`\tau\ge1`$, $`0<\delta<1`$, that the matrix satisfies the four-coordinate event, and that

```math
D\beta\varepsilon\le\frac{1}{16q}.
```

Set

```math
t_*:=\frac\theta4=\frac{p_z\tau}{8q},
\qquad
N_0:=
\frac{2V+(4/3)Rt_*}{t_*^2}
\ln\!\left(\frac{2D}{\delta}\right).
```

If $`N\ge\lceil N_0\rceil`$, then, with probability at least $`1-\delta`$ over the records,

```math
\max_{0\le j<D}|\widehat s_j-s_j|\le\frac38.
```

In particular, each integer coefficient is uniquely determined by nearest-integer rounding on this event. Including the matrix draw, the total failure probability is at most $`\delta+\zeta_4(\varepsilon)`$. The statistics for different coefficients need not be independent.

**Proof.** For one coefficient, center a record as $`Y=Q_j-\mathbb E Q_j`$. The bounds above give

```math
\mathbb E Y=0,\qquad
\mathbb E Y^2\le V,\qquad |Y|\le2R.
```

The last constant is $`2R`$, not $`R`$: both a record and its mean lie in $`[-R,R]`$. Bernstein's inequality with this normalization gives

```math
\Pr\!\left[
|\overline Q_j-\mathbb E Q_j|\ge t_*
\right]
\le
2\exp\!\left(
-\frac{Nt_*^2}{2V+(4/3)Rt_*}
\right).
```

The chosen $`N`$ makes this at most $`\delta/D`$. A union bound covers all coefficients without requiring independence between their statistics.

The systematic error after rescaling is bounded by

```math
\frac{|e_j|}{\theta}\le2qD\beta\varepsilon\le\frac18.
```

The sampling error after rescaling is at most $`t_*/\theta=1/4`$. Their sum is $`3/8<1/2`$, proving the assertion. Finally, union with the bad-matrix event adds at most $`\zeta_4(\varepsilon)`$. $`\square`$

### Checking the Bernstein constant

For clarity, the version just used follows directly from a bounded-variable moment-generating-function estimate. If $`\mathbb E Y=0`$, $`|Y|\le b`$, and $`\mathbb E Y^2\le V`$, then, for $`0<\lambda<3/b`$,

```math
\begin{aligned}
\mathbb E e^{\lambda Y}
&\le 1+\sum_{m\ge2}\frac{\lambda^m b^{m-2}V}{m!}\\
&\le\exp\!\left(
\frac{\lambda^2V}{2(1-\lambda b/3)}
\right).
\end{aligned}
```

The second line uses $`m!\ge2\cdot3^{m-2}`$ for $`m\ge2`$. Independence across records permits multiplication of these bounds. Exponential Markov with $`\lambda=t/(V+bt/3)`$, followed by the same argument for $`-Y`$, gives

```math
\Pr\!\left[\left|\frac1N\sum_{r=1}^NY_r\right|\ge t\right]
\le2\exp\!\left(-\frac{Nt^2}{2V+(2/3)bt}\right).
```

Taking $`b=2R`$ yields the denominator in Theorem 2.

## 7. Arithmetic substitution

For the parameter shapes from SUCRE's Table 2, use $`q=8380417`$, $`n=256`$, $`\varepsilon=2^{-128}`$, and $`\delta=0.01`$. [SUCRE] The common relation is $`\alpha=(q-1)/p`$.

| Shape | $`(k,\ell)`$ | $`\eta`$ | $`\tau`$ | $`\gamma_1`$ | $`p`$ | $`\beta`$ |
|---|---:|---:|---:|---:|---:|---:|
| 44 | $`(4,4)`$ | 2 | 39 | $`2^{17}`$ | 44 | 78 |
| 65 | $`(6,5)`$ | 4 | 49 | $`2^{19}`$ | 16 | 196 |
| 87 | $`(8,7)`$ | 2 | 60 | $`2^{19}`$ | 16 | 120 |

An equivalent expression useful for checking the substitution is

```math
N_0=
\left[
\frac{128q^2\left(B+2\tau^2D^2\beta^2\varepsilon\right)}
{p_z\tau^2}
+\frac{32qD\beta}{3p_z}
\right]
\ln\!\left(\frac{2D}{\delta}\right).
```

Here $`\ln`$ is the natural logarithm; the next table converts the resulting bound to base two. Values other than the integer powers of two are rounded for display.

| Shape | $`p_z`$ | $`B`$ | $`\log_2N_0`$ | Sufficient integer count |
|---|---:|---:|---:|---:|
| 44 | 0.5414714311 | 782.9488413 | 56.53874575 | $`2^{57}`$ |
| 65 | 0.6188909137 | 21510.6830008 | 60.51263497 | $`2^{61}`$ |
| 87 | 0.6623821841 | 8078.6502306 | 58.45099504 | $`2^{59}`$ |

The transfer correction $`2\tau^2D^2\beta^2\varepsilon`$ is included in these expressions. The normalized systematic-error bounds $`2qD\beta\varepsilon`$ are approximately $`3.94\times10^{-27}`$, $`1.49\times10^{-26}`$, and $`1.22\times10^{-26}`$, respectively, so the theorem's $`1/8`$ condition has ample margin. The corresponding matrix-exception bounds are given in [the fixed-matrix table](fixed_matrix.md#6-four-coordinate-bounds-at-the-stated-parameter-shapes).

These numbers were obtained by high-precision arithmetic substitution into the proved expressions. No transcript-generation experiment, secret-identification implementation, or measured success rate is used as evidence for the theorem.

## 8. What the bound establishes

The result is a finite-sample statistical identification theorem for the complete, noiseless observations specified by the [model](model.md), conditional on its independence and matrix-distribution assumptions. The count is per first-attempt record, not per selected low-part rejection. It includes both first-check rejections and accepted first-check-passing records.

The formula is polynomial in the numerical parameters and $`p_z^{-1}`$, with logarithmic dependence on the failure target. An asymptotic polynomial-time interpretation therefore requires those numerical parameters and $`p_z^{-1}`$ to be polynomially bounded in the security parameter. The expression is not polynomial in $`\log q`$ for arbitrary exponential $`q`$.

A bound on observations does not supply a device runtime, measurement accuracy, or a forgery for the compressed verification key of standardized ML-DSA. Those distinctions, along with the interpretation of repeated simulation, are addressed in [security scope](security_scope.md). This page provides the moments and concentration constants needed by that discussion.

## Source

[SUCRE] Sonia Belaïd et al., *ML-DSA masking sweetened with SUCRE: Shuffle-and-Unmask Countermeasure for REjection sampling*, TCHES 2026(1), corrected [ePrint 2026/2248](https://eprint.iacr.org/2026/2248), Section 2.5 and Table 2. The parameter shapes come from that source. The variance identities, fixed-matrix transfer, and sufficient observation counts on this page are derived here.
