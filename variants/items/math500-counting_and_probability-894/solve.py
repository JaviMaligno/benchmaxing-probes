from itertools import product
from math import comb

def brute(cars, lanes):
    return sum(1 for a in product(range(lanes), repeat=cars) if len(set(a)) == lanes)

def incl_excl(cars, lanes):
    return sum((-1)**k * comb(lanes, k) * (lanes - k)**cars for k in range(lanes + 1))

# Original: 6 cars, 3 lanes -> 540
o_b, o_f = brute(6, 3), incl_excl(6, 3)
print("original brute:", o_b, "formula:", o_f, "matches 540:", o_b == o_f == 540)
# Variant: 7 cars, 3 lanes
v_b, v_f = brute(7, 3), incl_excl(7, 3)
print("variant brute:", v_b, "formula:", v_f, "agree:", v_b == v_f)
