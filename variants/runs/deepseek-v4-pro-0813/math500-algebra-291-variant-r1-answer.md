Sea \(p\) la probabilidad de que Carla gane cuando es su turno.

- En su turno, Carla gana con probabilidad \(\frac{2}{6}=\frac13\) (saca 5 o 6).
- Si no gana, con probabilidad \(\frac23\), pasa el turno a Dev.
- En el turno de Dev, este gana con probabilidad \(\frac{2}{6}=\frac13\) (saca 1 o 2).
- Si Dev no gana, con probabilidad \(\frac23\), el juego vuelve a Carla en la misma situación inicial.

Por tanto, tras un turno de Carla y uno de Dev, la probabilidad de que el juego continúe sin ganador es:
\[
\frac23\cdot\frac23=\frac49
\]

Así, Carla gana en su primer turno con probabilidad \(\frac13\), o el juego se reinicia con probabilidad \(\frac49\). Entonces:
\[
p=\frac13+\frac49p
\]
\[
p-\frac49p=\frac13
\]
\[
\frac59p=\frac13
\]
\[
p=\frac35
\]

\[
\boxed{\frac35}
\]