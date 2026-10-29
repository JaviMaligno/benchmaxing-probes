Para que la gráfica de $y = f(x)$ interseque cada línea horizontal al menos una vez, el rango (o imagen) de la función $f(x)$ debe ser todo el conjunto de los números reales, $(-\infty, \infty)$.

Analicemos el comportamiento de $f(x)$ según el signo de $a$:

1. **Si $a = 0$:**
   La función es $f(x) = 0$ para todo $x$, cuyo rango es únicamente $\{0\}$, por lo que no cubre todas las líneas horizontales.

2. **Si $a > 0$:**
   - Para $x < a$, la función es $f(x) = ax + 2a$. Como $a > 0$, es una función lineal estrictamente creciente cuyo rango en el intervalo $(-\infty, a)$ es:
     \[ (-\infty, a^2 + 2a) \]
   - Para $x \geq a$, la función es $f(x) = ax^2$. Como $x \geq a > 0$, esta parábola es estrictamente creciente en $[a, \infty)$, alcanzando su valor mínimo en $x = a$, donde $f(a) = a(a^2) = a^3$. Por lo tanto, su rango en $[a, \infty)$ es:
     \[ [a^3, \infty) \]

   Para que la unión de ambos intervalos $(-\infty, a^2 + 2a) \cup [a^3, \infty)$ cubra toda la recta real $(-\infty, \infty)$ sin dejar huecos, es necesario que:
   \[ a^3 \leq a^2 + 2a \]
   Dado que $a > 0$, podemos dividir ambos lados de la desigualdad entre $a$:
   \[ a^2 \leq a + 2 \]
   \[ a^2 - a - 2 \leq 0 \]
   \[ (a - 2)(a + 1) \leq 0 \]
   Como estamos en el caso $a > 0$, esto se cumple para $0 < a \leq 2$.

3. **Si $a < 0$:**
   Cualquier solución en este caso sería menor que las soluciones positivas encontradas en el caso anterior.

Por lo tanto, el mayor valor posible de $a$ es $2$.

\boxed{2}