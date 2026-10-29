Sea \(f(x)=px^2+qx+r\). Como \(|f(x)|\le 1\) en \([0,2]\), en particular

\[
f(0)=r,\qquad f(1)=p+q+r,\qquad f(2)=4p+2q+r
\]

están todos entre \(-1\) y \(1\). Despejando,

\[
p=\frac{f(2)-2f(1)+f(0)}2,\qquad
q=\frac{4f(1)-3f(0)-f(2)}2,\qquad
r=f(0).
\]

Por la desigualdad triangular,

\[
|p|\le \frac{1+2+1}{2}=2,\qquad
|q|\le \frac{4+3+1}{2}=4,\qquad
|r|\le 1.
\]

Por lo tanto,

\[
|p|+|q|+|r|\le 7.
\]

Este valor se alcanza con

\[
f(x)=1-2(x-1)^2=-2x^2+4x-1,
\]

que satisface \(|f(x)|\le 1\) en \([0,2]\), y da

\[
|-2|+|4|+|-1|=7.
\]

\[
\boxed{7}
\]