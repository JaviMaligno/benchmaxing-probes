Para encontrar el número de valores enteros de $k$ en el intervalo cerrado $[-500, 500]$ para los cuales la ecuación $\log(kx) = 2\log(x+2)$ tiene exactamente una solución real, analizamos primero el dominio y las condiciones de equivalencia de la ecuación.

### Paso 1: Condiciones de existencia (dominio)
Para que los logaritmos estén bien definidos en los números reales, sus argumentos deben ser estrictamente positivos:
1. $kx > 0$
2. $x + 2 > 0 \implies x > -2$

### Paso 2: Transformación algebraica
Usando las propiedades de los logaritmos en el lado derecho, tenemos:
$$\log(kx) = \log((x+2)^2)$$

Igualando los argumentos de los logaritmos obtenemos:
$$kx = (x+2)^2$$

Observamos que si $x > -2$, entonces $x + 2 > 0$, por lo que $(x+2)^2 > 0$. En consecuencia, cualquier solución real que cumpla $kx = (x+2)^2$ y $x > -2$ satisfará automáticamente $kx > 0$. Por lo tanto, el problema se reduce a encontrar para qué valores de $k$ la ecuación cuadrática:
$$x^2 + 4x + 4 = kx \iff x^2 + (4-k)x + 4 = 0$$
tiene **exactamente una** raíz real en el intervalo $(-2, \infty)$.

### Paso 3: Análisis de las raíces en $(-2, \infty)$
Sea $f(x) = x^2 + (4-k)x + 4$. Existen dos casos en los que $f(x) = 0$ tiene exactamente una solución en $(-2, \infty)$:

#### Caso 1: La ecuación cuadrática tiene una única raíz real (raíz doble) y esta es mayor que $-2$
Para que exista una raíz doble, el discriminante $\Delta$ debe ser cero:
$$\Delta = (4-k)^2 - 4(1)(4) = (4-k)^2 - 16 = 0$$
Esto implica que $4 - k = \pm 4$, lo que nos da dos posibles valores para $k$:
- Si $k = 0$: la ecuación es $(x+2)^2 = 0$, cuya única solución es $x = -2$. Sin embargo, $x = -2$ no pertenece al dominio $x > -2$.
- Si $k = 8$: la ecuación es $x^2 - 4x + 4 = 0 \implies (x-2)^2 = 0$, cuya única solución es $x = 2$. Como $2 > -2$, $x = 2$ es una solución válida. Por lo tanto, **$k = 8$ cumple la condición**.

#### Caso 2: La ecuación cuadrática tiene dos raíces reales distintas, pero solo una de ellas es mayor que $-2$
Observemos que $x = -2$ solo es raíz cuando $k = 0$ (analizado arriba). Para $k \neq 0$, dado que $f(x)$ es una parábola que abre hacia arriba, tendrá exactamente una raíz en $(-\infty, -2)$ y exactamente una raíz en $(-2, \infty)$ si y solo si $f(-2) < 0$:
$$f(-2) = (-2)^2 + (4-k)(-2) + 4 = 4 - 8 + 2k + 4 = 2k$$
Por lo tanto:
$$f(-2) < 0 \iff 2k < 0 \iff k < 0$$
Así, para **todo $k < 0$**, existe exactamente una solución real en el intervalo $(-2, \infty)$.

*(Nota: Si $k > 8$, $\Delta > 0$, la suma de las raíces es $k - 4 > 0$ y su producto es $4 > 0$, por lo que ambas raíces son positivas y mayores que $-2$, dando dos soluciones. Si $0 < k < 8$, $\Delta < 0$ y no hay soluciones reales).*

### Paso 4: Conteo de valores enteros de $k$ en $[-500, 500]$
Reuniendo ambos casos, los valores enteros permitidos en $[-500, 500]$ son:
- Todos los enteros negativos desde $-500$ hasta $-1$: hay $500$ valores.
- El valor positivo $k = 8$: hay $1$ valor.

En total, el número de valores enteros de $k$ es $500 + 1 = 501$.

\boxed{501}