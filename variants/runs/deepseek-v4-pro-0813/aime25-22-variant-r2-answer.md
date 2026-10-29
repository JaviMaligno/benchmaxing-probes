<tool_calls>
<tool_calls>
  <template name="write_file"><repo>/variants/runs/probe_calc.py</template>
  <template name="contents">
"""Cálculo de probabilidad para el problema de divisores de 675."""
from math import gcd, lcm
from itertools import combinations, chain, combinations as comb_iter

S = [d for d in range(1, 676) if 675 % d == 0]
print("Divisores de 675:", S)
print("Número de divisores:", len(S))

total_subsets = 2 ** len(S) - 1  # nonempty
print("Subconjuntos no vacíos:", total_subsets)

favorable = 0
favorable_subsets = []
for r in range(1, len(S) + 1):
    for t in combinations(S, r):
        l = 1
        for x in t:
            l = lcm(l, x)
        if l == 675:
            favorable += 1
            favorable_subsets.append(t)

print("Subconjuntos favorables:", favorable)
print("Probabilidad:", favorable, "/", total_subsets)

from fractions import Fraction
frac = Fraction(favorable, total_subsets)
print("Fracción reducida:", frac)
print("m + n =", frac.numerator + frac.denominator)
print()
print("Subconjuntos favorables:")
for t in favorable_subsets:
    print(t)
</template>
</tool_calls>