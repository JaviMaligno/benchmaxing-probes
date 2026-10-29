# Modular inverse: brute force + pow(), checked on original data.
def inv_brute(a, m):
    return [n for n in range(m) if (a * n) % m == 1]

def solve(a, m):
    b = inv_brute(a, m)
    assert len(b) == 1 and b[0] == pow(a, -1, m)
    return b[0]

orig = solve(17, 83)
print("original 17^-1 mod 83 =", orig)
assert orig == 44

assert (13 * 7) % 89 == 2  # hint in variant
var = solve(13, 89)
print("variant 13^-1 mod 89 =", var)
