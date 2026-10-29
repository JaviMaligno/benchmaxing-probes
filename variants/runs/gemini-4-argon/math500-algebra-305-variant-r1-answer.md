Para encontrar los valores de $p$, $q$ y $r$, analizamos las asíntotas verticales y horizontales de la función racional $g(x) = \frac{3x}{x^2-3x-40}$.

**Paso 1: Encontrar las asíntotas verticales ($x = p$ y $x = q$)**
Las asíntotas verticales ocurren en los valores de $x$ donde el denominador es igual a cero y el numerador es distinto de cero. Igualamos el denominador a cero:
$$x^2 - 3x - 40 = 0$$

Factorizamos la expresión cuadrática:
$$(x - 8)(x + 5) = 0$$

Las soluciones son $x = 8$ y $x = -5$. Como el numerador $3x$ no se anula en ninguno de estos puntos ($3(8) = 24 \neq 0$ y $3(-5) = -15 \neq 0$), las asíntotas verticales son $x = 8$ y $x = -5$. Por lo tanto, $p$ y $q$ son $8$ y $-5$ (en cualquier orden), y su suma es:
$$p + q = 8 + (-5) = 3$$

*(Nota: También se puede obtener directamente por las fórmulas de Vieta, donde la suma de las raíces de $x^2 - 3x - 40 = 0$ es $-(-3)/1 = 3$).*

**Paso 2: Encontrar la asíntota horizontal ($y = r$)**
Observamos los grados del numerador y del denominador:
- El grado del numerador ($3x$) es $1$.
- El grado del denominador ($x^2 - 3x - 40$) es $2$.

Dado que el grado del numerador es estrictamente menor que el grado del denominador, cuando $x \to \pm\infty$, la función tiende a $0$:
$$\lim_{x \to \pm\infty} \frac{3x}{x^2-3x-40} = 0$$

Por lo tanto, la asíntota horizontal es $y = 0$, lo que significa que $r = 0$.

**Paso 3: Calcular $p + q + r$**
Sumamos los valores obtenidos:
$$p + q + r = 3 + 0 = 3$$

\boxed{3}