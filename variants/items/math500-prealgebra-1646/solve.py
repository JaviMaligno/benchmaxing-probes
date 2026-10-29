from fractions import Fraction
import math

def afd(angle_b, angle_c):
    # 3x+3y = 360 - B - C ; angle AFD = 180 - 2x - 2y
    s = Fraction(360 - angle_b - angle_c, 3)  # x+y
    return 180 - 2*s

def numeric_check(angle_b, angle_c, a_split=0.55):
    # build an actual quadrilateral: choose angle A, D = 360-B-C-A; trace sides and intersect trisectors
    tot = 360 - angle_b - angle_c
    A_ang = tot * a_split; D_ang = tot - A_ang
    x, y = A_ang/3, D_ang/3
    A = (0.0, 0.0); D = (10.0, 0.0)
    # F: ray from A at angle 2x above AD, ray from D at 2y above DA
    ta = math.tan(math.radians(2*x)); td = math.tan(math.radians(2*y))
    fx = 10*td/(ta+td); fy = fx*ta
    v1 = (A[0]-fx, A[1]-fy); v2 = (D[0]-fx, D[1]-fy)
    cosang = (v1[0]*v2[0]+v1[1]*v2[1])/math.hypot(*v1)/math.hypot(*v2)
    return math.degrees(math.acos(cosang))

orig = afd(110, 100)
print("original:", orig, "numeric:", round(numeric_check(110, 100), 9))
assert orig == 80
var = afd(120, 75)
print("variant:", var, "numeric:", round(numeric_check(120, 75), 9), round(numeric_check(120, 75, 0.4), 9))
