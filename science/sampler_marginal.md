# The one-transcript replacement marginal

The repeated-transcript result concerns a fixed secret and fixed matrix. A separate, simpler calculation concerns the replacement distribution in the corrected SUCRE assumption. This chapter isolates that discrepancy and shows why repairing it does not settle the repeated-transcript question.

The source is [SUCRE, corrected ePrint 2026/2248, Figure 7 and Definition 11](https://eprint.iacr.org/2026/2248), received September 28, 2026. The definitions below retain its nonzero-secret case, $`\eta\ge1`$ and $`\tau\ge1`$.

## The replacement rule being compared

Use the [model's rounding convention](model.md#the-rounding-convention). In the real experiment the high coefficient is $`H((Ay)_i)`$. The residual hint is absent when the first check fails. When that check passes, the source's replacement rule draws a fresh independent dummy secret $`s'_2`$ and assigns

**(S1)**

```math
u_i=
\begin{cases}
H(q-a+(cs'_2)_i),&r_i=-a,\\
U(\{0,\ldots,p-1\}),&r_i\ne-a.
\end{cases}
```

The first-check event $`P_z`$ is visible: the residual hint is different from $`\bot`$ exactly on this event. Consider the test of $`P_z`$ together with a zero high coefficient.

## The dummy shift

For every signed weight-$`\tau`$ challenge, $`(cs'_2)_i`$ has the same distribution as

```math
S_\tau=X_1+\cdots+X_\tau,
\qquad
X_j\leftarrow U(\{-\eta,\ldots,\eta\})
\quad\text{independently}.
```

The coordinate uses $`\tau`$ distinct secret coefficients. Challenge signs and negacyclic signs do not change their symmetric distribution. Define

```math
\theta=\Pr(S_\tau\ge0)
=\frac{1+\Pr(S_\tau=0)}2.
```

Because $`|S_\tau|\le\beta<a`$,

```math
H(q-a+S_\tau)=0
\quad\Longleftrightarrow\quad S_\tau\ge0.
```

Convolution with a probability mass function cannot increase the largest atom. Hence

**(S2)**

```math
\Pr(S_\tau=0)\le\frac1{2\eta+1},
\qquad
1-\theta\ge\frac{\eta}{2\eta+1}.
```

## Uniform scalar comparison

For a uniform field element $`w`$ and any fixed bounded shift, $`r=L_\alpha(w-d)`$ equals $`-a`$ with probability $`1/q`$. Thus the replacement rule has zero-high probability

**(S3)**

```math
\frac{1-1/q}{p}+\frac{\theta}{q}
=\frac{\alpha+\theta}{q}.
```

The real probability is $`(\alpha+1)/q`$. The deficit is $`(1-\theta)/q`$.

## Exact statement for the source's random-matrix experiment

The preceding calculation can be made exact for Definition 11 without assuming that $`Ay`$ is a uniform vector.

The definition samples $`A`$ uniformly and independently of the secrets, nonce, and challenge. Conditioning on $`P_z`$ does not change this independence, since the first check depends only on $`y,c,s_1`$. Let

```math
\omega=\Pr(y=0\mid P_z).
```

The translated-box argument gives $`0\le\omega\le L^{-M}`$. If $`\gamma_1>2\beta`$, then every possible $`cs_1`$ lies inside the interior box and $`\omega=L^{-M}`$.

For every fixed nonzero nonce vector $`y`$, each individual coefficient of $`Ay`$ is a nonzero linear functional of the independent coefficients of the corresponding row of $`A`$. It is therefore exactly uniform. No polynomial component of $`y`$ needs to be a unit.

When $`y=0`$, the real high coefficient is zero with certainty. Its residual is $`L_\alpha(-(cs_2)_i)=-(cs_2)_i`$, an ordinary low value because $`|(cs_2)_i|\le\beta<a`$. The replacement then outputs a uniform high coefficient and is zero with probability $`1/p`$.

Consequently the real-minus-replacement acceptance-probability difference of the stated test is exactly

**(S4)**

```math
\boxed{
\Delta_{\mathrm{marg}}
=p_z\left[
(1-\omega)\frac{1-\theta}{q}
+\omega\left(1-\frac1p\right)
\right].
}
```

Since $`1-1/p\ge(1-\theta)/q`$, (S2) gives

**(S5)**

```math
\boxed{
\Delta_{\mathrm{marg}}
\ge
\frac{p_z\eta}{(2\eta+1)q}.
}
```

This is an exact lower bound in the single-transcript random-matrix experiment, even after the two experiments retain their common public key and shuffled hints: the test simply ignores the additional coordinates.

For parameter families with polynomially bounded $`q`$ and inverse-polynomial $`p_z`$, this is a nonnegligible decision advantage. At the displayed ML-DSA parameter shapes it is a small but explicit probability gap. It contradicts indistinguishability of these two particular distributions at a smaller claimed advantage; it does not make a theorem with that hardness premise logically false. The premise can fail.

## A local repair

The correct conditional high distribution for a prescribed ordinary residual $`r`$ and dummy shift $`d'`$ can be defined by the exact preimage fiber:

**(S6)**

```math
J\leftarrow U(\{0,\ldots,p-1\}),
\qquad
u=H(\alpha J+r+d'\pmod q).
```

For the exceptional residual $`r=-a`$, the unique preimage gives

```math
u=H(q-a+d').
```

To verify the repair in the uniform scalar comparison, first draw $`r`$ with its genuine low-part law. Choosing a uniform point in its fiber makes the reconstructed pre-shift field element uniform. Adding any independent fixed or random $`d'`$ preserves that uniform law. Its high part therefore has the correct marginal $`(\alpha+1)/q`$.

This repairs the isolated high marginal. It is not a simulation theorem for the joint public key, indexed high vector, histogram, and many observations under one fixed secret. The [boundary statistic](boundary_statistic.md) detects a correlation with the actual persistent secret, and the [security consequence](security_scope.md) explains the additional requirement on a simulator for repeated views.

## Separation of conclusions

The marginal discrepancy concerns the source's precise replacement rule. The repeated-transcript theorem concerns the genuine observation distribution and is independent of how that replacement rule is repaired. The [related-work account](../references/RELATED_WORK.md) treats elementary rounding arithmetic as an inherited ingredient and locates the consequential contribution in the repeated-view analysis.
