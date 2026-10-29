

Sea

\[
F(x)=\sum_{k\ge 0}x^{3^k}=x+x^3+x^9+\cdots .
\]

Como las sumas son ordenadas, la función generadora de \(a_n\) (tomando \(a_0=1\) por la suma vacía) es

\[
A(x)=\sum_{n\ge 0}a_nx^n=\frac{1}{1-F(x)}.
\]

Trabajamos módulo \(3\), es decir, en \(\mathbb{F}_3[[x]]\). Por el homomorfismo de Frobenius,

\[
F(x)^3=\sum_{k\ge 0}x^{3^{k+1}}=F(x)-x.
\]

Sea \(C(x)=1/A(x)=1-F(x)\). Entonces

\[
C(x)^3=(1-F(x))^3=1-F(x)^3=1-(F(x)-x)=C(x)+x.
\]

Pero en \(\mathbb{F}_3\), \(C(x)^3=C(x^3)\), así que

\[
C(x^3)=C(x)+x,
\qquad\text{luego}\qquad
C(x)=C(x^3)-x.
\]

Por tanto,

\[
A(x)=\frac{1}{C(x^3)-x}
=\frac{A(x^3)}{1-xA(x^3)}
=\sum_{j\ge 0}x^jA(x^3)^{j+1}.
\]

Pongamos \(y=x^3\) y separemos según \(j\bmod 3\). Usando \(A(y)^3=A(y^3)\) y

\[
\frac{1}{1-yA(y^3)}=\frac{A(y)}{A(y^3)},
\]

obtenemos:

\[
A(x)=C(x^3)+x+x^2A(x^3).
\]

Ahora bien,

\[
C(x^3)=1-x^3-x^9-x^{27}-\cdots,
\]

donde \(-1\equiv 2\pmod 3\). Si \(b_n\equiv a_n\pmod 3\) con \(b_n\in\{0,1,2\}\), y definimos auxiliarmente \(b_0=1\), entonces:

\[
b_{3q}=
\begin{cases}
1,&q=0,\\
2,&q\text{ es una potencia de }3,\\
0,&\text{en otro caso},
\end{cases}
\]

\[
b_{3q+1}=
\begin{cases}
1,&q=0,\\
0,&q\ge 1,
\end{cases}
\qquad
b_{3q+2}=b_q.
\]

Definamos

\[
S_m=\sum_{n=1}^{3^m} b_n.
\]

Para \(m=1\),

\[
S_1=b_1+b_2+b_3=1+1+2=4.
\]

Para \(m\ge 2\), separamos \(1\le n\le 3^m\) por residuos módulo \(3\):

- Múltiplos de \(3\): contribuyen \(2\) por cada potencia \(3,9,\dots,3^m\), es decir \(m\) términos, aportando \(2m\).
- Números \(\equiv 1\pmod 3\): solo \(n=1\) contribuye, aportando \(1\).
- Números \(\equiv 2\pmod 3\): son \(n=3q+2\) con \(0\le q\le 3^{m-1}-1\), y aportan

\[
\sum_{q=0}^{3^{m-1}-1} b_q
= b_0+\sum_{q=1}^{3^{m-1}-1}b_q
=1+\bigl(S_{m-1}-b_{3^{m-1}}\bigr).
\]

Como \(m\ge 2\), \(b_{3^{m-1}}=2\), así que esta contribución es \(S_{m-1}-1\).

Por tanto,

\[
S_m=2m+1+(S_{m-1}-1)=S_{m-1}+2m.
\]

Con \(S_1=4\),

\[
S_m=4+2\sum_{j=2}^m j
=4+2\left(\frac{m(m+1)}2-1\right)
=m(m+1)+2.
\]

Para \(m=2025\),

\[
S_{2025}=2025\cdot 2026+2=4\,102\,652.
\]

\[
\boxed{4102652}
\]