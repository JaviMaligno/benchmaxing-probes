"""Expected size of the cluster of a corner cell in a 2 x infinity strip,
horizontal doors (same row) open w.p. qh, vertical doors (same column) open w.p. qv.

Method 1 (exact): column-by-column transfer over boundary connectivity states,
tracking probability and expected component masses (linear), summed to
infinity by solving (I - M) x = v0 exactly with sympy.
Method 2 (check): exact enumeration on finite strips 2 x n (all 2^(3n-2)
door configurations) for small n, plus Monte Carlo on a long strip.
"""
import itertools, random
from fractions import Fraction
import sympy as sp

def transfer_exact2(qh, qv):
    R=lambda t: sp.Rational(Fraction(t).numerator, Fraction(t).denominator)
    qh=R(qh); qv=R(qv); q=qv
    # boundary labels: each of top/bottom has label in {'O','X','Y'}; canonical states
    states = [('O','O'), ('O','X'), ('X','O')]  # O must touch the boundary while alive
    # vector entries per state: prob, mass of O, mass of X, mass of Y
    idx = {}
    for s in states:
        for c in ('P','O','X','Y'):
            idx[(s, c)] = len(idx)
    N = len(idx)
    M = sp.zeros(N, N)
    absorb = sp.zeros(1, N)   # O mass that leaves the boundary (final contribution)
    for s in states:
        labs = set(s)
        for hT, hB, v in itertools.product([0, 1], repeat=3):
            pr = 1
            for d, qq in ((hT,qh),(hB,qh),(v,qv)):
                pr *= qq if d else (1 - qq)
            # union-find over old labels + new cells 'T','B'
            parent = {x: x for x in list(labs) + ['T', 'B']}
            def f(x):
                while parent[x] != x:
                    x = parent[x]
                return x
            def u(a, b):
                ra, rb = f(a), f(b)
                if ra != rb:
                    # keep 'O' as root if present
                    if rb == 'O': ra, rb = rb, ra
                    parent[rb] = ra
            if hT: u(s[0], 'T')
            if hB: u(s[1], 'B')
            if v: u('T', 'B')
            rT, rB = f('T'), f('B')
            O_alive = f('O') in (rT, rB) if 'O' in labs else False
            # members: old labels and new cells grouped by root
            def mass_terms(root):
                # list of (component, ...) old labels merged into root, and count new cells
                olds = [l for l in labs if f(l) == root]
                new = sum(1 for c in ('T', 'B') if f(c) == root)
                return olds, new
            if not O_alive:
                # O component leaves boundary: its total mass absorbed
                olds, new = mass_terms(f('O'))
                for l in olds:
                    absorb[0, idx[(s, l)]] += pr
                absorb[0, idx[(s, 'P')]] += pr * new
                continue
            # canonical new state: label O for root of O, then X, Y in order T,B
            name = {f('O'): 'O'}
            for r in (rT, rB):
                if r not in name:
                    name[r] = 'X' if 'X' not in name.values() else 'Y'
            ns = (name[rT], name[rB])
            M[idx[(ns, 'P')], idx[(s, 'P')]] += pr
            for r, lab in name.items():
                olds, new = mass_terms(r)
                for l in olds:
                    M[idx[(ns, lab)], idx[(s, l)]] += pr
                M[idx[(ns, lab)], idx[(s, 'P')]] += pr * new
    # initial: column 1, origin = top cell; vertical door
    v0 = sp.zeros(N, 1)
    v0[idx[(('O', 'O'), 'P')]] = q
    v0[idx[(('O', 'O'), 'O')]] = 2 * q
    v0[idx[(('O', 'X'), 'P')]] = 1 - q
    v0[idx[(('O', 'X'), 'O')]] = 1 - q
    v0[idx[(('O', 'X'), 'X')]] = 1 - q
    x = (sp.eye(N) - M).LUsolve(v0)
    return sp.nsimplify(sp.simplify((absorb * x)[0, 0]))

def finite_exact(qh, qv, n):
    qh, qv = Fraction(qh), Fraction(qv)
    cells = [(r, c) for c in range(n) for r in range(2)]
    doors = [((0, c), (1, c)) for c in range(n)] + \
            [((r, c), (r, c + 1)) for c in range(n - 1) for r in range(2)]
    tot = Fraction(0)
    for conf in itertools.product([0, 1], repeat=len(doors)):
        pr = Fraction(1)
        adj = {x: [] for x in cells}
        for d, o in zip(doors, conf):
            qq = qv if d[0][1] == d[1][1] else qh
            pr *= qq if o else 1 - qq
            if o:
                adj[d[0]].append(d[1]); adj[d[1]].append(d[0])
        seen = {(0, 0)}; st = [(0, 0)]
        while st:
            x = st.pop()
            for y in adj[x]:
                if y not in seen:
                    seen.add(y); st.append(y)
        tot += pr * len(seen)
    return tot

def monte_carlo(qh, qv, trials=200000, n=200, seed=1):
    rng = random.Random(seed); tot = 0
    for _ in range(trials):
        # sweep with true reachability via BFS on lazily sampled doors
        doors = {}
        def op(a, b):
            k = (min(a, b), max(a, b))
            if k not in doors: doors[k] = rng.random() < (qv if a[1] == b[1] else qh)
            return doors[k]
        seen = {(0, 0)}; st = [(0, 0)]
        while st:
            r, c = st.pop()
            for y in ((1 - r, c), (r, c + 1), (r, c - 1)):
                if 0 <= y[1] < n and y not in seen and op((r, c), y):
                    seen.add(y); st.append(y)
        tot += len(seen)
    return tot / trials

if __name__ == '__main__':
    F = Fraction
    orig = transfer_exact2(F(1, 2), F(1, 2))
    print('ORIGINAL (all doors locked w.p. 1/2):', orig, '| matches 32/7:', orig == sp.Rational(32, 7))
    var = transfer_exact2(F(1, 2), F(3, 4))  # row doors locked 1/2, column doors locked 1/4
    print('VARIANT (row doors locked 1/2, column doors locked 1/4):', var, float(var))
    for qh, qv in ((F(1, 2), F(1, 2)), (F(1, 2), F(3, 4))):
        print(' finite exact n=1..5 (qh=%s,qv=%s):' % (qh, qv), [round(float(finite_exact(qh, qv, n)), 5) for n in range(1, 6)])
        print(' monte carlo, 200k trials:', monte_carlo(float(qh), float(qv), trials=200000))
