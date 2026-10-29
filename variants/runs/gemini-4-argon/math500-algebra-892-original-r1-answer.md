Para que la gráfica de $y = f(x)$ interseque cada línea horizontal al menos una vez, el rango (o imagen) de la función $f(x)$ debe ser el conjunto de todos los números reales, $(-\infty, \infty)$.

Analicemos el comportamiento de la función por casos según el signo de $a$:

**Caso 1: $a = 0$**
Si $a = 0$, entonces $f(x) = 0$ para todo $x \in \mathbb{R}$. El rango es únicamente $\{0\}$, por lo que no cumple la condición.

**Caso 2: $a > 0$**
* Para $x < a$, la función es lineal y estrictamente creciente: $f(x) = ax + 2a$. A medida que $x$ varía en $(-\infty, a)$, los valores de $f(x)$ cubren el intervalo:
  $$(-\infty, a(a) + 2a) = (-\infty, a^2 + 2a)$$
* Para $x \geq a$, dado que $a > 0$, la función cuadrática $f(x) = ax^2$ es estrictamente creciente en $[a, \infty)$. Por lo tanto, los valores de $f(x)$ en este tramo cubren el intervalo:
  $$[a(a)^2, \infty) = [a^3, \infty)$$

Para que la unión de ambos intervalos, $(-\infty, a^2 + 2a) \cup [a^3, \infty)$, cubra toda la recta real $(-\infty, \infty)$ sin dejar huecos, el extremo inferior del segundo intervalo debe ser menor o igual que el extremo superior del primero:
$$a^3 \leq a^2 + 2a$$

Como $a > 0$, podemos dividir ambos lados de la desigualdad entre $a$:
$$a^2 \leq a + 2$$
$$a^2 - a - 2 \leq 0$$
$$(a - 2)(a + 1) \leq 0$$

Dado que estamos en el caso $a > 0$, esta desigualdad se satisface para $0 < a \leq 2$.

*(Nota: Si $a < 0$, cualquier valor válido sería negativo, el cual es menor que los valores positivos encontrados).*

Por lo tanto, el mayor valor posible de $a$ es $2$.

\boxed{2}