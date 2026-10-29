# aime25-17 variant check: sum of positive n with (n+s) | c*(n+a)*(n^2+b)
from sympy import divisors

def brute(s, c, a, b, N=10**5):
    return sum(n for n in range(1, N) if (c*(n+a)*(n*n+b)) % (n+s) == 0)

def residue_method(s, c, a, b):
    r = c*(-s+a)*(s*s+b)          # value of the product at n = -s
    return sum(d - s for d in divisors(abs(r)) if d - s >= 1)

orig = (2, 3, 3, 9)   # n+2 | 3(n+3)(n^2+9)
var  = (3, 2, 5, 7)   # n+3 | 2(n+5)(n^2+7)
o_b, o_r = brute(*orig), residue_method(*orig)
v_b, v_r = brute(*var), residue_method(*var)
print("original brute:", o_b, "residue:", o_r, "expected 49:", o_b == o_r == 49)
print("variant  brute:", v_b, "residue:", v_r)
assert o_b == o_r == 49 and v_b == v_r
print("VARIANT ANSWER:", v_b)
