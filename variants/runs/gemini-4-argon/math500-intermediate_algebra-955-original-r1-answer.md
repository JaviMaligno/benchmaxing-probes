Sea $P(x) = ax^2 + bx + c$. Sabemos que $|P(x)| \le 1$ para todo $x \in [0, 1]$.

Evaluamos el polinomio en tres puntos específicos del intervalo $[0, 1]$, a saber, $x = 0$, $x = \frac{1}{2}$ y $x = 1$:
\begin{align*}
P(0) &= c \\
P\left(\frac{1}{2}\right) &= \frac{1}{4}a + \frac{1}{2}b + c \\
P(1) &= a + b + c
\end{align*}

Por la condición del problema, se cumple que $|P(0)| \le 1$, $\left|P\left(\frac{1}{2}\right)\right| \le 1$ y $|P(1)| \le 1$.

Ahora, despejamos los coeficientes $a, b, c$ en función de estos tres valores:
\begin{align*}
c &= P(0) \\
b &= -3P(0) + 4P\left(\frac{1}{2}\right) - P(1) \\
a &= 2P(0) - 4P\left(\frac{1}{2}\right) + 2P(1)
\end{align*}

Aplicando la desigualdad triangular a cada coeficiente, obtenemos las siguientes cotas superiores:
\begin{align*}
|a| &\le 2|P(0)| + 4\left|P\left(\frac{1}{2}\right)\right| + 2|P(1)| \le 2(1) + 4(1) + 2(1) = 8 \\
|b| &\le 3|P(0)| + 4\left|P\left(\frac{1}{2}\right)\right| + |P(1)| \le 3(1) + 4(1) + 1(1) = 8 \\
|c| &= |P(0)| \le 1
\end{align*}

Sumando estas tres desigualdades, tenemos que:
\[|a| + |b| + |c| \le 8 + 8 + 1 = 17.\]

Para verificar que el valor $17$ es alcanzable, consideremos el polinomio de Chebyshev trasladado $P(x) = 8x^2 - 8x + 1 = 8\left(x - \frac{1}{2}\right)^2 - 1$. 
Para todo $x \in [0, 1]$, se tiene que $-\frac{1}{2} \le x - \frac{1}{2} \le \frac{1}{2}$, por lo que $0 \le \left(x - \frac{1}{2}\right)^2 \le \frac{1}{4}$. Multiplicando por $8$ y restando $1$, obtenemos:
\[-1 \le 8\left(x - \frac{1}{2}\right)^2 - 1 \le 1,\]
lo cual confirma que $|P(x)| \le 1$ para todo $0 \le x \le 1$. Para este polinomio, $|a| + |b| + |c| = |8| + |-8| + |1| = 17$.

\boxed{17}