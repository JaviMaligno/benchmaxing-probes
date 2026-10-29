# Numeric brute force with high precision: S(c) = sum_{n>=1} sgn(sin(c*2^n))/2^n
from mpmath import mp, mpf, sin, pi, sign
mp.dps = 400  # enough to evaluate sin(c*2^n) exactly in sign for n <= 1000

def S(c, N=1000):
    return sum(int(sign(sin(c * mpf(2)**n))) * mpf(2)**(-n) for n in range(1, N + 1))

# Closed form via binary digits: sgn(sin(c*2^n)) = 1 - 2*b_n, b_n = n-th binary digit of frac(c/pi)
def closed(c):
    x = mpf(c) / pi
    return 1 - 2 * (x - int(x))

orig = S(1); print("original numeric:", mp.nstr(orig, 30), " 1-2/pi =", mp.nstr(1 - 2/pi, 30))
assert abs(orig - (1 - 2/pi)) < mpf(10)**-250
var = S(3); print("variant numeric:", mp.nstr(var, 30), " 1-6/pi =", mp.nstr(1 - 6/pi, 30), " closed:", mp.nstr(closed(3), 30))
assert abs(var - (1 - 6/pi)) < mpf(10)**-250
print("OK: original 1-2/pi reproduced; variant answer 1-6/pi")
