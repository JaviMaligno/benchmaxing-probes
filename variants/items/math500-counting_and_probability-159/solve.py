# Brute force: circular seatings up to rotation, each party contiguous.
from itertools import permutations
from math import factorial

def contiguous_circ(labels, party):
    n = len(labels)
    # party is contiguous on circle iff number of "starts" (party seat whose predecessor isn't party) is <= 1
    starts = sum(1 for i in range(n) if labels[i] == party and labels[i-1] != party)
    return starts <= 1

def count(d, r):
    # people: Independent fixed at seat 0 (canonical rep. of rotation class, since all people distinct)
    people = ['D%d' % i for i in range(d)] + ['R%d' % i for i in range(r)]
    total = 0
    for p in permutations(people):
        labels = ['I'] + [x[0] for x in p]
        if contiguous_circ(labels, 'D') and contiguous_circ(labels, 'R'):
            total += 1
    return total

def formula(d, r):
    return 2 * factorial(d) * factorial(r)

orig = count(5, 5)
print("original brute:", orig, "formula:", formula(5, 5))
assert orig == 28800
var = count(6, 4)
print("variant brute:", var, "formula:", formula(6, 4))
assert var == formula(6, 4)
