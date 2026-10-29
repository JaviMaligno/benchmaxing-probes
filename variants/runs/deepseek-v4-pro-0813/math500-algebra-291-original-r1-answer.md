Sea \(p\) la probabilidad de que Alicia gane cuando es su turno, y \(q\) la probabilidad de que Alicia gane cuando es el turno de Bob.

- En el turno de Alicia: con probabilidad \(1/2\) sale cara y gana; con probabilidad \(1/2\) pasa al turno de Bob.
  \[
  p = \frac12 + \frac12 q
  \]

- En el turno de Bob: con probabilidad \(1/2\) sale cruz y Bob gana (Alicia pierde); con probabilidad \(1/2\) pasa al turno de Alicia.
  \[
  q = \frac12 p
  \]

Sustituyendo:
\[
p = \frac12 + \frac12\left(\frac12 p\right)
= \frac12 + \frac14 p
\]
\[
\frac34 p = \frac12
\]
\[
p = \frac23
\]

Como Alicia empieza, la probabilidad de que gane es:
\[
\boxed{\frac23}
\]