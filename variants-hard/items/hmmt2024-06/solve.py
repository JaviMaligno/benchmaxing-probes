# Brute force: m = 2n+3 divides 2^{n!}-1 iff 2^{n!} == 1 (mod m).
# Compute 2^{n!} mod m by iterated powering: x <- x^k for k=1..n.
def bad_sum(lo, hi):
    s, bad = 0, []
    for n in range(lo, hi + 1):
        m = 2 * n + 3
        x = 2 % m
        for k in range(1, n + 1):
            x = pow(x, k, m)
        if x != 1:
            s += n; bad.append(n)
    return s, bad

orig, ob = bad_sum(50, 100)
print("original:", orig, ob)
assert orig == 222
var, vb = bad_sum(60, 120)
print("variant:", var, vb)
