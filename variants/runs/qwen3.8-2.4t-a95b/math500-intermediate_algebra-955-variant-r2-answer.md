

Sea \(f(x)=px^2+qx+r\). Como \(|f(x)|\le 1\) para todo \(0\le x\le 2\), en particular

\[
|f(0)|\le 1,\qquad |f(1)|\le 1,\qquad |f(2)|\le 1.
\]

Definamos

\[
A=f(0)=r,\qquad B=f(1)=p+q+r,\qquad C=f(2)=4p+2q+r.
\]

Resolviendo este sistema para \(p,q,r\):

\[
p=\frac{A-2B+C}{2},
\]

\[
q=\frac{-3A+4B-C}{2},
\]

\[
r=A.
\]

Por la desigualdad triangular,

\[
|p|\le \frac{|A|+2|B|+|C|}{2},
\]

\[
|q|\le \frac{3|A|+4|B|+|C|}{2},
\]

\[
|r|=|A|.
\]

Sumando,

\[
|p|+|q|+|r|
\le \frac{|A|+2|B|+|C|+3|A|+4|B|+|C|}{2}+|A|.
\]

Simplificando,

\[
|p|+|q|+|r|\le 3|A|+3|B|+|C|.
\]

Como \(|A|,|B|,|C|\le 1\),

\[
|p|+|q|+|r|\le 3+3+1=7.
\]

Ahora vemos que \(7\) sí es alcanzable. Tomemos

\[
f(x)=2x^2-4x+1=2(x-1)^2-1.
\]

Para \(0\le x\le 2\), se tiene \(0\le (x-1)^2\le 1\), así que

\[
-1\le 2(x-1)^2-1\le 1.
\]

Por tanto, esta función cumple la condición. Sus coeficientes son

\[
p=2,\qquad q=-4,\qquad r=1,
\]

y entonces

\[
|p|+|q|+|r|=2+4+1=7.
\]

\[
\boxed{7}
\]