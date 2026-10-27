# Learning route

The selected educational anchor is **Dan Boneh and Victor Shoup, [A Graduate Course in Applied Cryptography](https://toc.cryptobook.us/), version 0.6 (January 2023)**. It supplies the language of security games, indistinguishability, signatures, and simulation. The project supplies the specific rounding, finite-field, and moment arguments.

The route has **30 milestones: 10 foundations followed by 20 stages of the scientific argument**. Start with the example below, use the [local foundations](FOUNDATIONS.md) for the required algebra and probability, consult the [anchor bridge](ANCHOR.md) for targeted source sections and notation, and follow the [milestone map](MILESTONES.md) for the complete path. Each milestone states a conceptual target, its dependencies, and the relevant scientific sources. The [scientific overview](../science/README.md) remains the direct route to the formal results.

## A shuffle preserves counts

Consider four residual values:

```math
(-2,0,-2,1)
\quad\longrightarrow\quad
(-2,-2,1,0).
```

The order changes, but the number of occurrences of $`-2`$ remains two. A histogram records that count without identifying the coordinates that produced it.

The project studies such counts together with another observation that retains its coordinate labels: the commitment's high coefficients. The two observations come from the same underlying attempt. Their joint distribution can therefore carry information that neither marginal reveals by itself.

## A complete small counting example

Work modulo $`13`$: integers differing by a multiple of $`13`$ represent the same residue. Let the hidden residue $`w`$ be equally likely to be any of $`0,1,\ldots,12`$. Choose $`\alpha=6`$ and $`a=\alpha/2=3`$. The project's rounding rule splits a residue into a coarse bin $`H(w)`$ and a signed remainder $`L_\alpha(w)`$:

```math
w=6H(w)+L_\alpha(w)\pmod{13}.
```

The [exact endpoint convention](../science/model.md#the-rounding-convention) gives

```math
\{w:H(w)=0\}=\{0,1,2,3,10,11,12\},
```

and the remainder $`-2`$ has two preimages, $`4`$ and $`11`$. Thus the high bin is zero with probability $`7/13`$.

Now shift the value before taking its low part:

```math
r=L_\alpha(w-d).
```

Here $`d`$ is a small integer shift. The following table enumerates every value of $`w`$ that produces the selected residual.

| Shift $`d`$ | Values of $`w`$ giving $`r=-2`$ | Those also satisfying $`H(w)=0`$ | Joint probability |
|---|---|---|---:|
| $`-1`$ | $`3,10`$ | $`3,10`$ | $`2/13`$ |
| $`0`$ | $`4,11`$ | $`11`$ | $`1/13`$ |
| $`1`$ | $`5,12`$ | $`12`$ | $`1/13`$ |

For every row, the residual equals $`-2`$ with probability $`2/13`$. Its marginal distribution at that value does not distinguish these shifts. The joint event with the zero high bin does: at $`d=-1`$, both preimages land in that bin.

Center the two indicators by subtracting their means:

```math
U=\mathbf1_{\{H(w)=0\}}-\frac7{13},
\qquad
V=\mathbf1_{\{r=-2\}}-\frac2{13}.
```

An indicator is one when its stated event occurs and zero otherwise. Centering gives $`\mathbb E U=\mathbb E V=0`$. Multiplying and averaging gives

```math
\mathbb E[UV]
=\Pr[H(w)=0,\ r=-2]-\frac7{13}\frac2{13}.
```

The value is $`12/169`$ for $`d=-1`$ and $`-1/169`$ for the other two rows. The difference is caused by one extra joint preimage. This is the scalar mechanism proved in [Boundary statistic](../science/boundary_statistic.md#boundary-count-identity).

## From one coordinate to a histogram

In the independent-coordinate comparison law, multiply a centered high-bin indicator at coordinate $`i`$ by a centered sum of residual counts. Its same-coordinate term has the correlation just illustrated. Every other term has expectation zero because it is a product of independent centered variables. The whole histogram therefore retains the desired local correlation in expectation, while the other coordinates contribute to its variance.

The complete statistic weights several boundary values and averages against the signed challenge. Challenge symmetry converts the shift dependence into a linear secret mean. The [boundary chapter](../science/boundary_statistic.md) derives that identity.

The genuine commitment coordinates are related through the same fixed matrix. The next part of the proof establishes the approximation needed to use the comparison calculation. It controls only the small marginals that occur in the first and second moments. The good-matrix event has probability at least $`1-\zeta_4(\varepsilon)`$, with the parameter-dependent exception explicitly bounded in the [fixed-matrix theorem](../science/fixed_matrix.md).

## How the milestones assemble the result

| Milestones | Scientific purpose |
|---|---|
| **M01–M10** | Build the arithmetic, probability, observation, and security framework; finish with the complete experiment and its three different distributions. |
| **M11–M14** | Derive the boundary correlation, preserve the correct centered contribution after rejection checks, average the challenge, and identify the translated nonce box. |
| **M15–M18** | Connect sparse multiplication rank, box intersections, and collision probabilities to one good matrix working for every required translation. |
| **M19–M23** | Calculate the mixed moments, transfer them to genuine records, and convert them into a simultaneous finite-observation guarantee. |
| **M24–M27** | Complete the full algebraic key when the matrix is injective, validate any bounded witness, and understand the precise repeated-simulation consequence. |
| **M28–M30** | Place the separate replacement-marginal repair, complete resource costs, prior work, and scientific limits into the whole argument. |

The last step connects the information available to the observer, the statistical theorem for that information, and the computational assumption used by the simulation consequence. Full public keys, compressed keys, and physical trace interfaces provide different resources; the [security chapter](../science/security_scope.md) states the implications for each.

## Sources and verification

The [anchor bridge](ANCHOR.md) identifies the relevant portions of the selected book and the additional material supplied locally. The primary research papers remain in the [related-work account](../references/RELATED_WORK.md); they serve attribution and specialist verification.

The scalar table above is an instance of the finite distributions checked by [check_identities.py](../verification/check_identities.py). The [verification guide](../verification/README.md) explains the finite domains, expected output, and relation between those checks and the analytical proofs.
