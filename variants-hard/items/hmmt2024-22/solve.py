# Right angle at A; D,E,F = feet of altitude, bisector, median from A on BC.
# Independent check: parametrize legs (b,c) with b+c... solve numerically for BC given DE,EF,
# by direct coordinate computation (no isogonal lemma), then compare with closed form.
import sympy as sp

def positions(b, c):
    a = sp.sqrt(b**2 + c**2)
    BD = c**2 / a          # B--D distance (AB = c)
    BE = a * c / (b + c)   # angle bisector theorem
    BF = a / 2
    return a, BD, BE, BF

def solve_BC(DE, EF):
    # WLOG c < b so order on BC from B: D, E, F. Scale-free: set c = 1, b = t > 1.
    t = sp.symbols('t', positive=True)
    a, BD, BE, BF = positions(t, sp.Integer(1))
    ratio = sp.nsimplify(sp.Rational(DE, EF))
    f = (BE - BD) - ratio * (BF - BE)
    roots = set()
    for x0 in [1.01, 1.1, 1.5, 2, 3, 5, 10, 30]:
        try:
            r = sp.nsolve(f, t, x0, prec=40)
            if r > 1:
                roots.add(round(float(r), 12))
        except Exception:
            pass
    out = []
    for r in roots:
        r = sp.Float(r, 40)
        aa, BD_, BE_, BF_ = [sp.N(v.subs(t, r), 40) for v in (a, BD, BE, BF)]
        scale = DE / (BE_ - BD_)
        out.append(sp.N(aa * scale, 30))
    closed = sp.nsimplify(2*EF*(DE+EF)/sp.sqrt(EF**2 - DE**2))
    return out, closed

for name, (DE, EF) in {"original": (3, 5), "variant": (5, 13)}.items():
    num, closed = solve_BC(DE, EF)
    print(name, "DE=%d EF=%d" % (DE, EF), "numeric BC:", num, "closed form:", closed)

o_num, o_closed = solve_BC(3, 5)
assert o_closed == 20 and all(abs(x - 20) < 1e-9 for x in o_num), "original check failed"
v_num, v_closed = solve_BC(5, 13)
assert v_closed == 39 and all(abs(x - 39) < 1e-9 for x in v_num)
print("ORIGINAL CHECK OK (20); VARIANT ANSWER =", v_closed)
