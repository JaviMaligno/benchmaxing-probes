## Planteamiento

Sea $s = x+y$ y $t = x+y+z$. La expresión es
$$\frac{t\,(4s^2+t^2)}{xyz}.$$

**Paso 1: optimizar en $x,y$ con $s$ fijo.**
Como el numerador solo depende de $s$ y $t$, conviene maximizar $xy$. Por AM–GM, $xy \le s^2/4$, con igualdad si $x=y=s/2$. Entonces
$$\frac{t(4s^2+t^2)}{xyz} \ge \frac{4t(4s^2+t^2)}{s^2(t-s)},$$
usando $z = t-s$.

**Paso 2: reducir a una variable.**
Con $u = s/t \in (0,1)$, es decir $s = ut$:
$$\frac{4t\cdot t^2(4u^2+1)}{u^2t^2\cdot t(1-u)} = \frac{4(4u^2+1)}{u^2(1-u)} =: 4f(u).$$
El factor $t^3$ se cancela, así que el problema es homogéneo de grado cero, como debía ser.

**Paso 3: minimizar $f(u) = \dfrac{4u^2+1}{u^2-u^3}$.**
$$f'(u) = 0 \iff 8u(u^2-u^3) - (4u^2+1)(2u-3u^2) = 0 \iff 4u^4+3u^2-2u = 0,$$
y dividiendo por $u>0$: $4u^3+3u-2=0$, cuya raíz es $u = \tfrac12$ (factoriza como $(2u-1)(2u^2+u+2)=0$, y el factor cuadrático no tiene raíces reales). Es el único punto crítico en $(0,1)$, y $f\to\infty$ en ambos extremos, por lo que es mínimo.

$$f(1/2) = \frac{4\cdot\frac14+1}{\frac14\cdot\frac12} = \frac{2}{1/8} = 16 \quad\Longrightarrow\quad 4f(1/2) = 64.$$

**Paso 4: verificación de la igualdad.**
$u=1/2$ significa $x+y = z$, junto con $x=y$. Tomando $x=y=1$, $z=2$:
$$\frac{4\,[(2+2)^2+4^2]}{1\cdot1\cdot2} = \frac{4\cdot 32}{2} = 64. \checkmark$$

\boxed{64}