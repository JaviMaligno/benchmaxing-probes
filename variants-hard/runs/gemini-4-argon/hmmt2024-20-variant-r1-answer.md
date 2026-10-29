Para determinar cuántos números «linterna» (*lanterns*) son exactamente el doble de otro número linterna, analicemos la relación entre los dígitos de ambos números.

### 1. Caracterización mediante dígitos y acarreos

Sea $A = \overline{a_1 a_2 \dots a_9}$ un número linterna y sea $B = 2A = \overline{b_1 b_2 \dots b_9}$ otro número linterna. Tanto $A$ como $B$ son permutaciones del conjunto de dígitos $\{1, 2, 3, 4, 5, 6, 7, 8, 9\}$.

Al multiplicar $A$ por $2$, sea $c_i \in \{0, 1\}$ el acarreo que entra en la posición $i$ (proveniente de la posición $i+1$, con $c_9 = 0$), y sea $c_0$ el acarreo saliente de la primera posición (que debe ser $c_0 = 0$ para que $B$ tenga exactamente $9$ dígitos). En cada posición $i \in \{1, \dots, 9\}$ se cumple:
$$2a_i + c_i = 10 c_{i-1} + b_i$$

Observemos cómo se determina el acarreo saliente $c_{i-1}$ a partir de $a_i$:
- Si $a_i \in S = \{1, 2, 3, 4\}$, entonces $2a_i + c_i \le 2(4) + 1 = 9 < 10$, por lo que **$c_{i-1} = 0$ siempre**, sin importar el valor de $c_i$.
- Si $a_i \in L = \{5, 6, 7, 8, 9\}$, entonces $2a_i + c_i \ge 2(5) + 0 = 10$, por lo que **$c_{i-1} = 1$ siempre**, sin importar el valor de $c_i$.

De este modo, el acarreo depende únicamente de si el dígito de la derecha pertenece a $S$ o a $L$. Además, como $b_i \equiv 2a_i + c_i \equiv c_i \pmod 2$:
- $b_i$ es **par** si y solo si $c_i = 0$ (lo cual ocurre cuando $i = 9$ o $a_{i+1} \in S$).
- $b_i$ es **impar** si y solo si $c_i = 1$ (lo cual ocurre cuando $i \le 8$ y $a_{i+1} \in L$).

En particular, como $c_0 = 0$, necesariamente $a_1 \in S$.

---

### 2. Condiciones sobre los dígitos de $A$ y $B$

Analicemos qué dígito $b_i$ se obtiene según el valor de $a_i$ y del acarreo $c_i \in \{0, 1\}$:
1. **Para $a_i = 5$:**
   - Si $c_i = 0$, entonces $b_i = 0$, lo cual es imposible porque $B$ no contiene el dígito $0$.
   - Si $c_i = 1$, entonces $b_i = 1$.
   Por lo tanto, el dígito $5$ de $A$ **debe recibir acarreo $c_i = 1$** (y es la única manera de obtener el dígito $1$ en $B$).

2. **Para los pares de dígitos congruentes módulo $5$:**
   Agrupemos los $8$ dígitos restantes de $A$ en cuatro pares $P_k = \{k, k+5\}$ para $k \in \{1, 2, 3, 4\}$:
   $$P_1 = \{1, 6\}, \quad P_2 = \{2, 7\}, \quad P_3 = \{3, 8\}, \quad P_4 = \{4, 9\}$$
   Si $a_i \in P_k$:
   - Cuando $c_i = 0$, se obtiene $b_i = 2k$.
   - Cuando $c_i = 1$, se obtiene $b_i = 2k + 1$.

Para que $B$ contenga todos los dígitos $\{2, 3, 4, 5, 6, 7, 8, 9\}$ exactamente una vez, es necesario y suficiente que, para cada $k \in \{1, 2, 3, 4\}$, de los dos elementos de $P_k = \{k, k+5\}$ en $A$, **exactamente uno reciba acarreo $0$ y el otro reciba acarreo $1$**.

---

### 3. Traducción directa sobre la secuencia $B$

En términos de $B = (b_1, b_2, \dots, b_9)$, sabemos que para cada posición $i \in \{1, \dots, 9\}$, el dígito $a_i$ pertenece a $S$ si $c_{i-1} = 0$ y pertenece a $L$ si $c_{i-1} = 1$. Definiendo $b_0 = 0$ (par), la condición $c_{i-1} = 0$ equivale a que $b_{i-1}$ sea par, y $c_{i-1} = 1$ equivale a que $b_{i-1}$ sea impar.

