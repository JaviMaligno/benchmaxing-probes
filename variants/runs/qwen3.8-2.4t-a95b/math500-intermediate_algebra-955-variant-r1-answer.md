

Sea  
\[
f(x)=px^2+qx+r.
\]
Por hipótesis, \(|f(x)|\le 1\) para todo \(x\in[0,2]\). En particular,
\[
|f(0)|\le 1,\qquad |f(1)|\le 1,\qquad |f(2)|\le 1.
\]

Primero,
\[
r=f(0),
\]
así que
\[
|r|\le 1.
\]

Luego calculamos la segunda diferencia finita:
\[
f(2)-2f(1)+f(0)
=(4p+2q+r)-2(p+q+r)+r=2p.
\]
Por tanto,
\[
|2p|\le |f(2)|+2|f(1)|+|f(0)|\le 1+2+1=4,
\]
de donde
\[
|p|\le 2.
\]

Finalmente, usamos la combinación
\[
-3f(0)+4f(1)-f(2)
=-3r+4(p+q+r)-(4p+2q+r)=2q.
\]
Así,
\[
|2q|\le 3|f(0)|+4|f(1)|+|f(2)|\le 3+4+1=8,
\]
por lo que
\[
|q|\le 4.
\]

Entonces
\[
|p|+|q|+|r|\le 2+4+1=7.
\]

Este valor se alcanza con
\[
f(x)=2x^2-4x+1=2(x-1)^2-1.
\]
Para \(0\le x\le 2\), se tiene \((x-1)^2\in[0,1]\), luego \(f(x)\in[-1,1]\). Además,
\[
|p|+|q|+|r|=|2|+|-4|+|1|=7.
\]

\[
\boxed{7}
\]