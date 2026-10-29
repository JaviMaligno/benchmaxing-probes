## Planteamiento

Un número es divisible por 22 si lo es por 2 y por 11.

**Divisibilidad por 11.** Sean $A$ la suma de los dígitos en posiciones impares (1,3,5,7,9 — cinco dígitos) y $B$ la de las posiciones pares (2,4,6,8 — cuatro dígitos). Como $A+B=45$ y se requiere $11 \mid A-B$, con $A-B$ impar, solo caben $A-B=\pm 11$ (los valores $\pm 33$ son imposibles). Es decir, $A=28$ o $A=17$.

**Conjuntos posibles para las posiciones impares (5 dígitos):**

- $A=17$: solo $\{1,2,3,4,7\}$ y $\{1,2,3,5,6\}$ → 2 conjuntos.
- $A=28$: son los complementos de los 4-subconjuntos que suman 17, que son 9:
 $\{1,2,5,9\},\{1,2,6,8\},\{1,3,4,9\},\{1,3,5,8\},\{1,3,6,7\},\{1,4,5,7\},\{2,3,4,8\},\{2,3,5,7\},\{2,4,5,6\}$ → 9 conjuntos.

**Divisibilidad por 2.** La última cifra (posición 9, impar) debe ser par. Para cada conjunto $A$ con $e(A)$ dígitos pares, el número de arreglos es $e(A)\cdot 4!\cdot 4! = 576\,e(A)$.

**Conteo de $e(A)$:**

- $A=17$: $\{1,2,3,4,7\}\to 2$, $\{1,2,3,5,6\}\to 2$. Subtotal $4$.
- $A=28$ (complementos en el orden anterior): $\{3,4,6,7,8\}\to3$, $\{3,4,5,7,9\}\to1$, $\{2,5,6,7,8\}\to3$, $\{2,4,6,7,9\}\to3$, $\{2,4,5,8,9\}\to3$, $\{2,3,6,8,9\}\to3$, $\{1,5,6,7,9\}\to1$, $\{1,4,6,8,9\}\to3$, $\{1,3,7,8,9\}\to1$. Subtotal $21$.

Total: $\sum e(A)=25$, por lo que

$$N = 25\cdot 576 = 14400.$$

(Comprobación: sin la condición de paridad habría $11\cdot 5!\cdot 4! = 31680$ múltiplos de 11, valor conocido.)

Finalmente, $14400 - 14025 = 375$.

\boxed{375}