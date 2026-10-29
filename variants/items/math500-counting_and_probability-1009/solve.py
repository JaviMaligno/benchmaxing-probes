from itertools import product
from math import comb

def count(total, kinds):
    # brute force: number of nonnegative integer tuples (one count per kind) summing to total
    return sum(1 for t in product(range(total + 1), repeat=kinds) if sum(t) == total)

orig = count(6, 3)
assert orig == 28 == comb(6 + 2, 2), orig
print("original:", orig)

var = count(7, 3)
assert var == comb(7 + 2, 2)
print("variant:", var)
