# Related work and scope of comparison

**Sources checked:** 27 October 2026. Bibliographic keys refer to [references.bib](references.bib). The comparison distinguishes observation models, mathematical conclusions, and the hypotheses needed for simulation under a reused key.

## 1. Contribution and observation model

This project proves a correlation theorem for **anonymous residual histograms combined with indexed commitment high bits under a reused signing key**. In the [observation model](../science/model.md), the residual vector is

```math
r=\mathrm{LowBits}(w-cs_2),
```

and the indexed information includes $`h=\mathrm{HighBits}(w)`$, the challenge $`c`$, and the first-check outcome. The histogram is available on the specified rejected attempts. Selected boundary counts are also determined on accepted attempts, where they vanish.

The [boundary statistic](../science/boundary_statistic.md) has an exact secret-dependent mean under the uniform comparison law. The [fixed-matrix theorem](../science/fixed_matrix.md) controls the required small marginals for one matrix reused across records, uniformly over translations of the nonce box. The [concentration theorem](../science/concentration.md) transfers the moments and gives a finite-observation identification guarantee. The [security analysis](../science/security_scope.md) derives a conditional obstruction to public-key-only simulation of repeated augmented transcripts. A separate [replacement-marginal calculation](../science/sampler_marginal.md) identifies a discrepancy in the corrected SUCRE replacement rule and explains the limits of a local repair.

The scalar decomposition arithmetic, permutation-invariant inference, and accumulation across signatures are inherited ingredients. The contribution is their specific residual/high-bit application with a fixed-matrix guarantee and quantified simulation consequence. Its scope includes the stated branch visibility, conditioning, challenge distribution, and matrix event. The analytical observation counts concern the augmented transcript model; they are not practical physical-trace estimates.

## 2. Closest attack: Bronchain et al. (BAE+24)

