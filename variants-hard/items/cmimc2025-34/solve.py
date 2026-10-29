from itertools import permutations
from fractions import Fraction

def cross(o,a,b): return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
def onseg(p,q,r): return min(p[0],r[0])<=q[0]<=max(p[0],r[0]) and min(p[1],r[1])<=q[1]<=max(p[1],r[1])
def inter(p1,p2,p3,p4):
    d1,d2,d3,d4=cross(p3,p4,p1),cross(p3,p4,p2),cross(p1,p2,p3),cross(p1,p2,p4)
    if ((d1>0)!=(d2>0)) and d1!=0 and d2!=0 and ((d3>0)!=(d4>0)) and d3!=0 and d4!=0: return True
    if d1==0 and onseg(p3,p1,p4): return True
    if d2==0 and onseg(p3,p2,p4): return True
    if d3==0 and onseg(p1,p3,p2): return True
    if d4==0 and onseg(p1,p4,p2): return True
    return False
def simple(poly):
    n=len(poly)
    for i in range(n):
        if cross(poly[i-1],poly[i],poly[(i+1)%n])==0: return False  # degenerate vertex
        for j in range(i+1,n):
            if abs(i-j) in (1,n-1): continue
            if inter(poly[i],poly[(i+1)%n],poly[j],poly[(j+1)%n]): return False
    return True
def area(poly):
    return abs(Fraction(sum(poly[i][0]*poly[(i+1)%len(poly)][1]-poly[(i+1)%len(poly)][0]*poly[i][1] for i in range(len(poly))),2))
def solve(pts):
    areas=set()
    first=pts[0]
    for perm in permutations(pts[1:]):
        poly=[first]+list(perm)
        if simple(poly): areas.add(area(poly))
    return max(areas)-min(areas)

orig=[(0,0),(10,0),(10,10),(0,10),(3,4),(6,2)]
r=solve(orig); print("original:",r); assert r==44
var=[(0,0),(12,0),(12,12),(0,12),(5,4),(8,2)]
print("variant:",solve(var))
