Para encontrar el valor mínimo de la expresión dada para $0 \le x \le 40$ y $0 \le y \le 50$:

\[ S = \sqrt{x^2 + 400} + \sqrt{y^2 + 900} + \sqrt{x^2 + y^2 - 80x - 100y + 4100} \]

**Paso 1: Reescribir los términos algebraicamente**
Completamos cuadrados en el tercer radical y expresamos las constantes como cuadrados perfectos:
* $x^2 + 400 = x^2 + 20^2$
* $y^2 + 900 = 30^2 + y^2$
* $x^2 + y^2 - 80x - 100y + 4100 = (x^2 - 80x + 1600) + (y^2 - 100y + 2500) = (40 - x)^2 + (50 - y)^2$

Por lo tanto, la expresión equivale a:
\[ S = \sqrt{x^2 + 20^2} + \sqrt{30^2 + y^2} + \sqrt{(40 - x)^2 + (50 - y)^2} \]

**Paso 2: Interpretación vectorial y desigualdad triangular (o de Minkowski)**
Definimos los siguientes tres vectores en $\mathbb{R}^2$:
* $\vec{v}_1 = (x, 20)$
* $\vec{v}_2 = (30, y)$
* $\vec{v}_3 = (40 - x, 50 - y)$

Observamos que la suma de las normas euclidianas de estos tres vectores es exactamente nuestra expresión $S$:
\[ S = \|\vec{v}_1\| + \|\vec{v}_2\| + \|\vec{v}_3\| \]

Por la desigualdad triangular generalizada:
\[ \|\vec{v}_1\| + \|\vec{v}_2\| + \|\vec{v}_3\| \ge \|\vec{v}_1 + \vec{v}_2 + \vec{v}_3\| \]

Calculamos la suma de los vectores:
\[ \vec{v}_1 + \vec{v}_2 + \vec{v}_3 = (x + 30 + 40 - x, 20 + y + 50 - y) = (70, 70) \]

Calculamos la norma del vector resultante:
\[ \|(70, 70)\| = \sqrt{70^2 + 70^2} = \sqrt{9800} = 70\sqrt{2} \]

**Paso 3: Verificar la condición de igualdad**
La igualdad se alcanza si y solo si los tres vectores tienen la misma dirección y sentido (es decir, son múltiplos escalares positivos de $(1, 1)$):
* Para $\vec{v}_1 = (x, 20) \implies x = 20$
* Para $\vec{v}_2 = (30, y) \implies y = 30$
* Para $\vec{v}_3 = (40 - x, 50 - y) = (40 - 20, 50 - 30) = (20, 20)$, que también es paralelo a $(1, 1)$.

Dado que $x = 20 \in [0, 40]$ y $y = 30 \in [0, 50]$, el mínimo es alcanzable dentro del dominio permitido.

\boxed{70\sqrt{2}}