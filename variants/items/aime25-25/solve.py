from itertools import combinations
from math import comb

def brute(n, k):
    """Subsets of k chairs from n in a row with no three consecutive chairs (no one sits next to two others)."""
    cnt = 0
    for s in combinations(range(n), k):
        ss = set(s)
        if not any(i in ss and i+1 in ss and i+2 in ss for i in range(n-2)):
            cnt += 1
    return cnt

def formula(n, k):
    # gaps method: k occupied split into blocks of size 1 or 2, placed in n-k+1 gap slots
    tot = 0
    for b in range(0, k+1):          # b blocks of size 2
        blocks = k - b               # number of blocks
        if blocks < 0: continue
        tot += comb(blocks, b) * comb(n - k + 1, blocks)
    return tot

# Original: 16 chairs, 8 people
N0 = brute(16, 8); assert N0 == formula(16, 8)
print("original N =", N0, "mod 1000 =", N0 % 1000)
assert N0 % 1000 == 907

# Variant: 17 chairs, 9 people
N1 = brute(17, 9); assert N1 == formula(17, 9)
print("variant N =", N1, "mod 1000 =", N1 % 1000)
