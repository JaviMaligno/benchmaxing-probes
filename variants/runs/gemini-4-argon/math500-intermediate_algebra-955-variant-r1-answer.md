Para encontrar el mayor valor posible de $|p| + |q| + |r|,$ definamos el polinomio $f(x) = px^2 + qx + r.$ Sabemos que $|f(x)| \le 1$ para todo $0 \le x \le 2.$

En particular, podemos evaluar $f(x)$ en los puntos $x = 0, 1, 2$:
\begin{align*}
f(0) &= r \\
f(1) &= p + q + r \\
f(2) &= 4p + 2q + r
\end{align*}
Por la condición del problema, se cumple que $|f(0)| \le 1,$ $|f(1)| \le 1$ y $|f(2)| \le 1.$

Podemos despejar $p,$ $q$ y $r$ en términos de $f(0),$ $f(1)$ y $f(2)$ resolviendo el sistema de ecuaciones lineales:
\begin{align*}
r &= f(0) \\
p &= \frac{1}{2}f(2) - f(1) + \frac{1}{2}f(0) \\
q &= -\frac{1}{2}f(2) + 2f(1) - \frac{3}{2}f(0)
\end{align*}

Aplicando la desigualdad triangular a cada coeficiente y usando que $|f(0)|, |f(1)|, |f(2)| \le 1,$ obtenemos cotas superiores para $|p|,$ $|q|$ y $|r|$:
\begin{align*}
|p| &= \left|\frac{1}{2}f(0) - f(1) + \frac{1}{2}f(2)\right| \le \frac{1}{2}|f(0)| + |f(1)| + \frac{1}{2}|f(2)| \le \frac{1}{2} + 1 + \frac{1}{2} = 2, \\
|q| &= \left|-\frac{3}{2}f(0) + 2f(1) - \frac{1}{2}f(2)\right| \le \frac{3}{2}|f(0)| + 2|f(1)| + \frac{1}{2}|f(2)| \le \frac{3}{2} + 2 + \frac{1}{2} = 4, \\
|r| &= |f(0)| \le 1.
\end{align*}

Sumando estas tres desigualdades, obtenemos:
\[|p| + |q| + |r| \le 2 + 4 + 1 = 7.\]

Para verificar que este valor máximo de $7$ es alcanzable, observamos que las igualdades se cumplen simultáneamente cuando $f(0) = 1,$ $f(1) = -1$ y $f(2) = 1$ (o con los signos opuestos). Esto corresponde a $p = 2,$ $q = -4$ y $r = 1,$ lo que nos da el polinomio:
\[f(x) = 2x^2 - 4x + 1 = 2(x - 1)^2 - 1.\]

Para cualquier $x \in [0, 2],$ tenemos que $-1 \le x - 1 \le 1,$ por lo que $0 \le (x - 1)^2 \le 1,$ y en consecuencia:
\[-1 \le 2(x - 1)^2 - 1 \le 1.\]
Esto confirma que $|f(x)| \le 1$ en todo el intervalo $[0, 2],$ y para este polinomio tenemos $|p| + |q| + |r| = |2| + |-4| + |1| = 7.$

\boxed{7}