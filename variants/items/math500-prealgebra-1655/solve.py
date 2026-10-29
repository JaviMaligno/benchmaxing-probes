from fractions import Fraction

def prob(N, a, b):
    # brute force over 1..N: divisible by a and not divisible by b
    cnt = sum(1 for n in range(1, N + 1) if n % a == 0 and n % b != 0)
    # independent check via floor counting (a, b coprime here)
    assert cnt == N // a - N // (a * b)
    return Fraction(cnt, N)

orig = prob(100, 2, 3)
print("original:", orig)
assert orig == Fraction(17, 50)
var = prob(200, 3, 5)
print("variant:", var)
