# Inscribed hexagon ABCDEF: given angle ABC and angle EFA, find angle CDE.
# Method: arc AC = 360-2B, arc EA = 360-2F, arc CE = 360-2alpha, sum = 360.
import math
from fractions import Fraction

def formula(B, F):
    return Fraction(360) - B - F  # from (360-2a)+(360-2B)+(360-2F)=360

def angle(P, Q, R):
    v1 = (P[0]-Q[0], P[1]-Q[1]); v2 = (R[0]-Q[0], R[1]-Q[1])
    c = (v1[0]*v2[0]+v1[1]*v2[1]) / (math.hypot(*v1)*math.hypot(*v2))
    return math.degrees(math.acos(c))

def numeric(B, F, posB_frac=0.4, posD_frac=0.6, posF_frac=0.3):
    # build a concrete configuration on the unit circle and measure angle D
    a = -10.0
    arcAC = 360 - 2*B; arcEA = 360 - 2*F
    c = a + arcAC
    e = a - arcEA            # E reached going clockwise from A
    b = a + posB_frac*arcAC
    arcCE = (e + 360) - c
    d = c + posD_frac*arcCE
    f = e + 360 + posF_frac*arcEA
    pt = lambda t: (math.cos(math.radians(t)), math.sin(math.radians(t)))
    A,Bp,C,D,E,Fp = map(pt,[a,b,c,d,e,f])
    assert abs(angle(A,Bp,C)-B)<1e-9 and abs(angle(E,Fp,A)-F)<1e-9
    return angle(C,D,E)

for name,(B,F) in {"original":(110,105),"variant":(115,125)}.items():
    exact = formula(B,F)
    nums = [numeric(B,F,pb,pd,pf) for pb in (0.2,0.5,0.8) for pd in (0.3,0.7) for pf in (0.4,0.9)]
    assert all(abs(n-float(exact))<1e-9 for n in nums)
    print(name, "B=",B,"F=",F,"alpha =",exact, "numeric check:", round(nums[0],9))
assert formula(110,105)==145
