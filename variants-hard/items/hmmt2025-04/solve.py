from fractions import Fraction
def S(N, M):
    # brute force exact: sum_{j=-M}^{M} floor(N/(j+1/2)) = floor(2N/(2j+1))
    return sum((2*N)//(2*j+1) for j in range(-M, M+1))
def S_pair(N, M):
    # pairing method: j and -1-j cancel to -1 unless 2N/(2j+1) integer (i.e. 2j+1 | 2N, odd divisor of N)
    tot = 0
    for j in range(0, M):
        tot += 0 if (2*N) % (2*j+1) == 0 else -1
    tot += (2*N)//(2*M+1)
    return tot
orig = S(2025, 1000)
print("original:", orig, S_pair(2025,1000))
assert orig == -984
v = S(3150, 1200)
print("variant:", v, S_pair(3150,1200))
assert v == S_pair(3150,1200)
