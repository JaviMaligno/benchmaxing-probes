from itertools import combinations
from math import comb

def brute(a, b, k):
    people = ['A']*a + ['B']*b
    return sum(1 for c in combinations(range(a+b), k) if len({people[i] for i in c}) == 2)

def formula(a, b, k):
    return comb(a+b, k) - comb(a, k) - comb(b, k)

# original: 8 Republicans, 6 Democrats, subcommittee of 5
o = brute(8, 6, 5); assert o == formula(8, 6, 5) == 1940
print("original:", o)
# variant: 9 engineers, 6 designers, task force of 5
v = brute(9, 6, 5); assert v == formula(9, 6, 5)
print("variant:", v)
