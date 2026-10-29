# Resolución paso a paso

**Paso 1: Simplificar la ecuación.**

Como el término constante es $1$, $x = 0$ no es raíz. El polinomio es recíproco, así que dividimos entre $x^2$:

$$x^2 + ax - b + \frac{a}{x} + \frac{1}{x^2} = 0 \quad\Longrightarrow\quad \left(x + \frac{1}{x}\right)^2 + a\left(x + \frac{1}{x}\right) - b - 2 = 0.$$

**Paso 2: Sustitución.**

Sea $t = x + \frac{1}{x}$. La ecuación queda $t^2 + at - b - 2 = 0$, es decir $b = t^2 + at - 2$. La ecuación $x + \frac{1}{x} = t$ tiene solución real si y solo si $|t| \ge 2$.

**Paso 3: Caso $t \ge 2$.**

Con $a \ge 0$: $b = t^2 + at - 2 \ge 4 - 2 = 2 > 1$, lo cual viola $b \le 1$. No hay soluciones.

**Paso 4: Caso $t \le -2$.**

Escribimos $t = -u$ con $u \ge 2$: $\quad b = u^2 - au - 2.$

- **Cota $b \ge 0$:** para $u \ge 2$ y $a \le 1$, $b(u)$ es creciente y $b(2) = 2 - 2a \ge 0$. Se cumple automáticamente.
- **Cota $b \le 1$:** $b(2) = 2-2a \le 1$ exige $a \ge \tfrac12$, y $u$ puede crecer hasta $u^* = \frac{a + \sqrt{a^2+12}}{2}$, donde $b(u^*) = 1$.

Como $b(u)$ es continua y creciente en $[2, u^*]$, para cada $a \in [\tfrac12, 1]$ el valor de $b$ recorre todo el intervalo $[2-2a,\; 1]$.

**Paso 5: Área.**

$$S = \{(a,b) : \tfrac12 \le a \le 1,\; 2-2a \le b \le 1\}$$

$$\text{Área} = \int_{1/2}^{1} \bigl(1 - (2-2a)\bigr)\, da = \int_{1/2}^{1} (2a-1)\, da = \left[a^2 - a\right]_{1/2}^{1} = 0 - \left(\tfrac14 - \tfrac12\right) = \tfrac14.$$

$$\boxed{\dfrac{1}{4}}$$