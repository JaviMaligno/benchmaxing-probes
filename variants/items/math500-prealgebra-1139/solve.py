# Brute force: all full binary parenthesizations of a sequence of numbers with fixed operators.
from functools import lru_cache
import operator
OPS = {'*': operator.mul, '+': operator.add}

def values(nums, ops):
    nums, ops = tuple(nums), tuple(ops)
    @lru_cache(None)
    def rec(i, j):
        if i == j:
            return frozenset([nums[i]])
        out = set()
        for k in range(i, j):
            for a in rec(i, k):
                for b in rec(k + 1, j):
                    out.add(OPS[ops[k]](a, b))
        return frozenset(out)
    return sorted(rec(0, len(nums) - 1))

orig = values([2, 3, 4, 5, 1], ['*', '*', '*', '+'])
print("original values:", orig, "count:", len(orig))
assert 121 in orig and 144 in orig and len(orig) == 4

var = values([2, 3, 4, 5, 6, 1], ['*', '*', '*', '*', '+'])
print("variant values:", var, "count:", len(var))
assert 721 in var and 840 in var
print("ANSWER:", len(var))
