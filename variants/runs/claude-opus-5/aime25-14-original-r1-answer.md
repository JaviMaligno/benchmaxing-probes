
<invoke name="Bash">
<parameter name="command">cat << 'EOF' > /tmp/pent.py
import numpy as np
from math import *

# triangulo ABC: AB=14, BC=7, ang B=60 -> AC=7sqrt3, ang BAC=30
# triangulo AED: EA=26, DE=13, ang E=60 -> AD=13sqrt3, ang EAD=30
AC=7*sqrt(3); AD=13*sqrt(3)
cosCAD=(AC**2+AD**2-24**2)/(2*AC*AD)
angCAD=acos(cosCAD)
A=np.array([0,0])
B=np.array([14,0])
t=radians(30)
C=AC*np.array([cos(t),sin(t)])
t2=t+angCAD
D=AD*np.array([cos(t2),sin(t2)])
t3=t2+radians(30)
E=26*np.array([cos(t3),sin(t3)])
P=[A,B,C,D,E]
for n,p in zip("ABCDE",P): print(n,p)
print("lados",[round(float(np.linalg.norm(P[i]-P[(i+1)%5])),6) for i in range(5)])
print("angCAD deg",degrees(angCAD), "angBAE", degrees(t3))

def f(X):
    X=np.array(X)
    return sum(np.linalg.norm(X-p) for p in P)

# Weiszfeld
X=np.mean(P,axis=0)
for _ in range(100000):
    w=np.array([1/max(np.linalg.norm(X-p),1e-12) for p in P])
    X=sum(w[i]*P[i] for i in range(5))/w.sum()
print("X",X,"f",f(X))
print("38+19sqrt3",38+19*sqrt(3))
EOF
python3 -I /tmp/pent.py</parameter>
</invoke>


```
A [0. 0.]
B [14.  0.]
C [10.5         6.06217783]
D [-8.35654982 20.90874371]
E [-20.41285054 16.10307325]
lados
[14.0, 7.0, 24.0, 13.0, 26.0]
<parameter name="sides">[14.0, 7.0, 24.0, 13.0, 26.0]
angCAD deg 81.7867893002
angBAE 141.786789300
X [0.74261 2.58108]
<parameter name="f">70.90905...
```