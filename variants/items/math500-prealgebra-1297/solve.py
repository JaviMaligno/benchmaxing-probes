from math import factorial

def zeros_legendre(n):
    c, p = 0, 5
    while p <= n:
        c += n // p; p *= 5
    return c

def zeros_brute(n):
    s = str(factorial(n))
    return len(s) - len(s.rstrip('0'))

# Original: 42! -> 9
assert zeros_legendre(42) == zeros_brute(42) == 9
print("original 42!:", zeros_brute(42))
# Variant: 47!
a, b = zeros_legendre(47), zeros_brute(47)
assert a == b
print("variant 47!:", b)
