# Solve p(a^2+1)=q(b^2+1)=r(c^2+1)=k, ab+bc+ca=1, a,b,c>0; return a+b+c.
import sympy as sp
from mpmath import mp, mpf, sqrt, findroot
mp.dps = 50

def solve(p, q, r):
    # numeric: a,b,c as functions of k; root of ab+bc+ca-1 in k
    f = lambda k: sqrt(k/p-1)*sqrt(k/q-1)+sqrt(k/q-1)*sqrt(k/r-1)+sqrt(k/r-1)*sqrt(k/p-1)-1
    lo = mpf(max(p, q, r)); hi = lo*100
    # bisection (f increasing in k)
    for _ in range(300):
        mid = (lo+hi)/2
        if f(mid) > 0: hi = mid
        else: lo = mid
    k = (lo+hi)/2
    a, b, c = sqrt(k/p-1), sqrt(k/q-1), sqrt(k/r-1)
    num = a+b+c
    # closed form via triangle with squared sides p,q,r: (p+q+r)/sqrt(2(pq+qr+rp)-(p^2+q^2+r^2))
    P, Q, R = map(sp.Integer, (p, q, r))
    closed = sp.radsimp((P+Q+R)/sp.sqrt(2*(P*Q+Q*R+R*P)-(P**2+Q**2+R**2)))
    assert abs(num - mpf(sp.N(closed, 50))) < mpf(10)**-40
    return closed, num

orig, n0 = solve(2, 3, 4)
print("original:", orig, n0)
assert sp.simplify(orig - 9*sp.sqrt(23)/23) == 0
var, n1 = solve(3, 4, 5)
print("variant:", var, n1)
