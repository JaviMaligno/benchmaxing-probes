# Tower a^a^...^a (height h) mod m, via generalized Euler theorem with exact
# "is the true value >= threshold" tracking. Height is astronomically large in both
# problems; the residue stabilises after a few levels, so we check stability.
from sympy import totient

def tower(a, h, m):
    """Return (value mod m, capped true value) for a tower of height h."""
    CAP = 10**6
    if m == 1:
        # still need capped true value
        pass
    if h == 1:
        return a % m, min(a, CAP)
    phi = int(totient(m)) if m > 1 else 1
    e_mod, e_true = tower(a, h - 1, phi)
    # generalized Euler: a^e = a^(e mod phi + phi) mod m when e >= log2(m)
    if e_true >= 64:
        r = pow(a, e_mod + phi, m)
    else:
        r = pow(a, e_true, m)
    true = CAP if e_true >= 20 else min(a ** e_true, CAP)
    return r, true

def stable(a, m, start=10, stop=40):
    vals = {tower(a, h, m)[0] for h in range(start, stop)}
    assert len(vals) == 1, vals
    return vals.pop()

# Brute-force sanity check of tower() on small heights against Python big ints
for a in (3, 7):
    for m in (333, 777, 36, 37):
        assert tower(a, 2, m)[0] == pow(a, a, m)
        assert tower(a, 3, m)[0] == pow(a, a**a, m)

orig = stable(3, 333)
print("original (3-tower mod 333):", orig)
assert orig == 36
var = stable(7, 777)
print("variant (7-tower mod 777):", var)
# independent CRT check: mod 3 ->1, mod 7 ->0, mod 37 -> 7^7
from sympy.ntheory.modular import crt
print("CRT check:", crt([3, 7, 37], [1, 0, pow(7, 7, 37)])[0])
