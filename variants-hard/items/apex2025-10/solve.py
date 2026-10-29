from functools import lru_cache

PATS = ("123", "231", "312")

@lru_cache(maxsize=None)
def deletable(s):
    if s == "":
        return True
    for i in range(len(s) - 2):
        if s[i:i+3] in PATS and deletable(s[:i] + s[i+3:]):
            return True
    return False

def count(k):
    """strings with k each of 1,2,3, no two adjacent equal, fully deletable"""
    total = 0
    def rec(prefix, c):
        nonlocal total
        if sum(c) == 0:
            if deletable(prefix):
                total += 1
            return
        for d in range(3):
            if c[d] and (not prefix or prefix[-1] != "123"[d]):
                c[d] -= 1
                rec(prefix + "123"[d], c)
                c[d] += 1
    rec("", [k, k, k])
    return total

orig = count(5)
print("original (five each, length 15):", orig)
assert orig == 213
deletable.cache_clear()
var = count(6)
print("variant (six each, length 18):", var)
