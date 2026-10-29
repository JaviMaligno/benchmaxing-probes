from fractions import Fraction
from math import comb
from itertools import product

def answer(n, m):
    # exact count of subsets of size k for each residue class
    total = 2**n
    cnt = [0]*m
    for k in range(n+1):
        cnt[k % m] += comb(n, k)
    return sum(abs(Fraction(c, total) - Fraction(1, m)) for c in cnt), cnt

def brute(n, m):
    cnt = [0]*m
    for mask in range(2**n):
        cnt[bin(mask).count('1') % m] += 1
    return sum(abs(Fraction(c, 2**n) - Fraction(1, m)) for c in cnt)

orig, _ = answer(18, 5)
print("original (n=18, m=5):", orig, "matches 9349/327680:", orig == Fraction(9349, 327680))
print("brute original:", brute(18, 5) == orig)
for n, m in [(20, 5), (19, 5), (17, 5), (20, 6), (19, 6), (18, 6), (20, 7)]:
    a, c = answer(n, m)
    print(n, m, a, float(a))
var, _ = answer(20, 5)
print("variant (n=20, m=5):", var, "brute:", brute(20, 5) == var)
