## Razonamiento

**Paso 1: Reescribir el polinomio.**

La expresión 
$$w^{10} - w^9 + w^8 - \cdots - w + 1$$ 
es una serie geométrica de razón $-w$ con 11 términos:
$$1 - w + w^2 - \cdots + w^{10} = \frac{1 - (-w)^{11}}{1 - (-w)} = \frac{1 + w^{11}}{1 + w}.$$

**Paso 2: Resolver la ecuación.**

La ecuación equivale a 
$$\frac{w^{11} + 1}{w + 1} = 0,$$ 
es decir, $w^{11} = -1$ con $w \neq -1$.

Los ángulos que satisfacen $w^{11} = -1 = e^{i\pi}$ son 
$$\varphi = \frac{(2k+1)\pi}{11}, \qquad k = 0, 1, \dots, 10,$$ 
todos en $[0, 2\pi)$ (pues $\frac{21\pi}{11} < 2\pi$), con $\rho = 1 > 0$.

**Paso 3: Excluir $w = -1$.**

El valor $\varphi = \pi$ corresponde a $\frac{(2k+1)\pi}{11} = \pi$, o sea $k = 5$, que debe excluirse (en efecto, $w=-1$ da $11 \neq 0$).

**Paso 4: Sumar los ángulos válidos.**

$$\sum_{k=0}^{10} (2k+1) = 121, \qquad \text{excluyendo } k=5: \; 121 - 11 = 110.$$

$$\sum \varphi = \frac{110\pi}{11} = 10\pi.$$

$$\boxed{10\pi}$$