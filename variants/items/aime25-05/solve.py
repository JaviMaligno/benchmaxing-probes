from itertools import permutations

def count_div(digits, m):
    """Brute force: permutations of the digits (no leading zero) divisible by m."""
    c = 0
    for p in permutations(digits):
        if p[0] == 0:
            continue
        if int(''.join(map(str, p))) % m == 0:
            c += 1
    return c

# Original: digits 1..8, divisible by 22, answer N - 2025
N_orig = count_div(range(1, 9), 22)
print("original N =", N_orig, "answer =", N_orig - 2025)
assert N_orig - 2025 == 279

# Variant: digits 1..9 (nine-digit numbers), divisible by 22, answer N - 14025
N_var = count_div(range(1, 10), 22)
ans = N_var - 14025
print("variant N =", N_var, "answer =", ans)

# Independent combinatorial check: 5 odd positions (incl. last), 4 even positions,
# odd-position sum must be 17 or 28, last digit even.
from itertools import combinations
from math import factorial
tot = 0
for odd in combinations(range(1, 10), 5):
    if sum(odd) in (17, 28):
        ev = sum(1 for d in odd if d % 2 == 0)
        tot += ev * factorial(4) * factorial(4)
print("combinatorial N =", tot)
assert tot == N_var
assert ans == 375
