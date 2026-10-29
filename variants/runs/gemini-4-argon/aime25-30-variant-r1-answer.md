Para encontrar los valores reales positivos de $k$ tales que la función
$$g(x) = \frac{(x - 8)(x - 50)(x - 72)(x - k)}{x}$$
alcance su valor mínimo en el intervalo $(0, \infty)$ en exactamente dos números reales positivos, analicemos primero el comportamiento de $g(x)$ para $x > 0$ y $k > 0$:

1. **Existencia y caracterización del mínimo global:**
   Cuando $x \to 0^+$, el numerador tiende a $(-8)(-50)(-72)(-k) = 28800k > 0$, por lo que $g(x) \to +\infty$. Asimismo, cuando $x \to +\infty$, $g(x) \sim x^3 \to +\infty$. Como $g(x)$ es continua y diferenciable en $(0, \infty)$, debe alcanzar un mínimo global $m$.

   Si $g(x)$ alcanza su mínimo global $m$ en exactamente dos números reales positivos distintos $r$ y $s$, entonces $g(x) - m \ge 0$ para todo $x > 0$, y $r, s$ deben ser raíces dobles (pues $g(r) = g(s) = m$ y $g'(r) = g'(s) = 0$) del polinomio mónico de cuarto grado en el numerador de $g(x) - m$:
   $$(x - 8)(x - 50)(x - 72)(x - k) - mx = (x - r)^2(x - s)^2.$$
   Recíprocamente, si existe esta identidad polinómica con $r, s > 0$ y $r \neq s$, entonces para $x > 0$:
   $$g(x) - m = \frac{(x - r)^2(x - s)^2}{x} \ge 0,$$
   alcanzando el valor mínimo $m$ única y exclusivamente en $x = r$ y $x = s$.

2. **Factorización mediante cambio de variable:**
   Sea $u = r + s$ y $v = rs$, de modo que $(x - r)(x - s) = x^2 - ux + v$. La condición anterior equivale a:
   $$(x - 8)(x - 50)(x - 72)(x - k) = (x^2 - ux + v)^2 + mx.$$
   Evaluando en $x = 8$, el lado izquierdo se anula, por lo que $(8^2 - 8u + v)^2 = -8m \ge 0$, lo cual implica que $m \le 0$. Como las raíces $8, 50, 72$ son distintas, $m \neq 0$, así que podemos escribir $-m = t^2$ con $t > 0$.

   Haciendo el cambio de variable $x = y^2$ (con $y > 0$) y definiendo $y_1 = \sqrt{8} = 2\sqrt{2}$, $y_2 = \sqrt{50} = 5\sqrt{2}$, $y_3 = \sqrt{72} = 6\sqrt{2}$ y $y_4 = \sqrt{k} > 0$, obtenemos:
   $$\prod_{i=1}^4 (y^2 - y_i^2) = (y^4 - uy^2 + v)^2 - t^2y^2 = (y^4 - uy^2 - ty + v)(y^4 - uy^2 + ty + v).$$
   Las ocho raíces del lado izquierdo son $\pm y_1, \pm y_2, \pm y_3, \pm y_4$. Dado que el segundo factor se obtiene del primero al sustituir $y$ por $-y$, las cuatro raíces del polinomio
   $$Q(y) = y^4 - uy^2 - ty + v$$
   deben ser de la forma $\alpha_i = \epsilon_i y_i$ para $i \in \{1, 2, 3, 4\}$, donde cada $\epsilon_i \in \{1, -1\}$.

3. **Condiciones sobre las raíces $\alpha_i$:**
   - En $Q(y)$, el coeficiente de $y^3$ es $0$. Por las relaciones de Vieta, la suma de sus cuatro raíces es cero:
     $$\epsilon_1 y_1 + \epsilon_2 y_2 + \epsilon_3 y_3 + \epsilon_4 y_4 = 0.$$
     Sin pérdida de generalidad (cambiando el signo de $t$ si fuera necesario), podemos fijar $\epsilon_4 = -1$, con lo cual:
     $$\sqrt{k} = y_4 = \epsilon_1 y_1 + \epsilon_2 y_2 + \epsilon_3 y_3 = (2\epsilon_1 + 5\epsilon_2 + 6\epsilon_3)\sqrt{2}.$$
   - Para que $x^2 - ux + v = 0$ tenga dos raíces reales positivas distintas $r, s > 0$, se requiere que $u = r + s > 0$, $v = rs > 0$ y $\Delta = u^2 - 4v > 0$.
     Por las fórmulas de Vieta en $Q(y)$:
     $$u = -\sum_{i < j} \alpha_i \alpha_j = \frac{1}{2}\sum_{i=1}^4 \alpha_i^2 > 0, \qquad v = \alpha_1 \alpha_2 \alpha_3 \alpha_4.$$
     Como $\alpha_4 = -y_4 < 0$, el signo de $v$ es el signo de $-\epsilon_1 \epsilon_2 \epsilon_3$. Por tanto, $v > 0$ si y solo si exactamente uno de los signos $\epsilon_1, \epsilon_2, \epsilon_3$ es negativo (o los tres lo son, lo cual haría $y_4 < 0$, imposible).

4. **Cálculo de los valores de $k$:**
   Analizamos las cuatro combinaciones de signos $(\epsilon_1, \epsilon_2, \epsilon_3)$ que producen $y_4 > 0$:
   - Si $(\epsilon_1, \epsilon_2, \epsilon_3) = (+1, +1, +1)$, entonces $v < 0$, por lo que una de las raíces $r, s$ es negativa y $g(x)$ solo alcanza su mínimo en un número real positivo.
   - Si $(\epsilon_1, \epsilon_2, \epsilon_3) = (-1, +1, +1)$:
     $$y_4 = (-2 + 5 + 6)\sqrt{2} = 9\sqrt{2} \implies k = (9\sqrt{2})^2 = 162.$$
     Aquí $u = 4 + 25 + 36 + 81 = 146$ y $v = 4(-2)(5)(6)(-9) = 2160 > 0$, con $u^2 - 4v = 12676 > 0$.
   - Si $(\epsilon_1, \epsilon_2, \epsilon_3) = (+1, -1, +1)$:
     $$y_4 = (2 - 5 + 6)\sqrt{2} = 3\sqrt{2} \implies k = (3\sqrt{2})^2 = 18.$$
     Aquí $u = 4 + 25 + 36 + 9 = 74$ y $v = 4(2)(-5)(6)(-3) = 720 > 0$, con $u^2 - 4v = 2596 > 0$.
   - Si $(\epsilon_1, \epsilon_2, \epsilon_3) = (+1, +1, -1)$:
     $$y_4 = (2 + 5 - 6)\sqrt{2} = 1\sqrt{2} \implies k = (1\sqrt{2})^2 = 2.$$
     Aquí $u = 4 + 25 + 36 + 1 = 66$ y $v = 4(2)(5)(-6)(-1) = 240 > 0$, con $u^2 - 4v = 3396 > 0$.

Los tres valores reales positivos de $k$ son $162$, $18$ y $2$. Su suma es:
$$162 + 18 + 2 = 182.$$

\boxed{182}