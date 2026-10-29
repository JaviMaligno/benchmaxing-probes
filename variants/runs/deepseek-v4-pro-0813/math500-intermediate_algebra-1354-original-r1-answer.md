Vamos a razonar paso a paso.

Sea $\omega$ una raíz $1997$-ésima de la unidad distinta de $1$. Tenemos que la suma pedida es
\[
S=\sum_{k=1}^{1997}\frac{1}{1+\omega^k}.
\]

Como $\omega^{1997}=1$, los números $\omega,\omega^2,\dots,\omega^{1997}$ son todas las raíces $1997$-ésimas de la unidad (incluyendo $1=\omega^{1997}$).

Observemos que para $k=1997$, $\omega^{1997}=1$, y ese término es $\frac{1}{1+1}=\frac12$.

Para los demás términos, usamos una identidad útil: si $\omega^k\neq -1$, entonces
\[
\frac{1}{1+x}+\frac{1}{1+x^{-1}}=1.
\]
En efecto:
\[
\frac{1}{1+x}+\frac{x}{x+1}=\frac{1+x}{1+x}=1.
\]

Como $1997$ es impar, no hay ninguna raíz tal que $\omega^k=-1$, porque $(-1)^{1997}=-1\neq 1$.

Emparejemos cada término $\frac{1}{1+\omega^k}$ con $\frac{1}{1+\omega^{-k}}$ para $k=1,2,\dots,1996$. Cada pareja suma $1$. Hay $\frac{1996}{2}=998$ parejas.

Por lo tanto,
\[
S=998\cdot 1+\frac12=998+\frac12=\frac{1997}{2}.
\]

La respuesta es:
\[
\boxed{\frac{1997}{2}}
\]