# Lattice Shuffled Residues

## What survives a shuffle?

A shuffle hides which coordinate produced a value. It preserves the histogram of those values. This project proves that a histogram of rounding residuals can remain correlated with indexed commitment information across attempts made under one fixed lattice-signature key.

The setting is an explicitly enlarged observation model: each recorded first attempt reveals a public challenge, indexed commitment high bits, the first norm-check outcome, and the residual histogram when that check is reached. The histogram can be omitted on accepted attempts because the boundary counts used here are then known to be zero. The [model](science/model.md) states these resources and the exact rounding convention.

The main result is an analytical identification theorem for the bounded error secret $`s_2`$. Its proof works with **one public matrix sampled once and reused**, and with the nonce distribution obtained after conditioning on the first rejection check. A separate reduction explains the resulting obstruction to simulating many such views from a full public key.

## Principal results

| Result | Content | Authoritative account |
|---|---|---|
| A secret-dependent histogram correlation | A weighted boundary count, paired with indexed high bits and a signed challenge, has an exactly linear secret mean under the independent-coordinate comparison law. | [Boundary statistic](science/boundary_statistic.md) |
| A theorem for one fixed matrix | With probability at least $`1-\zeta_4(\varepsilon)`$, one uniform module matrix controls every marginal of at most four output coefficients, simultaneously for all translations of the relevant product box. The exception bound is explicit. | [Fixed-matrix theorem](science/fixed_matrix.md) |
| A finite observation guarantee | Exact mixed moments and Bernstein's inequality give an explicit sufficient count for simultaneous integer identification of all coefficients of $`s_2`$. | [Concentration](science/concentration.md) |
| A simulation consequence | With the full public key and a full-column-rank matrix, the statistical result yields a publicly verifiable bounded witness. A computationally indistinguishable simulator for the joint repeated view would therefore solve that search problem. | [Security scope](science/security_scope.md) |
| A separate one-transcript discrepancy | The replacement distribution in the corrected SUCRE assumption has an exact scalar probability deficit. A conditional-preimage construction repairs the uniform-scalar marginal. | [Replacement marginal](science/sampler_marginal.md) |

### The observable mean

Let $`D=kn`$ be the number of residual coefficients, $`\tau`$ the signed challenge weight, $`\beta=\eta\tau`$ the challenge–secret product bound, and $`p_z`$ the first-check pass probability. The observable statistic $`Q_{b,j}`$ is zero on first-check failures and retains its centered contribution on accepted attempts. Under the independent-coordinate comparison law,

```math
\mathbb E Q_{b,j}
=-\frac{p_z\tau}{2q}(s_{2,b})_j.
```

For the actual fixed matrix, on the good-matrix event of the theorem,

```math
\left|
\mathbb E[Q_{b,j}\mid A,s_1,s_2]
+\frac{p_z\tau}{2q}(s_{2,b})_j
\right|
\le p_z\tau D\beta\varepsilon.
```

The histogram need never be assigned back to individual residual coordinates. Averaging against the signed challenge converts the surviving correlation into a linear function of the secret.

### Why small marginals suffice

Conditional on the first check passing, the nonce is uniform on a translated product box of side length

```math
L=2(\gamma_1-\beta)-1.
```

For a fixed set $`I`$ of $`r`$ output positions, the proof establishes

```math
\mathbb E_A\mathrm{TV}
\bigl((AZ)_I,U(\mathbb F_q^r)\bigr)^2
\le
\frac{q^r(q^r-1)}
{4(q-1)L^{\ell\lceil n/r\rceil}}.
```

A union bound controls every such marginal for the same matrix; translation preserves its distance from uniform. Two-coordinate marginals control the mean, and four-coordinate marginals control the second moment. The complete output vector need not be close to uniform.

## Quantitative scale

The following substitutions use $`n=256`$, $`q=8380417`$, the indicated ML-DSA parameter shapes, marginal tolerance $`\varepsilon=2^{-128}`$, and conditional statistical failure target $`\delta=0.01`$. They are conservative **sufficient analytical counts of independent first-attempt records** in the stated observation model.

