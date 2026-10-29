## Planteamiento

El cociente es homogéneo de grado 0 (numerador y denominador son de grado 3), así que podemos normalizar.

**Paso 1: fijar $x+y$.** Sea $s=x+y$ y $t=x+y+z$. La expresión es

$$\frac{t\left[4s^2+t^2\right]}{xyz}.$$

Para $s$ fijo, el numerador no depende de cómo se reparta $s$ entre $x$ e $y$, así que conviene maximizar $xy$: por AM–GM, $xy\le s^2/4$, con igualdad en $x=y=s/2$.

**Paso 2: reducir a una variable.** Con $xy=s^2/4$:

$$\frac{t(4s^2+t^2)}{\frac{s^2}{4}z}=\frac{4t(4s^2+t^2)}{s^2 z}.$$

Normalizando $s=1$ y escribiendo $z=t-1$ (con $t>1$):

$$f(t)=\frac{4t(4+t^2)}{t-1}=\frac{4(t^3+4t)}{t-1}.$$

**Paso 3: minimizar.** La derivada se anula cuando

$$(3t^2+4)(t-1)-(t^3+4t)=2t^3-3t^2-4=0.$$

Como $t=2$ satisface $16-12-4=0$, y factorizando $2t^3-3t^2-4=(t-2)(2t^2+t+2)$ (el segundo factor no tiene raíces reales), $t=2$ es el único punto crítico, y es mínimo ($f\to\infty$ en $t\to1^+$ y $t\to\infty$).

$$f(2)=\frac{4\cdot 2\cdot(4+4)}{1}=64.$$

**Verificación.** Con $s=1$, $t=2$: $z=1$, $x=y=\tfrac12$. Entonces $x+y+z=2$, $2x+2y=2$, $xyz=\tfrac14$:

$$\frac{2\,[2^2+2^2]}{1/4}=\frac{16}{1/4}=64.$$

\boxed{64}