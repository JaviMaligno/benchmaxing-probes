from fractions import Fraction
import math, random

def diff(radii):
    r = sorted(radii)
    prev = 0
    areas = []
    for x in r:
        areas.append(x*x - prev*prev)  # coefficient of pi
        prev = x
    return max(areas) - min(areas), areas

def mc_check(radii, n=400000, seed=1):
    # independent Monte Carlo estimate of region areas
    random.seed(seed); R = max(radii); r = sorted(radii)
    cnt = [0]*3
    for _ in range(n):
        x, y = random.uniform(-R, R), random.uniform(-R, R)
        d = math.hypot(x, y)
        for i, ri in enumerate(r):
            if d < ri:
                cnt[i] += 1; break
    a = [c/n*(2*R)**2 for c in cnt]
    return (max(a)-min(a))/math.pi

o, oa = diff([4, 6, 7])
print("original areas/pi:", oa, "diff/pi:", o)
assert o == 7, o
v, va = diff([5, 8, 9])
print("variant areas/pi:", va, "diff/pi:", v)
print("variant MC estimate diff/pi:", round(mc_check([5, 8, 9]), 2))
print("ANSWER:", f"{v}*pi")
