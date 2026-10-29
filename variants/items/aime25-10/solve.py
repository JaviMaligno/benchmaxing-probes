from itertools import permutations
from math import factorial
from sympy import factorint

def row2_count_brute(w):
    # first row fixed as 0..3w-1 in order; block b = columns b*w..b*w+w-1
    n = 3*w
    blk = lambda c: c // w
    cnt = 0
    for p in permutations(range(n)):
        if all(blk(p[c]) != blk(c) for c in range(n)):  # number p[c] sat in row1 block blk(p[c])
            cnt += 1
    return cnt

def row2_count_formula(w):
    # casework: block 0 of row2 takes k numbers from row1-block1, w-k from block2
    f = factorial
    from math import comb
    tot = 0
    for k in range(w+1):
        # block0 row2: k from B1, w-k from B2; block1 row2: then needs w-k... from B0 and B2
        # B2 remaining w-(w-k)=k go to block1, so block1 takes k from B2, w-k from B0; block2 takes k from B0, w-k from B1
        tot += comb(w,k)**3 * comb(w, w-k)**0 * 1
    return tot * f(w)**3

def total(w, brute=True):
    n = 3*w
    r2 = row2_count_brute(w) if brute else row2_count_formula(w)
    return factorial(n) * r2 * factorial(w)**3

def score(N):
    return sum(p*a for p, a in factorint(N).items()), factorint(N)

# brute-force check of the full count on the variant via direct grid enumeration (w=2)
def total_full_brute(w):
    n = 3*w
    blk = lambda c: c // w
    rows = list(permutations(range(n)))
    cnt = 0
    r1 = tuple(range(n))
    for r2 in rows:
        if any(set(r1[b*w:(b+1)*w]) & set(r2[b*w:(b+1)*w]) for b in range(3)): continue
        for r3 in rows:
            if all(len(set(r1[b*w:(b+1)*w])|set(r2[b*w:(b+1)*w])|set(r3[b*w:(b+1)*w]))==n for b in range(3)):
                cnt += 1
    return factorial(n)*cnt

# ORIGINAL (w=3, 3x9, digits 1-9)
No = total(3, brute=True)
print("original count", No, "formula agrees:", No == total(3, brute=False), "score", score(No))
assert score(No)[0] == 81
# VARIANT (w=2, 3x6 grid, numbers 1-6, three 3x2 blocks)
Nv = total(2, brute=True)
Nv_full = total_full_brute(2)
print("variant count", Nv, "full-grid brute force:", Nv_full, "formula:", total(2, brute=False))
assert Nv == Nv_full == total(2, brute=False)
print("variant score", score(Nv))
