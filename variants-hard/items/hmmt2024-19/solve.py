# Count triples (f,g,h) of permutations of {1..n} with
# fgh = hgf = g, ghf = fhg = h, hfg = gfh = f  (composition as functions).
from itertools import permutations

def comp(a, b):  # (a o b)(x) = a(b(x))
    return tuple(a[b[x]] for x in range(len(a)))

def inv(a):
    r = [0]*len(a)
    for i, v in enumerate(a):
        r[v] = i
    return tuple(r)

def count_fast(n):
    # f(g(h(x))) = g(x) forces h = (f o g)^{-1} o g; check all the rest.
    P = list(permutations(range(n)))
    c = 0
    for f in P:
        for g in P:
            h = comp(inv(comp(f, g)), g)
            if (comp(h, comp(g, f)) == g and comp(g, comp(h, f)) == h and
                comp(f, comp(h, g)) == h and comp(h, comp(f, g)) == f and
                comp(g, comp(f, h)) == f and comp(f, comp(g, h)) == g):
                c += 1
    return c

def count_brute(n):
    P = list(permutations(range(n)))
    c = 0
    for f in P:
        for g in P:
            for h in P:
                if (comp(f, comp(g, h)) == g and comp(h, comp(g, f)) == g and
                    comp(g, comp(h, f)) == h and comp(f, comp(h, g)) == h and
                    comp(h, comp(f, g)) == f and comp(g, comp(f, h)) == f):
                    c += 1
    return c

for n in (3, 4):
    assert count_brute(n) == count_fast(n), n
orig = count_fast(5)
print("original n=5:", orig, "(expected 146)", "OK" if orig == 146 else "MISMATCH")
print("variant  n=6:", count_fast(6))
