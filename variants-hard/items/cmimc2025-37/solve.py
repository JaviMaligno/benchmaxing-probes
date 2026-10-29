# Brute force: coefficients of (1+x+x^2)^n mod 3, computed by repeated polynomial
# multiplication with coefficients reduced mod 3 (exact), then count those == r.
def count(n, r):
    p = [1]
    for _ in range(n):
        q = [0] * (len(p) + 2)
        for i, c in enumerate(p):
            if c:
                q[i] = (q[i] + c) % 3
                q[i + 1] = (q[i + 1] + c) % 3
                q[i + 2] = (q[i + 2] + c) % 3
        p = q
    assert len(p) == 2 * n + 1
    return sum(1 for c in p if c == r)

# Independent check via 1+x+x^2 = (1-x)^2 mod 3 and Lucas' theorem
from math import comb
def lucas(m, k):
    res = 1
    while m or k:
        res = res * comb(m % 3, k % 3) % 3
        m //= 3; k //= 3
    return res
def count_lucas(n, r):
    return sum(1 for k in range(2 * n + 1) if (lucas(2 * n, k) * (-1) ** k) % 3 == r)

orig = count(2024, 1)
print("original (n=2024, r=1):", orig, count_lucas(2024, 1))
assert orig == 648
var = count(2019, 1)
print("variant (n=2019, r=1):", var, count_lucas(2019, 1))
assert var == count_lucas(2019, 1)
assert var == 216
