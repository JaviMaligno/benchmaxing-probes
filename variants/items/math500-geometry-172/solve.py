from fractions import Fraction as Fr
import random

def area(P,Q,R):
    return abs((Q[0]-P[0])*(R[1]-P[1])-(R[0]-P[0])*(Q[1]-P[1]))/2

def inter(P,d,A,B):
    # intersect line P+t d with line A + s(B-A)
    ex,ey=B[0]-A[0],B[1]-A[1]
    det=d[0]*(-ey)-d[1]*(-ex)
    rx,ry=A[0]-P[0],A[1]-P[1]
    t=(rx*(-ey)-ry*(-ex))/det
    return (P[0]+t*d[0],P[1]+t*d[1])

def compute(total, which):
    vals=set()
    for _ in range(200):
        A,B,C=[(Fr(random.randint(-50,50)),Fr(random.randint(-50,50))) for _ in range(3)]
        S=area(A,B,C)
        if S==0: continue
        G=((A[0]+B[0]+C[0])/3,(A[1]+B[1]+C[1])/3)
        E=((A[0]+C[0])/2,(A[1]+C[1])/2)
        F=((A[0]+B[0])/2,(A[1]+B[1])/2)
        d=(C[0]-B[0],C[1]-B[1])
        M=inter(G,d,A,B); N=inter(G,d,A,C)
        a = area(E,N,G) if which=="ENG" else area(F,M,G)
        vals.add(a/S*total)
    assert len(vals)==1
    return vals.pop()

orig=compute(144,"ENG"); print("original ENG, area 144:", orig); assert orig==8
var=compute(270,"FMG"); print("variant FMG, area 270:", var)
