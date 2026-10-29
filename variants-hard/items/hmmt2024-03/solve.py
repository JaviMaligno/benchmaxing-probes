# Brute force: sum of two-digit x such that for every n-digit N divisible by x,
# the left-rotation of N's digits (first digit moved to the end) is divisible by x.
def rot(N):
    s = str(N)
    return int(s[1:] + s[0])

def solve(ndig):
    lo, hi = 10**(ndig-1), 10**ndig
    good = []
    for x in range(10, 100):
        if all(rot(N) % x == 0 for N in range(lo, hi) if N % x == 0):
            good.append(x)
    return good, sum(good)

g, s = solve(3)
print("original (3-digit):", g, s)
assert s == 64
g, s = solve(4)
print("variant (4-digit):", g, s)
