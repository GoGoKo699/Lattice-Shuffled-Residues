# A boundary count with a linear secret mean

The histogram retains how often each residual value occurs. Usually, combining one such count with a public high coefficient produces only a small correlation. The rounding convention makes that correlation exactly computable. Averaging it against the signed challenge removes its nonlinearity and leaves a linear function of the secret.

All notation and observation assumptions are fixed in the [model](model.md).

## Scalar preimages

Set $`a=\alpha/2`$ and

```math
p_0=\frac{\alpha+1}{q}.
```

The zero high bin is the interval $`[-a,a]`$ represented modulo $`q`$. For every ordinary low value $`r\in(-a,a]`$, its $`p`$ distinct preimages are

```math
x_j=\alpha j+r\pmod q,\qquad 0\le j\lt p.
```

The exceptional low value $`-a`$ has the unique preimage $`q-a`$. These facts can be checked directly in the definition of $`L_\alpha`$; they also account for all $`p\alpha+1=q`$ residues.

Fix an integer shift $`d`$ with $`|d|\le\beta\lt a`$, and choose $`1\le v\le\beta`$. The event $`L_\alpha(w-d)=-a+v`$ has preimages

```math
w_j=\alpha j-a+v+d\pmod q,\qquad 0\le j\lt p.
```

Put $`s=-a+v+d`$. Since $`-2a\lt s\lt a`$, only $`j=0`$ and $`j=1`$ can lie in the zero high bin. The former lies there exactly when $`s\ge-a`$; the latter exactly when $`s\le-a`$. Both occur precisely when $`s=-a`$, or $`d=-v`$. Every other $`j`$ lies outside that bin.

### Boundary-count identity

For uniform $`w\in\mathbb F_q`$,

**(B1)**

```math
\Pr\{H(w)=0,\ L_\alpha(w-d)=-a+v\}
=\frac{1+\mathbf1_{\{d=-v\}}}{q},
```

whereas

**(B2)**

```math
\Pr\{L_\alpha(w-d)=-a+v\}=\frac pq.
```

The extra joint preimage occurs at a shifted rounding endpoint. It is not an inference about an unknown permutation.

## Weighting the boundary values

Define a function on low values by

```math
g(r)=
\begin{cases}
v,&r=-a+v,\quad 1\le v\le\beta,\\
0,&\text{otherwise}.
\end{cases}
```

Write

```math
S_1=\frac{\beta(\beta+1)}2,
\qquad
S_2=\frac{\beta(\beta+1)(2\beta+1)}6,
\qquad
\mu=\frac pqS_1,
\qquad
K=\frac{(p-1)S_1}{q^2}.
```

Let $`f(w)=\mathbf1_{\{H(w)=0\}}-p_0`$. Equations (B1) and (B2) give

```math
\mathbb E\,g(L_\alpha(w-d))=\mu,
\qquad
\mathbb E[\mathbf1_{\{H(w)=0\}}g(L_\alpha(w-d))]
=\frac{S_1+(-d)_+}{q}.
```

Subtracting the product of the marginal means yields

**(B3)**

```math
\boxed{
\mathbb E[f(w)(g(L_\alpha(w-d))-\mu)]
=\frac{(-d)_+}{q}-K.
}
```

Here $`x_+=\max(x,0)`$. The constant term follows from $`p\alpha=q-1`$. This count is elementary arithmetic of the standard decomposition; the statistical use of it is the point of the construction.

## From a histogram to an indexed correlation

For the whole residual vector let

```math
F=\sum_{j=0}^{D-1}g(r_j),
\qquad F_c=F-D\mu.
```

The value of $`F`$ is a weighted histogram count and is unchanged by any permutation, including a permutation mixing different module blocks.

Temporarily use the comparison law in which the coordinates of $`w`$ are independent and uniform, conditional on $`c`$. Write $`d=cs_2`$ and $`f_i=\mathbf1_{\{h_i=0\}}-p_0`$. For a fixed coordinate $`i`$,

**(B4)**

```math
\mathbb E[f_iF_c\mid c]
=\frac{(-d_i)_+}{q}-K.
```

Indeed, every off-diagonal term in $`f_i\sum_j(g(r_j)-\mu)`$ has zero expectation by independence of the two coordinates and their centered marginal means. The remaining term is (B3).

No location for a particular residual value is identified. The indexed high coefficient selects its own same-coordinate contribution in expectation, while the other histogram entries add variance.

