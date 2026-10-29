Para encontrar cuántos números enteros $k$ en el intervalo cerrado $[-250, 400]$ hacen que la ecuación
$$\log(kx) = 2\log(x+3)$$
tenga exactamente una solución real, analizamos primero el dominio de definición de los logaritmos y luego la ecuación algebraica equivalente.

### Paso 1: Condiciones de existencia (dominio)
Para que los logaritmos estén bien definidos en los números reales, sus argumentos deben ser estrictamente positivos:
1. $kx > 0$
2. $x + 3 > 0 \iff x > -3$

Usando las propiedades de los logaritmos, la ecuación se puede reescribir como:
$$\log(kx) = \log((x+3)^2)$$
Dado que la función logarítmica es inyectiva, esto equivale a:
$$kx = (x+3)^2$$

Observemos que si $x > -3$, entonces $x + 3 > 0$, lo que implica que $(x+3)^2 > 0$. Por lo tanto, cualquier solución $x > -3$ de la ecuación $kx = (x+3)^2$ cumple automáticamente que $kx = (x+3)^2 > 0$. Así, el problema se reduce a encontrar para qué valores de $k$ la ecuación cuadrática
$$kx = (x+3)^2 \iff x^2 + (6 - k)x + 9 = 0$$
tiene **exactamente una** raíz real en el intervalo $(-3, \infty)$.

---

### Paso 2: Análisis de las raíces de la ecuación cuadrática
Sea $g(x) = x^2 + (6 - k)x + 9$. El discriminante de esta ecuación cuadrática es:
$$\Delta = (6 - k)^2 - 4(1)(9) = (k - 6)^2 - 36 = k(k - 12)$$

Analizamos los casos según el valor del discriminante y la posición de las raíces respecto a $x = -3$:

#### Caso 1: $\Delta = 0$ (una única raíz real doble)
Esto ocurre cuando $k = 0$ o $k = 12$:
- **Si $k = 0$:** La ecuación es $(x+3)^2 = 0$, cuya única solución es $x = -3$. Como requerimos $x > -3$, no hay ninguna solución válida.
- **Si $k = 12$:** La ecuación es $x^2 - 6x + 9 = (x-3)^2 = 0$, cuya única solución es $x = 3$. Como $3 > -3$, esta solución es válida. Por lo tanto, **$k = 12$** cumple la condición.

#### Caso 2: $\Delta > 0$ (dos raíces reales distintas $x_1 < x_2$)
Esto ocurre cuando $k < 0$ o $k > 12$. Evaluamos la parábola $g(x)$ en el extremo del dominio $x = -3$:
$$g(-3) = (-3)^2 + (6 - k)(-3) + 9 = 9 - 18 + 3k + 9 = 3k$$

- **Si $k > 12$:** Tenemos $\Delta > 0$. Además, por las fórmulas de Vieta, la suma de las raíces es $x_1 + x_2 = k - 6 > 6 > 0$ y el producto es $x_1 x_2 = 9 > 0$. Esto significa que ambas raíces son positivas ($0 < x_1 < x_2$) y, por tanto, ambas pertenecen a $(-3, \infty)$. En este caso hay **dos** soluciones reales, por lo que no se cumple la condición.
- **Si $k < 0$:** Como el coeficiente principal de $g(x)$ es positivo ($1 > 0$) y $g(-3) = 3k < 0$, el número $-3$ se encuentra estrictamente entre las dos raíces de la parábola ($x_1 < -3 < x_2$). En consecuencia, $x_1$ queda fuera del dominio y $x_2 > -3$ está dentro del dominio. Esto garantiza que para todo **$k < 0$** existe **exactamente una** solución real válida.

---

### Paso 3: Conteo de valores enteros de $k$ en $[-250, 400]$
Los valores de $k$ que cumplen la propiedad son todos los $k < 0$ y $k = 12$:
- Para $k < 0$ dentro del intervalo $[-250, 400]$, tenemos los enteros desde $-250$ hasta $-1$, lo que nos da $250$ valores.
- Para $k > 0$ dentro del intervalo $[-250, 400]$, tenemos únicamente el valor $k = 12$, lo que añade $1$ valor.

Sumando ambos casos, el total de números enteros $k$ es $250 + 1 = 251$.

\boxed{251}