from fractions import Fraction as F

def dave_time(dist, others, dave_v0, factor=2):
    """Event simulation: Dave's speed multiplies by `factor` each time another runner finishes."""
    finishes = sorted(F(dist) / F(v) for v in others)
    t, pos, v = F(0), F(0), F(dave_v0)
    for tf in finishes + [None]:
        if tf is not None and tf <= t:
            v *= factor; continue
        if tf is None or pos + v * (tf - t) >= dist:
            return t + (F(dist) - pos) / v
        pos += v * (tf - t); t = tf; v *= factor

def numeric_check(dist, others, v0, factor=2, dt=1e-6):
    t = pos = 0.0; v = v0; fin = sorted(dist / x for x in others); i = 0
    while pos < dist:
        while i < len(fin) and t >= fin[i]:
            v *= factor; i += 1
        pos += v * dt; t += dt
    return t

orig = dave_time(1, [8, 4, 2], F(2, 2))
print("original:", orig, "expected 13/32 ->", orig == F(13, 32))
var = dave_time(1, [12, 6, 3], F(3, 3))
print("variant:", var, float(var))
print("numeric check variant:", round(numeric_check(1.0, [12, 6, 3], 1.0), 5))
