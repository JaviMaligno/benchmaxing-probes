# f(x) = sin(a*pi*sin(b*x)) on 0 < x < 2*pi: count zeros n and tangency points t, return n + t.
import math
import numpy as np

def exact(a, b):
    roots = set()
    for k in range(-a, a + 1):
        c = k / a
        s = math.asin(c)
        for m in range(-2, 2 * b + 3):
            for base in (s, math.pi - s):
                x = (base + 2 * math.pi * m) / b
                if 1e-9 < x < 2 * math.pi - 1e-9:
                    roots.add(round(x, 9))
    n = len(roots)
    # tangent: f'(x) = a*pi*b*cos(b x)*cos(a pi sin(bx)) = 0 at a zero  <=> cos(bx)=0
    t = sum(1 for x in roots if abs(math.cos(b * x)) < 1e-7)
    return n, t

def numeric(a, b, N=4_000_000):
    # independent check: zeros of f <=> g(x)=a*sin(bx) is an integer.
    # Transversal zeros = crossings of integer levels strictly between -a and a (counted on a dense grid);
    # touching zeros = interior extrema of g, where g = +-a exactly.
    x = np.linspace(0, 2 * math.pi, N + 1)[1:-1]
    g = np.clip(a * np.sin(b * x), -a + 1e-6, a - 1e-6)
    crossings = int(np.sum(np.abs(np.diff(np.floor(g)))))
    # g(x) passes 0 at grid-free points; x=0 and 2pi are excluded (open interval), sin(bx)=0 interior roots are crossings.
    t = sum(1 for j in range(4 * b) if 0 < (math.pi / 2 + math.pi * j) / b < 2 * math.pi)
    return crossings + t, t

for label, a, b, expected in [("original", 7, 5, 149), ("variant", 8, 6, None)]:
    n, t = exact(a, b)
    n2, t2 = numeric(a, b)
    print(f"{label}: a={a}, b={b}: exact n={n}, t={t}, n+t={n+t}; numeric n={n2}, t={t2}; formula 4ab-1+2b={4*a*b-1+2*b}")
    if expected is not None:
        assert n + t == expected, (n + t, expected)
        print(f"{label} matches official answer {expected}")
