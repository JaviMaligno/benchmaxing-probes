Primero, simplificamos la congruencia:

\[
14u \equiv 46 \pmod{100}.
\]

Dividimos todo entre 2, ya que \(\operatorname{mcd}(14,46,100) = 2\):

\[
7u \equiv 23 \pmod{50}.
\]

Ahora necesitamos el inverso de \(7\) módulo \(50\). Calculamos:

\[
7 \cdot 7 = 49 \equiv -1 \pmod{50},
\]

por lo que

\[
7^{-1} \equiv -7 \equiv 43 \pmod{50}.
\]

Multiplicamos ambos lados por \(43\):

\[
u \equiv 23 \cdot 43 \pmod{50}.
\]

Calculamos:

\[
23 \cdot 43 = 989.
\]

Y:

\[
989 \div 50 = 19 \text{ resto } 39.
\]

Por tanto:

\[
u \equiv 39 \pmod{50}.
\]

Las soluciones positivas son:

\[
u = 39, 89, 139, \ldots
\]

Las dos más pequeñas son \(39\) y \(89\). Su promedio es:

\[
\frac{39 + 89}{2} = \frac{128}{2} = 64.
\]

\[
\boxed{64}
\]