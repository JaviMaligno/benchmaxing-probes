

Sea \(N=24q+r\), con \(0\le r\le 23\). Definamos

\[
c(t)=\left\lfloor \frac{t}{10}\right\rfloor+(t\bmod 10),
\]

el número mínimo de monedas de \(10\) y \(1\) centavos necesarias para formar \(t\). El algoritmo voraz toma \(q\) monedas de \(24\) y luego forma \(r\) con monedas de \(10\) y \(1\), así que usa

\[
G=q+c(r)
\]

monedas.

Cualquier otra colección debe usar \(q-x\) monedas de \(24\), para algún \(x\ge 0\). Entonces debe formar \(r+24x\) usando monedas de \(10\) y \(1\), lo cual óptimamente toma \(c(r+24x)\) monedas. El total sería

\[
T_x=q-x+c(r+24x).
\]

Como \(c(y+20)=c(y)+2\), tenemos

\[
c(r+24x)=2x+c(r+4x),
\]

y por tanto

\[
T_x-G=x+c(r+4x)-c(r).
\]

Para \(0\le r\le 23\), se cumple \(c(r)\le 10\). Si \(x\ge 10\), entonces

\[
T_x-G\

\[
T_x-G=x+c(r+4x)-c(r)\ge x-c(r)\ge 0,
\]

así que solo \(x=1,\dots,9\) pueden producir una falla.

Escribamos \(r=10u+v\) con \(0\le v\le 9\), y \(4x=10k+m\) con \(0\le m\le 9\). Sea \(\varepsilon=1\) si \(v+m\ge 10\) (acarreo) y \(\varepsilon=0\) en caso contrario. Entonces

\[
c(r)=u+v,\qquad c(r+4x)=u+k+v+m-9\varepsilon,
\]

por lo que

\[
T_x-G=x+k+m-9\varepsilon=5x-9k-9\varepsilon.
\]

Para \(x=1,\dots,9\):

\[
\begin{array}{c|c|c|c|c}
x & 4x & T_x-G\text{ sin acarreo} & T_x-G\text{ con acarreo} & \text{condición de acarreo}\\
\hline
1 & 4 & 5 & -4 & v\ge 6\\
2 & 8 & 10 & 1 & v\ge 2\\
3 & 12 & 6 & -3 & v\ge 8\\
4 & 16 & 11 & 2 & v\ge 4\\
5 & 20 & 7 & - & \text{imposible}\\
6 & 24 & 12 & 3 & v\ge 6\\
7 & 28 & 17 & 8 & v\ge 2\\
8 & 32 & 13 & 4 & v\ge 8\\
9 & 36 & 18 & 9 & v\ge 4
\end{array}
\]

Los únicos casos negativos son \(x=1\) con \(v\ge 6\), y \(x=3\) con \(v\ge 8\) (este último ya incluido en el anterior). Por tanto, para \(q\ge 1\), el algoritmo falla exactamente cuando \(r\) termina en \(6,7,8,9\); es decir,

\[
r\in\{6,7,8,9,16,17,18,19\}.
\]

Para \(q=0\) (\(1\le N\le 23\)), no se puede quitar ninguna moneda de \(24\), y el algoritmo voraz con monedas de \(10\) y \(1\) es óptimo.

Ahora contamos hasta \(1000\). Como

\[
1000=24\cdot 41+16,
\]

hay:

- \(N=1,\dots,23\): \(23\) éxitos.
- Bloques completos \(q=1,\dots,40\): cada bloque tiene \(24\) valores, de los cuales \(8\) fallan, así que hay \(16\) éxitos por bloque: \(40\cdot 16=640\).
- Bloque final \(q=41\), \(r=0,\dots,16\): hay \(17\) valores, y fallan \(r=6,7,8,9,16\), o sea \(5\) fallas; quedan \(12\) éxitos.

Total de éxitos:

\[
23+640+12=675.
\]

\[
\boxed{675}
\]