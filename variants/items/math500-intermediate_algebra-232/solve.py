# Count integer pairs (a,b) with |a+bi| <= R, i.e. a^2+b^2 <= R^2 (exact integer brute force)
def count(R2):
    import math
    r = math.isqrt(R2)
    return sum(1 for a in range(-r-1, r+2) for b in range(-r-1, r+2) if a*a + b*b <= R2)

orig = count(25)
print("original (R=5):", orig)
assert orig == 81
# independent check: column-wise formula
import math
def count2(R2):
    r = math.isqrt(R2)
    return sum(2*math.isqrt(R2 - a*a) + 1 for a in range(-r, r+1))
v = count(36)
assert v == count2(36)
print("variant (R=6):", v)
