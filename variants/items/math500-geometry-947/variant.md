# math500-geometry-947 — variant

In the diagram below, points $A$, $O$, and $B$ lie on a line with $O$ between $A$ and $B$, and ray $OC$ is drawn above the line. We have $\sin \angle COB = \frac{8}{17}$. What is $\cos \angle COA$?

[asy]
pair C,O,B,A;
A = (-2,0);
O = (0,0);
B = (2,0);
C = rotate(aSin(8/17))*(1.5,0);
dot("$A$",A,S);
dot("$B$",B,S);
dot("$C$",C,N);
dot("$O$",O,S);
draw(B--A);
draw(O--C);
[/asy]

**Answer:** $-\frac{15}{17}$
