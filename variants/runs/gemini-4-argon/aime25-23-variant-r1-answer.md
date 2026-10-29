Para determinar para cuántos valores de $N$ entre $1$ y $1000$ inclusive tiene éxito el algoritmo voraz (*greedy algorithm*), comparemos la cantidad de monedas que utiliza este algoritmo con la cantidad de monedas de cualquier otra combinación válida.

### Paso 1: Formulación del algoritmo voraz y otras colecciones
Dado un entero positivo $N$, podemos dividirlo entre $24$ para escribirlo de forma única como:
$$N = 24q + r$$
donde $q = \lfloor N/24 \rfloor \ge 0$ y $0 \le r \le 23$.

El algoritmo voraz toma primero $q$ monedas de $24$ centavos, y luego forma el resto $r$ utilizando la mayor cantidad posible de monedas de $10$ centavos y el resto con monedas de $1$ centavo. 

Para cualquier entero no negativo $x$, si formamos $x$ centavos usando únicamente monedas de $10$ y de $1$ centavo de manera óptima (lo cual siempre se logra tomando el máximo número de monedas de $10$), la cantidad de monedas necesarias es:
$$h(x) = \left\lfloor \frac{x}{10} \right\rfloor + (x \bmod 10)$$
Por lo tanto, el número total de monedas que utiliza el algoritmo voraz para formar $N$ es:
$$G(N) = q + h(r)$$

Cualquier otra colección óptima de monedas para formar $N$ utilizará $q - j$ monedas de $24$ centavos (para algún entero $j$ tal que $0 \le j \le q$) y formará el valor restante, $r + 24j$, de manera óptima utilizando monedas de $10$ y $1$ centavo. El número total de monedas empleadas en dicha colección es:
$$(q - j) + h(r + 24j)$$

El algoritmo voraz tiene éxito para $N = 24q + r$ si y solo si para todo $1 \le j \le q$ se cumple que:
$$q + h(r) \le (q - j) + h(r + 24j) \iff h(r + 24j) - j - h(r) \ge 0$$

---

### Paso 2: Análisis del cambio al reemplazar monedas de $24$ centavos
Escribamos $r = 10a + b$, donde $a = \lfloor r/10 \rfloor$ y $b = r \bmod 10 \in \{0, 1, \dots, 9\}$. Notemos que:
$$h(r) = a + b$$
$$h(r + 24j) = a + \left\lfloor \frac{b + 24j}{10} \right\rfloor + ((b + 24j) \bmod 10) = a + h(b + 24j)$$

Al restar ambas expresiones, el término $a$ se cancela:
$$h(r + 24j) - j - h(r) = h(b + 24j) - j - b$$
Esto significa que el éxito del algoritmo voraz depende únicamente de $q$ y del último dígito $b = r \bmod 10$.

Analicemos cómo cambia la expresión $h(x) - j$ cuando $j$ aumenta en $1$ (lo que equivale a sumar $24$ al resto $x$ y restar $1$ moneda de $24$ centavos):
- **Caso 1:** Si el dígito de las unidades de $x$ cumple $x \bmod 10 \le 5$, al sumar $24 = 20 + 4$ no se produce acarreo adicional en las decenas: el número de monedas de $10$ aumenta en $2$ y el de monedas de $1$ aumenta en $4$. Contando la moneda de $24$ que quitamos, el cambio neto en el número de monedas es $+2 + 4 - 1 = +5$.
- **Caso 2:** Si el dígito de las unidades de $x$ cumple $x \bmod 10 \ge 6$, al sumar $24 = 30 - 6$ se produce un acarreo: el número de monedas de $10$ aumenta en $3$ y el de monedas de $1$ disminuye en $6$. Contando la moneda de $24$ que quitamos, el cambio neto en el número de monedas es $+3 - 6 - 1 = -4$.

Además, si ocurre el Caso 2 ($x \bmod 10 \in \{6, 7, 8, 9\}$), el nuevo dígito de las unidades pasa a ser $(x + 4) \bmod 10 \in \{0, 1, 2, 3\} \le 5$. Esto implica que **nunca pueden ocurrir dos cambios de $-4$ consecutivos**; todo cambio de $-4$ va seguido inmediatamente de un cambio de $+5$.

De esto deducimos dos comportamientos según el valor de $b = r \bmod 10$:
1. **Si $b \in \{0, 1, 2, 3, 4, 5\}$:** El primer cambio (para $j=1$) es $+5$. Como nunca hay dos $-4$ seguidos y cada par $(-4, +5)$ suma $+1 > 0$, la suma acumulada $h(b + 24j) - j - b$ es siempre positiva ($\ge 1$) para todo $j \ge 1$. Por tanto, el algoritmo voraz **siempre tiene éxito**.
2. **Si $b \in \{6, 7, 8, 9\}$:** El primer cambio (para $j=1$) es $-4 < 0$. Por lo tanto, si $q \ge 1$, tomar $j = 1$ (una moneda menos de $24$ centavos) ahorra $4$ monedas y el algoritmo voraz **falla**. En este caso, solo tiene éxito cuando $q = 0$.

---

### Paso 3: Conteo para $1 \le N \le 1000$
Entre los $24$ posibles restos $r \in \{0, 1, \dots, 23\}$, aquellos que tienen su último dígito en $\{6, 7, 8, 9\}$ son exactamente $8$ valores:
$$r \in \{6, 7, 8, 9, 16, 17, 18, 19\}$$
Los otros $16$ restos tienen último dígito en $\{0, 1, 2, 3, 4, 5\}$.

Dividimos $1000$ entre $24$:
$$1000 = 24 \times 41 + 16$$

Contemos los valores de $N$ en los que el algoritmo voraz **falla** (es decir, $q \ge 1$ y $r \in \{6, 7, 8, 9, 16, 17, 18, 19\}$):
- Para $q = 0$ ($1 \le N \le 23$): $0$ valores fallan.
- Para $1 \le q \le 40$ ($24 \le N \le 983$): Hay $40$ bloques completos de $24$ números, y en cada bloque fallan $8$ valores, lo que da $40 \times 8 = 320$ valores.
- Para $q = 41$ ($984 \le N \le 1000$): El resto $r$ recorre el conjunto $\{0, 1, \dots, 16\}$. Dentro de este rango se encuentran $5$ restos que fallan: $r \in \{6, 7, 8, 9, 16\}$.

En total, el algoritmo voraz falla para $320 + 5 = 325$ valores de $N$.

Por lo tanto, el número de valores de $N$ entre $1$ y $1000$ inclusive para los cuales el algoritmo voraz tiene éxito es:
$$1000 - 325 = 675$$

\boxed{675}