# Local mathematical foundations

These notes supply the finite algebra and probability used by the [milestone map](MILESTONES.md). The [Boneh–Shoup bridge](ANCHOR.md) identifies the selected book's developed material on cryptographic security. The formal observation model and proofs remain in [science/](../science/README.md).

## Residues and integer representatives

Working modulo a positive integer $`q`$ identifies integers whose difference is divisible by $`q`$. A residue can be displayed by its representative in $`\{0,\ldots,q-1\}`$ or, for odd $`q`$, by its centered representative in

```math
\left\{-\frac{q-1}{2},\ldots,\frac{q-1}{2}\right\}.
```

For example, $`12`$ and $`-1`$ denote the same residue modulo $`13`$. They are different integers. A claim about the size of a secret coefficient must specify its integer representative.

When $`q`$ is prime, residues form the finite field $`\mathbb F_q`$: addition and multiplication are performed modulo $`q`$, and every nonzero residue has a multiplicative inverse. Linear equations over this field use modular arithmetic. Integer bounds such as $`|s_j|\le\eta`$ refer to the chosen small integer coefficients before reduction. If $`2\eta<q`$, each allowed integer has a distinct field image.

The low-part function $`L_\alpha`$ in this project uses its own rounding interval and endpoint convention. A centered field representative and a low rounding remainder are therefore separate definitions; the [model](../science/model.md#the-rounding-convention) specifies the latter.

## Negacyclic polynomials and module matrices

A polynomial in

```math
R_q=\mathbb F_q[X]/(X^n+1)
```

is stored by $`n`$ coefficients. Products are reduced using $`X^n=-1`$. A term that passes degree $`n-1`$ wraps around with a minus sign, which is the meaning of *negacyclic*.

For $`n=4`$ and $`q=13`$,

```math
X(2+X^3)=2X+X^4=-1+2X.
```

The output coefficient vector is $`(12,2,0,0)`$ over the field, or $`(-1,2,0,0)`$ using centered representatives.

The ring $`R_q`$ need not be a field. In the same example,

```math
(X^2-5)(X^2+5)=X^4-25=0\quad\text{in }R_{13}.
```

Both factors are nonzero. Such factors are called zero divisors, and they show why a nonzero polynomial need not define invertible multiplication.

A module vector is a list of polynomials. A $`k\times\ell`$ matrix over $`R_q`$ maps $`\ell`$ input polynomials to $`k`$ output polynomials by ordinary matrix multiplication with ring operations. In coefficient coordinates, it is a linear map

```math
\mathbb F_q^{M}\longrightarrow\mathbb F_q^{D},
\qquad M=\ell n,\quad D=kn.
```

This viewpoint lets the proof use field linear algebra while retaining the structured, negacyclic form of the matrix. Its rank and kernel have their usual field meanings.

## Rank, kernels, and uniform fibers

For a linear map $`T:\mathbb F_q^m\to\mathbb F_q^d`$, the **image** is the set of attainable outputs. The **rank** $`\rho`$ is the dimension of that image. The **kernel** is the set of inputs mapped to zero. Its dimension is $`m-\rho`$.

A *fiber* is the set of inputs giving one specified output. Every nonempty fiber of a linear map is a translate of the kernel and has $`q^{m-\rho}`$ elements. Thus a uniform input gives a uniform output on the image. It gives a uniform output on all of $`\mathbb F_q^d`$ exactly when $`\rho=d`$.

For example,

```math
T(x_1,x_2)=x_1+2x_2\quad\text{over }\mathbb F_{13}
```

has rank one. For each chosen output and each of the thirteen choices of $`x_2`$, exactly one $`x_1`$ works. Every output therefore has thirteen preimages among the $`169`$ inputs.

The [fixed-matrix proof](../science/fixed_matrix.md#4-collision-proof-of-theorem-1) applies this fact with the coefficients of the random matrix as inputs and a nonce difference held fixed. It then uses collision probabilities to obtain the stated exception bound for individual matrices. Uniformity on a linear map's image alone does not supply that later fixed-matrix conclusion for box-distributed nonces.

## Expectations, centering, and moments

For a finite random variable $`X`$, its expectation is the probability-weighted average

```math
\mathbb E X=\sum_x x\Pr[X=x].
```

Centering subtracts that average: $`X-\mathbb E X`$ has mean zero. The second moment is $`\mathbb E[X^2]`$, and the variance measures squared fluctuation around the mean:

```math
\mathrm{Var}(X)
=\mathbb E[(X-\mathbb E X)^2]
=\mathbb E[X^2]-(\mathbb E X)^2.
```

For two variables, covariance measures their centered joint fluctuation:

```math
\mathrm{Cov}(X,Y)
=\mathbb E[(X-\mathbb E X)(Y-\mathbb E Y)].
```

Independent centered variables have zero product mean. Centering alone does not make variables independent. The high-bin indicator and the residual weight at one coordinate are functions of the same hidden value, so the proof retains their nonzero covariance.

If a statistic is a sum of products, squaring it creates products of four factors. This is why the [concentration chapter](../science/concentration.md) needs mixed fourth moments and marginals involving at most four output coordinates. The second moment bounds the variance from above, which remains useful when the conditional mean itself changes with the challenge.

## Independence after conditioning

Conditioning means restricting to an event or fixing a variable, then renormalizing the remaining probabilities. For $`\Pr[E]>0`$,

```math
\Pr[B\mid E]=\frac{\Pr[B\cap E]}{\Pr[E]}.
```

Independence must always be stated relative to the randomness still being sampled. A simple example makes the distinction visible. Draw one fair sign $`S`$, and set $`X_1=S`$ and $`X_2=S`$. Conditional on $`S`$, both outputs are fixed and their joint law is the product of their point-mass laws. Without conditioning, however,

```math
\Pr[X_1=1,X_2=1]=\frac12,
\qquad
\Pr[X_1=1]\Pr[X_2=1]=\frac14.
```

The shared hidden variable creates dependence in the averaged experiment.

In this project, the public matrix and secrets are held fixed across records. Fresh nonces and fresh oracle challenge inputs give independent first-attempt records conditional on those fixed objects. Coordinates within a record have a different dependence structure. The proof first establishes a good-matrix event, then applies concentration conditional on that matrix and the secrets. The matrix-exception probability is paid once.

Conditioning on the first norm check also changes a nonce's distribution. The [model's translated-box calculation](../science/model.md#exact-conditioning-on-the-first-check) derives that distribution exactly, including its pass probability.

## Statistical distance and observable means

For distributions $`P,Q`$ on the same finite set, total variation distance is

```math
\mathrm{TV}(P,Q)=\frac12\sum_x|P(x)-Q(x)|.
```

It equals the largest difference in the probability of an event. Thus it controls all tests of the sample, including tests with unlimited computational power. Computational indistinguishability restricts the tests by their allowed resources and inputs; those restrictions are part of the security definition.

If a real-valued function $`f`$ takes values in an interval of width $`b`$, then

```math
|\mathbb E_P f-\mathbb E_Q f|
\le b\,\mathrm{TV}(P,Q).
```

To see this, subtract the lower endpoint and divide by $`b`$ when $`b>0`$. The resulting function lies in $`[0,1]`$; weighting the positive and negative parts of $`P-Q`$ by numbers in that interval bounds the expectation difference by their common total mass, which is the total variation distance. A constant function has zero difference.

This is the bridge from small-marginal approximation to observable means. Applying a deterministic function to both distributions also cannot increase total variation: each output event is the preimage of an input event. The proof uses these facts on the specific coordinate functions appearing in its moments.

## The bounded public-key relation

The full public relation is

```math
t=As_1+s_2\pmod q,
\qquad
\|s_1\|_\infty,\|s_2\|_\infty\le\eta.
```

The infinity norm is the largest absolute integer coefficient. The observer receives the public matrix and vector; both bounded secret vectors are initially unknown.

Without coefficient bounds, the ring equation has many easy solutions: choose $`s_1`$ and set $`s_2=t-As_1`$. The cryptographic search problem requires a solution with **both** vectors small. Its hardness is an explicit assumption for the stated distribution, not a consequence of the equation's appearance.

If the correct $`s_2`$ is supplied and $`A`$ is injective, solving $`As_1=t-s_2`$ becomes linear algebra. This explains the statistical theorem's role in the [full-key consequence](../science/security_scope.md#2-full-key-identification-and-matrix-rank).

A proposed bounded pair can be verified publicly by checking its bounds and the equation. That check accepts any valid bounded witness. It does not need to know which pair the original key generator sampled. The [simulation argument](../science/security_scope.md#3-a-publicly-verifiable-search-problem) uses exactly this publicly testable event.

## Continue through the project

The [worked introduction](README.md) applies these ideas to a scalar rounding count. The [milestone map](MILESTONES.md) then organizes the full proof, and the [anchor bridge](ANCHOR.md) connects its security language to Boneh–Shoup. The canonical statements retain their precise observation models, exception probabilities, and resource assumptions.
