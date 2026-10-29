Sea \(h=3^{3^3}=3^{27}\) el número de treses de la torre, y denotemos la torre como \(T_h\).

Como \(333=9\cdot 37\), usamos el teorema chino del resto.

**Módulo 9:**  
El exponente de la base \(3\) es \(T_{h-1}\), que es al menos \(3\). Entonces \(3^{T_{h-1}}\) es divisible por \(9\):

\[
T_h \equiv 0 \pmod 9.
\]

**Módulo 37:**  
Como \(\gcd(3,37)=1\) y \(\varphi(37)=36\), necesitamos \(T_{h-1}\bmod 36\).

Para \(T_{h-1}\):
- Módulo \(4\): \(T_{h-1}=3^{T_{h-2}}\), y \(T_{h-2}\) es impar, luego
  \[
  T_{h-1}\equiv 3 \pmod 4.
  \]
- Módulo \(9\): como \(T_{h-2}\ge 2\),
  \[
  T_{h-1}\equiv 0 \pmod 9.
  \]

Resolviendo
\[
x\equiv 0\pmod 9,\qquad x\equiv 3\pmod 4,
\]
obtenemos
\[
T_{h-1}\equiv 27 \pmod{36}.
\]

Por tanto,
\[
T_h \equiv 3^{T_{h-1}} \equiv 3^{27} \pmod{37}.
\]

Como
\[
3^9 \equiv -1 \pmod{37},
\]
se tiene
\[
3^{27}=(3^9)^3\equiv (-1)^3=-1\equiv 36 \pmod{37}.
\]

Finalmente resolvemos
\[
T_h\equiv 0\pmod 9,\qquad T_h\equiv 36\pmod{37}.
\]
Escribiendo \(T_h=9k\), queda
\[
9k\equiv 36\pmod{37}.
\]
Como \(9^{-1}\equiv 33\pmod{37}\),

\[
k\equiv 36\cdot 33\equiv (-1)\cdot 33\equiv 4\pmod{37}.
\]

Así \(T_h=9\cdot 4=36\).

\[
\boxed{36}
\]