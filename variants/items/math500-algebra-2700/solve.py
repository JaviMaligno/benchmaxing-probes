from fractions import Fraction as F
from itertools import product

def max_slope(sqA, sqB, n=40):
    # Brute force over a fine rational grid of both squares (includes all corners).
    (ax0, ay0), (ax1, ay1) = sqA
    (bx0, by0), (bx1, by1) = sqB
    def grid(lo, hi):
        return [F(lo) + F(hi - lo) * k / n for k in range(n + 1)]
    best = None
    Ax, Ay, Bx, By = grid(ax0, ax1), grid(ay0, ay1), grid(bx0, bx1), grid(by0, by1)
    # slope = (yB - yA)/(xB - xA) with xB > xA always; x and y choices independent
    for xa, xb in product(Ax, Bx):
        dx = xb - xa
        assert dx > 0
        s = (max(By) - min(Ay)) / dx  # y part maximized independently (dy>0 here)
        if best is None or s > best:
            best = s
    # independent full check on corners only
    corners = lambda sq: [(x, y) for x in (sq[0][0], sq[1][0]) for y in (sq[0][1], sq[1][1])]
    cbest = max(F(b[1] - a[1], b[0] - a[0]) for a in corners(sqA) for b in corners(sqB))
    assert cbest == best
    return best

orig = max_slope(((0, 0), (2, 2)), ((4, 2), (5, 3)))
print("original:", orig)
assert orig == F(3, 2)
var = max_slope(((0, 0), (3, 3)), ((6, 4), (7, 5)))
print("variant:", var)
