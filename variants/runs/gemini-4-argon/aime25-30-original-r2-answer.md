Para hallar los valores de $k > 0$ tales que la función
$$f(x) = \frac{(x - 18)(x - 72)(x - 98)(x - k)}{x}$$
alcance su valor mínimo en exactamente dos números reales positivos $x$, analizamos la condición de mínimo global en $(0, \infty)$.

### Paso 1: Condición algebraica para el doble mínimo
Dado que $k > 0$, cuando $x \to 0^+$ y cuando $x \to +\infty$, tenemos $f(x) \to +\infty$. Sea $m$ el valor mínimo de $f(x)$ en $(0, \infty)$, alcanzado en dos puntos distintos $a, b > 0$. Entonces $f(x) - m \ge 0$ para todo $x > 0$, y se anula únicamente en $x = a$ y $x = b$.

Multiplicando por $x > 0$, el polinomio mónico de cuarto grado
$$P(x) = (x - 18)(x - 72)(x - 98)(x - k) - mx$$
debe ser no negativo para todo $x > 0$ y tener raíces en $x = a$ y $x = b$. Para que $P(x)$ no cambie de signo en $a$ ni en $b$, ambas deben ser raíces de multiplicidad par (al menos 2). Como $\deg P = 4$, se sigue que:
$$(x - 18)(x - 72)(x - 98)(x - k) - mx = (x - a)^2(x - b)^2.$$

Sean $s = a + b$ y $p = ab$. Para que $a$ y $b$ sean reales positivos y distintos, necesitamos $s > 0$, $p > 0$ y $s^2 - 4p > 0$. Reescribiendo la identidad anterior:
$$(x - 18)(x - 72)(x - 98)(x - k) = (x^2 - sx + p)^2 + mx.$$

### Paso 2: Cambio de variable y factorización
Evaluando en $x = 18$, $72$, $98$ y $k$, el lado izquierdo se anula, por lo que $mx = -(x^2 - sx + p)^2 \le 0$. Como las raíces son positivas, se deduce que $m \le 0$. Sea $-m = c^2$ con $c \ge 0$. Haciendo el cambio de variable $x = u^2$ ($u > 0$), la identidad implica que para $r_1 = 18$, $r_2 = 72$, $r_3 = 98$ y $r_4 = k$:
$$(u^2 - r_1)(u^2 - r_2)(u^2 - r_3)(u^2 - r_4) = (u^4 - su^2 + p)^2 - c^2 u^2 = (u^4 - su^2 - cu + p)(u^4 - su^2 + cu + p).$$

Observamos que los dos factores de cuarto grado a la derecha son $Q(u)$ y $Q(-u)$, donde
$$Q(u) = u^4 - su^2 - cu + p.$$
Por lo tanto, eligiendo signos adecuados $\epsilon_i \in \{+1, -1\}$ para cada $i \in \{1, 2, 3, 4\}$, las cuatro raíces de $Q(u)$ son exactamente $u_i = \epsilon_i \sqrt{r_i}$.

### Paso 3: Aplicación de las fórmulas de Vieta
Aplicando las relaciones de Vieta al polinomio $Q(u) = u^4 - su^2 - cu + p$:
1. El coeficiente de $u^3$ es $0$, por lo que la suma de las raíces es cero:
   $$\epsilon_1 \sqrt{18} + \epsilon_2 \sqrt{72} + \epsilon_3 \sqrt{98} + \epsilon_4 \sqrt{k} = 0.$$
2. El término independiente es $p = u_1 u_2 u_3 u_4$:
   $$p = \epsilon_1 \epsilon_2 \epsilon_3 \epsilon_4 \sqrt{18 \cdot 72 \cdot 98 \cdot k}.$$

Como requerimos $p = ab > 0$, necesariamente debe cumplirse que $\epsilon_1 \epsilon_2 \epsilon_3 \epsilon_4 = +1$. Dado que las cuatro raíces no pueden tener todas el mismo signo (pues su suma es $0$), exactamente dos de los signos $\epsilon_i$ son $+1$ y los otros dos son $-1$. Sin pérdida de generalidad, podemos fijar $\epsilon_4 = +1$, lo que implica que uno de $\{\epsilon_1, \epsilon_2, \epsilon_3\}$ es $+1$ y los otros dos son $-1$.

### Paso 4: Cálculo de los tres valores de $k$
Simplificando las raíces conocidas:
$$\sqrt{18} = 3\sqrt{2}, \quad \sqrt{72} = 6\sqrt{2}, \quad \sqrt{98} = 7\sqrt{2}.$$

Analizamos los tres casos posibles según cuál de los tres primeros términos tenga el mismo signo que $\sqrt{k}$:

1. **Caso 1 ($\epsilon_1 = +1, \epsilon_2 = -1, \epsilon_3 = -1$):**
   $$\sqrt{k} = 6\sqrt{2} + 7\sqrt{2} - 3\sqrt{2} = 10\sqrt{2} \implies k_1 = (10\sqrt{2})^2 = 200.$$

2. **Caso 2 ($\epsilon_1 = -1, \epsilon_2 = +1, \epsilon_3 = -1$):**
   $$\sqrt{k} = 3\sqrt{2} + 7\sqrt{2} - 6\sqrt{2} = 4\sqrt{2} \implies k_2 = (4\sqrt{2})^2 = 32.$$

3. **Caso 3 ($\epsilon_1 = -1, \epsilon_2 = -1, \epsilon_3 = +1$):**
   $$\sqrt{k} = 3\sqrt{2} + 6\sqrt{2} - 7\sqrt{2} = 2\sqrt{2} \implies k_3 = (2\sqrt{2})^2 = 8.$$

*(En los tres casos se verifica directamente que $s = \frac{1}{2}(r_1 + r_2 + r_3 + k) > 0$ y $s^2 - 4p > 0$, garantizando dos mínimos positivos distintos).*

Finalmente, la suma de los tres valores de $k$ es:
$$200 + 32 + 8 = 240.$$

\boxed{240}