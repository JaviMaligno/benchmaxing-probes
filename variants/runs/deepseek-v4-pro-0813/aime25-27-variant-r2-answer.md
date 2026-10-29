Sea \(r_i = B_1B_i\) para \(i=2,\dots,11\). Para cada \(2\le i\le 10\), el ángulo \(\angle B_iB_1B_{i+1}\) cumple
\[
\cos\theta_i=\frac45,\qquad \sin\theta_i=\frac35.
\]
Como el área del triángulo \(B_iB_1B_{i+1}\) es \(1\),
\[
\frac12 r_i r_{i+1}\cdot \frac35=1
\]
y por tanto
\[
r_i r_{i+1}=\frac{10}{3}.
\]
Entonces los radios de índice par e impar se alternan:
\[
r_2=r_4=\cdots=r_{10}=a,\qquad r_3=r_5=\cdots=r_{11}=b,
\]
con
\[
ab=\frac{10}{3}.
\]

Sea \(s=a+b\). Para cada lado \(B_iB_{i+1}\) con \(2\le i\le 10\), por la ley del coseno:
\[
B_iB_{i+1}^2=a^2+b^2-2ab\cdot \frac45.
\]
Sustituyendo \(ab=\frac{10}{3}\):
\[
B_iB_{i+1}^2=a^2+b^2-\frac{16}{3}
=s^2-2ab-\frac{16}{3}
=s^2-\frac{20}{3}-\frac{16}{3}
=s^2-12.
\]
Así, los \(9\) lados intermedios miden \(\sqrt{s^2-12}\).

El perímetro es
\[
20=B_1B_2+B_2B_3+\cdots+B_{10}B_{11}+B_{11}B_1
=a+9\sqrt{s^2-12}+b.
\]
Luego
\[
s+9\sqrt{s^2-12}=20.
\]
Despejando y elevando al cuadrado:
\[
9\sqrt{s^2-12}=20-s,
\]
\[
81(s^2-12)=(20-s)^2,
\]
\[
81s^2-972=400-40s+s^2,
\]
\[
80s^2+40s-1372=0,
\]
\[
20s^2+10s-343=0.
\]
La solución positiva es
\[
s=\frac{-10+\sqrt{10^2+4\cdot 20\cdot 343}}{40}
=\frac{-10+\sqrt{27540}}{40}
=\frac{-10+18\sqrt{85}}{40}
=\frac{9\sqrt{85}-5}{20}.
\]
Por lo tanto,
\[
B_1B_2+B_1B_{11}=a+b=s=\frac{9\sqrt{85}-5}{20}.
\]
Entonces \(m=9\), \(n=85\), \(p=5\), \(q=20\), y
\[
m+n+p+q=9+85+5+20=119.
\]

\[
\boxed{119}
\]