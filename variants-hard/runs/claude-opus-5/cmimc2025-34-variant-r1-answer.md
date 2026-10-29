
<invoke_name>Bash</invoke_name>
<parameter name="command">cd /tmp && cat > hexa.py <<'EOF'
from itertools import permutations
from fractions import Fraction as F

pts=[(0,0),(12,0),(12,12),(0,12),(5,4),(8,2)]

def area2(poly):
    s=0
    n=len(poly)
    for i in range(n):
        x1,y1=poly[i]; x2,y2=poly[(i+1)%n]
        s+=x1*y2-x2*y1
    return abs(s)

def seg_proper_int(p1,p2,p3,p4):
    # check if segments p1p2 and p3p4 intersect (excluding shared endpoints handling)
    def cross(o,a,b):
        return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    d1=cross(p3,p4,p1); d2=cross(p3,p4,p2); d3=cross(p1,p2,p3); d4=cross(p1,p2,p4)
    if ((d1>0 and d2<0) or (d1<0 and d2>0)) and ((d3>0 and d4<0) or (d3<0 and d4>0)):
        return True
    def onseg(p,q,r):
        return cross(p,q,r)==0 and min(p[0],q[0])<=r[0]<=max(p[0],q[0]) and min(p[1],q[1])<=r[1]<=max(p[1],q[1])
    if onseg(p3,p4,p1) or onseg(p3,p4,p2) or onseg(p1,p2,p3) or onseg(p1,p2,p4):
        return True
    return False

def simple(poly):
    n=len(poly)
    for i in range(n):
        for j in range(i+1,n):
            a,b=poly[i],poly[(i+1)%n]
            c,d=poly[j],poly[(j+1)%n]
            if j==i or (j+1)%n==i or (i+1)%n==j:
                # adjacent: only check collinear overlap
                continue
            if seg_proper_int(a,b,c,d):
                return False
    # also check adjacent edges not overlapping (collinear degenerate)
    return True

areas=set()
best=None;worst=None
for perm in permutations(pts):
    if perm[0]!=pts[0]: continue
    if simple(perm):
        a=area2(perm)
        areas.add(a)
        if best is None or a>best[0]: best=(a,perm)
        if worst is None or a<worst[0]: worst=(a,perm)
print(sorted(F(a,2) for a in areas))
print("max",F(best[0],2),best[1])
print("min",F(worst[0],2),worst[1])
EOF
python3 -I hexa.py</parameter>
</invoke_name>