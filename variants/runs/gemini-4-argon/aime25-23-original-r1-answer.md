Para determinar para cuántos valores de $N$ entre $1$ y $1000$ inclusive tiene éxito el algoritmo voraz (*greedy algorithm*), analicemos cuántas monedas utiliza este algoritmo en comparación con otras posibles colecciones de monedas.

### 1. Representación del algoritmo voraz
Para cualquier entero positivo $N$, podemos dividir $N$ entre $25$:
$$N = 25q + r$$
donde $q = \lfloor N/25 \rfloor \ge 0$ es el número de monedas de $25$ centavos que elige el algoritmo voraz, y $r \in \{0, 1, \dots, 24\}$ es el resto.

A continuación, el algoritmo voraz divide $r$ entre $10$:
$$r = 10d + p$$
donde $d = \lfloor r/10 \rfloor \in \{0, 1, 2\}$ es el número de monedas de $10$ centavos y $p \in \{0, 1, \dots, 9\}$ es el número de monedas de $1$ centavo.

Así, el número total de monedas que utiliza el algoritmo voraz para formar $N$ centavos es:
$$G(N) = q + d + p$$

---

### 2. Condición para que el algoritmo voraz falle
Cualquier otra colección óptima de monedas para formar $N$ centavos debe usar algún número $q' = q - k$ de monedas de $25$ centavos (con $1 \le k \le q$) y cubrir el valor restante $r + 25k$ de manera óptima usando únicamente monedas de $10$ y $1$ centavo.

Sustituyendo $r = 10d + p$, el valor restante a cubrir con monedas de $10$ y $1$ centavo al quitar $k$ monedas de $25$ es:
$$r + 25k = 10(d + 2k) + (p + 5k)$$

Analicemos qué ocurre al variar $k$:
* **Si $k = 2m$ es par ($m \ge 1$):** Reducir el número de monedas de $25$ en $2m$ equivale a reemplazar $50m$ centavos por $5m$ monedas de $10$ centavos. Esto cambia el número total de monedas en $-2m + 5m = +3m > 0$. Por lo tanto, restar un número par de monedas de $25$ centavos siempre aumenta la cantidad total de monedas. Del mismo modo, cualquier $k$ impar mayor que $1$ ($k = 2m + 1$) usará $3m$ monedas más que $k = 1$.
* **Si $k = 1$ (posible solo si $q \ge 1$):** El resto a cubrir con monedas de $10$ y $1$ centavo es $r + 25 = 10(d + 2) + (p + 5)$.
  * Si $p < 5$, entonces $p + 5 < 10$, por lo que el número mínimo de monedas para esta alternativa es:
    $$(q - 1) + (d + 2) + (p + 5) = q + d + p + 6 > G(N)$$
    En este caso, el algoritmo voraz tiene éxito.
  * Si $p \ge 5$, entonces $p + 5 \ge 10$, lo que permite formar una moneda adicional de $10$ centavos dejando $p - 5$ monedas de $1$ centavo. El número total de monedas pasa a ser:
    $$(q - 1) + (d + 3) + (p - 5) = q + d + p - 3 < G(N)$$
    En este caso, la colección alternativa utiliza $3$ monedas menos que el algoritmo voraz, por lo que el algoritmo voraz **falla**.

En conclusión, el algoritmo voraz **falla si y solo si** se cumplen simultáneamente dos condiciones:
1. $q \ge 1$ (es decir, $N \ge 25$).
2. $p \ge 5$, donde $p = (N \bmod 25) \bmod 10$.

---

### 3. Conteo de valores de $N$ entre $1$ y $1000$
Los posibles restos $r = N \bmod 25$ van de $0$ a $24$:
* Para $r \in \{0, 1, \dots, 9\}$, $p = r$, por lo que $p \ge 5$ ocurre para $r \in \{5, 6, 7, 8, 9\}$ ($5$ valores).
* Para $r \in \{10, 11, \dots, 19\}$, $p = r - 10$, por lo que $p \ge 5$ ocurre para $r \in \{15, 16, 17, 18, 19\}$ ($5$ valores).
* Para $r \in \{20, 21, 22, 23, 24\}$, $p = r - 20 \in \{0, 1, 2, 3, 4\}$, por lo que nunca se cumple $p \ge 5$ ($0$ valores).

Así, por cada bloque de $25$ números consecutivos con un mismo cociente $q \ge 1$, el algoritmo voraz falla en exactamente $5 + 5 = 10$ valores.

Dividamos el rango $1 \le N \le 1000$:
* **Para $1 \le N \le 24$ ($q = 0$):** Como $q = 0$, no se puede quitar ninguna moneda de $25$ centavos; el algoritmo voraz falla en $0$ valores.
* **Para $25 \le N \le 999$ ($1 \le q \le 39$):** Hay $39$ bloques completos de $25$ números cada uno. En cada bloque hay $10$ fallos, lo que da un total de $39 \times 10 = 390$ valores donde el algoritmo voraz falla.
* **Para $N = 1000$ ($q = 40, r = 0$):** Como $p = 0 < 5$, el algoritmo voraz tiene éxito ($0$ fallos).

Restando el total de fallos de los $1000$ valores posibles de $N$:
$$1000 - 390 = 610$$

\boxed{610}