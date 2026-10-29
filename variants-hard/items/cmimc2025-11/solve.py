from itertools import permutations
from fractions import Fraction

def prob(word):
    """Beads (labeled, so all n! placements equally likely) put on a circular
    bracelet; success if the bracelet reads `word` up to rotation/reflection."""
    n = len(word)
    targets = set()
    for s in (word, word[::-1]):
        for r in range(n):
            targets.add(s[r:] + s[:r])
    perms = list(permutations(word))
    good = sum(''.join(q) in targets for q in perms)
    return Fraction(good, len(perms))

# Independent check: count via distinct circular arrangements (multiset perms with
# position 0 fixed is not needed; use dihedral orbit size / number of multiset strings)
def prob_orbit(word):
    n = len(word)
    strings = set(''.join(q) for q in permutations(word))
    orbit = set()
    for s in (word, word[::-1]):
        for r in range(n):
            orbit.add(s[r:] + s[:r])
    return Fraction(len(orbit), len(strings))

orig = prob("CMIMC")
assert orig == Fraction(1, 6) == prob_orbit("CMIMC"), orig
print("original CMIMC:", orig)
var = prob("LETTER")
assert var == prob_orbit("LETTER")
print("variant LETTER:", var)
