Vamos a razonar paso a paso.

La función es

\[
f(x)=
\begin{cases}
ax^2, & x\ge a,\\
ax+2a, & x<a.
\end{cases}
\]

Queremos que la gráfica de \(y=f(x)\) corte **toda recta horizontal** al menos una vez. Una recta horizontal es \(y=c\), con \(c\in\mathbb R\). Es decir, para todo \(c\in\mathbb R\) debe existir \(x\) tal que \(f(x)=c\).

Esto equivale a que el rango de \(f\) sea todo \(\mathbb R\): \(\operatorname{Im}(f)=\mathbb R\).

**Caso para \(x\ge a\):**

Aquí \(f(x)=ax^2\).

- Si \(a>0\), obtenemos valores \(ax^2\ge 0\), concretamente en \(x\ge a\) nos da desde \(a\cdot a^2=a^3\) hasta \(+\infty\). Es decir, \([a^3,\infty)\) (si \(a>0\), \(a<a^3\) no es relevante; el mínimo en esta rama es \(a^3\)).
- Si \(a<0\), \(ax^2\le 0\); en \(x\ge a\) (donde \(x\) puede ser positivo o negativo según \(a\)) el rango no está acotado inferiormente ni superiormente de forma inmediata, tendremos que analizar.
- Si \(a=0\), \(f(x)=0\) para \(x\ge0\), y \(f(x)=0\) para \(x<0\); el rango es \(\{0\}\), no cubre todo.

**Caso para \(x<a\):**

Aquí \(f(x)=ax+2a=a(x+2)\).

Como \(x<a\), si \(a>0\) entonces \(x+2<a+2\), luego multiplicando por \(a>0\):

\[
f(x)<a(a+2)=a^2+2a.
\]

Y no hay cota inferior: cuando \(x\to-\infty\), \(ax+2a\to-\infty\). Entonces el rango de esta rama para \(a>0\) es \((-\infty,\;a^2+2a)\).

**Uniendo las ramas para \(a>0\):**

- Rama izquierda: \((-\infty,\;a^2+2a)\).
- Rama derecha: \([a^3,\infty)\).

Además hay solape o hueco según estos valores. Para cubrir todo \(\mathbb R\), el hueco entre \(a^2+2a\) y \(a^3\) no debe existir; es decir, necesitamos que el máximo de la rama izquierda sea al menos el mínimo de la rama derecha:

\[
a^2+2a \ge a^3.
\]

Además, notemos que en \(x=a\) las dos fórmulas coinciden: \(a\cdot a^2=a^3\) y \(a\cdot a+2a=a^2+2a\). Pero la definición asigna \(x=a\) a la primera rama. Para \(a>0\), la segunda rama está definida para \(x<a\), por lo que en \(x=a\) el valor \(a^2+2a=a^3\) solo se alcanza si \(a^2+2a=a^3\).

La condición \(a^2+2a\ge a^3\) con \(a>0\):

\[
a^2+2a-a^3\ge0 \implies -a(a^2-a-2)\ge0 \implies -a(a-2)(a+1)\ge0.
\]

Como \(a>0\), \(a+1>0\), así que la desigualdad se reduce a \(-(a-2)\ge0\), es decir \(a\le2\).

Por tanto, para \(a>0\), la condición es \(0<a\le2\). El mayor valor posible en esta zona es \(a=2\).

**¿Y para \(a<0\)?**

Analicemos rápido. Para \(a<0\):

- Rama derecha \(x\ge a\): \(ax^2\le0\). Como \(x\) puede ser grande en valor absoluto (positivo), \(ax^2\to-\infty\). El máximo en esta rama es \(0\), cuando \(x=0\), siempre que \(0\ge a\), lo cual es cierto si \(a<0\). Así la rama derecha da \((-\infty,0]\).
- Rama izquierda \(x<a\): \(ax+2a\). Como \(a<0\), cuando \(x\to-\infty\), \(ax+2a\to+\infty\). Para \(x=a^{-}\), \(f(x)\to a^2+2a\) (sin incluir). Entonces da \((a^2+2a,\infty)\).

Uniendo: \((-\infty,0]\) y \((a^2+2a,\infty)\). Para cubrir todo \(\mathbb R\) no debe haber hueco: necesitamos \(a^2+2a\le0\). Eso es \(a(a+2)\le0\), es decir \(-2\le a\le0\). Con \(a<0\): \(-2\le a<0\).

El mayor valor aquí es cercano a \(0\), pero menor que \(0\). Comparado con \(a=2\), es menor.

Por lo tanto, el mayor valor posible de \(a\) es

\[
\boxed{2}
\]