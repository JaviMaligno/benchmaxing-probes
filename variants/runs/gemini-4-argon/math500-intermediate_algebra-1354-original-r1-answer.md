Para evaluar la suma dada:
\[S = \frac{1}{1 + \omega} + \frac{1}{1 + \omega^2} + \dots + \frac{1}{1 + \omega^{1997}},\]
utilizamos la propiedad de que $\omega^{1997} = 1$.

**Paso 1: Evaluar el último término de la suma**
Dado que $\omega^{1997} = 1$, el último término (correspondiente al exponente $1997$) es:
\[\frac{1}{1 + \omega^{1997}} = \frac{1}{1 + 1} = \frac{1}{2}.\]

**Paso 2: Emparejar los primeros $1996$ términos**
Observemos que para cualquier entero $k$ tal que $1 \le k \le 1996$, se cumple que:
\[\omega^{1997 - k} = \frac{\omega^{1997}}{\omega^k} = \frac{1}{\omega^k} = \omega^{-k}.\]

Si sumamos el término $k$-ésimo con el término $(1997 - k)$-ésimo, obtenemos:
\[\frac{1}{1 + \omega^k} + \frac{1}{1 + \omega^{1997 - k}} = \frac{1}{1 + \omega^k} + \frac{1}{1 + \omega^{-k}}.\]

Multiplicando el numerador y el denominador de la segunda fracción por $\omega^k$:
\[\frac{1}{1 + \omega^k} + \frac{\omega^k}{\omega^k + 1} = \frac{1 + \omega^k}{1 + \omega^k} = 1.\]
*(Nota: Como $1997$ es impar, ningún $\omega^k$ puede ser igual a $-1$, por lo que los denominadores nunca se anulan).*

**Paso 3: Calcular la suma total**
Los primeros $1996$ términos se pueden agrupar en $\frac{1996}{2} = 998$ parejas, donde cada pareja suma $1$:
\[S = \sum_{k=1}^{998} \left( \frac{1}{1 + \omega^k} + \frac{1}{1 + \omega^{1997 - k}} \right) + \frac{1}{1 + \omega^{1997}}\]
\[S = 998 \cdot 1 + \frac{1}{2} = \frac{1997}{2}.\]

\boxed{\frac{1997}{2}}