Definimos la transformación

\[
t_k=\frac32\cdot \frac{y_k-1}{y_k+1}.
\]

Sustituyendo en la recurrencia se obtiene

\[
t_{k+1}=t_k^2-\frac34.
\]

Como \(y_1=\frac{19}{14}\),

\[
t_1=\frac32\cdot \frac{\frac{19}{14}-1}{\frac{19}{14}+1}
=\frac32\cdot \frac{5/14}{33/14}
=\frac{5}{22}.
\]

Afirmamos que

\[
t_k=\frac{A_k}{2\cdot 11^{2^{k-1}}}
\]

con \(A_1=5\) y

\[
A_{k+1}=\frac{A_k^2-3\cdot 11^{2^k}}2.
\]

En efecto, esto sale de

\[
t_{k+1}=t_k^2-\frac34.
\]

La transformación inversa es

\[
y_k=\frac{2t_k+3}{3-2t_k}.
\]

Así, poniendo \(E=2^{k-1}\),

\[
y_k=\frac{A_k+3\cdot 11^E}{3\cdot 11^E-A_k}.
\]

Se comprueba que \(A_k\) es impar y no es divisible por \(3\) ni por \(11\). Por tanto,

\[
\gcd(A_k+3B,3B-A_k)=2,
\]

donde \(B=11^E\). Al reducir la fracción, queda

\[
m+n=\frac{(A_k+3B)+(3B-A_k)}2=3B=3\cdot 11^E.
\]

Para \(k=2025\),

\[
E=2^{2024},
\]

así que

\[
m+n=3\cdot 11^{2^{2024}}.
\]

Calculamos módulo \(1000\):

Módulo \(8\), como \(11\equiv 3\) y el exponente es par,

\[
3\cdot 11^{2^{2024}}\equiv 3\pmod 8.
\]

Módulo \(125\), como \(\varphi(125)=100\),

\[
2^{2024}\equiv 16\pmod{100},
\]

luego

\[
11^{2^{2024}}\equiv 11^{16}\pmod{125}.
\]

Además,

\[
11^2\equiv -4,\quad 11^4\equiv 16,\quad 11^8\equiv 6,\quad 11^{16}\equiv 36\pmod{125}.
\]

Por tanto,

\[
3\cdot 11^{2^{2024}}\equiv 3\cdot 36=108\pmod{125}.
\]

Resolviendo

\[
x\equiv 3\pmod 8,\qquad x\equiv 108\pmod{125},
\]

se obtiene

\[
x\equiv 483\pmod{1000}.
\]

\[
\boxed{483}
\]