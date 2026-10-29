# Count partitions of {1..n} into k unlabeled blocks of size s, each ball sharing a block with a neighbor.
import sys
from functools import lru_cache
sys.setrecursionlimit(10000)

def dfs_count(n, k, s):
    blocks = []          # list of sizes
    where = [None]*(n+2)
    cnt = 0
    def ok(b):  # ball b (1-indexed) satisfied, given b-1 and b+1 placed
        return (b > 1 and where[b-1] == where[b]) or (b < n and where[b+1] == where[b])
    def rec(i):
        nonlocal cnt
        if i > n:
            if ok(n): cnt += 1
            return
        options = list(range(len(blocks)))
        if len(blocks) < k: options.append(len(blocks))
        for bi in options:
            if bi == len(blocks): blocks.append(0)
            if blocks[bi] < s:
                blocks[bi] += 1; where[i] = bi
                if i == 1 or ok(i-1):
                    rec(i+1)
                blocks[bi] -= 1; where[i] = None
            if blocks[bi] == 0 and bi == len(blocks)-1: blocks.pop()
    rec(1)
    return cnt

def structural_count(n, k, s):
    # Independent method (s=4 only): every block is a run of 4 or a union of two runs of 2.
    # Enumerate compositions of n into parts 2/4, pair the 2-runs in all ways,
    # build the set partition, and deduplicate (adjacent 2-runs paired = a 4-run).
    assert s == 4
    seen = set()
    def comps(m):
        if m == 0: yield []; return
        for p in (2, 4):
            if p <= m:
                for c in comps(m-p): yield [p]+c
    def pairings(lst):
        if not lst: yield []; return
        a = lst[0]
        for j in range(1, len(lst)):
            for rest in pairings(lst[1:j]+lst[j+1:]): yield [(a, lst[j])]+rest
    for c in comps(n):
        runs, pos = [], 1
        for p in c: runs.append(tuple(range(pos, pos+p))); pos += p
        fours = [r for r in runs if len(r) == 4]
        twos = [r for r in runs if len(r) == 2]
        if len(fours) + len(twos)//2 != k or len(twos) % 2: continue
        for pr in pairings(twos):
            part = frozenset([frozenset(r) for r in fours] + [frozenset(a+b) for a, b in pr])
            seen.add(part)
    return len(seen)

orig = dfs_count(16, 4, 4)
orig2 = structural_count(16, 4, 4)
print("original (16 balls, 4 boxes of 4): dfs =", orig, " structural =", orig2)
assert orig == orig2 == 105
var = dfs_count(20, 5, 4)
var2 = structural_count(20, 5, 4)
print("variant (20 balls, 5 boxes of 4): dfs =", var, " structural =", var2)
assert var == var2
