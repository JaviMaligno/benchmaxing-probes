# Horizontal-chord problem: continuous f, exactly N integer-length horizontal chords,
# one of length n. Known extremal answer: N_min = 2n - 1.
# (1) Formula check on original (n=2025 -> 4049) and variant (n=2030).
# (2) Independent numeric check of the lower bound N >= 2n-1 for small n:
#     random piecewise-linear f with f(0)=f(n)=0, extended linearly (slope c>0 on both
#     sides, so only finitely many chords). Chords of length k <-> zeros of f(x+k)-f(x).
import numpy as np

def nmin(n): return 2*n - 1

assert nmin(2025) == 4049, "original answer not reproduced"
print("original n=2025 ->", nmin(2025))
print("variant  n=2030 ->", nmin(2030))

rng = np.random.default_rng(0)
def make_f(n, m, c=50.0):
    xs = np.linspace(0, n, m+1)
    ys = rng.normal(0, 1, m+1); ys[0] = ys[-1] = 0.0
    def f(x):
        x = np.asarray(x, float)
        inside = np.interp(x, xs, ys)
        return np.where(x < 0, c*x, np.where(x > n, c*(x-n), inside))
    return f, ys

def count_chords(f, n, ys, c=50.0):
    span = 2*np.abs(ys).max()/c + 1
    lo, hi = -span - 1, n + span + 1
    dx = 1/20000
    x = np.arange(np.floor(lo), np.ceil(hi), dx)  # contains x=0 exactly
    x = np.round(x/dx)*dx
    fx = None
    total = 0
    K = int(hi - lo) + 2
    for k in range(1, K+1):
        h = f(x + k) - f(x)
        s = np.sign(h)
        # exact zero at x=0 for k=n handled as a sign change
        total += np.count_nonzero(s[:-1]*s[1:] < 0) + np.count_nonzero(s == 0)
    return total

worst = {}
for n in (1, 2, 3):
    mins = []
    for t in range(40):
        f, ys = make_f(n, int(rng.integers(3, 9))*n)
        mins.append(count_chords(f, n, ys))
    worst[n] = min(mins)
    print(f"n={n}: min chords over random samples = {worst[n]}, bound 2n-1 = {nmin(n)}")
    assert worst[n] >= nmin(n)
print("ANSWER", nmin(2030))
