from fractions import Fraction
def avg_two_smallest(a, b, m, limit=10000):
    sols = [u for u in range(1, limit) if (a*u - b) % m == 0][:2]
    return sols, Fraction(sum(sols), 2)
s, o = avg_two_smallest(14, 46, 100)
print("original:", s, o); assert o == 64
s, v = avg_two_smallest(22, 38, 100)
print("variant:", s, v)
