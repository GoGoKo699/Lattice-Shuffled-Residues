# The selected anchor and the project

**Dan Boneh and Victor Shoup, [A Graduate Course in Applied Cryptography](https://toc.cryptobook.us/), version 0.6, January 2023**, is the single educational anchor. The [official PDF](https://toc.cryptobook.us/book.pdf) was checked against that cover version. The bibliography key is `BonehShoup23` in [references.bib](../references/references.bib).

The book supplies the security language used below. The [local foundations](FOUNDATIONS.md) supply the project's algebra and probability prerequisites; the [science pages](../science/README.md) contain its proofs. These play different roles: understanding a general security definition does not establish that a particular observation model satisfies it.

## Verified source sections

Page numbers are the book's printed numbers, not PDF viewer indices.

| Source location | Pages | Connection to this project |
|---|---:|---|
| §3.4.1, Parallel composition | 54–58 | Understand what a hybrid reduction must generate around its challenge. |
| §3.11, Computational and statistical indistinguishability; Definitions 3.4–3.6, Theorems 3.10–3.11 | 82–87 | Separate finite probability bounds from computational assumptions. |
| §8.10.2, Random oracles: a useful heuristic | 327–331 | Explain the independent challenge in a fresh first attempt; the oracle table appears on p. 330. |
| §8.10.4, The leftover hash lemma; Theorem 8.11 | 334–335 | Recognize the importance of independence between a public random map and its source. |
| §§13.1–13.1.1, Signature syntax and security; Attack Game 13.1 | 528–530 | Keep one key fixed across signing queries and specify what the observer receives. |
| §19.4, Sigma protocols: basic definitions; Definitions 19.2–19.5 | 771–775 | Translate relations, witnesses, challenges, and simulation. |
| §20.4.2, Special computational HVZK; Attack Game 20.4 and Definition 20.6 | 840–841 | Identify the witness available in a transcript hybrid. |

**Coverage limits.** Chapter 17 is listed in the table of contents but absent from the v0.6 PDF body: printed p. 711 is followed by p. 714. Appendix B begins with a placeholder; its birthday section B.1 is present, while B.1.1 remains an outline. Section 8.10.4 states the leftover hash lemma without proving it. None of these locations is used as a substitute for the local algebra, conditioning, or concentration proofs.

## Translate notation before translating a claim

The book's relation convention in §19.4 is easy to reverse accidentally. Its variables also collide with several project symbols.

| Book notation | Meaning here |
|---|---|
| Witness $`x`$ | A bounded pair $`(s_1,s_2)`$. |
| Statement $`y`$ | The full public key $`(A,t)`$. The project's $`y`$ is instead a fresh nonce. |
| Binary relation $`R\subseteq X\times Y`$ | The bounded public-key relation defined below. The project's $`R_q`$ is a ring. |
| Commitment $`t`$ in a conversation $`(t,c,z)`$ | The project uses $`h=H(Ay)`$ for the indexed high-part observation. Its $`t=As_1+s_2`$ belongs to the public key. |
| Challenge space $`C`$ | The signed weight-$`\tau`$ polynomial space $`\mathcal B_\tau`$. |
| Statistical distance $`\Delta[P,Q]`$ | The same half-$`\ell_1`$ convention denoted $`\mathrm{TV}(P,Q)`$ locally. |

The local witness relation is

```math
\mathcal W_\eta(A,t)=
\left\{(u,v):
Au+v=t,\quad
\|u\|_\infty\le\eta,\quad
\|v\|_\infty\le\eta
\right\}.
```

Here $`u\in R_q^\ell`$ and $`v\in R_q^k`$. The equation is evaluated in the ring; the bounds use the specified centered integer representatives of its coefficients. Finding any member of this set is the bounded-witness search problem. It need not identify the particular witness drawn by key generation.

A conversation in an ordinary signature or Sigma-protocol game also differs from the project's observation. The latter includes an indexed high-part vector, a challenge, check outcomes, and a residual histogram when that check is reached. Those additional observations must be included in the simulated distribution. A result for accepted signatures alone does not answer that enlarged question. The complete interface is fixed in [the model](../science/model.md).

## From statistical distance to a moment bound

The following finite calculation explains the role of §3.11 in the proof. For two distributions on the same finite space, put

```math
\mathrm{TV}(P,Q)=\frac12\sum_x|P(x)-Q(x)|.
```

Let a real-valued function $`f`$ take values in $`[a,b]`$. The positive and negative parts of $`P-Q`$ each have total mass $`\mathrm{TV}(P,Q)`$. Since the constant $`a`$ cancels from the expectation difference and $`0\le f-a\le b-a`$, this gives the moment-transfer inequality

```math
\left|\mathbb E_P f-\mathbb E_Q f\right|
\le (b-a)\,\mathrm{TV}(P,Q).
```

This argument is about actual probability distributions and applies without a runtime restriction. A computational indistinguishability hypothesis instead bounds tests of specified computational cost. The two kinds of statements enter different parts of the project.

In [the boundary calculation](../science/boundary_statistic.md), expanding the mean produces terms involving at most two output coordinates. Expanding the second moment produces terms involving at most four. The proof transfers those terms separately using their ranges and the relevant small marginals. It never replaces the whole vector $`Ay`$ by independent uniform coefficients.

This distinction matters quantitatively. The useful mean is small, and the range of the full statistic grows with its dimension and weights. Saying that a distribution is merely “close to uniform” supplies too little information: the approximation error must remain smaller than the mean separation after multiplication by those ranges. [Concentration](../science/concentration.md) keeps the resulting error terms explicit.

## From a random map to one fixed matrix

The conceptual connection to §8.10.4 is extraction by a public random map. Applying that connection here requires additional work: negacyclic multiplication is a structured family, and the same matrix is reused in every observation.

Let $`Z`$ be uniform on the fixed product box obtained after the first rejection check. Its base support is independent of $`A`$. Call $`A`$ good when, simultaneously for every set $`I`$ of at most four output coordinates and every translation $`\boldsymbol b\in R_q^\ell`$,

```math
\mathrm{TV}\!\left(
\mathcal L((A(Z+\boldsymbol b))_I),
\mathrm{Unif}(\mathbb F_q^{|I|})
\right)\le\varepsilon.
```

The [fixed-matrix theorem](../science/fixed_matrix.md) proves

```math
\Pr_A[A\text{ is good}]\ge1-\zeta_4(\varepsilon)
```

and defines the explicit exception bound $`\zeta_4`$ and its parameter conditions. The assertion controls all translations of that fixed base box; it does not control every possible base box simultaneously.

There are two useful steps behind its quantifiers. First, a sparse coefficient relation among selected outputs becomes an annihilator equation for polynomial multiplication. A rank bound then limits the number of product-box pairs that can collide. Collision probability bounds statistical distance, and Markov's inequality plus a finite union bound selects the good matrix event. These are local finite-field arguments.

Second, once a particular matrix is good, translating the input simply translates the selected output by $`(A\boldsymbol b)_I`$. Uniform output is invariant under that translation, so the distance is unchanged. This pointwise argument permits $`\boldsymbol b=-cs_1`$ to depend on the challenge, secrets, and even the matrix. It does not invoke independence for a translated source that may lack it.

Consequently, the probability of choosing a bad matrix is paid once at key generation. The proof does not pay a fresh matrix-exception term at every signing attempt.

## From one transcript to repeated transcripts

A useful way to read the hybrid material is to ask what the reduction can sample while it embeds its one challenge. In this project, all records refer to the same public key and hidden witness. With fresh nonces and the model's independent challenges, records are independent conditional on the full key; averaging over the hidden key can still leave correlations between records.

For example, take a hidden fair sign $`S`$, a number $`0<\epsilon<1/2`$, and conditionally independent signs $`X_i`$ with

```math
\Pr[X_i=S\mid S]=\frac12+\epsilon.
```

Every individual $`X_i`$ is fair. Nevertheless,

```math
\mathbb E[X_1X_2]
=\mathbb E\!\left[
\mathbb E[X_1\mid S]\mathbb E[X_2\mid S]
\right]
=4\epsilon^2.
```

Simulating each marginal independently by a fair sign loses that correlation. This example shows a logical failure of marginal reasoning; it does not rule out a simulator that generates correlated outputs.

In the book's Attack Game 20.4, the distinguisher chooses a valid witness–statement pair and therefore knows its witness. Page 841 uses a transcript hybrid with loss proportional to the number of transcripts. For the project's analogous hybrid, witness access allows the reduction to generate the other real records under the same key while it replaces one record at a time.

That capability is a hypothesis to check, not a consequence of matching a public-key-only one-record distribution. Moreover, the book's Sigma-protocol syntax requires honest acceptance; the local experiment includes aborted attempts. The exact abort-aware DFPS definition and corrected SUCRE comparison therefore remain separate, as documented in [related work](../references/RELATED_WORK.md#4-the-strong-hvzk-hypothesis-dfps-versus-sucre).

The project's [simulation theorem](../science/security_scope.md#4-repeated-transcript-simulation) covers stateful, correlated simulators directly. Its test applies the statistical identification procedure, completes a bounded witness when the full public matrix is injective, and checks the public relation. Successful simulation would make that test succeed and thus solve the stated bounded-witness search problem. The conclusion is conditional on that computational assumption and the displayed resource bounds; it does not exclude an unbounded simulator or assert a theorem about a different observation interface.

## From an oracle table to a fresh challenge

For the local oracle formulation, use an unambiguous input $`m\mathbin\|h`$. Before its first challenge query, the signer has already formed the commitment from its nonce. If no prior query uses the fresh message prefix $`m`$, this input is absent from the shared oracle table. Assigning it a fresh uniform output makes the challenge independent of that nonce and the earlier records. This is the role of the table construction in §8.10.2.

Distinct oracle inputs may return equal challenge values; such equality is compatible with independence. Repeated queries to one input instead reuse its output. Retaining first attempts under fresh prefixes avoids a separate retry-dependence argument. A finite message prehash needs its collision event accounted for, and a concrete seeded matrix generator needs its own distributional assumption. [The model](../science/model.md#first-attempts-and-the-random-oracle-model) and [security scope](../science/security_scope.md#6-fresh-messages-first-attempts-and-resource-costs) state those qualifications.

## Where the project supplies the remaining arguments

| Local source | Material supplied locally |
|---|---|
| [Foundations](FOUNDATIONS.md) | Coefficient representatives, quotient-ring algebra, finite probability, and the public witness relation. |
| [Model](../science/model.md) | Exact rounding convention, observation and censoring rules, and the translated nonce law after conditioning. |
| [Boundary statistic](../science/boundary_statistic.md) | Scalar fiber counting, histogram centering, and the challenge-weighted linear mean. |
| [Fixed matrix](../science/fixed_matrix.md) | Sparse multiplication rank, product-box intersections, collision bounds, and uniformity over translations. |
| [Concentration](../science/concentration.md) | Mixed second moments, explicit approximation errors, and the exponential-moment proof of the observation bound. |
| [Security scope](../science/security_scope.md) | Injectivity, bounded-witness validation, the correlated-simulation reduction, and costs and model limits. |
| [Sampler marginal](../science/sampler_marginal.md) | The separate replacement-sampler marginal discrepancy and the limited effect of repairing it. |

The [milestone map](MILESTONES.md) connects these sources in dependency order. The anchor provides a common security vocabulary throughout; the local statements preserve the precise assumptions and quantifiers needed for this result.
