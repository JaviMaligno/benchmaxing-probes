Sea \(T_n\) la torre de \(n\) sietes, con asociación hacia la derecha:
\[
T_1=7,\qquad T_{n+1}=7^{T_n}.
\]
Queremos \(T_N\) módulo \(777\), donde \(N=7^{7^7}\).

Factoramos
\[
777=3\cdot 7\cdot 37.
\]

**1. Módulo \(7\):**
\[
T_N=7^{T_{N-1}}\equiv 0 \pmod 7,
\]
pues el exponente es positivo.

**2. Módulo \(3\):**
Como \(7\equiv 1\pmod 3\),
\[
T_N\equiv 1 \pmod 3.
\]

**3. Módulo \(37\):**
El orden de \(7\) módulo \(37\) es \(9\), ya que
\[
7^3\equiv 10\pmod{37},\qquad 7^9\equiv 10^3=1000\equiv 1\pmod{37},
\]
y ningún divisor propio de \(9\) da \(1\).

Necesitamos \(T_{N-1}\pmod 9\). Módulo \(9\), el orden de \(7\) es \(3\). Además,
\[
T_{N-2}\equiv 1\pmod 3,
\]
porque \(7\equiv 1\pmod 3\). Por lo tanto,
\[
T_{N-1}=7^{T_{N-2}}\equiv 7^1\equiv 7\pmod 9.
\]
Así,
\[
T_N\equiv 7^{T_{N-1}}\equiv 7^7\pmod{37}.
\]
Calculamos:
\[
7^2\equiv 12,\qquad 7^4\equiv 33,\qquad 7^7=7^4\cdot 7^2\cdot 7\equiv 33\cdot 12\cdot 7\equiv 34\pmod{37}.
\]

**4. Teorema chino del resto:** buscamos \(x\) tal que
\[
x\equiv 0\pmod 7,\qquad x\equiv 1\pmod 3,\qquad x\equiv 34\pmod{37}.
\]
Escribimos \(x=7a\). Entonces
\[
7a\equiv a\equiv 1\pmod 3,
\]
y
\[
7a\equiv 34\pmod{37}.
\]
Como \(7^{-1}\equiv 16\pmod{37}\),
\[
a\equiv 34\cdot 16\equiv 26\pmod{37}.
\]
Resolviendo \(a\equiv 1\pmod 3\) y \(a\equiv 26\pmod{37}\), obtenemos \(a=100\). Por lo tanto,
\[
x=7a=700.
\]

\[
\boxed{700}
\]