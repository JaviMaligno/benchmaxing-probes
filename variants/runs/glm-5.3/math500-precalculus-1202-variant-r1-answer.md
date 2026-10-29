# Solución

**Planteamiento.** Sea
$$A = \arccos x, \quad B = \arccos 2x, \quad C = \arccos 4x,$$
con $A, B, C \in [0, \pi]$ y $A + B + C = \pi$.

**1. Dominio y signo de $x$.** Necesitamos $x \in [-\tfrac14, \tfrac14]$. Si $x \le 0$, entonces $x \le 0$, $2x \le 0$, $4x \le 0$, así que cada arccoso es $\ge \tfrac{\pi}{2}$ y la suma sería $\ge \tfrac{3\pi}{2} > \pi$. Por lo tanto $x > 0$.

**2. Despejar usando $C = \pi - (A+B)$.** Como $\cos A = x$, $\cos B = 2x$, y $\sin A = \sqrt{1-x^2} \ge 0$, $\sin B = \sqrt{1-4x^2} \ge 0$:
$$\cos(A+B) = \cos A \cos B - \sin A \sin B = 2x^2 - \sin A \sin B.$$
Entonces
$$4x = \cos C = -\cos(A+B) = -2x^2 + \sin A \sin B,$$
de donde
$$\sqrt{1-x^2}\,\sqrt{1-4x^2} = 4x + 2x^2 > 0.$$

**3. Elevar al cuadrado.** Con $x > 0$ ambos lados son positivos, así que al cuadrar no aparece nada espurio:
$$(1-x^2)(1-4x^2) = (4x+2x^2)^2$$
$$1 - 5x^2 + 4x^4 = 16x^2 + 16x^3 + 4x^4$$
$$16x^3 + 21x^2 - 1 = 0.$$

**4. Existencia y unicidad de la solución.** Sea $g(x) = 16x^3 + 21x^2 - 1$. Tenemos $g(0) = -1 < 0$ y $g(\tfrac14) = \tfrac{9}{16} > 0$; además $g'(x) = 6x(8x+7) > 0$ en $(0,\tfrac14]$, así que $g$ tiene **exactamente una** raíz $x \in (0, \tfrac14)$, que es la solución única de la ecuación original (numéricamente $x \approx 0.2031$, y en efecto $\arccos x + \arccos 2x + \arccos 4x \approx 3.1416$).

**5. Polinomio mínimo y suma mínima.** $g$ es irreducible sobre $\mathbb{Q}$: no tiene raíces racionales (se comprueban los candidatos $\pm 1, \pm\tfrac12, \pm\tfrac14, \pm\tfrac18, \pm\tfrac1{16}$ y ninguno anula $g$). Por lo tanto $x$ tiene grado $3$ y su polinomio mínimo es $g$ (que es primitivo).

Si $p(x) = ax^3 + bx^2 + cx + d \in \mathbb{Z}[X]$ es cualquier cúbica con raíz $x$, el polinomio mínimo divide a $p$; como ambos tienen grado $3$, se tiene $p = k\,g$ con $k \in \mathbb{Z} \setminus \{0\}$ (por el lema de Gauss, ya que $g$ es primitivo). Entonces
$$|a| + |b| + |c| + |d| = |k|\left(16 + 21 + 0 + 1\right) = 38|k| \ge 38,$$
con igualdad para $g(x) = 16x^3 + 21x^2 - 1$.

$$\boxed{38}$$