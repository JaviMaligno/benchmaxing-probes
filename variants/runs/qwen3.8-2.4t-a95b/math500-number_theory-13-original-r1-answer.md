

Tenemos la congruencia:

\[
14u \equiv 46 \pmod{100}.
\]

Primero calculamos \(\gcd(14,100)=2\). Como \(2\mid 46\), la congruencia tiene solución, y al dividir entre \(2\) obtenemos:

\[
7u \equiv 23 \pmod{50}.
\]

Ahora buscamos el inverso de \(7\) módulo \(50\). Como

\[
7\cdot 43 = 301 \equiv 1 \pmod{50},
\]

el inverso es \(43\). Multiplicamos ambos lados por \(43\):

\[
u \equiv 23\cdot 43 \pmod{50}.
\]

Calculamos:

\[
23\cdot 43 = 989 \equiv 39 \pmod{50}.
\]

Por tanto,

\[
u \equiv 39 \pmod{50}.
\]

Módulo \(100\), esto da dos clases de soluciones:

\[
u \equiv 39 \pmod{100}
\quad \text{o} \quad
u \equiv 89 \pmod{100}.
\]

Las dos soluciones enteras positivas más pequeñas son \(39\) y \(89\). Su promedio es

\[
\frac{39+89}{2}=\frac{128}{2}=64.
\]

\[
\boxed{64}
\]