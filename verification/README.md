# Verification

The repository combines analytical proofs with finite arithmetic checks. The script checks identities that are easy to mis-normalize, signs introduced by negacyclic multiplication, and the numerical scale of the stated bounds.

## Run

Use Python 3.11 or later. Only the standard library is required.

```bash
python3 verification/check_identities.py
```

Run this command from the repository root. All checks use assertions and must complete without an assertion failure. The script prints a JSON summary and writes the same summary to [results.json](results.json). No external data, network access, package installation, or random seed is required.

## What is checked

| Check | Finite domain | Claim supported |
|---|---|---|
| Rounding fibers and scalar covariance | 16 rounding parameter pairs over moduli 13, 17, 29, 41, and 61; 1,210 boundary joint counts | The exceptional low value has one preimage, ordinary low values have $`p`$, and the selected high/low joint count has the stated extra preimage. |
| Replacement marginal and local repair | Exact rational probabilities in the same scalar domains | The specified dummy-shift example has the predicted probability deficit; conditional-preimage sampling restores the uniform-scalar high marginal. |
| Sparse negacyclic rank | 7,264 nonzero polynomials over $`(n,q)=(4,3),(4,5),(8,3)`$ | Multiplication rank is at least $`\lceil n/s\rceil`$ when the polynomial has support size $`s`$. |
| Signed challenge covariance | All 24 signed weight-two challenges at degree four | $`\mathbb E[C(c)^TC(c)]=\tau I`$, including the negacyclic signs. |
| Mixed fourth moment | Three cases with 33,643 independent-coordinate tuples in total | Direct exact enumeration agrees with the second-moment expansion, including within-coordinate correlation and all off-diagonal terms. |
| Analytical parameter substitution | Three ML-DSA parameter shapes, using 80-digit decimal arithmetic | The stated observation exponents and bad-matrix exponents follow from the displayed formulas and include the finite-marginal transfer correction. |

The scalar and moment checks use integer arithmetic and exact rational numbers. The parameter substitutions use Python's `decimal` module. The output records a concise summary; the script itself specifies every finite domain.

## Expected scale

| Shape | $`\log_2 N_0`$ | Sufficient power of two | $`\log_2\zeta_4(2^{-128})`$ |
|---|---:|---:|---:|
| 44 | 56.5387457497 | $`2^{57}`$ | −4157.38203034 |
| 65 | 60.5126349683 | $`2^{61}`$ | −5947.08755719 |
| 87 | 58.4509950444 | $`2^{59}`$ | −8505.45049111 |

These counts refer to independent first-attempt observations, including first-check failures and the centered contribution from accepted attempts. They are sufficient bounds from the theorem, not empirical estimates.

## How to read the evidence

Finite enumeration detects arithmetic mistakes in the stated identities and their implementation. It cannot prove the general sparse-rank lemma, the all-translations fixed-matrix theorem, or the concentration theorem for arbitrary dimensions. Those proofs are in [fixed_matrix.md](../science/fixed_matrix.md) and [concentration.md](../science/concentration.md).

The script enumerates scalar distributions and abstract matrices. It does not generate signatures, collect device traces, or run an end-to-end key-identification experiment. Consequently the recorded output is evidence for the mathematical identities and resource substitutions only. The [security scope](../science/security_scope.md) states the additional information and assumptions needed for the cryptographic consequence.

## Formula map

- `scalar_checks` corresponds to equations (B1)–(B3) in [Boundary statistic](../science/boundary_statistic.md) and the uniform-scalar comparison in [Replacement marginal](../science/sampler_marginal.md).
- `sparse_rank_checks` corresponds to Lemma 2 of [Fixed public matrix](../science/fixed_matrix.md).
- `challenge_covariance_check` corresponds to equation (B7) of [Boundary statistic](../science/boundary_statistic.md).
- `fourth_moment_checks` corresponds to the exact second-moment expansion in [Concentration](../science/concentration.md).
- `resource_bounds` evaluates the sufficient observation count and the four-coordinate bad-matrix bound in [Concentration](../science/concentration.md).
