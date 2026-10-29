Sea \(p\) la probabilidad de que Alice gane cuando le toca lanzar a ella.

**Planteamiento recursivo:**

1. En su turno, Alice gana de inmediato con probabilidad \( \tfrac{1}{2} \) (sale cara).
2. Con probabilidad \( \tfrac{1}{2} \) sale cruz y el turno pasa a Bob.
3. En el turno de Bob, él gana con probabilidad \( \tfrac{1}{2} \) (sale cruz). Con probabilidad \( \tfrac{1}{2} \) sale cara y el juego vuelve a Alice, exactamente en la misma situación inicial.

Entonces:

\[
p = \frac{1}{2} + \frac{1}{2}\cdot\frac{1}{2}\cdot p = \frac{1}{2} + \frac{p}{4}
\]

Resolviendo:

\[
p - \frac{p}{4} = \frac{1}{2} \quad\Rightarrow\quad \frac{3p}{4} = \frac{1}{2} \quad\Rightarrow\quad p = \frac{2}{3}
\]

**Verificación por serie:** Alice gana en su \(k\)-ésimo intento con probabilidad \(\left(\tfrac{1}{4}\right)^{k-1}\cdot\tfrac{1}{2}\) (cada "ronda completa fallida" ocurre con probabilidad \(\tfrac{1}{2}\cdot\tfrac{1}{2}=\tfrac{1}{4}\)):

\[
\sum_{k=0}^{\infty} \frac{1}{2}\left(\frac{1}{4}\right)^{k} = \frac{1/2}{1 - 1/4} = \frac{2}{3}
\]

\[
\boxed{\dfrac{2}{3}}
\]