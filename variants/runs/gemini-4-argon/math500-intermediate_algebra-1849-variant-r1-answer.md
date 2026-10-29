Para determinar cuántos enteros $k$ en el intervalo cerrado $[-250, 400]$ cumplen que la ecuación

$$\log(kx) = 2\log(x+3)$$

tiene exactamente una solución real, analizamos primero el dominio de definición de los logaritmos y luego la ecuación resultante.

### Paso 1: Condiciones de existencia (dominio)
Para que ambos logaritmos estén bien definidos en los números reales, sus argumentos deben ser estrictamente positivos:
1. $kx > 0$
2. $x + 3 > 0 \implies x > -3$

### Paso 2: Transformación a una ecuación algebraica
Aplicando las propiedades de los logaritmos en el lado derecho, tenemos:
$$\log(kx) = \log((x+3)^2)$$

Por la inyectividad de la función logarítmica, esto equivale a:
$$kx = (x+3)^2$$

Observamos que si $x > -3$, entonces $x + 3 > 0$, lo que implica automáticamente que $(x+3)^2 > 0$. Por lo tanto, cualquier solución de $kx = (x+3)^2$ que cumpla $x > -3$ satisfará también de forma automática la condición $kx > 0$.

Expandiendo la ecuación, obtenemos la ecuación cuadrática:
$$x^2 + 6x + 9 = kx \implies x^2 + (6 - k)x + 9 = 0$$

Buscamos los valores enteros de $k$ para los cuales esta ecuación cuadrática tiene **exactamente una solución real** en el intervalo $(-3, \infty)$.

### Paso 3: Análisis según los valores de $k$
Sea $P(x) = x^2 + (6 - k)x + 9$. El discriminante de esta ecuación cuadrática es:
$$\Delta = (6 - k)^2 - 4(1)(9) = (k - 6)^2 - 36 = k(k - 12)$$

Analizamos los casos para $k$:

1. **Caso 1: $\Delta = 0$ (una única raíz real doble)**
   Esto ocurre cuando $k = 0$ o $k = 12$:
   - Si $k = 0$, la ecuación es $(x+3)^2 = 0$, cuya única solución es $x = -3$. Sin embargo, $x = -3$ no pertenece al dominio $x > -3$, por lo que para $k = 0$ **no hay soluciones reales**.
   - Si $k = 12$, la ecuación es $(x-3)^2 = 0$, cuya única solución es $x = 3$. Como $3 > -3$, esta solución es válida. Por tanto, **$k = 12$** produce exactamente una solución real.

2. **Caso 2: $\Delta < 0$ (ninguna raíz real)**
   Para $0 < k < 12$, el discriminante es negativo, por lo que no existen soluciones reales.

3. **Caso 3: $\Delta > 0$ (dos raíces reales distintas $r_1 < r_2$)**
   Esto ocurre cuando $k > 12$ o $k < 0$.
   - **Subcaso $k > 12$:** La suma de las raíces es $r_1 + r_2 = k - 6 > 6 > 0$ y el producto es $r_1 r_2 = 9 > 0$. Por lo tanto, ambas raíces son positivas ($0 < r_1 < r_2$). Como ambas son mayores que $-3$, la ecuación tiene **dos** soluciones reales válidas.
   - **Subcaso $k < 0$:** Evaluamos el polinomio $P(x)$ en el extremo del dominio $x = -3$:
     $$P(-3) = (-3)^2 + (6 - k)(-3) + 9 = 9 - 18 + 3k + 9 = 3k$$
     Como $k < 0$, se tiene que $P(-3) = 3k < 0$. Dado que el coeficiente principal de $P(x)$ es positivo ($1 > 0$) y $P(-3) < 0$, el valor $x = -3$ se encuentra estrictamente entre las dos raíces:
     $$r_1 < -3 < r_2$$
     Esto significa que, para todo $k < 0$, la raíz $r_1$ queda fuera del dominio y la raíz $r_2$ cumple $r_2 > -3$, dando lugar a **exactamente una solución real** válida.

### Paso 4: Conteo de valores enteros de $k$ en $[-250, 400]$
Los valores enteros de $k$ en $[-250, 400]$ que cumplen la propiedad son:
- Todos los enteros negativos desde $-250$ hasta $-1$, lo que nos da $250$ valores.
- El valor positivo $k = 12$, que nos da $1$ valor adicional.

Sumando ambos casos, el total de enteros es $250 + 1 = 251$.

\boxed{251}