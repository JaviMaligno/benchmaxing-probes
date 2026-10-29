# Count ordered triples (a,b,c), 1<=a,b,c<=B, with a^3+b^3+c^3 == 0 mod M.
# Method: distribution of cubes mod M, then convolution (exact integer counting).
from collections import Counter
from itertools import product

def count(B, M):
    d = Counter(pow(x, 3, M) for x in range(1, B + 1))
    # pairwise sums
    pair = Counter()
    for r1, c1 in d.items():
        for r2, c2 in d.items():
            pair[(r1 + r2) % M] += c1 * c2
    return sum(c * pair.get((-r) % M, 0) for r, c in d.items())

def brute(B, M):
    return sum(1 for a, b, c in product(range(1, B + 1), repeat=3) if (a**3 + b**3 + c**3) % M == 0)

# sanity: convolution vs brute force on small cases
for k in (2, 3):
    assert count(3**k, 3**(k + 1)) == brute(3**k, 3**(k + 1))
    assert count(5**2, 5**3) == brute(5**2, 5**3)

orig = count(3**6, 3**7)
print("original N =", orig, "N mod 1000 =", orig % 1000)
assert orig % 1000 == 735

var = count(3**7, 3**8)
print("variant N =", var, "N mod 1000 =", var % 1000)
