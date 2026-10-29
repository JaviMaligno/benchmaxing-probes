# Count Hamiltonian paths on a 3 x n grid starting at a given point (any endpoint).
# Brute-force DFS with a reachability prune (unvisited cells must stay connected).
import sys
sys.setrecursionlimit(10000)

def count(rows, cols, start):
    N = rows * cols
    idx = lambda i, j: (i - 1) * cols + (j - 1)
    nbr = [[] for _ in range(N)]
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
                a, b = i + di, j + dj
                if 1 <= a <= rows and 1 <= b <= cols:
                    nbr[idx(i, j)].append(idx(a, b))
    vis = [False] * N
    def connected(cur, left):
        # unvisited cells together with cur must form a connected set
        seen = {cur}; st = [cur]; c = 0
        while st:
            u = st.pop()
            for v in nbr[u]:
                if not vis[v] and v not in seen:
                    seen.add(v); st.append(v); c += 1
        return c == left
    def dfs(u, left):
        if left == 0:
            return 1
        if not connected(u, left):
            return 0
        # dead-end prune: at most one unvisited cell (other than the final one) may have <=1 free neighbour
        tot = 0
        for v in nbr[u]:
            if not vis[v]:
                vis[v] = True
                tot += dfs(v, left - 1)
                vis[v] = False
        return tot
    s = idx(*start)
    vis[s] = True
    return dfs(s, N - 1)

if __name__ == "__main__":
    for n in range(2, 13):
        print("n =", n, "paths from (2,1):", count(3, n, (2, 1)))
    orig = count(3, 24, (2, 1))
    print("original 3x24 from (2,1):", orig, "check", orig == 4096)
    var = count(3, 20, (2, 1))
    print("variant 3x20 from (2,1):", var)
