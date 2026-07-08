"""One-sided Fisher's exact test (treatment pass rate > control).

Usage: python fisher.py <treat_pass> <treat_fail> <ctrl_pass> <ctrl_fail>
p = P(X >= treat_pass) under the hypergeometric null with fixed margins.
"""
import sys
from math import comb


def fisher_one_sided(a: int, b: int, c: int, d: int) -> float:
    n1, n2, k = a + b, c + d, a + c
    total = comb(n1 + n2, k)
    return sum(comb(n1, i) * comb(n2, k - i) for i in range(a, min(n1, k) + 1)) / total


if __name__ == "__main__":
    a, b, c, d = map(int, sys.argv[1:5])
    p = fisher_one_sided(a, b, c, d)
    print(f"table=[[{a},{b}],[{c},{d}]]  one-sided p = {p:.6g}  ({'SIGNIFICANT' if p < 0.005 else 'not significant'} at alpha=0.005)")

    # self-check: 6v6 perfect separation must equal 1/C(12,6)
    assert abs(fisher_one_sided(6, 0, 0, 6) - 1 / comb(12, 6)) < 1e-12
    assert fisher_one_sided(3, 3, 3, 3) > 0.5
