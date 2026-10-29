from fractions import Fraction as F

def first_meet(rpm_a, rpm_b, limit_sec=100000):
    # rates in turns per second; brute force over t = n/den seconds using exact fractions
    ra, rb = F(rpm_a)/60, F(rpm_b)/60
    # gear marks north when turns are integers: t*ra and t*rb integral.
    # enumerate candidate times t that make gear A integral: t = k / ra
    k = 1
    while True:
        t = F(k) / ra
        if (t * rb).denominator == 1:
            return t
        k += 1
        if t > limit_sec:
            return None

orig = first_meet(F(100, 3), 45)
print("original:", orig)
assert orig == 36
var = first_meet(F(75, 2), 54)
print("variant:", var)
# independent check: scan seconds in steps of 1/100
cands = [F(n, 100) for n in range(1, 10000) if (F(n,100)*F(75,2)/60).denominator == 1 and (F(n,100)*F(54)/60).denominator == 1]
print("scan min:", cands[0])
assert cands[0] == var
