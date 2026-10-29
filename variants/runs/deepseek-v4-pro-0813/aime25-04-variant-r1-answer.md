Voy a resolver paso a paso.

Queremos contar los pares ordenados $(x,y)$ con $x,y\in\{-100,\dots,100\}$ que cumplen

\[
10x^2+7xy-12y^2=0.
\]

**1. Factorizar el polinomio.** Buscamos factorizar $10x^2+7xy-12y^2$. Por ejemplo, probando $(2x+3y)(5x-4y)$:

\[
(2x+3y)(5x-4y)=10x^2-8xy+15xy-12y^2=10x^2+7xy-12y^2.
\]

Entonces la ecuación es equivalente a

\[
(2x+3y)(5x-4y)=0.
\]

Por lo tanto, o bien $2x+3y=0$, o bien $5x-4y=0$.

**2. Primer caso: $2x+3y=0$.**

Despejamos: $2x=-3y$, así que $x=-\frac32 y$. Para que $x$ sea entero, $y$ debe ser par. Escribimos $y=2k$ con $k\in\mathbb Z$. Entonces

\[
x=-3k.
\]

La restricción es $-100\le x,y\le 100$:

- Para $y=2k$: $-100\le 2k\le 100$ implica $-50\le k\le 50$.
- Para $x=-3k$: $-100\le -3k\le 100$ implica $-100\le -3k\le 100$, es decir $-\frac{100}{3}\le k\le \frac{100}{3}$, lo que da $-33\le k\le 33$.

La intersección es $-33\le k\le 33$, lo que da $33-(-33)+1=67$ valores.

**3. Segundo caso: $5x-4y=0$.**

Despejamos: $5x=4y$, así que $x=\frac45 y$. Para que $x$ sea entero, $y$ debe ser múltiplo de $5$. Escribimos $y=5k$ con $k\in\mathbb Z$. Entonces

\[
x=4k.
\]

Las restricciones:

- Para $y=5k$: $-100\le 5k\le 100$ implica $-20\le k\le 20$.
- Para $x=4k$: $-100\le 4k\le 100$ implica $-25\le k\le 25$.

La intersección es $-20\le k\le 20$, lo que da $20-(-20)+1=41$ valores.

**4. Intersección de los dos casos.**

¿Hay pares que cumplan ambas condiciones a la vez? Si $2x+3y=0$ y $5x-4y=0$, el sistema solo tiene la solución trivial $(0,0)$. Veamos: de $2x+3y=0$ tenemos $x=-\frac32 y$; sustituyendo en $5x-4y=0$ queda $-\frac{15}{2}y-4y=0$, es decir $-\frac{23}{2}y=0$, luego $y=0$ y $x=0$.

El par $(0,0)$ ya está contado en ambos casos: en el primer caso corresponde a $k=0$ y en el segundo también a $k=0$. Por lo tanto, hay que restar $1$.

**5. Total.**

\[
67+41-1=107.
\]

La respuesta es

\[
\boxed{107}
\]