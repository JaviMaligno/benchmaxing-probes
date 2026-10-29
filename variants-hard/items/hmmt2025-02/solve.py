# sqrt(N) = a*sqrt(rest), N has k digits, a = leading digit, rest = remaining k-1 digits
# <=> N == a^2 * rest (exact integer check, both sides nonnegative)
def sols(k):
    out = []
    for N in range(10**(k-1), 10**k):
        a = N // 10**(k-1)
        rest = N % 10**(k-1)
        if N == a*a*rest:
            out.append(N)
    return out

orig = sols(4)
print("original (4-digit) solutions:", orig)
assert orig == [3375]
var = sols(5)
print("variant (5-digit) solutions:", var, "sum =", sum(var))
# independent float check
import math
for N in var:
    a, r = N // 10**4, N % 10**4
    assert abs(math.sqrt(N) - a*math.sqrt(r)) < 1e-9
print("ANSWER", sum(var))
