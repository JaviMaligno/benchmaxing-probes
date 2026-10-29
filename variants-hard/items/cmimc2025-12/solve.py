from fractions import Fraction as F
from itertools import product

def exact(p1, pink, sick):
    """Probability the total on the day it first reaches >= pink is < sick (DP over totals)."""
    p2 = 1 - p1
    dist = {0: F(1)}  # probability of being at total t (t < pink) at some point
    reach = [F(0)] * (pink + 2)
    reach[0] = F(1)
    for t in range(pink):
        reach[t + 1] += reach[t] * p1
        reach[t + 2] += reach[t] * p2
    # first total >= pink is pink (if reached exactly) or pink+1 (jump from pink-1)
    return sum(reach[t] for t in range(pink, sick))

def brute(p1, pink, sick):
    """Enumerate all sequences of day-choices of length pink (enough to cross threshold)."""
    p2 = 1 - p1
    tot = F(0)
    for seq in product((1, 2), repeat=pink):
        s = 0; pr = F(1)
        for x in seq:
            s += x; pr *= p1 if x == 1 else p2
            if s >= pink:
                break
        # each prefix counted once per completion; normalise by unused tail
        pass
    # cleaner: recursive enumeration of stopped paths
    def rec(s, pr):
        if s >= pink:
            return pr if s < sick else F(0)
        return rec(s + 1, pr * p1) + rec(s + 2, pr * p2)
    return rec(0, F(1))

orig = exact(F(1, 2), 10, 11)
print("original:", orig, brute(F(1, 2), 10, 11), orig == F(683, 1024))
var = exact(F(2, 3), 8, 9)
print("variant:", var, brute(F(2, 3), 8, 9), float(var))
print("closed form 3/4+(1/4)(-1/3)^8:", F(3, 4) + F(1, 4) * F(-1, 3) ** 8)
