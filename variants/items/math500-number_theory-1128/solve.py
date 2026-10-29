from sympy import primerange

def sum_bad_primes(a, b=1, bound=2000):
    # brute force: primes p for which a*x = b (mod p) has no solution x
    total = 0
    for p in primerange(2, bound):
        if not any((a * x - b) % p == 0 for x in range(p)):
            total += p
    return total

orig = sum_bad_primes(8)
print("original (8x=1 mod p):", orig)
assert orig == 2
var = sum_bad_primes(45)
print("variant (45x=1 mod p):", var)
