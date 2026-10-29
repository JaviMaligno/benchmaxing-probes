Para hallar el valor esperado de la suma dada, sea $n = 23$. Por la linealidad de la esperanza, podemos escribir:

$$\mathbb{E}\left[\sum_{k=1}^{n}\bigl(g(g(k))-k\bigr)^{2}\right] = \sum_{k=1}^{n}\mathbb{E}\left[\bigl(g(g(k))-k\bigr)^{2}\right].$$

Analicemos la distribución de $g(g(k))$ para un valor fijo de $k \in \{1, 2, \ldots, n\}$:

1. **Caso 1: $g(k) = k$.**
   Como $g$ se elige uniformemente al azar, esto ocurre con probabilidad $\frac{1}{n}$. En este caso, $g(g(k)) = g(k) = k$, por lo que $\bigl(g(g(k)) - k\bigr)^2 = 0$.

2. **Caso 2: $g(k) = j \neq k$.**
   Esto ocurre con probabilidad $\frac{n-1}{n}$. Dado que $j \neq k$, el valor de $g(j) = g(g(k))$ es independiente de la elección de $g(k)$ y está distribuido uniformemente en el conjunto $\{1, 2, \ldots, n\}$. Por lo tanto, condicionado a que $g(k) \neq k$, el valor esperado de $\bigl(g(g(k)) - k\bigr)^2$ es:
   $$\frac{1}{n}\sum_{m=1}^{n}(m-k)^2.$$

Combinando ambos casos por la ley de la esperanza total, para cada $k$ tenemos:

$$\mathbb{E}\left[\bigl(g(g(k))-k\bigr)^{2}\right] = \frac{1}{n}\cdot 0 + \frac{n-1}{n}\left(\frac{1}{n}\sum_{m=1}^{n}(m-k)^2\right) = \frac{n-1}{n^2}\sum_{m=1}^{n}(m-k)^2.$$

Sumando sobre todos los valores de $k$ desde $1$ hasta $n$:

$$\mathbb{E}\left[\sum_{k=1}^{n}\bigl(g(g(k))-k\bigr)^{2}\right] = \frac{n-1}{n^2}\sum_{k=1}^{n}\sum_{m=1}^{n}(m-k)^2.$$

Desarrollamos la suma doble utilizando las fórmulas conocidas de las sumas de potencias:

$$\begin{aligned}
\sum_{k=1}^{n}\sum_{m=1}^{n}(m-k)^2 &= \sum_{k=1}^{n}\sum_{m=1}^{n}(m^2 - 2mk + k^2) \\
&= 2n\sum_{m=1}^{n}m^2 - 2\left(\sum_{m=1}^{n}m\right)\left(\sum_{k=1}^{n}k\right) \\
&= 2n\cdot\frac{n(n+1)(2n+1)}{6} - 2\left(\frac{n(n+1)}{2}\right)^2 \\
&= \frac{n^2(n+1)}{6}\bigl(2(2n+1) - 3(n+1)\bigr) \\
&= \frac{n^2(n+1)(n-1)}{6} = \frac{n^2(n^2-1)}{6}.
\end{aligned}$$

Sustituyendo este resultado en la expresión de la esperanza:

$$\mathbb{E}\left[\sum_{k=1}^{n}\bigl(g(g(k))-k\bigr)^{2}\right] = \frac{n-1}{n^2}\cdot\frac{n^2(n^2-1)}{6} = \frac{(n-1)^2(n+1)}{6}.$$

Finalmente, evaluamos para $n = 23$:

$$\frac{(23-1)^2(23+1)}{6} = \frac{22^2 \cdot 24}{6} = 484 \cdot 4 = 1936.$$

\boxed{1936}