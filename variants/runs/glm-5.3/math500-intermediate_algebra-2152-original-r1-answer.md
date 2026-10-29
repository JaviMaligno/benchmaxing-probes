**Paso 1: Identificar la estructura.** Cada término es un polinomio de grado 2 en $x$ (por ejemplo, el primero se anula en $x=b$ y $x=c$, y vale 1 en $x=a$). Son exactamente los polinomios de la base de Lagrange para los nodos $a,b,c$. Por lo tanto, $p(x)$ interpola la función constante $1$ en esos tres puntos: $p(a)=p(b)=p(c)=1$.

**Paso 2: Verificar que los coeficientes de grado 2 y 1 se cancelan.** Si $p(x)$ tuviera grado 2, al ser $p(a)=p(b)=p(c)=1$, el polinomio $p(x)-1$ tendría tres raíces distintas, lo que obliga a $p(x)-1\equiv 0$. Es decir, $p(x)=1$ para todo $x$.

**Paso 3: Confirmación con un ejemplo.** Con $a=0,\ b=1,\ c=2$:
$$\frac{(x-1)(x-2)}{2} - x(x-2) + \frac{x(x-1)}{2} = \frac{x^2-3x+2}{2} - x^2+2x + \frac{x^2-x}{2} = 1.$$

Los términos en $x^2$ y en $x$ se cancelan y queda la constante 1. Así, $p(x)$ es el polinomio constante 1.

**Conclusión.** El grado de $p(x)$ es

$$\boxed{0}$$