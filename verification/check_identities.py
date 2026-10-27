#!/usr/bin/env python3
"""Finite arithmetic checks for the mathematical identities in this repository.

This program enumerates small finite distributions and sparse multiplication
matrices. It also substitutes published parameter shapes into analytical bounds.
It does not ingest signatures, simulate a signing service, or recover a key.
Only Python's standard library is required.
"""

from collections import Counter
from decimal import Decimal, localcontext
from fractions import Fraction as F
from itertools import combinations, product
from math import ceil, comb
import json
from pathlib import Path


def decompose(x, q, alpha):
    x %= q
    a = alpha // 2
    r = x % alpha
    if r > a:
        r -= alpha
    if x - r == q - 1:
        return 0, r - 1
    return (x - r) // alpha, r


def weight(r, a, beta):
    v = r + a
    return v if 1 <= v <= beta else 0


def scalar_checks():
    count = 0
    pairs = 0
    for q in (13, 17, 29, 41, 61):
        for alpha in range(4, (q - 1) // 2 + 1, 2):
            if (q - 1) % alpha:
                continue
            p, a = (q - 1) // alpha, alpha // 2
            table = [decompose(x, q, alpha) for x in range(q)]
            assert all((alpha * h + r - x) % q == 0
                       for x, (h, r) in enumerate(table))
            hc = Counter(h for h, _ in table)
            lc = Counter(r for _, r in table)
            assert hc[0] == alpha + 1
            assert all(hc[h] == alpha for h in range(1, p))
            assert lc[-a] == 1
            assert all(lc[r] == p for r in range(-a + 1, a + 1))
            pairs += 1
            for beta in sorted({1, min(3, a - 1), a - 1}):
                s1 = beta * (beta + 1) // 2
                mu = F(p * s1, q)
                for d in range(-beta, beta + 1):
                    m = F(0)
                    for x in range(q):
                        h = table[x][0]
                        r = table[(x - d) % q][1]
                        m += (F(h == 0) - F(alpha + 1, q)) * (
                            F(weight(r, a, beta)) - mu)
                    m /= q
                    expected = F(max(-d, 0), q) - F((p - 1) * s1, q*q)
                    assert m == expected
                    for v in range(1, beta + 1):
                        selected = [x for x in range(q)
                                    if table[(x - d) % q][1] == -a + v]
                        assert len(selected) == p
                        assert sum(table[x][0] == 0 for x in selected) == (
                            1 + (d == -v))
                        count += 1
                # eta=1, tau=1: the dummy shift is uniform on {-1,0,1}.
                theta = F(2, 3)
                fake = F(q - 1, q*p) + theta / q
                assert F(alpha + 1, q) - fake == F(1, 3*q)
                # Exact conditional-preimage repair, for each fixed dummy shift.
                for d in (-1, 0, 1):
                    repaired = F(0)
                    for r, multiplicity in lc.items():
                        xs = ([q-a] if r == -a else
                              [(alpha*j+r) % q for j in range(p)])
                        assert len(xs) == multiplicity
                        conditional = F(sum(decompose(x+d, q, alpha)[0] == 0
                                            for x in xs), len(xs))
                        repaired += F(multiplicity, q) * conditional
                    assert repaired == F(alpha + 1, q)
    return {"rounding_parameter_pairs": pairs,
            "boundary_joint_counts": count}


def negacyclic_matrix(v, q=None):
    n = len(v)
    a = [[0] * n for _ in range(n)]
    for j in range(n):
        for u, x in enumerate(v):
            target = j + u
            a[target % n][j] = x if target < n else -x
    if q is not None:
        a = [[x % q for x in row] for row in a]
    return a


def rank(a, q):
    a = [row[:] for row in a]
    m, n = len(a), len(a[0])
    r = 0
    for j in range(n):
        pivot = next((i for i in range(r, m) if a[i][j] % q), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inverse = pow(a[r][j], -1, q)
        a[r] = [(x * inverse) % q for x in a[r]]
        for i in range(m):
            if i != r and a[i][j]:
                factor = a[i][j]
                a[i] = [(x - factor*y) % q for x, y in zip(a[i], a[r])]
        r += 1
        if r == m:
            break
    return r


def sparse_rank_checks():
    count = 0
    for n, q in ((4, 3), (4, 5), (8, 3)):
        for v in product(range(q), repeat=n):
            support = sum(x != 0 for x in v)
            if not support:
                continue
            assert rank(negacyclic_matrix(v, q), q) >= ceil(n/support)
            count += 1
    return {"nonzero_sparse_polynomials": count}


def challenge_covariance_check():
    n, tau = 4, 2
    total = [[0]*n for _ in range(n)]
    count = 0
    for support in combinations(range(n), tau):
        for signs in product((-1, 1), repeat=tau):
            c = [0]*n
            for index, sign in zip(support, signs):
                c[index] = sign
            a = negacyclic_matrix(c)
            for j in range(n):
                for k in range(n):
                    total[j][k] += sum(row[j]*row[k] for row in a)
            count += 1
    assert all(total[j][k] == count*tau*(j == k)
               for j in range(n) for k in range(n))
    return {"signed_weight_challenges": count}


def fourth_moment_checks():
    cases = [
        (13, 6, 2, (-2, 1), (1, -1)),
        (17, 8, 3, (-3, 0, 2), (1, -1, 0)),
        (13, 6, 2, (-2, -1, 1, 2), (1, 1, -1, 0)),
    ]
    total_tuples = 0
    for q, alpha, beta, shifts, coefficients in cases:
        dsize = len(shifts)
        p, a = (q-1)//alpha, alpha//2
        s1 = beta*(beta+1)//2
        s2 = beta*(beta+1)*(2*beta+1)//6
        p0, mu = F(alpha+1, q), F(p*s1, q)
        u, v = p0*(1-p0), F(p*s2, q)-mu*mu
        marginals = []
        mixed, fourth = [], []
        for d in shifts:
            values = []
            for x in range(q):
                hi = decompose(x, q, alpha)[0]
                lo = decompose(x-d, q, alpha)[1]
                un = q*(hi == 0)-(alpha+1)
                vn = q*weight(lo, a, beta)-p*s1
                values.append((un, vn))
            marginals.append(values)
            mixed.append(F(sum(un*vn for un, vn in values), q**3))
            fourth.append(F(sum(un*un*vn*vn for un, vn in values), q**5))
        total, total2 = 0, 0
        for row in product(*marginals):
            xn = sum(c*item[0] for c, item in zip(coefficients, row))
            yn = sum(item[1] for item in row)
            tn = xn*yn
            total += tn
            total2 += tn*tn
        observations = q**dsize
        total_tuples += observations
        exact_mean = F(total, observations*q*q)
        exact_second = F(total2, observations*q**4)
        tau = sum(c*c for c in coefficients)
        mixed_sum = sum(c*m for c, m in zip(coefficients, mixed))
        formula = tau*dsize*u*v + 2*mixed_sum*mixed_sum + sum(
            c*c*(w-u*v-2*m*m)
            for c, w, m in zip(coefficients, fourth, mixed))
        assert exact_mean == mixed_sum
        assert exact_second == formula
        mstar = F(beta, q)+F((p-1)*s1, q*q)
        upper = tau*((dsize-1)*u+1)*v + 2*tau*tau*mstar*mstar
        assert exact_second <= upper
    return {"fourth_moment_cases": len(cases),
            "independent_coordinate_tuples": total_tuples}


def resource_bounds():
    with localcontext() as context:
        context.prec = 80
        two, q, n = Decimal(2), 8380417, 256
        eps, delta = two**(-128), Decimal("0.01")
        rows = []
        shapes = [
            ("44", 4, 4, 2, 39, 2**17, 44),
            ("65", 6, 5, 4, 49, 2**19, 16),
            ("87", 8, 7, 2, 60, 2**19, 16),
        ]
        for label, k, ell, eta, tau, gamma, p in shapes:
            dsize, beta, m = k*n, eta*tau, ell*n
            alpha = (q-1)//p
            box = 2*(gamma-beta)-1
            p0 = Decimal(alpha+1)/q
            s1 = beta*(beta+1)//2
            s2 = beta*(beta+1)*(2*beta+1)//6
            mu = Decimal(p*s1)/q
            u, v = p0*(1-p0), Decimal(p*s2)/q-mu*mu
            mstar = Decimal(beta)/q+Decimal((p-1)*s1)/(q*q)
            b = tau*((dsize-1)*u+1)*v + 2*tau*tau*mstar*mstar
            pz = (Decimal(box)/(2*gamma))**m
            second = pz*(b+2*tau*tau*dsize*dsize*beta*beta*eps)
            limit = tau*dsize*beta
            tolerance = pz*tau/(8*q)
            count = ((2*second+Decimal(4)*limit*tolerance/3) /
                     (tolerance*tolerance)) * (2*Decimal(dsize)/delta).ln()
            log_count = count.ln()/two.ln()
            rounded = int(log_count.to_integral_value(rounding="ROUND_CEILING"))
            jr = (q**4-1)//(q-1)
            bad = (Decimal(comb(dsize, 4)*q**4*jr) *
                   Decimal(box)**(-ell*ceil(n/4)) / (4*eps*eps))
            assert dsize*beta*eps <= Decimal(1)/(16*q)
            rows.append({
                "shape": label,
                "beta": beta,
                "z_pass_probability": f"{pz:.12f}",
                "second_moment_comparison_bound": f"{b:.9f}",
                "log2_observation_bound": f"{log_count:.10f}",
                "sufficient_power_of_two": rounded,
                "log2_bad_matrix_bound": f"{bad.ln()/two.ln():.8f}",
                "scaled_mean_bias_bound": f"{2*q*dsize*beta*eps:.8E}",
            })
        assert [row["sufficient_power_of_two"] for row in rows] == [57, 61, 59]
        return rows


def main():
    report = {
        "scope": "Finite identity and bound checks; no signing or recovery experiment",
        "scalar": scalar_checks(),
        "sparse_rank": sparse_rank_checks(),
        "challenge_covariance": challenge_covariance_check(),
        "fourth_moment": fourth_moment_checks(),
        "analytical_parameter_substitution": resource_bounds(),
    }
    output = Path(__file__).with_name("results.json")
    output.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
