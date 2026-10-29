from itertools import combinations

def components(n, k):
    N = 1 << n
    parent = list(range(N))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    masks = [sum(1 << i for i in c) for c in combinations(range(n), k)]
    for v in range(N):
        rv = find(v)
        for m in masks:
            ru = find(v ^ m)
            if ru != rv:
                parent[ru] = rv
    return len({find(v) for v in range(N)})

def formula(n, k):
    if k == n: return 2 ** (n - 1)
    return 1 if k % 2 else 2

def total(N, brute=True):
    s = 0
    for n in range(1, N + 1):
        for k in range(1, n + 1):
            c = components(n, k) if brute else formula(n, k)
            if brute: assert c == formula(n, k), (n, k)
            s += c
    return s

assert components(3, 2) == 2
orig = total(10)
print("original (n<=10):", orig, "expected 1088:", orig == 1088)
var = total(12)
print("variant (n<=12):", var)
