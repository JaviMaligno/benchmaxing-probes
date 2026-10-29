Resolvemos paso a paso:

Queremos las soluciones positivas de  
\[
14u \equiv 46 \pmod{100}.
\]

Primero calculamos \(\gcd(14,100)=2\). Como \(2\mid 46\), la congruencia tiene soluciones.

Dividimos toda la congruencia entre \(2\):

\[
7u \equiv 23 \pmod{50}.
\]

Ahora buscamos el inverso multiplicativo de \(7\) módulo \(50\). Como

\[
7\cdot 43 = 301 \equiv 1 \pmod{50},
\]

el inverso es \(43\). Multiplicamos ambos lados por \(43\):

\[
u \equiv 23\cdot 43 \pmod{50}.
\]

Calculamos:

\[
23\cdot 43 = 989.
\]

Y reducimos módulo \(50\):

\[
989 \equiv 39 \pmod{50}.
\]

Por lo tanto, las soluciones módulo \(100\) son

\[
u \equiv 39 \pmod{50}.
\]

Las dos menores soluciones positivas son entonces

\[
u=39 \quad \text{y} \quad u=89.
\]

Su promedio es

\[
\frac{39+89}{2}=\frac{128}{2}=64.
\]

\[
\boxed{64}
\]