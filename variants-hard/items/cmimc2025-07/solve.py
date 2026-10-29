# Brute force: a_n is the integer whose digits are the last digits of 1..n.
def v3(m):
    t = 0
    while m % 3 == 0:
        m //= 3
        t += 1
    return t

def S(N):
    a = 0; s = 0
    for n in range(1, N + 1):
        a = a * 10 + n % 10
        s += v3(a)
    return s

orig = S(810)
print("original (N=810):", orig)
assert orig == 932
print("variant (N=1080):", S(1080))
