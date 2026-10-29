from fractions import Fraction as F

def hallway_m(hours_per_km, seconds):
    sec_per_km = F(hours_per_km) * 3600
    return F(1000) * F(seconds) / sec_per_km

orig = hallway_m(F(5, 2), 90)
print("original:", orig)
assert orig == 10

var = hallway_m(F(3, 2), 81)
# independent check: speed in m/s times time
speed = F(1000) / (F(3, 2) * 60 * 60)
assert speed * 81 == var
print("variant:", var)
