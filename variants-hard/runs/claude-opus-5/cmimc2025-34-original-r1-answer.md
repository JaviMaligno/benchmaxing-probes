
᠎
᠎name: Bash
᠎
᠎command: cd /tmp && mkdir -p hexprobe && cd hexprobe && cat > hex.py <<'EOF'
from itertools import permutations

P=[(0,0),(10,0),(10,10),(0,10),(3,4),(6,2)]

def seg_int(a,b,c,d):
    def cr(o,a,b): return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    d1=cr(a,b,c); d2=cr(a,b,d); d3=cr(c,d,a); d4=cr(c,d,b)
    if ((d1>0)!=(d2>0)) and ((d3>0)!=(d4>0)): return True
    # collinear / touching cases
    def on(p,q,r):
        return cr(p,q,r)==0 and min(p[0],q[0])<=r[0]<=max(p[0],q[0]) and min(p[1],q[1])<=r[1]<=max(p[1],q[1])
    if on(a,b,c) or on(a,b,d) or on(c,d,a) or on(c,d,b): return True
    return False

def simple(poly):
    n=len(poly)
    for i in range(n):
        for j in range(i+1,n):
            a,b=poly[i],poly[(i+1)%n]
            c,d=poly[j],poly[(j+1)%n]
            if j==i or (j+1)%n==i or (i+1)%n==j:
                # adjacent edges: check they only share the endpoint
                continue
            if seg_int(a,b,c,d): return False
    return True

def area(poly):
    s=0
    n=len(poly)
    for i in range(n):
        x1,y1=poly[i]; x2,y2=poly[(i+1)%n]
        s+=x1*y2-x2*y1
    return abs(s)/2

res=[]
for perm in permutations(P):
    if perm[0]!=P[0]: continue
    if simple(list(perm)):
        res.append((area(list(perm)),perm))
res.sort()
print("min",res[0])
print("max",res[-1])
print("diff",res[-1][0]-res[0][0])
print("count",len(res))
EOF
python3 -I hex.py
᠎
᠎description: Brute force hexagon areas
᠎
᠎
᠎

{"stdout":"min (41.0, ((0, 0), (0, 10), (3, 4), (10, 10), (10, 0), (6, 2)))\nmin (41.0, ((0, 0), (0, 10), (3, 4), (10, 10), (10, 0), (6, 2)))\nmax (91.0, ((0, 0), (10, 0), (6, 2), (3, 4), (0, 10), (10, 10)))\nmax (91.0, ((0, 0), (10, 0), (6, 2), (3, 4), (0, 10), (10, 10)))\ncont 240","stderr":"","description":"Hexagon areas"}