

Para calcular \(g^{-1}(0)+g^{-1}(12)\), buscamos los valores de \(x\) tales que \(g(x)=0\) y \(g(x)=12\).

La función es

\[
g(x)=
\begin{cases}
4-x, & x\le 4,\\
-x^3+3x^2+4x, & x>4.
\end{cases}
\]

Primero buscamos \(g^{-1}(0)\).

En la primera rama:

\[
4-x=0 \implies x=4.
\]

Como \(x=4\) sí cumple \(x\le 4\), tenemos \(g^{-1}(0)=4\).

En la segunda rama, para \(x>4\),

\[
-x^3+3x^2+4x=-x(x-4)(x+1).
\]

Para \(x>4\), esta expresión es negativa, así que no produce \(0\). Por tanto, la única solución es \(x=4\).

Ahora buscamos \(g^{-1}(12)\).

En la primera rama:

\[
4-x=12 \implies x=-8.
\]

Como \(-8\le 4\), esto es válido, así que \(g^{-1}(12)=-8\).

En la segunda rama:

\[
-x^3+3x^2+4x=12
\]

\[
x^3-3x^2-4x+12=0
\]

\[
(x-3)(x^2-4)=0
\]

\[
(x-3)(x-2)(x+2)=0.
\]

Las soluciones son \(x=3,2,-2\), pero ninguna cumple \(x>4\). Por tanto, la única solución es \(x=-8\).

Finalmente,

\[
g^{-1}(0)+g^{-1}(12)=4+(-8)=-4.
\]

\[
\boxed{-4}
\]