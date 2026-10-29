Sea \(p_n\) la probabilidad buscada cuando quedan \(n\) amigos en el círculo y Michael y James siguen vivos.

Para una ronda con \(n\) jugadores, la probabilidad de que ambos sean elegidos para la batalla es

\[
\frac{\binom{n-2}{2}}{\binom{n}{4}}=\frac{12}{n(n-1)}.
\]

Si ambos son elegidos, ya batallaron en la misma ronda.

Si no son elegidos ambos, para que aún puedan batallar juntos más adelante deben sobrevivir ambos a la ronda. La probabilidad de que ninguno sea elegido es

\[
\frac{\binom{n-2}{4}}{\binom{n}{4}}=\frac{(n-4)(n-5)}{n(n-1)},
\]

y la probabilidad de que exactamente uno sea elegido es

\[
\frac{2\binom{n-2}{3}}{\binom{n}{4}}=\frac{8(n-4)}{n(n-1)}.
\]

Si exactamente uno es elegido, gana con probabilidad \(\frac14\). Por lo tanto, la probabilidad de que ambos sobrevivan es

\[
\frac{(n-4)(n-5)}{n(n-1)}+\frac14\cdot \frac{8(n-4)}{n(n-1)}
=\frac{(n-4)(n-3)}{n(n-1)}.
\]

Así,

\[
p_n=\frac{12}{n(n-1)}+\frac{(n-4)(n-3)}{n(n-1)}p_{n-3}.
\]

Claramente \(p_4=1\). Afirmamos que \(p_n=\frac4n\). En efecto, si \(p_{n-3}=\frac{4}{n-3}\),

\[
p_n=\frac{12}{n(n-1)}+\frac{(n-4)(n-3)}{n(n-1)}\cdot\frac{4}{n-3}
=\frac{12+4(n-4)}{n(n-1)}
=\frac{4}{n}.
\]

Como inicialmente hay \(34\) amigos,

\[
p_{34}=\frac{4}{34}=\frac{2}{17}.
\]

\[
\boxed{\frac{2}{17}}
\]