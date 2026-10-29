Para determinar para cuántos valores de $N$ entre $1$ y $1000$ inclusive tiene éxito el algoritmo voraz (*greedy algorithm*), expresemos cualquier entero positivo $N$ dividiéndolo entre $24$:
$$N = 24q + r$$
donde $q = \lfloor N/24 \rfloor \ge 0$ y $r \in \{0, 1, \dots, 23\}$ es el residuo.

### Paso 1: Número de monedas en el algoritmo voraz
Para formar un monto $x \ge 0$ utilizando únicamente monedas de $10$ y $1$ centavo, la forma óptima (y la que elige el algoritmo voraz) requiere:
$$h(x) = \left\lfloor \frac{x}{10} \right\rfloor + (x \bmod 10) = x - 9\left\lfloor \frac{x}{10} \right\rfloor \text{ monedas.}$$

Por lo tanto, el algoritmo voraz para $N = 24q + r$ toma $q$ monedas de $24$ centavos y forma el resto $r$ con monedas de $10$ y $1$ centavo, utilizando en total:
$$G(N) = q + h(r) \text{ monedas.}$$

### Paso 2: Comparación con otras colecciones de monedas
Cualquier otra colección que pueda mejorar al algoritmo voraz debe usar $a$ monedas de $24$ centavos, con $0 \le a \le q$, y formar el monto restante $N - 24a$ de manera óptima con monedas de $10$ y $1$ centavo. 

Sea $k = q - a$ el número de monedas de $24$ centavos que dejamos de usar respecto al algoritmo voraz, donde $1 \le k \le q$. El monto restante a cubrir con monedas de $10$ y $1$ centavo es $24k + r$, por lo que el número total de monedas empleadas es:
$$C(N, k) = (q - k) + h(24k + r)$$

El algoritmo voraz **falla** para $N$ si y solo si existe algún entero $k \in \{1, 2, \dots, q\}$ tal que $C(N, k) < G(N)$, es decir:
$$(q - k) + h(24k + r) < q + h(r) \iff -k + h(24k + r) < h(r)$$

### Paso 3: Simplificación de la condición de fallo
Notemos que para cualquier $m \ge 0$ y $x \ge 0$, se cumple $h(x + 10m) = m + h(x)$. Como $24k + r = 20k + (4k + r)$, tenemos:
$$h(24k + r) = 2k + h(4k + r)$$
Sustituyendo esto en la desigualdad anterior, la condición de fallo se convierte en:
$$k + h(4k + r) < h(r)$$

Escribamos ahora $r = 10d + u$, donde $d = \lfloor r/10 \rfloor \in \{0, 1, 2\}$ es el dígito de las decenas de $r$ y $u = r \bmod 10 \in \{0, 1, \dots, 9\}$ es el dígito de las unidades. Entonces:
$$h(r) = d + u \quad \text{y} \quad h(4k + r) = h(10d + 4k + u) = d + h(4k + u)$$
Al sustituir y cancelar $d$ en ambos lados, obtenemos que el algoritmo voraz falla para un $k \ge 1$ si y solo si:
$$k + h(4k + u) < u$$
Usando la identidad $h(x) = x - 9\lfloor x/10 \rfloor$, esto equivale a:
$$k + 4k + u - 9\left\lfloor \frac{4k + u}{10} \right\rfloor < u \iff 5k < 9\left\lfloor \frac{4k + u}{10} \right\rfloor$$

Analicemos para qué valores de $k \ge 1$ y $u \in \{0, 1, \dots, 9\}$ se satisface esta desigualdad:
* Como $u \le 9$, tenemos $9\left\lfloor \frac{4k + u}{10} \right\rfloor \le 9\left(\frac{4k + 9}{10}\right) = 3.6k + 8.1$. Para que $5k < 3.6k + 8.1$, necesariamente $1.4k < 8.1$, por lo que $k \le 5$.
* Para $k = 1$: $5 < 9\left\lfloor \frac{4 + u}{10} \right\rfloor \iff \left\lfloor \frac{4 + u}{10} \right\rfloor \ge 1 \iff 4 + u \ge 10 \iff u \in \{6, 7, 8, 9\}$.
* Para $k = 2$: $10 < 9\left\lfloor \frac{8 + u}{10} \right\rfloor \iff \left\lfloor \frac{8 + u}{10} \right\rfloor \ge 2 \iff 8 + u \ge 20$, imposible pues $u \le 9$.
* Para $k = 3$: $15 < 9\left\lfloor \frac{12 + u}{10} \right\rfloor \iff \left\lfloor \frac{12 + u}{10} \right\rfloor \ge 2 \iff 12 + u \ge 20 \iff u \in \{8, 9\}$ (que ya fallaban desde $k = 1$).
* Para $k = 4$: $20 < 9\left\lfloor \frac{16 + u}{10} \right\rfloor \iff 16 + u \ge 30$, imposible.
* Para $k = 5$: $25 < 9\left\lfloor \frac{20 + u}{10} \right\rfloor \iff 20 + u \ge 30$, imposible.

Por consiguiente, el algoritmo voraz **falla** para $N = 24q + r$ si y solo si se cumplen dos condiciones:
1. $q \ge 1$ (pues se necesita poder elegir al menos $k = 1 \le q$), y
2. $r \bmod 10 \in \{6, 7, 8, 9\}$, lo que para $0 \le r < 24$ corresponde exactamente a los $8$ residuos:
$$r \in \{6, 7, 8, 9, 16, 17, 18, 19\}.$$

### Paso 4: Conteo para $1 \le N \le 1000$
Contemos cuántos valores de $N$ entre $1$ y $1000$ fallan:
Como $1000 = 24 \times 41 + 16$:
* Para $q = 0$ ($1 \le N \le 23$), ninguno falla.
* Para cada $q \in \{1, 2, \dots, 40\}$ ($24 \le N \le 983$), todos los $24$ residuos están presentes, por lo que fallan exactamente $8$ valores por cada $q$. Esto da $40 \times 8 = 320$ valores.
* Para $q = 41$ ($984 \le N \le 1000$), el residuo $r$ varía desde $0$ hasta $16$. Los residuos de fallo en este rango son $r \in \{6, 7, 8, 9, 16\}$, lo que aporta $5$ valores más.

En total, el algoritmo voraz falla para $320 + 5 = 325$ valores de $N$.
Por lo tanto, el número de valores de $N$ entre $1$ y $1000$ inclusive para los cuales el algoritmo voraz tiene éxito es:
$$1000 - 325 = 675$$

\boxed{675}