| Shape | $`(k,\ell)`$ | $`(\eta,\tau)`$ | First-check pass probability | $`\log_2 N_0`$ | Sufficient count |
|---|---:|---:|---:|---:|---:|
| 44 | $`(4,4)`$ | $`(2,39)`$ | 0.54147 | 56.53875 | $`2^{57}`$ |
| 65 | $`(6,5)`$ | $`(4,49)`$ | 0.61889 | 60.51263 | $`2^{61}`$ |
| 87 | $`(8,7)`$ | $`(2,60)`$ | 0.66238 | 58.45100 | $`2^{59}`$ |

At these counts, every rescaled coefficient estimate is within $`3/8`$ of its integer target, with failure probability at most $`\delta+\zeta_4(\varepsilon)`$. The base-two logarithms of the bad-matrix bounds $`\zeta_4`$ are approximately $`-4157.38`$, $`-5947.09`$, and $`-8505.45`$, respectively. These probabilities concern recovery of $`s_2`$ in the mathematical observation model. Completion of the full algebraic key adds the separate matrix-rank exception described in [Security scope](science/security_scope.md#2-full-key-identification-and-matrix-rank).

The counts are enormous and are not estimates of optimal sample complexity or practical device-attack cost. The theorem is polynomial in the numerical modulus and the stated parameters, including $`p_z^{-1}`$; it does not assert polynomial dependence on $`\log q`$ for arbitrary growing moduli.

## Reading routes

Start with the [scientific overview](science/README.md) for the complete argument and its dependencies.

- **Learn the project:** [Worked introduction](learning/README.md) → [Boneh–Shoup bridge](learning/ANCHOR.md) → [30-milestone map](learning/MILESTONES.md).
- **Understand the observation:** [Model](science/model.md) → [Boundary statistic](science/boundary_statistic.md).
- **Check the proof:** [Fixed matrix](science/fixed_matrix.md) → [Moments and concentration](science/concentration.md) → [Security consequence](science/security_scope.md).
- **Audit the source comparison:** [Replacement marginal](science/sampler_marginal.md) → [Related work and versions](references/RELATED_WORK.md).
- **Reproduce the finite checks:** [Verification guide](verification/README.md) and [recorded output](verification/results.json).

The [structured bibliography](references/references.bib) records primary sources and distinct paper versions. [llms.txt](llms.txt) maps questions to their authoritative pages.

The single educational anchor is **Boneh and Shoup, A Graduate Course in Applied Cryptography, version 0.6 (January 2023)**. The learning route uses selected sections and locally supplied derivations. Its ten foundation milestones assemble the experiment; twenty further milestones develop the mechanism, proof, and security consequence.

## Reproduction

From the repository root, with Python 3.11 or later:

```bash
python3 verification/check_identities.py
```

The standard-library script checks small exact rounding distributions, sparse negacyclic multiplication ranks, challenge covariance, mixed fourth moments, the repaired scalar marginal, and high-precision substitutions into the analytical bounds. It writes [verification/results.json](verification/results.json). The [verification guide](verification/README.md) explains how these finite calculations support the proofs and which claims remain analytical.

## Scope and attribution

The observation model follows the enlarged shuffled view used in the proof of [SUCRE, corrected ePrint 2026/2248](https://eprint.iacr.org/2026/2248). It grants more information than an unspecified physical probe or noisy trace. The fixed-matrix theorem assumes an ideal uniform matrix and independent box nonces; a seeded implementation requires its own randomness model. The full-key consequence uses $`t=As_1+s_2`$, whereas standard compressed verification keys reveal less.

Earlier work already combines shuffled information with indexed public data and accumulates it across signatures sharing a secret. The closest comparator is [Bronchain et al., Section 6](https://eprint.iacr.org/2023/1545). The contribution developed here is the residual/high-bit statistic, its translated-box fixed-matrix proof, quantitative concentration, and the resulting precisely scoped simulation statement. The [related-work account](references/RELATED_WORK.md) records two recent papers for which the full-text overlap comparison remains incomplete.

The scalar replacement discrepancy and the repeated-view result have separate logical roles. A false indistinguishability premise can make a conditional security statement inapplicable; it does not by itself falsify the implication. Repairing the scalar marginal also leaves the repeated-view simulation question open. These distinctions are developed in [Security scope](science/security_scope.md) and [Replacement marginal](science/sampler_marginal.md).

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
