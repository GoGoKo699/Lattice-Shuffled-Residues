# Thirty milestones for understanding shuffled residues

This map follows the scientific argument of Lattice Shuffled Residues: how a shuffled residual histogram retains an indexed correlation, why that correlation survives reuse of one public matrix, and what repeated observations imply under the stated security assumptions. The thirty milestones identify conceptual dependencies and understanding targets. The linked scientific pages contain the complete definitions, proofs, and specialist calculations.

## Allocation and reading order

**M01–M10 are background/preliminaries.** They assemble finite arithmetic, probability, observed information, and cryptographic experiments into the project's complete model. Their order moves from individual values and maps to a signature experiment with a persistent key and explicitly specified observations.

**M11–M30 are narrative/innovation.** This phase starts with one rounding endpoint and ends with the contribution's scope. Its twenty milestones reflect the length of the project's main argument: the scalar mechanism, the translated-box and fixed-matrix proof, moment transfer and concentration, and the computational consequence. The separate replacement-marginal discrepancy joins the source comparison without becoming a premise of the identification theorem. The allocation follows these dependencies; it is not a division of a textbook into thirty reading assignments.

Dependencies name earlier milestones only. A dependency supplies an idea used by the current target; it does not assert that every detail of its source must be mastered first. M10 integrates the background, and M30 integrates the whole scientific account.

## The educational anchor and the local bridge

