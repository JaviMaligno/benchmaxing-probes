**Planteamiento de las áreas.** Las rectas $y=ax+c$ y $y=ax+d$ son paralelas con separación vertical $|d-c|$. El paralelogramo formado con las rectas de pendiente $b$ tiene base vertical $|d-c|$ y "anchura" horizontal determinada por dónde se cruzan las rectas de distintas pendientes: la distancia horizontal entre las intersecciones es $\frac{|d-c|}{|a-b|}$. Por lo tanto, el área del primer paralelogramo es

$$\frac{(d-c)^2}{|a-b|} = 18.$$

Para el segundo paralelogramo, las separaciones verticales son $|c-(-d)| = c+d$, así que

$$\frac{(c+d)^2}{|a-b|} = 72.$$

**Resolución.** Dividiendo las dos ecuaciones:

$$\frac{(c+d)^2}{(d-c)^2} = 4 \implies c+d = 2|d-c|.$$

Tomando $d>c$ (ambos positivos): $c+d = 2(d-c)$, es decir $d = 3c$.

Sustituyendo en la primera ecuación: $(3c-c)^2 = 18|a-b|$, o sea $4c^2 = 18|a-b|$, lo que da $2c^2 = 9|a-b|$.

Como $c$ es entero positivo, $9 \mid 2c^2$ implica $3 \mid c$. El menor valor es $c=3$, que da $|a-b| = 2$ y $d = 9$.

**Minimizar $a+b$.** Necesitamos enteros positivos con $|a-b|=2$: lo mínimo es $a=3, b=1$ (o viceversa), con $a+b=4$.

**Verificación:** $\frac{(9-3)^2}{2} = \frac{36}{2} = 18$ ✓ y $\frac{(3+9)^2}{2} = \frac{144}{2} = 72$ ✓.

Entonces $a+b+c+d = 3+1+3+9 = 16$.

$$\boxed{16}$$