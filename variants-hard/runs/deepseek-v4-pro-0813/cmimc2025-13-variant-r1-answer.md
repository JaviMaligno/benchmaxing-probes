Sea \(P_n\) la probabilidad de que Priya y Tomás bailen en la misma ronda cuando quedan \(n\) personas en el círculo y ambos siguen vivos.

En una ronda con \(n\) personas, hay \(\binom{n}{5}\) formas de elegir a los 5 que bailan.

La probabilidad de que **ambos sean elegidos** en esa ronda es

\[
\frac{\binom{n-2}{3}}{\binom{n}{5}}
=
\frac{20}{n(n-1)}.
\]

En ese caso ya bailan juntos.

Si no son elegidos juntos, pueden seguir ambos vivos para la siguiente ronda. La probabilidad de que ambos sobrevivan a la ronda (o no son elegidos, o uno es elegido y gana) es

\[
\frac{(n-4)(n-5)}{n(n-1)}.
\]

Por lo tanto,

\[
P_n=\frac{20}{n(n-1)}+\frac{(n-4)(n-5)}{n(n-1)}P_{n-4}.
\]

Además, cuando quedan \(5\) personas, todos bailan, así que

\[
P_5=1.
\]

Afirmamos que

\[
P_n=\frac{5}{n}.
\]

Lo comprobamos por inducción. Si \(P_{n-4}=\frac{5}{n-4}\), entonces

\[
P_n
=
\frac{20}{n(n-1)}
+
\frac{(n-4)(n-5)}{n(n-1)}\cdot \frac{5}{n-4}
=
\frac{20+5(n-5)}{n(n-1)}
=
\frac{5}{n}.
\]

Como empezamos con \(n=45\),

\[
P_{45}=\frac{5}{45}=\frac{1}{9}.
\]

\[
\boxed{\frac{1}{9}}
\]