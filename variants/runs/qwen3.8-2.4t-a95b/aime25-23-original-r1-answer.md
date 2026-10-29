

Sea \(N=25q+r\), con \(0\le r<25\). El algoritmo voraz toma \(q\) monedas de \(25\) centavos y luego completa \(r\) usando monedas de \(10\) y \(1\) centavos.

Para una cantidad \(M\) usando solo monedas de \(1\) y \(10\), el número mínimo de monedas es

\[
h(M)=\left\lfloor \frac{M}{10}\right\rfloor+(M\bmod 10),
\]

pues siempre conviene usar la mayor cantidad posible de monedas de \(10\).

Si usamos \(x\) monedas de \(25\), el total de monedas es

\[
T(x)=x+h(N-25x).
\]

El algoritmo voraz usa \(x=q\). Comparemos con quitar \(k\) monedas de \(25\), es decir, usar \(x=q-k\). Entonces la diferencia es

\[
T(q-k)-T(q)=h(r+25k)-h(r)-k.
\]

Analicemos cómo cambia \(h\) al sumar \(25\). Si \(m\equiv s\pmod{10}\), con \(0\le s\le 9\):

- si \(s\in\{0,1,2,3,4\}\), entonces \(h(m+25)-h(m)=7\);
- si \(s\in\{5,6,7,8,9\}\), entonces \(h(m+25)-h(m)=-2\).

Por tanto, para \(k=1\),

\[
T(q-1)-T(q)=
\begin{cases}
7-1=6>0, & r\equiv 0,1,2,3,4\pmod{10},\\
-2-1=-3<0, & r\equiv 5,6,7,8,9\pmod{10}.
\end{cases}
\]

Así que quitar una moneda de \(25\) mejora el resultado exactamente cuando

\[
r\in\{5,6,7,8,9,15,16,17,18,19\}.
\]

Para \(k\ge 2\), los cambios de \(h\) al añadir \(25\) alternan entre \(+7\) y \(-2\), de modo que cada dos pasos aumentan \(h\) en \(5\). Entonces:

- si \(k=2t\), la diferencia es \(5t-2t=3t>0\);
- si \(k=2t+1\) con \(t\ge 1\), la diferencia es al menos \(5t-2-(2t+1)=3t-3\ge 0\).

Luego ninguna reducción de dos o más monedas de \(25\) produce estrictamente menos monedas. Por tanto, el algoritmo voraz falla exactamente cuando \(q\ge 1\) y

\[
r\in\{5,6,7,8,9,15,16,17,18,19\}.
\]

Ahora contamos entre \(1\) y \(1000\).

- De \(1\) a \(24\), tenemos \(q=0\), así que el algoritmo siempre tiene éxito: \(24\) valores.
- De \(25\) a \(999\), hay \(39\) bloques completos de \(25\) números. En cada bloque fallan \(10\) valores y tienen éxito \(15\):  
  \[
  39\cdot 15=585.
  \]
- \(N=1000\) corresponde a \(q=40\), \(r=0\), y tiene éxito: \(1\) valor.

Total:

\[
24+585+1=610.
\]

\[
\boxed{610}
\]