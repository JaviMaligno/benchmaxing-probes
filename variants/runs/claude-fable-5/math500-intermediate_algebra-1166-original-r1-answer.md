## Solución

**Paso 1: Reducir a dos variables.** Para $a+b$ fijo, el numerador no cambia, pero el denominador $abc$ se maximiza cuando $a=b$ (pues $ab \le \frac{(a+b)^2}{4}$). Así que el mínimo ocurre con $a=b=t$.

**Paso 2: Sustituir.** Con $a=b=t$, la expresión queda:
$$\frac{(2t+c)\left[4t^2+(2t+4c)^2\right]}{t^2 c}.$$

Es homogénea de grado 0, así que pongamos $u = c/t$ (equivalentemente $t=1$, $c=u$):
$$f(u)=\frac{(2+u)\left[4+(2+4u)^2\right]}{u}=\frac{8(2+u)(2u^2+2u+1)}{u}=8\left(2u^2+6u+5+\frac{2}{u}\right).$$

**Paso 3: Minimizar.** Derivando:
$$f'(u)=8\left(4u+6-\frac{2}{u^2}\right)=0 \;\Longrightarrow\; 2u^3+3u^2-1=0.$$

Probando $u=\tfrac12$: $2\cdot\tfrac18+3\cdot\tfrac14-1 = \tfrac14+\tfrac34-1=0$. ✓ (Es la única raíz positiva, pues $2u^3+3u^2$ es creciente en $u>0$.)

**Paso 4: Evaluar.** Con $u=\tfrac12$:
$$f\left(\tfrac12\right)=8\left(2\cdot\tfrac14+3+5+4\right)=8\left(\tfrac12+12\right)=8\cdot\tfrac{25}{2}=100.$$

El mínimo se alcanza, por ejemplo, con $a=b=2$, $c=1$: $\frac{5\,[16+64]}{4}=\frac{400}{4}=100$. ✓

$$\boxed{100}$$