Para encontrar el área de la región finita, primero factorizamos las desigualdades dadas.

La primera desigualdad es:
$$x - yz < y - zx$$
Pasando todos los términos al lado izquierdo y agrupando:
$$x - y + zx - yz < 0$$
$$(x - y) + z(x - y) < 0$$
$$(x - y)(z + 1) < 0$$

La segunda desigualdad es:
$$y - zx < z - xy$$
De manera análoga, agrupamos los términos en el lado izquierdo:
$$y - z + xy - zx < 0$$
$$(y - z) + x(y - z) < 0$$
$$(y - z)(x + 1) < 0$$

Por lo tanto, el sistema de desigualdades equivale a:
1. $(x - y)(z + 1) < 0$
2. $(y - z)(x + 1) < 0$

Analizamos las combinaciones de signos de los factores sobre el plano $x + y + z = 75$:

- **Caso 1:** $z + 1 > 0$ y $x + 1 > 0$. 
  Esto implica que $z > -1$ y $x > -1$. Para que los productos sean negativos, debemos tener $x - y < 0$ y $y - z < 0$, lo que significa $x < y < z$. Combinando todo, obtenemos:
  $$-1 < x < y < z$$
  Dado que $x + y + z = 75$ y las tres variables están acotadas inferiormente por $-1$, también están acotadas superiormente. Por lo tanto, esta región es **finita** (acotada).

- **Caso 2:** $z + 1 > 0$ y $x + 1 < 0 \implies z > -1, x < -1, x < y, y > z$. Esta región no está acotada porque $x$ puede tender a $-\infty$ mientras $y$ o $z$ tienden a $+\infty$.
- **Caso 3:** $z + 1 < 0$ y $x + 1 > 0 \implies z < -1, x > -1, x > y, y < z$. Esta región tampoco está acotada porque $y$ y $z$ pueden tender a $-\infty$ mientras $x$ tiende a $+\infty$.
- **Caso 4:** $z + 1 < 0$ y $x + 1 < 0 \implies z < -1, x < -1, x > y > z$. Esto implica $x, y, z < -1$, por lo que $x + y + z < -3$, lo cual contradice que $x + y + z = 75$ (región vacía).

La única región de área finita corresponde al **Caso 1**, cuya clausura en el plano $x + y + z = 75$ está determinada por las condiciones:
$$x \ge -1, \quad x \le y, \quad y \le z$$

Hallamos los vértices del triángulo formado por la intersección de las fronteras de estas desigualdades en el plano $x + y + z = 75$:

1. Para $x = -1$ y $x = y$: tenemos $x = -1, y = -1$, y $z = 75 - (-1) - (-1) = 77$.
   $$A = (-1, -1, 77)$$
2. Para $x = -1$ y $y = z$: tenemos $-1 + 2y = 75 \implies y = 38, z = 38$.
   $$B = (-1, 38, 38)$$
3. Para $x = y$ y $y = z$: tenemos $3x = 75 \implies x = y = z = 25$.
   $$C = (25, 25, 25)$$

Calculamos los vectores de dos de los lados a partir del vértice $B$:
$$\vec{BA} = A - B = (0, -39, 39) = 39(0, -1, 1)$$
$$\vec{BC} = C - B = (26, -13, -13) = 13(2, -1, -1)$$

Observamos el producto escalar entre $\vec{BA}$ y $\vec{BC}$:
$$\vec{BA} \cdot \vec{BC} = 39 \cdot 13 \cdot (0 \cdot 2 + (-1)(-1) + 1(-1)) = 0$$
Como los vectores son perpendiculares, el triángulo $ABC$ es rectángulo en $B$. Las longitudes de sus catetos son:
$$|BA| = 39\sqrt{0^2 + (-1)^2 + 1^2} = 39\sqrt{2}$$
$$|BC| = 13\sqrt{2^2 + (-1)^2 + (-1)^2} = 13\sqrt{6}$$

El área del triángulo es:
$$\text{Área} = \frac{1}{2} |BA| |BC| = \frac{1}{2} (39\sqrt{2})(13\sqrt{6}) = \frac{507}{2}\sqrt{12} = 507\sqrt{3}$$

Expresando el área en la forma $a\sqrt{b}$, tenemos $a = 507$ y $b = 3$. Por lo tanto, $a + b = 507 + 3 = 510$.

\boxed{510}