Para encontrar el número $N$ de enteros positivos de nueve dígitos (formados usando cada uno de los dígitos del $1$ al $9$ exactamente una vez) que son divisibles por $22$, debemos imponer que sean divisibles simultáneamente por $2$ y por $11$.

### Paso 1: Condición de divisibilidad por 11
Sea el número de nueve dígitos $d_1 d_2 d_3 d_4 d_5 d_6 d_7 d_8 d_9$. 
Definimos el conjunto de dígitos en las posiciones impares como $O = \{d_1, d_3, d_5, d_7, d_9\}$ (con $5$ elementos) y el conjunto de dígitos en las posiciones pares como $E = \{d_2, d_4, d_6, d_8\}$ (con $4$ elementos).

La suma de todos los dígitos es:
$$S(O) + S(E) = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45$$

Por el criterio de divisibilidad del $11$, necesitamos que:
$$S(O) - S(E) \equiv 0 \pmod{11}$$
Dado que $S(O) + S(E) = 45$ es impar, la diferencia $S(O) - S(E)$ también debe ser un múltiplo impar de $11$, es decir, $\pm 11$ o $\pm 33$:
- Si $S(O) - S(E) = 11$, entonces $2S(E) = 45 - 11 = 34 \implies S(E) = 17$ y $S(O) = 28$.
- Si $S(O) - S(E) = -11$, entonces $2S(E) = 45 + 11 = 56 \implies S(E) = 28$ y $S(O) = 17$.
- Si $S(O) - S(E) = \pm 33$, tendríamos $S(E) = 6$ o $S(O) = 6$, lo cual es imposible ya que la suma mínima de $4$ dígitos distintos es $1+2+3+4 = 10$.

Por lo tanto, el número es divisible por $11$ si y solo si la suma de los $4$ dígitos en $E$ es $S(E) = 17$ o $S(E) = 28$.

---

### Paso 2: Condición de divisibilidad por 2 y conteo de subconjuntos
Para que el número sea divisible por $2$, el último dígito $d_9 \in O$ debe ser par. Para una partición fija $(O, E)$, si $k(O)$ es la cantidad de dígitos pares en $O$, tenemos:
- $k(O)$ opciones para elegir $d_9$.
- $4! = 24$ formas de permutar los $4$ dígitos restantes de $O$ en las posiciones $d_1, d_3, d_5, d_7$.
- $4! = 24$ formas de permutar los $4$ dígitos de $E$ en las posiciones $d_2, d_4, d_6, d_8$.

Como hay $4$ dígitos pares en total ($\{2, 4, 6, 8\}$), se cumple que $k(O) = 4 - k(E)$, donde $k(E)$ es la cantidad de dígitos pares en $E$.

#### Caso 1: $S(E) = 17$
Listamos todos los subconjuntos $E \subset \{1, \dots, 9\}$ de $4$ elementos que suman $17$ y contamos cuántos elementos pares $k(E)$ tienen:
1. $\{1, 2, 5, 9\} \implies k(E) = 1 \implies k(O) = 3$
2. $\{1, 2, 6, 8\} \implies k(E) = 3 \implies k(O) = 1$
3. $\{1, 3, 4, 9\} \implies k(E) = 1 \implies k(O) = 3$
4. $\{1, 3, 5, 8\} \implies k(E) = 1 \implies k(O) = 3$
5. $\{1, 3, 6, 7\} \implies k(E) = 1 \implies k(O) = 3$
6. $\{1, 4, 5, 7\} \implies k(E) = 1 \implies k(O) = 3$
7. $\{2, 3, 4, 8\} \implies k(E) = 3 \implies k(O) = 1$
8. $\{2, 3, 5, 7\} \implies k(E) = 1 \implies k(O) = 3$
9. $\{2, 4, 5, 6\} \implies k(E) = 3 \implies k(O) = 1$

La suma de los valores de $k(O)$ en este caso es:
$$6 \times 3 + 3 \times 1 = 18 + 3 = 21$$

#### Caso 2: $S(E) = 28$
Listamos todos los subconjuntos $E \subset \{1, \dots, 9\}$ de $4$ elementos que suman $28$:
1. $\{4, 7, 8, 9\} \implies k(E) = 2 \implies k(O) = 2$
2. $\{5, 6, 8, 9\} \implies k(E) = 2 \implies k(O) = 2$

La suma de los valores de $k(O)$ en este caso es:
$$2 \times 2 = 4$$

---

### Paso 3: Cálculo de $N$ y la diferencia
Sumando las opciones para $d_9$ en ambos casos, obtenemos $\sum k(O) = 21 + 4 = 25$. Multiplicando por las permutaciones de las demás posiciones:
$$N = 25 \times 4! \times 4! = 25 \times 24 \times 24 = 25 \times 576 = 14400$$

Finalmente, calculamos la diferencia entre $N$ y $14025$:
$$14400 - 14025 = 375$$

\boxed{375}