## Challenge symmetry

Let $`C(c)`$ be the $`n\times n`$ integer matrix of multiplication by $`c`$ in $`R`$. Every column has exactly $`\tau`$ entries in $`\{-1,1\}`$. For a fixed output module block $`b`$ and secret coefficient $`j`$, define

**(B5)**

```math
T_{b,j}
=F_c\sum_{i=0}^{n-1}C(c)_{i,j}f_{bn+i}.
```

Under the comparison law, (B4) gives

```math
\mathbb E[T_{b,j}\mid c]
=\sum_i C(c)_{i,j}
\left(\frac{(-(cs_{2,b})_i)_+}{q}-K\right).
```

The challenge distribution is invariant under $`c\mapsto-c`$. Both $`C(c)_{i,j}`$ and $`(cs_{2,b})_i`$ change sign under this map. Therefore

**(B6)**

```math
\mathbb E_c[C(c)_{i,j}(-(cs_{2,b})_i)_+]
=-\frac12\mathbb E_c[C(c)_{i,j}(cs_{2,b})_i].
```

To see the sign, average the expression for $`c`$ with that for $`-c`$ and use $`(-x)_+-x_+=-x`$.

For signed weight-$`\tau`$ challenges,

**(B7)**

```math
\mathbb E[c_u c_v]=\frac{\tau}{n}\mathbf1_{\{u=v\}},
\qquad
\mathbb E[C(c)^TC(c)]=\tau I_n.
```

The first identity follows by conditioning on the support and averaging the independent signs. Each row of $`C(c)`$ is a signed permutation of the coefficient vector, so summing its covariance over the $`n`$ rows proves the second. Also $`\mathbb E C(c)=0`$.

Combining (B6) and (B7) cancels the constant $`K`$ and gives the exact comparison mean:

**(B8)**

```math
\boxed{
\mathbb E T_{b,j}
=-\frac{\tau}{2q}(s_{2,b})_j.
}
```

The identity holds for every secret with the stated coefficient bound. It identifies a signed coefficient with a known scale; there is no unknown global sign or normalization.

## Visibility and rejection

Each selected residual value is negative and satisfies

```math
|-a+v|=a-v\ge a-\beta.
```

Consequently any positive selected count forces the low-part norm check to reject. If an attempt passes that check, $`F=0`$ exactly. When the histogram of an accepted attempt is omitted, the centered count remains known:

```math
F_c=-D\mu.
```

The statistic must retain this centered contribution on accepted attempts whose first check passed. Omitting those records would change its mean. On a first-check rejection, define the entire observation statistic to be zero:

**(B9)**

```math
Q_{b,j}=\mathbf1_{P_z}T_{b,j}.
```

This convention requires neither an unavailable low vector nor conditioning on the final rejection event.

## Transfer to the actual fixed matrix

The comparison law is a device for computing moments. The actual distribution is $`w=A(Z-cs_1)`$ after the first check. The [fixed-matrix theorem](fixed_matrix.md) supplies an event on which every two-coordinate marginal is within $`\varepsilon`$ of uniform, simultaneously for every translation.

Expand (B5) into at most $`\tau D`$ summands, each a product $`f_i(g(r_j)-\mu)`$ involving at most two output coordinates. Its range has width at most $`\beta`$. One way to see this is to let the negative and positive extents of $`f_i`$ be $`u_-,u_+`$, with sum one, and those of $`g-\mu`$ be $`v_-,v_+`$, with sum $`\beta`$. The width of the product range is at most

```math
(u_-+u_+)(v_-+v_+)=\beta.
```

The expectation of a function of range width $`b`$ changes by at most $`b\varepsilon`$ under total variation distance $`\varepsilon`$. Therefore, for every such fixed matrix and every pair of bounded secrets,

**(B10)**

```math
\left|
\mathbb E[Q_{b,j}\mid A,s_1,s_2]
+\frac{p_z\tau}{2q}(s_{2,b})_j
\right|
\le p_z\tau D\beta\varepsilon.
```

The challenge remains uniform after the first check, and its conditional nonce is a translated box, as proved in the [model](model.md#exact-conditioning-on-the-first-check). Thus the same good-matrix event applies throughout the challenge average.

Equation (B10) is the main observable mean. The [second-moment and concentration analysis](concentration.md) controls the observations needed to separate adjacent integer coefficients.
