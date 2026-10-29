Para hallar el valor de $a+b$, calculemos primero la suma de los números en cada una de las dos cuadrículas de tamaño $a \times b$.

**1. Suma de la cuadrícula de Isabella ($S_I$):**
La cuadrícula contiene todos los números enteros consecutivos desde $1$ hasta $ab$. Usando la fórmula para la suma de los primeros $n$ enteros positivos, obtenemos:
$$S_I = \sum_{k=1}^{ab} k = \frac{ab(ab+1)}{2}$$

**2. Suma de la cuadrícula de Vidur ($S_V$):**
El número en la fila $i$ y la columna $j$ es $ij$. Sumando sobre todas las filas ($1 \le i \le a$) y todas las columnas ($1 \le j \le b$), podemos factorizar la suma de la siguiente manera:
$$S_V = \sum_{i=1}^{a} \sum_{j=1}^{b} ij = \left(\sum_{i=1}^{a} i\right)\left(\sum_{j=1}^{b} j\right) = \frac{a(a+1)}{2} \cdot \frac{b(b+1)}{2}$$

**3. Diferencia entre ambas sumas:**
Restamos las dos cantidades y simplificamos:
$$S_I - S_V = \frac{ab(ab+1)}{2} - \frac{ab(a+1)(b+1)}{4}$$
$$S_I - S_V = \frac{ab}{4} \big(2(ab+1) - (ab + a + b + 1)\big)$$
$$S_I - S_V = \frac{ab(ab - a - b + 1)}{4} = \frac{ab(a-1)(b-1)}{4}$$

Podemos reescribir esta expresión agrupando los términos en $a$ y en $b$ como el producto de dos números triangulares:
$$\frac{a(a-1)}{2} \cdot \frac{b(b-1)}{2} = 1200$$

**4. Búsqueda de $a$ y $b$:**
Sea $T_n = \frac{n(n+1)}{2}$ el $n$-ésimo número triangular. Buscamos dos números triangulares $T_{a-1}$ y $T_{b-1}$ cuyo producto sea $1200 = 2^4 \cdot 3 \cdot 5^2$.

Listamos los primeros números triangulares y verificamos cuáles dividen a $1200$ dando como cociente otro número triangular:
- $T_1 = 1 \implies 1200 / 1 = 1200$ (no es triangular, pues $1200 \cdot 2 = 2400$ no es de la forma $n(n+1)$).
- $T_2 = 3 \implies 1200 / 3 = 400$ (no es triangular, pues $400 \cdot 2 = 800$ y $28 \cdot 29 = 812$).
- $T_3 = 6 \implies 1200 / 6 = 200$ (no es triangular, pues $200 \cdot 2 = 400$ y $19 \cdot 20 = 380$).
- $T_4 = 10 \implies 1200 / 10 = 120$. Como $120 = \frac{15 \cdot 16}{2} = T_{15}$, ¡este sí es un número triangular!
- $T_5 = 15 \implies 1200 / 15 = 80$ (no es triangular, pues $80 \cdot 2 = 160$ y $12 \cdot 13 = 156$).
- Para $6 \le n \le 14$, ningún $T_n$ divide a $1200$.

Por simetría, el conjunto $\{a-1, b-1\}$ debe ser $\{4, 15\}$, lo que implica que $\{a, b\} = \{5, 16\}$.

Finalmente, calculamos la suma $a+b$:
$$a + b = 5 + 16 = 21$$

\boxed{21}