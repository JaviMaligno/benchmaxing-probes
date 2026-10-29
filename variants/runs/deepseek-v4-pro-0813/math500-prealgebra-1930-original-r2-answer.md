Vamos a analizar el cuadrado mágico.

El cuadrado es:

| | | |
|---|---|---|
| $n-3$ | $n+2$ | $2$ |
| $3$ | $2n-9$ | $n$ |
| $n+1$ | $1$ | $n-1$ |

En un cuadrado mágico, la suma de cada fila, columna y diagonal es la misma.

**Paso 1: Calcular la suma de una fila.**

Tomemos la primera fila:

\[
(n-3) + (n+2) + 2 = 2n + 1
\]

**Paso 2: Usar la diagonal principal.**

La diagonal principal es:

\[
(n-3) + (2n-9) + (n-1)
\]

\[
= n - 3 + 2n - 9 + n - 1 = 4n - 13
\]

Como debe ser igual a $2n+1$:

\[
4n - 13 = 2n + 1
\]

\[
2n = 14
\]

\[
n = 7
\]

**Paso 3: Verificar.**

Con $n=7$, el cuadrado queda:

\[
\begin{matrix}
4 & 9 & 2\\
3 & 5 & 7\\
8 & 1 & 6
\end{matrix}
\]

Cada fila, columna y diagonal suma $15$. Por lo tanto, es correcto.

\[
\boxed{7}
\]