[BAERS24](https://eprint.iacr.org/2023/1545), *Exploiting Small-Norm Polynomial Multiplication with Physical Attacks*, is the closest methodological comparator. In Section 6, pp. 377–378, equation (27) aggregates coefficient likelihoods from a shuffled nonce without observing the permutation. Equation (28) combines this anonymous information with each indexed public response coefficient $`z_i`$, obtaining likelihoods for $`(cs)_i=z_i-y_i`$. These initialize belief propagation across signatures sharing a secret. The section credits earlier generic shuffling analysis. Section 5 separately studies rejected attempts using nonce leakage and acceptance information.

| Aspect | BAE+24, Section 6 | Present result |
|---|---|---|
| Anonymous observation | Noisy information about shuffled nonce coefficients | Residual histogram on the specified rejected attempts |
| Indexed observation | Full public response coefficients $`z_i`$ | Commitment high bits $`h_i`$ |
| Processing | Anonymous likelihoods, then a factor graph | Exact boundary moments and finite-marginal estimates |
| Repeated secret | Information combines across signatures | One signing key and one public matrix remain fixed |
| Mathematical distinction | Anonymous inference without reconstructing the shuffle | Residual/high-bit identification and a conditional simulation obstruction |

Anonymous shuffled inference and shared-key accumulation are therefore established prior art. The distinction here is the observed residual/high-bit pair and the quantitative theorem for that pair under one fixed matrix.

## 3. Other attacks and their observation models

[Pessl16](https://eprint.iacr.org/2017/033), *Analyzing the Shuffling Side-Channel Countermeasure for Lattice-Based Signatures*, predates BAE+24. The author's [INDOCRYPT slides](https://pessl.cc/slides/indocrypt16.pdf), slides 16–19, explain how a leak-free shuffle can still leave Gaussian samples assignable to indexed BLISS responses, especially in the tails. This yields secret-dependent relations through likely coordinate associations. BAE+24's anonymous likelihood aggregation is the closer predecessor to the present statistic.

[ZWSY25](https://eprint.iacr.org/2025/214), *Rejected Signatures' Challenges Pose New Challenges*, derives indexed constraints and an integer-linear-programming formulation. Its Theorems 1–2 use rejected response coefficient values **and their positions**, together with the challenge. Those positions are a substantive resource absent from an anonymous residual histogram. Its discussion of shuffling is tied to this indexed observation model.

[LiuEtAl25](https://eprint.iacr.org/2025/582), *Release the Power of Rejected Signatures*, describes in its abstract a common soft-analytical side-channel factor graph using accepted and rejected leakage. It supplies further prior context for the value of rejected attempts. The comparison here is limited to that abstract and does not establish theorem-level non-overlap with the complete paper.

## 4. The strong-HVZK hypothesis: DFPS versus SUCRE

### DFPS includes the witness

The original four-author [DFPS23](https://doi.org/10.1007/978-3-031-38554-4_11) full version uses **Definition 7, p. 19**. The five-author revision of 14 May 2024 [DFPSX24](https://eprint.iacr.org/2023/245) uses **Definition 10, p. 23**. For statement/witness pairs $`(x,y)\in R`$, a protocol $`((P_1,P_2),(V_1,V_2))`$ is $`(\varepsilon_{\mathrm{zk}},T)`$-sc-HVZK if a simulator of runtime at most $`T`$ satisfies, for every polynomial-time distinguisher $`D`$ and every $`(x,y)\in R`$,

```math
\left|
\Pr\!\left[
D((w,c,z),y)=1\;:\;
\begin{array}{l}
(w,\mathrm{st})\leftarrow P_1(x,y),\\
c\leftarrow V_1(x,w),\\
z\leftarrow P_2(x,y,c,w,\mathrm{st})
\end{array}
\right]
-
\Pr\!\left[D((w,c,z),y)=1\;:\;(w,c,z)\leftarrow\mathrm{Sim}(x)\right]
\right|
\leq\varepsilon_{\mathrm{zk}}.
```

Here $`\varepsilon_{\mathrm{zk}}`$ is negligible; classical or quantum distinguishers can be considered. **The distinguisher receives the witness; the simulator does not.** Aborting transcripts are included. In a public-coin protocol, a uniform challenge can instead be supplied to the simulator. The surrounding explanation connects the witness requirement to a hybrid replacing many transcripts.

[Fallahpour24](https://pouriafallahpour.github.io/Thesis-with-acknowledgements.pdf), **Definition 29, printed p. 74** (PDF page 88), independently reproduces the definition. Its preceding paragraph explicitly motivates the witness condition through the relation between one-transcript and many-transcript security.

### Corrected SUCRE states a weaker experiment

[SUCRE26corr](https://eprint.iacr.org/2026/2248), **Definition 5**, compares

```math
D(vk,\mathrm{Trans}(sk,c))
\quad\text{and}\quad
D(vk,\mathrm{Sim}(vk,c)),
```

averaging over key generation and one uniform challenge. It does not give $`sk`$ to the distinguisher. This remains true in the corrected ePrint received on 28 September 2026, rather than only in the [journal version](https://doi.org/10.46586/tches.v2026.i1.618-659). The following Theorem 1 cites DFPS for the signing-query reduction. Section 5.2 represents shuffled values by frequency maps; Remark 1 explicitly distinguishes BAE+24's nonce/full-response exposure from SUCRE's rejected-value model.

The stated single-transcript experiment does not supply the witness-equipped premise used in the cited DFPS hybrid. Replacing one transcript while retaining other honest transcripts requires a way to generate those other records under the same challenge key. The witness supplies that capability. Averaging a one-transcript experiment over a fresh key does not supply it automatically.

This comparison establishes a missing hypothesis in the stated composition route. The [simulation theorem](../science/security_scope.md#4-repeated-transcript-simulation) separately states the computational obstruction for repeated augmented views, including correlated simulators, under its bounded-witness hardness assumption. The definition mismatch alone does not exclude every replacement proof or a security theorem for a different observation model.

## 5. Decomposition arithmetic and recent work

[NIST204](https://csrc.nist.gov/pubs/fips/204/final), Algorithms 36–38 and printed pp. 40–41, specifies the special wrap-around case in `Decompose`, followed by `HighBits` and `LowBits`. Fiber counts and translated intersections follow by elementary arithmetic from these definitions. The [scalar lemma](../science/boundary_statistic.md#scalar-preimages) is included to make the statistical argument self-contained; scalar decomposition counting is not claimed as an independent novelty.

[PS26](https://eprint.iacr.org/2026/895), *On the Properties of HighBits and LowBits Functions and their Applications*, is directly relevant adjacent work. Its primary abstract reports a seven-valued error characterization for the HighBits of a sum and applications to advanced signatures. The [AFRICACRYPT publication](https://doi.org/10.1007/978-3-032-31130-6_14) appeared online on 9 July 2026. Because the complete paper was unavailable in this comparison, no claim is made that a particular scalar identity is absent from it.

[ZCQLZ26](https://eprint.iacr.org/2026/056), *Rejection Matters*, describes templates built from public data on the target device to infer rejected challenges, followed by correlation power analysis using accepted and rejected attempts. Its [DATE publisher record](https://doi.org/10.23919/DATE69613.2026.11539074), abstract, and indexed contents support this observation-model comparison. The full paper was unavailable, so overlap with a shuffled-residual or boundary-correlation argument remains unresolved.

## 6. Coverage

The comparison uses the relevant full-text passages of BAE+24, Zhou et al., corrected SUCRE, the original and revised DFPS definitions, and Fallahpour's thesis. The DFPS passages were available as indexed primary text. The Pessl comparison uses author slides; Liu et al. was checked at abstract level. **Full-text comparison remains open for ePrint 2026/895 and 2026/056.** Their primary abstracts and publication records were checked, with indexed contents also available for the latter. These limits constrain the priority assessment; absence from an abstract is not evidence of absence from a paper. Version dates and venue metadata are preserved in the bibliography.

## 7. Scope of comparison

The established contribution is a residual/high-bit identification theorem for the stated augmented view, a quantitative fixed-matrix justification, and a conditional obstruction to repeated public-key-only simulation. BAE+24 supplies direct prior art for anonymous shuffled inference and shared-key accumulation. Standard decomposition arithmetic and PS26 supply the adjacent arithmetic context. The exact DFPS and corrected SUCRE definitions identify the missing premise in the cited composition route.

The [security scope](../science/security_scope.md) specifies the simulator class, hardness assumption, public-key convention, and resource costs. The [replacement-marginal result](../science/sampler_marginal.md) concerns a particular comparison distribution; repairing that marginal does not settle simulation of the joint repeated view. These conclusions establish neither practical physical-trace feasibility nor exposure of a full histogram by a bounded number of probes. The source comparison does not exclude overlap in the two inaccessible complete papers.