The single educational anchor is Dan Boneh and Victor Shoup, [*A Graduate Course in Applied Cryptography*, version 0.6, January 2023](https://toc.cryptobook.us/book.pdf), abbreviated **BS** below. Section and page references are to that version's printed pages. Its games, hybrids, signature definitions, and witness-based simulation language provide the cryptographic framework.

The [local foundations](FOUNDATIONS.md) introduce the arithmetic and probability prerequisites. The exact conditional-box law, sparse-rank and collision proofs, rounding counts, mixed moments, and Bernstein calculation are supplied by the scientific pages. A book pointer supplies only the stated conceptual background; it does not attribute these project-specific arguments to the book. No result here depends on an unfinished lattice chapter or probability appendix. Primary research cited through the project pages remains evidence for attribution and proof comparison, not an additional educational anchor.

**Notation bridge.** BS §19.4 uses $`x`$ for a witness and $`y`$ for a statement. The project's nonce is also written $`y`$, while the DFPS definition quoted in the related-work account uses $`x`$ for a statement and $`y`$ for a witness. These are different local conventions. In this map, “statement,” “witness,” and “nonce” identify the roles explicitly. The project also distinguishes the box size $`L`$ from the low-part function $`L_\alpha`$, and the coordinate sets $`\mathcal S_i`$ from the scalar sums $`S_1,S_2`$.

## Phase I: background/preliminaries

### M01 — Residues, representatives, and finite fields

**Phase:** Background/preliminaries.

**Central question:** How can a coefficient have both a modular value and an integer magnitude?

**Understanding target:** Distinguish a residue modulo the prime $`q`$ from its chosen integer representative. Explain why equal residues may have different written representatives, why coefficient bounds refer to specified integers, and why reducing modulo $`q`$ is different from discarding a high or low part.

**Dependencies and story role:** None. This is the local arithmetic vocabulary on which the module equation and the rounding mechanism depend.

**Conceptual connection:** A distribution lives on mathematical values, while a norm bound and a rounding interval use representations. Keeping both roles visible prevents an endpoint or wrap-around convention from disappearing in later probability counts.

**Sources:** [Foundations, “Residues and integer representatives”](FOUNDATIONS.md#residues-and-integer-representatives); project [Model, “Algebra and parameters” and “The rounding convention”](../science/model.md#algebra-and-parameters). The required finite arithmetic is introduced locally; no algebra appendix is assumed.

### M02 — Negacyclic products and module equations

**Phase:** Background/preliminaries.

**Central question:** What does polynomial multiplication mean as a map between coefficient vectors?

**Understanding target:** Interpret $`X^n=-1`$, signed wrap-around, and the module matrix $`A`$. Relate polynomial vectors to the $`M=\ell n`$ input and $`D=kn`$ output coefficients. Explain rank as the dimension of an image and kernel as the inputs mapped to zero; distinguish a ring coefficient from a field matrix entry.

**Dependencies and story role:** M01. This supplies the linear-map language needed both for the later sparse-rank theorem and for completing a full algebraic key.

**Conceptual connection:** The same negacyclic multiplication can be viewed as a polynomial operation or an ordinary linear map over $`\mathbb F_q`$. Moving between those views makes signs, coordinate functionals, and injectivity explicit.

**Sources:** [Foundations, “Negacyclic polynomials and module matrices”](FOUNDATIONS.md#negacyclic-polynomials-and-module-matrices) and [“Rank, kernels, and uniform fibers”](FOUNDATIONS.md#rank-kernels-and-uniform-fibers); project [Model, “Algebra and parameters”](../science/model.md#algebra-and-parameters) and [Fixed matrix, §2](../science/fixed_matrix.md#2-the-coefficient-pairing-and-the-negacyclic-signs). These algebraic preliminaries are local to the project.

### M03 — Sampling, fibers, and conditional laws

**Phase:** Background/preliminaries.

**Central question:** How do a function and an observed event change a finite probability distribution?

**Understanding target:** Read uniform sampling, a function's preimage fiber, conditioning, and independence conditional on a fixed key. Interpret expectation, centering, first and second moments, and variance. Explain why a centered variable can still correlate with another centered variable, and why retaining only some records changes the sampling law.

**Dependencies and story role:** M01–M02. This establishes the probabilistic operations used throughout the mechanism, censoring analysis, and moment calculation.

**Conceptual connection:** Counting equally likely preimages gives scalar probabilities; conditioning restricts and renormalizes a sample space. Expectations then summarize those probabilities without making unproved independence assumptions.

**Sources:** [Foundations, “Expectations, centering, and moments”](FOUNDATIONS.md#expectations-centering-and-moments) and [“Independence after conditioning”](FOUNDATIONS.md#independence-after-conditioning); project [Model, “One independent attempt” and “Exact conditioning on the first check”](../science/model.md#one-independent-attempt). General finite conditioning and moment identities are supplied locally.

### M04 — Histograms, joint observations, and retained correlation

**Phase:** Background/preliminaries.

**Central question:** Which information survives a shuffle, and which relationships can still be observed?

**Understanding target:** Distinguish an indexed vector, its shuffled presentation, and its histogram. Explain why knowing each marginal distribution does not determine a joint law, and why an anonymous count may correlate with a separate indexed public quantity without revealing the hidden permutation.

**Dependencies and story role:** M02–M03. This states the information question before introducing the signature-specific mechanism.

**Conceptual connection:** Removing coordinate labels preserves symmetric functions of the vector. The project asks what those preserved functions reveal when combined with information that retains its labels.

**Sources:** [Foundations, “Independence after conditioning”](FOUNDATIONS.md#independence-after-conditioning); project [Model, “One independent attempt”](../science/model.md#one-independent-attempt) and [Boundary statistic, “From a histogram to an indexed correlation”](../science/boundary_statistic.md#from-a-histogram-to-an-indexed-correlation); [Related work, §2](../references/RELATED_WORK.md#2-closest-attack-bronchain-et-al-bae24) for the inherited anonymous-inference idea.

### M05 — Statistical distance and bounded observations

**Phase:** Background/preliminaries.

**Central question:** What does it mean for two laws to be close enough that a bounded statistic has nearly the same expectation?

**Understanding target:** Interpret total variation as a bound on event-probability differences. Connect it to the expectation error of a function with known range width. Distinguish statistical from computational indistinguishability, and understand why projection cannot increase statistical distance while a common translation preserves distance to uniform.

**Dependencies and story role:** M03–M04. This gives a quantitative language for comparing the project's convenient calculation law with its actual observations.

**Conceptual connection:** A theorem about small marginals becomes useful only after identifying which coordinates a statistic uses and how much it can vary.

**Sources:** BS §3.11, “A broader perspective: computational and statistical indistinguishability,” pp. 82–87, especially Definitions 3.4–3.6, and Exercise 3.10(b), p. 92; [Foundations, “Statistical distance and observable means”](FOUNDATIONS.md#statistical-distance-and-observable-means); project [Concentration, §5](../science/concentration.md#5-transfer-to-a-fixed-matrix).

### M06 — Signature keys, commitments, and rejecting attempts

**Phase:** Background/preliminaries.

**Central question:** What objects persist across signing requests, and what is freshly sampled inside an attempt?

**Understanding target:** Separate key generation, a signing request, an internal attempt, and the final signature. Identify the full public relation $`t=As_1+s_2`$, the persistent bounded secrets, the fresh nonce, the commitment high part, and the two norm checks. Distinguish declared observations from values that merely exist internally.

**Dependencies and story role:** M02–M04. This places the local arithmetic and probability in the computational task being studied.

**Conceptual connection:** Standard signature syntax specifies the external security task. The project's enlarged observation model specifies additional information about internal attempts, so its consequences must be interpreted with that interface in view.

**Sources:** BS §13.1 and §13.1.1, pp. 528–530, signature syntax and Attack Game 13.1; [Foundations, “The bounded public-key relation”](FOUNDATIONS.md#the-bounded-public-key-relation); project [Model, “One independent attempt”](../science/model.md#one-independent-attempt) and [Security scope, §7](../science/security_scope.md#7-compressed-verification-keys-and-physical-observations).

### M07 — Fresh oracle challenges under one reused key

**Phase:** Background/preliminaries.

**Central question:** How can records be independent when the key is the same and each challenge is computed from a commitment?

**Understanding target:** Explain the first-attempt, fresh-message-prefix strategy in the classical random-oracle model. Distinguish a fresh oracle input from a new output value, and independence conditional on the key from averaging over different keys. Recognize the separate assumptions needed for finite prehashes, seeded matrices, and deterministic nonce sources.

**Dependencies and story role:** M03, M06. This identifies the source of repeated independent records before concentration or simulation is discussed.

**Conceptual connection:** Reusing a key is essential to accumulation. Fresh inputs supply the independent attempt randomness, while the oracle and source assumptions determine when the mathematical sampling model applies.

**Sources:** BS §8.10.2, “Random oracles: a useful heuristic,” pp. 327–331, especially the fresh-input sampling construction on p. 330; project [Model, “First attempts and the random-oracle model”](../science/model.md#first-attempts-and-the-random-oracle-model) and [Security scope, §6](../science/security_scope.md#6-fresh-messages-first-attempts-and-resource-costs). The project supplies the first-attempt application and its interface assumptions.

### M08 — Security games, reductions, and resource budgets

**Phase:** Background/preliminaries.

**Central question:** What must an algorithm accomplish before a statistical observation has a computational security consequence?

**Understanding target:** Distinguish a search task from a decision test, a theorem from its hardness assumption, and a success probability from a runtime claim. Explain a reduction's inputs, output validation, and combined resource budget. Interpret negligible asymptotic error separately from a small concrete probability.

**Dependencies and story role:** M05–M07. This supplies the symbolic reduction and accounting language used later, before detailed costs are evaluated.

**Conceptual connection:** If a simulator is followed by a postprocessor, the assumed hard problem must remain hard at their combined cost. An observation count alone does not specify that cost or the assumed key distribution.

**Sources:** BS §3.4, “Composing PRGs,” pp. 54–61, for reductions and hybrids, and §3.11, pp. 82–87, for indistinguishability; project [Security scope, §§3–4](../science/security_scope.md#3-a-publicly-verifiable-search-problem).

### M09 — Simulated views, witnesses, and repeated experiments

**Phase:** Background/preliminaries.

**Central question:** Which information may a simulator and a distinguisher use when comparing real and simulated transcripts?

**Understanding target:** Identify a public statement, a valid witness, and a transcript. Separate the simulator's inputs from the distinguisher's auxiliary information. Explain why replacing one record inside a repeated experiment may require generating the other real records under the same witness.

**Dependencies and story role:** M06, M08. This introduces the simulation framework that the project's source comparison will later inspect precisely.

**Conceptual connection:** A hybrid is an algorithmic construction as well as a sequence of distributions. Its reduction must possess the information required to generate the parts it leaves real.

**Sources:** BS §19.4, pp. 771–775, effective relations, witnesses, and special honest-verifier zero knowledge; §20.4.2, pp. 840–841, Attack Game 20.4, Definition 20.6, and the repeated-interaction hybrid; project [Security scope, §5](../science/security_scope.md#5-the-one-transcript-definition-and-composition).

### M10 — The complete observation experiment and its three laws

**Phase:** Background/preliminaries.

**Central question:** What is the complete experiment whose information and simulability this project studies?

**Understanding target:** Assemble the fixed matrix and secrets, fresh attempt randomness, indexed high values, histogram, and visible check outcomes into one model. Distinguish the genuine fixed-key law, the independent-coordinate comparison law, and the source's replacement sampler. State which law supports each kind of claim and which information is actually available.

**Dependencies and story role:** M01–M09. This integrates the background into the single framework used throughout the research phase.

**Conceptual connection:** The subsequent proof computes moments in one law, transfers them to another, and separately diagnoses a third. Keeping those roles explicit makes the logical route from observation to security assessable.

**Sources:** Project [Scientific overview, “Three distributions to keep distinct”](../science/README.md#three-distributions-to-keep-distinct); [Model](../science/model.md); [Replacement marginal, “The replacement rule being compared”](../science/sampler_marginal.md#the-replacement-rule-being-compared). BS §§3.11 and 19.4 supply the comparison and simulation vocabulary.

## Phase II: narrative/innovation

### M11 — The endpoint that creates an extra joint preimage

**Phase:** Narrative/innovation.

**Central question:** Where does the scalar secret-dependent correlation first enter the rounding calculation?

**Understanding target:** Explain the exceptional high and low fibers under $`q=p\alpha+1`$. For a selected residual $`-a+v`$ and bounded shift $`d`$, understand why the joint event with a zero high part gains one preimage exactly at $`d=-v`$. Keep the shifted joint count separate from the unchanged low marginal.

**Dependencies and story role:** M01, M03, M10. This is the local mechanism from which the rest of the argument grows.

**Conceptual connection:** A one-residue endpoint asymmetry creates a dependence that survives aggregation. Its consequence comes from how it is used in the joint observation, rather than from assuming a biased low marginal.

**Sources:** Project [Boundary statistic, “Scalar preimages” and “Boundary-count identity,” (B1)–(B2)](../science/boundary_statistic.md#scalar-preimages); [Model, “The rounding convention”](../science/model.md#the-rounding-convention). This counting derivation is supplied locally.

### M12 — A centered histogram that remains observable after censoring

**Phase:** Narrative/innovation.

**Central question:** How does an anonymous count become an indexed statistic that is still known when some residuals are suppressed?

**Understanding target:** Explain the weighted sum $`F`$, its centering $`F_c=F-D\mu`$, and the centered high indicator. Under the comparison law, identify why off-diagonal terms cancel and the same-coordinate covariance remains. Retain $`F_c=-D\mu`$ on accepted first-check-passing attempts, and assign zero only to first-check failures.

**Dependencies and story role:** M03–M04, M06, M11. This constructs an observable statistic without changing the record population by selecting only final rejections.

**Conceptual connection:** Centering makes independent background contributions cancel in expectation. The boundary-band visibility rule makes the centered statistic observable even when the accepted residual histogram is omitted.

**Sources:** Project [Boundary statistic, “Weighting the boundary values,” “From a histogram to an indexed correlation,” and “Visibility and rejection,” (B3)–(B4), (B9)](../science/boundary_statistic.md#weighting-the-boundary-values); [Concentration, “Which records contribute”](../science/concentration.md#which-records-contribute).

### M13 — Challenge symmetry turns the correlation into a linear mean

**Phase:** Narrative/innovation.

**Central question:** How does a nonlinear function of $`cs_2`$ reveal a signed coefficient of $`s_2`$ in expectation?

**Understanding target:** Follow the pairing of $`c`$ with $`-c`$ and the identity $`\mathbb E[C(c)^TC(c)]=\tau I`$. Explain why the comparison mean is $`-\tau(s_{2,b})_j/(2q)`$ and why the transpose and negacyclic signs matter. Do not treat a challenge coefficient and its induced secret product as independent.

**Dependencies and story role:** M02–M03, M12. This converts the scalar covariance into the coefficientwise signal needed for identification.

**Conceptual connection:** Symmetry removes the positive-part nonlinearity; second moments of the signed challenge isolate the original coefficient with a known normalization.

**Sources:** Project [Boundary statistic, “Challenge symmetry,” (B5)–(B8)](../science/boundary_statistic.md#challenge-symmetry); [Concentration, §4](../science/concentration.md#4-averaging-the-challenge). These identities are local derivations.

### M14 — First-check conditioning produces a translated box

**Phase:** Narrative/innovation.

**Central question:** What is the actual nonce law after the first norm check passes?

**Understanding target:** Explain the exact identity $`y=Z-cs_1`$ conditional on passing, with $`Z`$ uniform on an interior box of side $`L=2(\gamma_1-\beta)-1`$. Account for the strict endpoints and the challenge-independent probability $`p_z=(L/(2\gamma_1))^M`$. Understand why the challenge remains uniform after conditioning.

**Dependencies and story role:** M01–M03, M07, M10. This replaces a potential rejection-conditioning obstacle with a precise input distribution for the fixed-matrix proof.

**Conceptual connection:** A bounded secret-dependent shift changes the position of the box, while leaving its shape and size fixed. That structure is exactly what the later all-translations conclusion needs.

**Sources:** Project [Model, “Exact conditioning on the first check”](../science/model.md#exact-conditioning-on-the-first-check); [Fixed matrix, §5](../science/fixed_matrix.md#5-conditioning-on-the-first-check).

### M15 — Sparse multiplication rank and coordinate functionals

**Phase:** Narrative/innovation.

**Central question:** Why can a relation among a few output coefficients impose many constraints on a nonce difference?

**Understanding target:** Explain the nondegenerate coefficient pairing and the negative exponents that represent selected coordinates. Follow the sparse multiplication rank bound $`\lceil n/s\rceil`$: basis rows must collectively cover every nonzero column. Distinguish this finite-field argument from an unproved Fourier or real-valued uncertainty claim.

**Dependencies and story role:** M02, M14. This supplies the algebraic reason that a small output relation forces a substantial input constraint.

**Conceptual connection:** Sparsity limits how many columns one row can cover, so a multiplication map needs enough independent rows. The coefficient pairing translates that rank statement into the relation arising from selected outputs.

**Sources:** Project [Fixed matrix, §2 and Lemma 2 in §3](../science/fixed_matrix.md#2-the-coefficient-pairing-and-the-negacyclic-signs). This is a project-local algebraic proof.

### M16 — Turning subspace dimension into a box probability

**Phase:** Narrative/innovation.

**Central question:** How does an algebraic dimension bound restrict the probability of a difference of box samples?

**Understanding target:** Explain why a $`t`$-dimensional affine subspace contains at most $`L^t`$ points of a product of size-$`L`$ coordinate sets. Apply the injective coordinate projection idea to $`Z-Z'`$, with independent box samples, without assuming that this difference is itself uniform on a box.

**Dependencies and story role:** M02–M03, M14–M15. This turns the algebraic restriction into the probability estimate required by the collision proof.

**Conceptual connection:** Independent coordinate choices provide a counting resource. Codimension removes choices, and that loss becomes a power of $`L`$ in the probability bound.

**Sources:** Project [Fixed matrix, Lemma 3](../science/fixed_matrix.md#lemma-3--a-product-box-meets-a-subspace-in-few-points). The proof supplies the finite-dimensional counting argument locally.

### M17 — From deficient rank to a marginal collision bound

**Phase:** Narrative/innovation.

**Central question:** How can two independent inputs colliding under a random matrix control the distribution of selected outputs?

**Understanding target:** Follow the collision map for a fixed difference, the deficient-rank event, and the union over coefficient relations up to nonzero scalar multiplication. Explain the role of $`J_r=(q^r-1)/(q-1)`$ and how collision excess bounds squared total variation for a selected $`r`$-coordinate marginal.

**Dependencies and story role:** M05, M15–M16. This joins the algebraic and counting ingredients into an averaged bound over the public-matrix draw.

**Conceptual connection:** Full rank gives the uniform collision probability. Rare deficient-rank differences account for the excess; Cauchy–Schwarz converts that excess into statistical closeness.

**Sources:** Project [Fixed matrix, §4](../science/fixed_matrix.md#4-collision-proof-of-theorem-1). BS §3.11, pp. 82–87, supplies the statistical-distance vocabulary. BS §8.10.4, pp. 334–335, states a leftover-hash result as a related extraction principle; it does not prove this structured-matrix claim. The rank and collision argument is proved locally.

### M18 — One good matrix for every required coordinate set and translation

**Phase:** Narrative/innovation.

**Central question:** How does an average over random matrices justify repeated use of one fixed matrix for every challenge?

**Understanding target:** Explain the Markov and union bounds defining the explicit exception $`\zeta_4(\varepsilon)`$. State the quantifiers: outside that event, every marginal of at most four coordinates is close to uniform for every translation of one fixed base box. Understand why translation needs no additional union bound, and why full-vector uniformity or arbitrary adaptive base boxes do not follow.

**Dependencies and story role:** M05, M14, M17. This completes the fixed-matrix bridge needed to reuse the secret and matrix across records.

**Conceptual connection:** Probability is paid once for the matrix draw. Exact translation invariance then makes the same matrix event serve every allowed secret shift and challenge.

**Sources:** Project [Fixed matrix, Theorem 1, §4, and §6](../science/fixed_matrix.md#1-notation-and-statement). The concrete exceptions and the uniform-matrix assumption are part of this statement.

### M19 — Same-coordinate dependence and exact mixed moments

**Phase:** Narrative/innovation.

**Central question:** Which moment calculations remain necessary when two centered variables share the same underlying coefficient?

**Understanding target:** Identify $`U_i`$ and $`V_i`$, their marginal variances $`u,v`$, their mixed mean $`m_i`$, and the fourth moment $`\kappa_i=\mathbb E[U_i^2V_i^2]`$. Explain why same-coordinate dependence must be retained, how the scalar preimage count gives the mixed moments, and why $`\kappa_i\le v`$ is a valid uniform bound.

**Dependencies and story role:** M03, M11–M12. This supplies the local moment data required to control the noise around the secret-dependent mean.

**Conceptual connection:** Centering removes marginal means, not dependence. The same local correlation that supplies the signal must also be included in the fluctuation calculation.

**Sources:** Project [Concentration, §2](../science/concentration.md#2-exact-one-coordinate-moments); [Boundary statistic, (B1)–(B3)](../science/boundary_statistic.md#boundary-count-identity). These exact moments are supplied locally.

### M20 — Across-coordinate expansion and challenge-mixture variance

**Phase:** Narrative/innovation.

**Central question:** How do the local moments combine into a bound for a full histogram statistic with a random challenge?

**Understanding target:** Classify the surviving index patterns in $`\mathbb E T^2`$, including the two cross-pairings and the vanishing singleton terms. Explain why the bound $`B`$ is uniform in the challenge and why averaging conditional variances alone would omit fluctuations of the conditional mean.

**Dependencies and story role:** M03, M12–M13, M19. This turns the local moment identities into the comparison-law second-moment bound.

**Conceptual connection:** Independence applies between distinct coordinate pairs. A second-moment bound survives the challenge mixture directly, preserving the dependence of both weights and shifts on that challenge.

**Sources:** Project [Concentration, §3](../science/concentration.md#3-exact-second-moment-and-a-challenge-uniform-bound) and [§4](../science/concentration.md#4-averaging-the-challenge).

### M21 — Transferring moments to the actual fixed-key observations

**Phase:** Narrative/innovation.

**Central question:** Why are four-coordinate marginals enough to justify the actual statistic's mean and variance?

**Understanding target:** Count the coordinates in a summand of $`T`$ and $`T^2`$, apply range-width bounds to the marginal error, and include the factor $`p_z`$ when returning to all first attempts. Identify the mean bias, second-moment correction, and pointwise bound $`R=\tau D\beta`$ for $`Q`$.

**Dependencies and story role:** M05, M12–M14, M18, M20. This completes the passage from the convenient comparison law to genuine observations for one fixed key.

**Conceptual connection:** The proof compares only the low-order moments it uses. It does not replace the whole record distribution or accumulate a total-variation error across all records.

**Sources:** BS Exercise 3.10(b), p. 92, for the bounded-expectation inequality; project [Boundary statistic, (B10)](../science/boundary_statistic.md#transfer-to-the-actual-fixed-matrix) and [Concentration, §5](../science/concentration.md#5-transfer-to-a-fixed-matrix), where the two- and four-coordinate transfers are derived.

### M22 — Concentration, bias, and integer identification

**Phase:** Narrative/innovation.

**Central question:** When does a small observable mean determine every bounded integer coefficient reliably?

**Understanding target:** Separate systematic transfer bias from sampling error. Explain the rescaling by $`\theta=p_z\tau/(2q)`$, the centered range bound $`2R`$ in Bernstein's inequality, and the union bound across coefficients. Relate the resulting $`3/8`$ estimation error to unique nearest-integer identification and the total failure bound $`\delta+\zeta_4(\varepsilon)`$.

**Dependencies and story role:** M03, M07, M18, M21. This integrates the signal, actual-law moment bounds, and independent records into the statistical identification theorem.

**Conceptual connection:** The target is separated from neighboring integer coefficients by a fixed gap. A concentration guarantee plus a controlled bias keeps the rescaled estimate inside that gap.

**Sources:** Project [Concentration, Theorem 2 and “Checking the Bernstein constant” in §6](../science/concentration.md#6-a-simultaneous-finite-observation-theorem). The Bernstein derivation is included locally rather than assumed from an unfinished appendix.

### M23 — Reading the observation counts and finite verification evidence

**Phase:** Narrative/innovation.

**Central question:** What do the numerical bounds and finite checks establish about the theorem?

**Understanding target:** Interpret $`2^{57},2^{61},2^{59}`$ as conservative sufficient counts of independent first-attempt records, including zero-valued first-check failures and accepted centered contributions. Distinguish arithmetic substitution, finite identity checks, general proofs, optimal sample complexity, and measured device performance.

**Dependencies and story role:** M12, M18, M20–M22. This makes the statistical theorem concrete while preserving the evidential role of each calculation.

**Conceptual connection:** Reproduction checks signs, factors, and numerical substitutions. It supports the proofs without turning a small finite enumeration into a theorem for every dimension or an operational experiment.

**Sources:** Project [Concentration, §7](../science/concentration.md#7-arithmetic-substitution); [Fixed matrix, §6](../science/fixed_matrix.md#6-four-coordinate-bounds-at-the-stated-parameter-shapes); [Verification guide](../verification/README.md), including its formula map and recorded-output link.

### M24 — Completing the full algebraic key and paying the rank exception

**Phase:** Narrative/innovation.

**Central question:** What additional public information and matrix property turn identification of $`s_2`$ into identification of $`s_1`$?

**Understanding target:** Use the full public equation and injectivity to explain linear completion. Understand the Chinese remainder factors in the stated rank probability, the conditions $`k\ge\ell`$ and $`q\equiv1\pmod{2n}`$ for the displayed split-factor formula, and the additional exception $`\delta_{\rm rk}`$. Separate this exception from the good-marginal event and recognize that a small concrete rank failure need not be negligible in every parameter family.

**Dependencies and story role:** M02, M06, M08, M22. This adds an algebraic consequence to the statistical result without merging their assumptions.

**Conceptual connection:** The statistical theorem reveals an error vector. A full public equation and an injective linear map then determine the remaining secret; a compressed public key leaves an additional unknown term.

**Sources:** Project [Security scope, §2, Proposition 1 and Corollary 2](../science/security_scope.md#2-full-key-identification-and-matrix-rank). The module-rank and Chinese remainder arguments are supplied locally.

### M25 — Any bounded witness and its public verification

**Phase:** Narrative/innovation.

**Central question:** How can a public observer validate success without knowing the originally generated secret?

**Understanding target:** Define the bounded-witness relation by the public equation and coefficient bounds. Explain why any valid bounded pair suffices for the search problem, how validation avoids comparison with an unavailable original key, and how the bounded-support counting argument links witness search to the specified decisional Module-LWE experiment.

**Dependencies and story role:** M02, M08–M09, M24. This constructs the publicly decidable success event needed for a simulation distinguisher.

**Conceptual connection:** A reduction needs a recognizable output condition. Witness verification supplies that condition while keeping the exact secret and error distributions in the hardness statement visible.

**Sources:** BS §19.4, pp. 771–775, for effective relations and witnesses; project [Security scope, §3 and the decision-assumption discussion in §4, (S4)–(S8)](../science/security_scope.md#3-a-publicly-verifiable-search-problem).

### M26 — Joint repeated-view simulation implies bounded-witness search

**Phase:** Narrative/innovation.

**Central question:** Why would an indistinguishable simulator for the full repeated view solve a public-key search problem?

**Understanding target:** Compose a public-key-only simulator with the identification and validation procedure. Track the genuine-view success, matrix exceptions, and the hardness bound at $`T_{\rm sim}+T_{\rm ext}`$. Explain why the conclusion includes stateful simulators with correlated outputs, and identify the excluded witness, trapdoor, and unbounded-computation resources.

**Dependencies and story role:** M05, M08–M09, M22, M24–M25. This joins statistical identification to a conditional computational obstruction, with the combined-resource premise stated symbolically at this stage.

**Conceptual connection:** Public validation is an efficient test whose acceptance probabilities differ if real views identify a witness but simulated views cannot do so within the assumed search budget.

**Sources:** BS §3.11, pp. 82–87, and §19.4, pp. 771–775; project [Security scope, Theorem 3 in §4, (S5)–(S6)](../science/security_scope.md#4-repeated-transcript-simulation).

### M27 — Why the witness matters in a one-transcript hybrid

**Phase:** Narrative/innovation.

**Central question:** Which missing input prevents a one-transcript comparison from automatically justifying many transcripts under the same key?

**Understanding target:** Compare the exact information given to the distinguisher in the cited DFPS and corrected SUCRE definitions. Explain the witness's role in producing the other real records during a hybrid replacement, the accumulated one-record error, and the distinction between a missing composition premise and exclusion of every possible alternative proof.

**Dependencies and story role:** M08–M10, M26. This connects the general simulation theorem to the specific source-level proof issue.

**Conceptual connection:** The validity of a hybrid depends on both closeness of adjacent laws and implementability of the reduction connecting them. Auxiliary witness information can supply the latter while remaining unavailable to the simulator.

**Sources:** BS §3.4, pp. 54–61, and §20.4.2, pp. 840–841; project [Security scope, §5](../science/security_scope.md#5-the-one-transcript-definition-and-composition); [Related work, §4](../references/RELATED_WORK.md#4-the-strong-hvzk-hypothesis-dfps-versus-sucre), including the exact original and revised primary definitions.

### M28 — The particular replacement marginal and its local repair

**Phase:** Narrative/innovation.

**Central question:** What is wrong with the source's specific one-view replacement, and what does correcting that marginal accomplish?

**Understanding target:** Explain the zero-high probability deficit, including conditioning on the first check and the zero-nonce exception in the random-matrix experiment. Understand conditional-preimage sampling as a repair of the isolated high marginal in the uniform-scalar comparison law. Keep that diagnostic separate from the genuine repeated-view theorem and distinguish a false hardness premise from a false conditional implication.

**Dependencies and story role:** M03, M05, M08, M10–M11, M14, M27. This incorporates the independent source-sampler finding without making the main mechanism depend on it.

**Conceptual connection:** Correct marginals are a necessary distributional check. Matching one marginal leaves open the joint correlations with the public key, indexed high values, and persistent secret across records.

**Sources:** Project [Replacement marginal, “Exact statement for the source's random-matrix experiment,” “A local repair,” and “Separation of conclusions,” (S4)–(S6)](../science/sampler_marginal.md#exact-statement-for-the-sources-random-matrix-experiment). BS §3.11, pp. 82–87, supplies the event-test interpretation of a distinguishing gap.

### M29 — Charging source cost, exact arithmetic, memory, and asymptotic scale

**Phase:** Narrative/innovation.

**Central question:** Which costs and parameter conditions must accompany the observation bound and simulation reduction?

**Understanding target:** Account for obtaining complete signing requests, keeping first records, accumulating exact integer statistics, final rational rescaling, and linear completion. Distinguish record count, bit operations, storage, and physical acquisition. Explain why polynomial runtime requires bounds on the numerical parameters and $`p_z^{-1}`$, while negligible $`\zeta_4`$ separately requires enough entropy-exponent slack to dominate its prefactor beyond logarithmic scale in the security parameter.

**Dependencies and story role:** M07–M08, M18, M22–M24, M26. This fills in the combined-resource premise and checks its asymptotic interpretation after the full proof chain is established.

**Conceptual connection:** Exact arithmetic prevents a small-mean estimate from hiding a free precision resource. Explicit probability exponents prevent small concrete exceptions from silently becoming universal asymptotic negligibility claims.

**Sources:** Project [Security scope, §6 and “Exact integer processing and storage,” (S9)–(S13)](../science/security_scope.md#6-fresh-messages-first-attempts-and-resource-costs); [Concentration, §8](../science/concentration.md#8-what-the-bound-establishes); [Fixed matrix, Theorem 1 and §6](../science/fixed_matrix.md#1-notation-and-statement). BS §§3.4 and 3.11 provide the reduction and asymptotic framework.

### M30 — The complete contribution, its inherited ingredients, and its limits

**Phase:** Narrative/innovation.

**Central question:** What has the complete argument established, what is inherited, and which further conclusions need new work?

**Understanding target:** Connect the endpoint mechanism, observable centering, fixed-matrix theorem, moment transfer, concentration, and witness reduction into one account. State the full-histogram, indexed-information, independent-source, uniform-matrix, and full-key assumptions at their proper steps. Credit earlier anonymous shuffled inference and standard decomposition arithmetic, and retain the unresolved full-text comparisons for ePrint 2026/895 and 2026/056. Distinguish the proved ideal-model result from compressed-key forgery and physical-trace feasibility.

**Dependencies and story role:** M10–M29. This is the global synthesis of the narrative/innovation phase and the complete project.

**Conceptual connection:** The contribution is the specific correlation and the theorem that carries it through a reused matrix and key to a scoped computational consequence. Its significance depends on both that complete chain and the boundaries of the available observations and sources.

**Sources:** Project [Scientific overview](../science/README.md); [Security scope, §§5–7](../science/security_scope.md#5-the-one-transcript-definition-and-composition); [Related work, §§2 and 4–7](../references/RELATED_WORK.md#2-closest-attack-bronchain-et-al-bae24). BS §§3.11, 13.1, 19.4, and 20.4.2 supply the general security vocabulary used to state the final distinctions.
