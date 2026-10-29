Para encontrar el mayor valor posible de $|a| + |b| + |c|$, sea $P(x) = ax^2 + bx + c$. Sabemos que $|P(x)| \le 1$ para todo $x \in [0, 1]$.

Evaluemos el polinomio en tres puntos específicos dentro del intervalo $[0, 1]$: $x = 0$, $x = \frac{1}{2}$ y $x = 1$:
\begin{align*}
P(0) &= c \\
P\left(\frac{1}{2}\right) &= \frac{1}{4}a + \frac{1}{2}b + c \\
P(1) &= a + b + c
\end{align*}

Por la condición del problema, se cumple que $|P(0)| \le 1$, $\left|P\left(\frac{1}{2}\right)\right| \le 1$ y $|P(1)| \le 1$.

Ahora, podemos despejar los coeficientes $a, b$ y $c$ como combinaciones lineales de estos tres valores:
\begin{align*}
c &= P(0) \\
a &= 2P(0) - 4P\left(\frac{1}{2}\right) + 2P(1) \\
b &= -3P(0) + 4P\left(\frac{1}{2}\right) - P(1)
\end{align*}

Aplicando la desigualdad triangular a cada coeficiente y utilizando que el valor absoluto de $P(x)$ en cada uno de estos puntos es a lo sumo $1$, obtenemos las siguientes cotas superiores:
\begin{align*}
|a| &= \left|2P(0) - 4P\left(\frac{1}{2}\right) + 2P(1)\right| \le 2|P(0)| + 4\left|P\left(\frac{1}{2}\right)\right| + 2|P(1)| \le 2(1) + 4(1) + 2(1) = 8 \\
|b| &= \left|-3P(0) + 4P\left(\frac{1}{2}\right) - P(1)\right| \le 3|P(0)| + 4\left|P\left(\frac{1}{2}\right)\right| + |P(1)| \le 3(1) + 4(1) + 1(1) = 8 \\
|c| &= |P(0)| \le 1
\end{align*}

Sumando estas tres desigualdades, resulta:
\[|a| + |b| + |c| \le 8 + 8 + 1 = 17.\]

Para verificar que el valor $17$ es alcanzable, tomamos $P(0) = 1$, $P\left(\frac{1}{2}\right) = -1$ y $P(1) = 1$, lo que nos da el polinomio de Chebyshev trasladado:
\[P(x) = 8x^2 - 8x + 1 = 2(2x - 1)^2 - 1.\]

Para todo $x \in [0, 1]$, tenemos que $2x - 1 \in [-1, 1]$, por lo que $0 \le (2x - 1)^2 \le 1$, lo cual implica que:
\[-1 \le 2(2x - 1)^2 - 1 \le 1.\]

Así, $|8x^2 - 8x + 1| \le 1$ se cumple en todo el intervalo $[0, 1]$, alcanzando $|a| + |b| + |c| = |8| + |-8| + |1| = 17$.

\boxed{17}