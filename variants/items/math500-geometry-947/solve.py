# S, P, Q collinear with P between S and Q; ray PR above line. angle RPS = 180 - angle RPQ.
from sympy import Rational, sqrt, simplify, acos, asin, cos, pi, N
import math

def cos_RPS(sin_RPQ):
    # angle RPQ acute (R drawn at rotate(asin(s))) -> cos positive
    c = sqrt(1 - sin_RPQ**2)
    return simplify(-c)

def numeric(sin_RPQ):
    s = float(sin_RPQ)
    th = math.asin(s)
    R = (math.cos(th), math.sin(th)); S = (-2.0, 0.0)
    # cos of angle between PR and PS (P at origin)
    dot = R[0]*S[0] + R[1]*S[1]
    return dot / (math.hypot(*R) * math.hypot(*S))

orig = cos_RPS(Rational(7, 25))
print("original:", orig, N(orig), numeric(Rational(7,25)))
assert orig == Rational(-24, 25)
var = cos_RPS(Rational(8, 17))
print("variant:", var, N(var), numeric(Rational(8,17)))
assert abs(float(var) - numeric(Rational(8,17))) < 1e-12
