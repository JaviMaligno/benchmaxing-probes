import sympy as sp, random
x, a, b, c = sp.symbols('x a b c')

def p(w):
    return (w(a)*(x-b)*(x-c)/((a-b)*(a-c)) + w(b)*(x-a)*(x-c)/((b-a)*(b-c))
            + w(c)*(x-a)*(x-b)/((c-a)*(c-b)))

def degree(w):
    e = sp.cancel(sp.together(p(w)))
    poly = sp.Poly(e, x)
    d = poly.degree()
    # check degree is the same for many random distinct numeric triples (generic + edge)
    for _ in range(50):
        va, vb, vc = random.sample(range(-30, 31), 3)
        q = sp.Poly(sp.cancel(e.subs({a: va, b: vb, c: vc})), x)
        assert q.degree() == d
    return e, d

e0, d0 = degree(lambda t: 1)
print("original p(x) =", e0, " degree =", d0)
assert d0 == 0
e1, d1 = degree(lambda t: 3*t - 1)
print("variant  p(x) =", e1, " degree =", d1)
