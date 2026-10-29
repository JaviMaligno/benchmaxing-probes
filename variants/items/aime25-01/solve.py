# Brute force: sum of bases b > minb with (d1 d0)_b dividing (e1 e0)_b.
# Divisor b+d0 must be <= dividend e1*b+e0 < e1*(b+d0) ... bounded; search generously.
def solve(div, num, minb, limit=100000):
    tot, bases = 0, []
    for b in range(minb + 1, limit):
        a = div[0] * b + div[1]
        n = num[0] * b + num[1]
        if n % a == 0:
            tot += b; bases.append(b)
    return tot, bases

orig = solve((1, 7), (9, 7), 9)
print("original (17_b | 97_b, b>9):", orig)
assert orig[0] == 70
var = solve((1, 8), (9, 8), 9)
print("variant (18_b | 98_b, b>9):", var)
