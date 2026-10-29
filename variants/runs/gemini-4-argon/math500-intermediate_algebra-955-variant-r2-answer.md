Sea $f(x) = px^2 + qx + r$. Sabemos que $|f(x)| \le 1$ para todo $0 \le x \le 2$.

En particular, evaluando $f(x)$ en $x = 0, 1, 2$, obtenemos:
\begin{align*}
f(0) &= r, \\
f(1) &= p + q + r, \\
f(2) &= 4p + 2q + r.
\end{align*}
Como $0, 1, 2 \in [0, 2]$, se cumple que $|f(0)| \le 1$, $|f(1)| \le 1$ y $|f(2)| \le 1$.

Podemos despejar $p, q, r$ en función de $f(0), f(1)$ y $f(2)$:
\begin{align*}
r &= f(0), \\
p &= \frac{1}{2}f(2) - f(1) + \frac{1}{2}f(0), \\
q &= -\frac{1}{2}f(2) + 2f(1) - \frac{3}{2}f(0).
\end{align*}

Aplicando la desigualdad triangular a cada coeficiente y usando que $|f(0)|, |f(1)|, |f(2)| \le 1$:
\begin{align*}
|p| &= \left| \frac{1}{2}f(2) - f(1) + \frac{1}{2}f(0) \right| \le \frac{1}{2}|f(2)| + |f(1)| + \frac{1}{2}|f(0)| \le \frac{1}{2} + 1 + \frac{1}{2} = 2, \\
|q| &= \left| -\frac{1}{2}f(2) + 2f(1) - \frac{3}{2}f(0) \right| \le \frac{1}{2}|f(2)| + 2|f(1)| + \frac{3}{2}|f(0)| \le \frac{1}{2} + 2 + \frac{3}{2} = 4, \\
|r| &= |f(0)| \le 1.
\end{align*}

Sumando las tres desigualdades, obtenemos una cota superior:
\[ |p| + |q| + |r| \le 2 + 4 + 1 = 7. \]

Para verificar que este valor máximo es alcanzable, tomamos $f(0) = 1$, $f(1) = -1$ y $f(2) = 1$, lo que corresponde al polinomio:
\[ f(x) = 2x^2 - 4x + 1 = 2(x - 1)^2 - 1. \]
Para todo $x \in [0, 2]$, tenemos que $-1 \le x - 1 \le 1$, por lo que $0 \le (x - 1)^2 \le 1$, y en consecuencia $-1 \le 2(x - 1)^2 - 1 \le 1$. Por tanto, se cumple la condición $|f(x)| \le 1$ en $[0, 2]$ y:
\[ |p| + |q| + |r| = |2| + |-4| + |1| = 7. \]

\boxed{7}