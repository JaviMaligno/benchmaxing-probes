

Sea \(p\) la probabilidad de que Alice gane cuando es su turno, y \(q\) la probabilidad de que Alice gane cuando es el turno de Bob.

- En el turno de Alice, ella gana con probabilidad \(\frac{1}{2}\) si sale cara. Si sale cruz, pasa al turno de Bob:
  \[
  p = \frac{1}{2} + \frac{1}{2}q
  \]

- En el turno de Bob, él gana con probabilidad \(\frac{1}{2}\) si sale cruz, así que Alice pierde. Si sale cara, vuelve al turno de Alice:
  \[
  q = \frac{1}{2}p
  \]

Sustituyendo:

\[
p = \frac{1}{2} + \frac{1}{2}\cdot \frac{1}{2}p
\]

\[
p = \frac{1}{2} + \frac{1}{4}p
\]

\[
\frac{3}{4}p = \frac{1}{2}
\]

\[
p = \frac{2}{3}
\]

\[
\boxed{\frac{2}{3}}
\]