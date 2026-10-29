Para encontrar el número $N$ de enteros positivos de ocho dígitos formados al usar cada uno de los dígitos $1, 2, 3, 4, 5, 6, 7, 8$ exactamente una vez y que sean divisibles por $22$, debemos aplicar los criterios de divisibilidad por $2$ y por $11$.

Sea el número de ocho dígitos $d_1 d_2 d_3 d_4 d_5 d_6 d_7 d_8$.

### Paso 1: Condición de divisibilidad por 11
Un número es divisible por $11$ si y solo si la diferencia entre la suma de los dígitos en posiciones pares y la suma de los dígitos en posiciones impares es un múltiplo de $11$.
Sean:
$$S_+ = d_2 + d_4 + d_6 + d_8$$
$$S_- = d_1 + d_3 + d_5 + d_7$$

La suma total de todos los dígitos es:
$$S_+ + S_- = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 = 36$$

Como la suma mínima posible de cuatro dígitos distintos de este conjunto es $1 + 2 + 3 + 4 = 10$ y la máxima es $5 + 6 + 7 + 8 = 26$, tenemos que:
$$-16 \le S_+ - S_- \le 16$$

Además, como $S_+ + S_- = 36$ es par, la diferencia $S_+ - S_-$ también debe ser par. El único múltiplo par de $11$ en el intervalo $[-16, 16]$ es $0$. Por lo tanto:
$$S_+ - S_- = 0 \implies S_+ = S_- = 18$$

### Paso 2: Subconjuntos de 4 dígitos que suman 18
Buscamos todos los subconjuntos $A \subset \{1, 2, 3, 4, 5, 6, 7, 8\}$ de $4$ elementos cuya suma sea $18$. Cada subconjunto $A$ que contiene al $8$ se empareja con su complemento $A^c$ (que no contiene al $8$ y también suma $36 - 18 = 18$).

Si $8 \in A$, los otros $3$ elementos deben pertenecer a $\{1, 2, 3, 4, 5, 6, 7\}$ y sumar $18 - 8 = 10$. Las ternas posibles son:
1. $\{1, 2, 7\} \implies A_1 = \{1, 2, 7, 8\}$ y $A_1^c = \{3, 4, 5, 6\}$
2. $\{1, 3, 6\} \implies A_2 = \{1, 3, 6, 8\}$ y $A_2^c = \{2, 4, 5, 7\}$
3. $\{1, 4, 5\} \implies A_3 = \{1, 4, 5, 8\}$ y $A_3^c = \{2, 3, 6, 7\}$
4. $\{2, 3, 5\} \implies A_4 = \{2, 3, 5, 8\}$ y $A_4^c = \{1, 4, 6, 7\}$

En total, hay $4 \times 2 = 8$ subconjuntos posibles para el conjunto de dígitos en las posiciones pares $\{d_2, d_4, d_6, d_8\}$.

### Paso 3: Condición de divisibilidad por 2 y conteo total
Para que el número sea divisible por $2$, el último dígito $d_8$ debe ser par.
Observamos que como $18$ es par y las sumas de todos los impares ($1+3+5+7=16$) o todos los pares ($2+4+6+8=20$) no son $18$, cada uno de los $8$ subconjuntos encontrados contiene exactamente $2$ dígitos pares y $2$ dígitos impares.

Para cada elección de uno de los $8$ subconjuntos como $\{d_2, d_4, d_6, d_8\}$:
- Hay $2$ opciones para elegir el dígito par $d_8$.
- Hay $3! = 6$ formas de ordenar los $3$ dígitos restantes del subconjunto en las posiciones $d_2, d_4, d_6$.
- Hay $4! = 24$ formas de ordenar los $4$ dígitos del subconjunto complementario en las posiciones impares $d_1, d_3, d_5, d_7$.

Por lo tanto, el número total $N$ de dichos enteros es:
$$N = 8 \times 2 \times 3! \times 4! = 16 \times 6 \times 24 = 2304$$

### Paso 4: Diferencia entre $N$ y 2025
Calculamos la diferencia:
$$N - 2025 = 2304 - 2025 = 279$$

\boxed{279}