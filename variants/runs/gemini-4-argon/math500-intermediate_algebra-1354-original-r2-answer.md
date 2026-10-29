Para evaluar la suma dada, denotemos por $S$ a la expresión:
\[S = \sum_{k=1}^{1997} \frac{1}{1 + \omega^k} = \frac{1}{1 + \omega} + \frac{1}{1 + \omega^2} + \dots + \frac{1}{1 + \omega^{1996}} + \frac{1}{1 + \omega^{1997}}.\]

**Paso 1: Evaluar el último término.**
Sabemos que $\omega^{1997} = 1$, por lo que el último término de la suma (para $k = 1997$) es:
\[\frac{1}{1 + \omega^{1997}} = \frac{1}{1 + 1} = \frac{1}{2}.\]

**Paso 2: Agrupar los términos restantes en parejas.**
Para cualquier entero $k$ tal que $1 \le k \le 1996$, se cumple que $\omega^{1997 - k} = \omega^{1997}\omega^{-k} = \omega^{-k}$. Además, como $1997$ es impar, $(-1)^{1997} = -1 \neq 1$, lo cual garantiza que $\omega^k \neq -1$ y ningún denominador se anula.

Podemos emparejar el término $k$-ésimo con el término $(1997 - k)$-ésimo:
\[\frac{1}{1 + \omega^k} + \frac{1}{1 + \omega^{1997 - k}} = \frac{1}{1 + \omega^k} + \frac{1}{1 + \omega^{-k}}.\]

Multiplicando el numerador y el denominador de la segunda fracción por $\omega^k$, obtenemos:
\[\frac{1}{1 + \omega^k} + \frac{\omega^k}{\omega^k + 1} = \frac{1 + \omega^k}{1 + \omega^k} = 1.\]

**Paso 3: Sumar todas las parejas y el término final.**
Los primeros $1996$ términos forman exactamente $\frac{1996}{2} = 998$ parejas, y cada pareja suma $1$. Sumando a esto el último término que calculamos en el Paso 1, resulta:
\[S = 998 \cdot 1 + \frac{1}{2} = 998 + \frac{1}{2} = \frac{1997}{2}.\]

\boxed{\frac{1997}{2}}