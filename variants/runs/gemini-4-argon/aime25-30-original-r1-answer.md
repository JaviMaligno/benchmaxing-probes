Para encontrar los valores de $k > 0$ tales que la función
$$f(x) = \frac{(x - 18)(x - 72)(x - 98)(x - k)}{x}$$
alcance su valor mínimo en exactamente dos números reales positivos $x$, analizamos el comportamiento de $f(x)$ para $x > 0$.

### Paso 1: Condición para el mínimo doble
Dado que $k > 0$, cuando $x \to 0^+$ tenemos $f(x) \to +\infty$, y cuando $x \to +\infty$ también se cumple $f(x) \to +\infty$. Por tanto, $f(x)$ alcanza un mínimo global $m$ en $(0, \infty)$.

Para que $f(x)$ alcance su mínimo global $m$ en exactamente dos reales positivos distintos $a$ y $b$, la diferencia $f(x) - m$ debe ser no negativa para todo $x > 0$ y anularse únicamente en $x = a$ y $x = b$. Como $x(f(x) - m)$ es un polinomio mónico de grado $4$ y $a, b$ deben ser raíces dobles (al ser mínimos locales en el interior del dominio), debe cumplirse la identidad polinómica:
$$(x - 18)(x - 72)(x - 98)(x - k) - mx = (x - a)^2(x - b)^2$$

Sea $s = a + b$ y $p = ab$. Para que $a$ y $b$ sean reales positivos y distintos, necesitamos $s > 0$, $p > 0$ y $s^2 > 4p$. Desarrollando el lado derecho:
$$(x - a)^2(x - b)^2 + mx = (x^2 - sx + p)^2 + mx = x^4 - 2sx^3 + (s^2 + 2p)x^2 + (m - 2sp)x + p^2$$

### Paso 2: Igualación de coeficientes
Sean $r_1 = 18$, $r_2 = 72$, $r_3 = 98$ y $r_4 = k$. Igualando los coeficientes de grado $3$, $2$ y $0$ de ambos polinomios (el coeficiente de grado $1$ simplemente determina el valor de $m$), obtenemos:
1. $2s = r_1 + r_2 + r_3 + r_4 = e_1$
2. $s^2 + 2p = \sum_{1 \le i < j \le 4} r_i r_j = e_2$
3. $p^2 = r_1 r_2 r_3 r_4 = e_4 \implies p = \sqrt{r_1 r_2 r_3 r_4}$ (ya que $p > 0$)

Sustituyendo $s = \frac{e_1}{2}$ y $p = \sqrt{e_4}$ en la segunda ecuación:
$$\frac{e_1^2}{4} + 2\sqrt{e_4} = e_2 \implies e_1^2 - 4e_2 + 8\sqrt{e_4} = 0$$

Expresando $e_1^2 - 4e_2$ en términos de $r_i$:
$$\sum_{i=1}^4 r_i^2 - 2\sum_{1 \le i < j \le 4} r_i r_j + 8\sqrt{r_1 r_2 r_3 r_4} = 0$$

### Paso 3: Factorización y cálculo de $k$
Realizamos el cambio de variable $r_i = y_i^2$ con $y_i > 0$. La ecuación anterior se convierte en:
$$y_1^4 + y_2^4 + y_3^4 + y_4^4 - 2\sum_{1 \le i < j \le 4} y_i^2 y_j^2 + 8 y_1 y_2 y_3 y_4 = 0$$

Esta expresión se factoriza clásicamente como:
$$(y_1 + y_2 + y_3 + y_4)(y_1 + y_2 - y_3 - y_4)(y_1 - y_2 + y_3 - y_4)(y_1 - y_2 - y_3 + y_4) = 0$$

Dado que $y_i > 0$, el primer factor es estrictamente positivo, por lo que $y_4 = \sqrt{k}$ debe anular alguno de los otros tres factores:
1. $y_4 = y_1 + y_2 - y_3$
2. $y_4 = y_1 - y_2 + y_3$
3. $y_4 = -y_1 + y_2 + y_3$

Observamos que:
$$y_1 = \sqrt{18} = 3\sqrt{2}, \quad y_2 = \sqrt{72} = 6\sqrt{2}, \quad y_3 = \sqrt{98} = 7\sqrt{2}$$

Sustituyendo estos valores obtenemos las tres soluciones para $y_4 = \sqrt{k}$:
1. $\sqrt{k_1} = 3\sqrt{2} + 6\sqrt{2} - 7\sqrt{2} = 2\sqrt{2} \implies k_1 = (2\sqrt{2})^2 = 8$
2. $\sqrt{k_2} = 3\sqrt{2} - 6\sqrt{2} + 7\sqrt{2} = 4\sqrt{2} \implies k_2 = (4\sqrt{2})^2 = 32$
3. $\sqrt{k_3} = -3\sqrt{2} + 6\sqrt{2} + 7\sqrt{2} = 10\sqrt{2} \implies k_3 = (10\sqrt{2})^2 = 200$

(En los tres casos se verifica directamente que $s^2 > 4p$, garantizando que $a$ y $b$ son reales positivos distintos).

### Paso 4: Suma de los valores de $k$
Sumando los tres valores obtenidos:
$$k_1 + k_2 + k_3 = 8 + 32 + 200 = 240$$

\boxed{240}