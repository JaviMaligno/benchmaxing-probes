# Count tilings of an H x W rectangle by a x b rectangles (both orientations).
# Exact enumeration: fill the first empty cell (row-major) with each orientation;
# memoised on the full occupancy bitmask.
import sys
from functools import lru_cache
sys.setrecursionlimit(100000)

def count(H, W, a, b):
    N = H * W
    shapes = {(a, b), (b, a)}
    masks = []  # per cell: list of masks of tiles whose top-left is that cell
    for r in range(H):
        for c in range(W):
            lst = []
            for (h, w) in shapes:
                if r + h <= H and c + w <= W:
                    m = 0
                    for i in range(h):
                        for j in range(w):
                            m |= 1 << ((r + i) * W + c + j)
                    lst.append(m)
            masks.append(lst)
    full = (1 << N) - 1
    @lru_cache(maxsize=None)
    def f(occ):
        if occ == full:
            return 1
        free = ~occ & full
        p = (free & -free).bit_length() - 1
        t = 0
        for m in masks[p]:
            if m & occ == 0:
                t += f(occ | m)
        return t
    return f(0)

if __name__ == "__main__":
    orig = count(20, 24, 4, 5)
    print("original 20x24 by 4x5:", orig)
    assert orig == 6
    if len(sys.argv) > 1:
        for s in sys.argv[1:]:
            H, W, a, b = map(int, s.split(","))
            print(s, count(H, W, a, b))
    else:
        v = count(20, 28, 4, 5)
        print("variant 20x28 by 4x5:", v)
