from fractions import Fraction as F

def closed(initial, miles, keep):
    return initial * keep**miles

def simulate(initial, miles, keep):
    amt = F(initial)
    for _ in range(miles):
        amt = amt * keep  # end of mile has `keep` times the amount at its start
    return amt

# Original: 2 gallons, 3 miles, 2/3 retained
o = simulate(2, 3, F(2, 3))
assert o == closed(2, 3, F(2, 3)) == F(16, 27), o
print("original:", o)

# Variant: 3 gallons, 3 miles, 3/4 retained
v = simulate(3, 3, F(3, 4))
assert v == closed(3, 3, F(3, 4))
assert v != F(16, 27)
print("variant:", v, float(v))
