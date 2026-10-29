Para determinar el número de formas de ordenar $3$ copias de cada una de las $26$ letras minúsculas del alfabeto inglés cumpliendo la condición dada, analicemos primero la restricción sobre cualquier par de letras distintas.

### Paso 1: Análisis para un par de letras
Sean $a$ y $b$ dos letras distintas cualesquiera. Si restringimos nuestra atención únicamente a las $6$ posiciones ocupadas por las $3$ copias de $a$ y las $3$ copias de $b$, la condición exige que:
1. El número de letras $b$ entre la primera y la segunda aparición de $a$ sea igual al número de letras $b$ entre la segunda y la tercera aparición de $a$.
2. El número de letras $a$ entre la primera y la segunda aparición de $b$ sea igual al número de letras $a$ entre la segunda y la tercera aparición de $b$.

Como solo hay $3$ copias de $b$ en total, el número común de letras $b$ en cada uno de los dos intervalos entre copias consecutivas de $a$ solo puede ser $0$ o $1$ (ya que $2 + 2 = 4 > 3$).

- **Caso 1 (0 copias de $b$ entre las $a$):** Las tres copias de $a$ deben ser consecutivas en la subpalabra restringida a $\{a, b\}$. Para que las $b$ también tengan el mismo número de copias de $a$ entre la primera y la segunda que entre la segunda y la tercera, las tres copias de $b$ también deben ser consecutivas. Esto da únicamente dos patrones válidos:
  $$aaabbb \quad \text{y} \quad bbbaaa$$

- **Caso 2 (1 copia de $b$ entre las $a$):** Las tres copias de $a$ y dos de las copias de $b$ deben alternarse en la forma $ababa$. La tercera copia de $b$ puede colocarse al principio o al final, y en ambos casos se cumple la condición simétrica para $b$. Esto da otros dos patrones válidos:
  $$ababab \quad \text{y} \quad bababa$$

Por lo tanto, para cualquier par de letras distintas $\{a, b\}$, su orden relativo debe corresponder exactamente a uno de los cuatro patrones: $aaabbb$, $bbbaaa$, $ababab$ o $bababa$.

---

### Paso 2: Estructura global de la palabra
Para cada letra $x$, denotemos por $x_1 < x_2 < x_3$ las posiciones de su primera, segunda y tercera aparición, respectivamente.

Observamos que en los cuatro patrones válidos para un par $\{a, b\}$, el orden relativo entre sus primeras apariciones coincide con el de sus segundas y terceras apariciones:
$$a_1 < b_1 \iff a_2 < b_2 \iff a_3 < b_3$$

Ordenemos las $n = 26$ letras según la posición de su primera aparición. Hay $n! = 26!$ formas de elegir este orden. Llamemos a las letras $1, 2, \dots, n$ en dicho orden, de modo que:
$$1_1 < 2_1 < \dots < n_1, \qquad 1_2 < 2_2 < \dots < n_2, \qquad 1_3 < 2_3 < \dots < n_3$$

Para cualquier par $i < j$, como $i_1 < j_1$, su subpalabra debe ser de la forma $iiijjj$ (lo cual equivale a $i_3 < j_1$) o de la forma $ijijij$ (lo cual equivale a $j_1 < i_2$ y $j_2 < i_3$).

Analicemos la relación entre letras consecutivas $i$ e $i+1$ para cada $i \in \{1, 2, \dots, n-1\}$:
1. Si el par $(i, i+1)$ sigue el patrón $iii(i+1)(i+1)(i+1)$, entonces $i_3 < (i+1)_1$. Por monotonía, para todo $a \le i$ y $b \ge i+1$ se cumple $a_3 \le i_3 < (i+1)_1 \le b_1$. Esto significa que todas las apariciones de $\{1, \dots, i\}$ preceden completamente a todas las apariciones de $\{i+1, \dots, n\}$, produciendo un corte independiente entre ambos bloques.
2. Si para un bloque contiguo de letras $\{a, a+1, \dots, b\}$ cada par adyacente $(i, i+1)$ sigue el patrón alternado $i(i+1)i(i+1)i(i+1)$, entonces para cualesquiera $i < j < k$ dentro del bloque donde $(i, j)$ y $(j, k)$ se alternan, tenemos $k_1 < j_2 < i_3$. Esto impide que $(i, k)$ sea del tipo $iiikkk$ (que requiere $i_3 < k_1$), forzando a que $(i, k)$ también sea del tipo alternado $ikikik$. En particular, $(a, b)$ debe alternarse, lo que implica $b_1 < a_2$ y $b_2 < a_3$. Combinado con el orden de las apariciones, esto fija de manera única el orden de todas las letras del bloque como:
   $$a_1 < (a+1)_1 < \dots < b_1 < a_2 < (a+1)_2 < \dots < b_2 < a_3 < (a+1)_3 < \dots < b_3$$
   Es decir, el bloque completo $B = (a, a+1, \dots, b)$ aparece repetido tres veces de forma consecutiva: $BBB$.

---

### Paso 3: Conteo final
Toda disposición válida queda determinada de forma única por:
1. Una permutación de las $26$ letras (que define el orden de sus primeras apariciones): $26!$ opciones.
2. Para cada uno de los $25$ espacios entre letras consecutivas $(i, i+1)$ de la permutación, la elección de hacer un corte (patrón $iiijjj$) o mantenerlas en el mismo bloque repetido (patrón $ijijij$): $2^{25}$ opciones.

En consecuencia, el número total de formas de ordenar las letras es $2^{25} \cdot 26!$ (que es igual a $13532813598359960949788508160000000$).

\boxed{2^{25} \cdot 26!}