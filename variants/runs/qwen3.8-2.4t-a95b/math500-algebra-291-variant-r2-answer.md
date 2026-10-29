

Sea \(P\) la probabilidad de que Carla gane el juego desde el inicio.

- En el turno de Carla, ella gana si saca 5 o 6:
  \[
  \Pr(\text{Carla gana en su turno})=\frac{2}{6}=\frac{1}{3}
  \]
- Si no gana, con probabilidad \(\frac{2}{3}\), pasa al turno de Dev.
- En el turno de Dev, él gana si saca 1 o 2:
  \[
  \Pr(\text{Dev gana en su turno})=\frac{2}{6}=\frac{1}{3}
  \]
- Si Dev no gana, con probabilidad \(\frac{2}{3}\), el juego vuelve al estado inicial.

Entonces:
\[
P=\frac{1}{3}+\frac{2}{3}\cdot\frac{2}{3}\cdot P
\]
\[
P=\frac{1}{3}+\frac{4}{9}P
\]
\[
P-\frac{4}{9}P=\frac{1}{3}
\]
\[
\frac{5}{9}P=\frac{1}{3}
\]
\[
P=\frac{1}{3}\cdot\frac{9}{5}=\frac{3}{5}
\]

\[
\boxed{\frac{3}{5}}
\]