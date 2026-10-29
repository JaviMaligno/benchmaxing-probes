from math import factorial
from sympy import divisors

def s(n, d):
    return sum(x for x in divisors(factorial(n)) if x % 10 == d)

orig = s(9, 1)
print("original (9!, units digit 1):", orig)
assert orig == 103
var = s(11, 3)
print("variant (11!, units digit 3):", var)
