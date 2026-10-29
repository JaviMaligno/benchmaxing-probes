<tool_calls>
<invoke name="exec_command">
<parameter name="cmd">python3 - <<'PY'
from collections import defaultdict

def b_counts(P):
    P=set(P)
    # only cells with nonzero s are inside cells and outside neighbors? Need consider outside cells adjacent to P plus maybe outside cells with zero not counted.
    cells=set(P)
    for (x,y) in P:
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            q=(x+dx,y+dy)
            if q not in P:
                cells.add(q)
    counts=[0]*5
    for (x,y) in cells:
        s=0
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            q=(x+dx,y+dy)
            if (q in P) != ((x,y) in P):
                s+=1
        if s>0:
            counts[s]+=1
    return counts

def R(P):
    b=b_counts(P)
    return (2*b[1]+3*b[2])/b[3] if b[3] else None, b

# test unit square
P=[(0,0)]
print('1x1',R(P))
# 1x2 rectangle
P=[(0,0),(1,0)]
print('1x2',R(P))
# 2x2 rectangle
P=[(0,0),(1,0),(0,1),(1,1)]
print('2x2',R(P))
# U-shape 2x3 minus bottom center
P=[(0,0),(2,0),(0,1),(1,1),(2,1)]
print('U5',R(P))
# 1x3 rectangle
P=[(0,0),(1,0),(2,0)]
print('1x3',R(P))
PY</parameter>
<parameter name="reason">Calcular b_i para formas pequeñas</parameter>
</invoke>
</tool_calls>