Así, una permutación $B = (b_1, \dots, b_9)$ de $\{1, 2, \dots, 9\}$ es el doble de un número linterna $A$ si y solo si cumple:
1. $b_9$ es par (pues $c_9 = 0$).
2. El dígito $1$ (que proviene de $a_i = 5 \in L$) está precedido en $B$ por un dígito impar $b_{i-1}$.
3. Para cada $k \in \{1, 2, 3, 4\}$, los dígitos $\{2k, 2k+1\}$ en $B$ provienen de $\{k, k+5\}$ en $A$ (uno en $S$ y otro en $L$). Por tanto, de los dos dígitos $\{2k, 2k+1\}$, **exactamente uno debe ir precedido por un dígito par** (incluyendo $b_0 = 0$ para la primera posición) **y el otro debe ir precedido por un dígito impar**.

---

### 4. Conteo combinatorio

En la secuencia extendida $(b_0, b_1, \dots, b_9)$, que comienza en el par $b_0 = 0$ y termina en el par $b_9 \in \{2, 4, 6, 8\}$, los $5$ dígitos impares $\{1, 3, 5, 7, 9\}$ y los dígitos pares se alternan formando $y$ bloques contiguos de dígitos impares y $y$ bloques contiguos de dígitos pares después de $b_0$ (además del bloque inicial que encabeza $b_0$), para algún $y \in \{1, 2, 3, 4\}$:
$$(b_0 \dots) \, [\text{Bloque Impar } 1] \, [\text{Bloque Par } 1] \dots [\text{Bloque Impar } y] \, [\text{Bloque Par } y]$$

Para cada uno de los $4$ pares $\{2k, 2k+1\}$ ($k = 1, 2, 3, 4$), tenemos dos opciones:
- **Tipo I:** el par $2k$ va precedido por un par y el impar $2k+1$ va precedido por un impar.
- **Tipo II:** el impar $2k+1$ va precedido por un par y el par $2k$ va precedido por un impar.

El número de pares $\{2k, 2k+1\}$ de Tipo II es exactamente el número $y$ de dígitos impares precedidos por un par, es decir, el número $y$ de bloques de impares (con $1 \le y \le 4$):

1. **Elección de los tipos:** Para un $y \in \{1, 2, 3, 4\}$ fijo, hay $\binom{4}{y}$ maneras de elegir cuáles $y$ de los $4$ pares $\{2k, 2k+1\}$ son de Tipo II.
2. **Formación de los bloques pares:** Hay $y$ dígitos pares que deben ir precedidos por un impar (encabezando los $y$ bloques pares) y $4 - y$ dígitos pares que deben ir precedidos por otro par.
   - Los $y$ encabezados de los bloques pares se pueden ordenar de $y!$ maneras.
   - Los $4 - y$ dígitos pares restantes se insertan sucesivamente detrás de algún par ya colocado (incluyendo $b_0$), lo que puede hacerse de $(y+1)(y+2)\cdots 4 = \frac{4!}{y!}$ maneras.
   - En total, hay $y! \cdot \frac{4!}{y!} = 4!$ maneras de formar los bloques pares.
3. **Formación de los bloques impares:** Hay $y$ dígitos impares que deben ir precedidos por un par (encabezando los $y$ bloques impares) y $5 - y$ dígitos impares (incluyendo el $1$) que deben ir precedidos por otro impar.
   - Los $y$ encabezados de los bloques impares se pueden ordenar de $y!$ maneras.
   - Los $5 - y$ dígitos impares restantes se insertan sucesivamente detrás de algún impar ya colocado, lo que puede hacerse de $y(y+1)\cdots 4 = y \cdot \frac{4!}{y!}$ maneras.
   - En total, hay $y! \cdot y \cdot \frac{4!}{y!} = y \cdot 4!$ maneras de formar los bloques impares.

Multiplicando estas cantidades y sumando sobre todos los valores posibles de $y \in \{1, 2, 3, 4\}$, obtenemos el total de números linterna buscados:
$$\text{Total} = \sum_{y=1}^{4} \binom{4}{y} \cdot 4! \cdot (y \cdot 4!) = (4!)^2 \sum_{y=1}^{4} y \binom{4}{y}$$

Usando la identidad $\sum_{y=1}^{4} y \binom{4}{y} = 4 \cdot 2^{4-1} = 32$ y sabiendo que $4! = 24$:
$$\text{Total} = 24^2 \times 32 = 576 \times 32 = 18432$$

\boxed{18432}