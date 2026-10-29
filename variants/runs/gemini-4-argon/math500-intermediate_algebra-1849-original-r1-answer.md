Para determinar el número de valores enteros de $k$ en el intervalo cerrado $[-500, 500]$ para los cuales la ecuación
$$\log(kx) = 2\log(x+2)$$
tiene exactamente una solución real, analizamos primero el dominio de la ecuación y luego sus soluciones algebraicas.

### Paso 1: Condiciones de existencia (Dominio)
Para que los logaritmos estén bien definidos en los números reales, sus argumentos deben ser estrictamente positivos:
1. $kx > 0$
2. $x + 2 > 0 \implies x > -2$

Usando las propiedades de los logaritmos, podemos reescribir la ecuación como:
$$\log(kx) = \log((x+2)^2)$$

Dado que la función logarítmica es inyectiva, esto equivale a:
$$kx = (x+2)^2$$

Observemos que si $x > -2$, entonces $x + 2 > 0$, por lo que $(x+2)^2 > 0$. En consecuencia, cualquier valor de $x > -2$ que satisfaga $kx = (x+2)^2$ cumplirá automáticamente la condición $kx > 0$. Por lo tanto, el problema se reduce a encontrar para qué valores de $k$ la ecuación cuadrática
$$kx = x^2 + 4x + 4 \iff x^2 + (4 - k)x + 4 = 0$$
tiene **exactamente una solución real** en el intervalo $(-2, \infty)$.

---

### Paso 2: Análisis de las raíces según el valor de $k$
Sea $f(x) = x^2 + (4 - k)x + 4$. Su discriminante es:
$$\Delta = (4 - k)^2 - 4(1)(4) = k^2 - 8k = k(k - 8)$$

Analizamos los posibles casos para que exista exactamente una raíz en $(-2, \infty)$:

#### Caso 1: La cuadrática tiene una única raíz real (raíz doble)
Esto ocurre cuando $\Delta = 0$, es decir, $k(k - 8) = 0$, lo que nos da $k = 0$ o $k = 8$.
- Si $k = 0$: la ecuación es $(x + 2)^2 = 0 \implies x = -2$. Sin embargo, $x = -2$ no pertenece al dominio $(-2, \infty)$, por lo que no hay solución.
- Si $k = 8$: la ecuación es $(x - 2)^2 = 0 \implies x = 2$. Como $2 > -2$, $x = 2$ es una solución válida. Por tanto, **$k = 8$** cumple la condición.

#### Caso 2: La cuadrática tiene dos raíces reales distintas, pero solo una es mayor que $-2$
Para que existan dos raíces reales distintas $x_1 < x_2$, necesitamos que $\Delta > 0$, lo cual ocurre cuando $k < 0$ o $k > 8$.
- Si $k > 8$: la suma de las raíces es $x_1 + x_2 = k - 4 > 4 > 0$ y el producto es $x_1 x_2 = 4 > 0$. Esto implica que ambas raíces son positivas ($0 < x_1 < x_2$), por lo que ambas son mayores que $-2$. Así, para $k > 8$ hay dos soluciones válidas.
- Si $k < 0$: evaluando la parábola $f(x) = x^2 + (4 - k)x + 4$ en el extremo del dominio $x = -2$, obtenemos:
  $$f(-2) = (-2)^2 + (4 - k)(-2) + 4 = 2k$$
  Como $k < 0$, tenemos que $f(-2) = 2k < 0$. Dado que el coeficiente principal de la parábola es positivo ($a = 1 > 0$) y $f(-2) < 0$, el valor $x = -2$ se encuentra estrictamente entre las dos raíces de la ecuación:
  $$x_1 < -2 < x_2$$
  Por lo tanto, para todo $k < 0$, exactamente una raíz ($x_2$) pertenece al intervalo $(-2, \infty)$.

---

### Paso 3: Conteo de valores enteros de $k$
Los valores de $k$ para los cuales la ecuación tiene exactamente una solución real son:
$$k < 0 \quad \text{y} \quad k = 8$$

Restringiendo al intervalo cerrado $[-500, 500]$:
- Para $k < 0$, los enteros son $-500, -499, \dots, -1$, lo que da un total de $500$ valores enteros.
- Para $k \ge 0$, el único valor entero válido es $k = 8$ ($1$ valor).

Sumando ambos casos, el número total de valores enteros de $k$ es $500 + 1 = 501$.

\boxed{501}