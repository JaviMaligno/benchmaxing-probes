Para encontrar los valores reales positivos de $k$ tales que la función
$$g(x) = \frac{(x - 8)(x - 50)(x - 72)(x - k)}{x}$$
alcance su valor mínimo sobre $(0, \infty)$ en exactamente dos números reales positivos, analicemos la condición de minimalidad.

### Paso 1: Condición para el mínimo doble
Dado que $k > 0$, cuando $x \to 0^+$ y cuando $x \to \infty$, tenemos que $g(x) \to +\infty$. Por lo tanto, $g(x)$ alcanza un mínimo global $M$ en $(0, \infty)$.

Si $g(x)$ alcanza su valor mínimo $M$ en exactamente dos números reales positivos distintos $a$ y $b$, entonces $g(x) - M \ge 0$ para todo $x > 0$, con igualdad únicamente en $x = a$ y $x = b$. Multiplicando por $x > 0$, el polinomio mónico de cuarto grado
$$P(x) = x(g(x) - M) = (x - 8)(x - 50)(x - 72)(x - k) - Mx$$
debe cumplir $P(x) \ge 0$ en $(0, \infty)$ y anularse en los puntos interiores $x = a$ y $x = b$. Esto implica que $a$ y $b$ son raíces dobles de $P(x)$, por lo que podemos escribir:
$$(x - 8)(x - 50)(x - 72)(x - k) - Mx = (x - a)^2(x - b)^2$$
con $a, b > 0$ y $a \neq b$.

### Paso 2: Cambio de variable y factorización
Sean $s = a + b > 0$ y $p = ab > 0$ (con $s^2 > 4p$ para que $a$ y $b$ sean reales y distintos). La ecuación anterior se escribe como:
$$(x - 8)(x - 50)(x - 72)(x - k) = (x^2 - sx + p)^2 + Mx$$
Al evaluar en las cuatro raíces $r_1 = 8, r_2 = 50, r_3 = 72, r_4 = k > 0$, el lado izquierdo se anula, por lo que $(r_i^2 - sr_i + p)^2 + Mr_i = 0$, lo que exige $M = -c^2 \le 0$ para algún $c \ge 0$.

Haciendo el cambio de variable $x = t^2$ y definiendo $t_1 = \sqrt{8} = 2\sqrt{2}$, $t_2 = \sqrt{50} = 5\sqrt{2}$, $t_3 = \sqrt{72} = 6\sqrt{2}$ y $t_4 = \sqrt{k} > 0$, obtenemos:
$$\prod_{i=1}^4 (t^2 - t_i^2) = (t^4 - st^2 + p)^2 - c^2 t^2 = (t^4 - st^2 + ct + p)(t^4 - st^2 - ct + p)$$

Los dos factores cuárticos del lado derecho tienen las raíces opuestas entre sí. Por lo tanto, para cada $i \in \{1, 2, 3, 4\}$, exactamente uno de los valores $\pm t_i$ es raíz del primer factor $A(t) = t^4 - st^2 + ct + p$, y el otro es raíz de $A(-t)$. Sean $\epsilon_i t_i$ (con $\epsilon_i \in \{1, -1\}$) las cuatro raíces de $A(t)$.

1. Como el coeficiente de $t^3$ en $A(t)$ es $0$, la suma de sus raíces es cero:
   $$\epsilon_1 t_1 + \epsilon_2 t_2 + \epsilon_3 t_3 + \epsilon_4 t_4 = 0$$
2. Como el término independiente de $A(t)$ es $p = ab > 0$, el producto de sus raíces debe ser positivo:
   $$(\epsilon_1 t_1)(\epsilon_2 t_2)(\epsilon_3 t_3)(\epsilon_4 t_4) = p > 0 \implies \epsilon_1 \epsilon_2 \epsilon_3 \epsilon_4 = 1$$

### Paso 3: Cálculo de los tres valores de $k$
Como $t_i > 0$ y la suma $\sum \epsilon_i t_i = 0$, no todos los signos $\epsilon_i$ pueden ser iguales. Dado que su producto es $+1$, exactamente dos de los signos $\epsilon_i$ son $+1$ y los otros dos son $-1$.

Escribiendo $t_4 = \sqrt{k} = w\sqrt{2}$ (es decir, $k = 2w^2$ con $w > 0$) y dividiendo la relación $\sum \epsilon_i t_i = 0$ entre $\sqrt{2}$, tenemos que la suma de dos elementos de $\{2, 5, 6, w\}$ debe ser igual a la suma de los otros dos:

- **Caso 1:** $w + 2 = 5 + 6 \implies w = 9 \implies k = 2(9^2) = 162$.
- **Caso 2:** $w + 5 = 2 + 6 \implies w = 3 \implies k = 2(3^2) = 18$.
- **Caso 3:** $w + 6 = 2 + 5 \implies w = 1 \implies k = 2(1^2) = 2$.

En los tres casos se verifica que $s = \frac{1}{2}(8 + 50 + 72 + k) = 65 + w^2$ y $p = t_1 t_2 t_3 t_4 = 120w$ cumplen $s^2 > 4p$, garantizando dos mínimos positivos distintos $a$ y $b$.

Finalmente, la suma de estos tres valores de $k$ es:
$$2 + 18 + 162 = 182$$

\boxed{182}