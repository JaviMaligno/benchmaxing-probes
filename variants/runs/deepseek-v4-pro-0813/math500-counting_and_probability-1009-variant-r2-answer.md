Este es un problema de combinaciones con repetición (también llamado «de estrellas y barras»). Queremos elegir 7 muffins de entre 3 tipos, sin importar el orden y pudiendo repetir tipos, con al menos 7 de cada tipo disponibles.

Debemos contar las soluciones enteras no negativas de:

\[
x_1 + x_2 + x_3 = 7
\]

donde \(x_1, x_2, x_3\) son las cantidades de cada tipo de muffin.

La fórmula de combinaciones con repetición es:

\[
\binom{n+k-1}{k-1}
\]

con \(n=7\) (objetos) y \(k=3\) (tipos):

\[
\binom{7+3-1}{3-1} = \binom{9}{2} = \frac{9 \cdot 8}{2} = 36
\]

Por tanto, Maya puede elegir 36 surtidos diferentes.

\[
\boxed{36}
\]