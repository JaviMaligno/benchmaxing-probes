import sys
sys.setrecursionlimit(10000)
MOVES = [(1,0),(0,1),(-1,1),(1,-1)]
def count(W, H, target):
    """Self-avoiding paths from (0,0) to target with 0<=x<=W, 0<=y<=H using MOVES."""
    seen = {(0,0)}
    def dfs(p):
        if p == target:
            return 1
        tot = 0
        for dx, dy in MOVES:
            q = (p[0]+dx, p[1]+dy)
            if 0 <= q[0] <= W and 0 <= q[1] <= H and q not in seen:
                seen.add(q); tot += dfs(q); seen.remove(q)
        return tot
    return dfs((0,0))

orig = count(3, 3, (3,3))
print("original (box 0..3 x 0..3, target (3,3)):", orig)
assert orig == 2304
for W,H in [(4,2),(2,4),(5,2),(4,3)]:
    print(f"box 0..{W} x 0..{H}, target ({W},{H}):", count(W,H,(W,H)))
print("variant (box 0..4 x 0..2, target (4,2)):", count(4,2,(4,2)))
