## Planteamiento

Para que un número sea divisible por 22 = 2 · 11, debe ser divisible por 2 y por 11.

**Criterio del 11:** la suma alternada de dígitos debe ser múltiplo de 11. Si $S_1$ es la suma de los dígitos en las posiciones impares (1.ª, 3.ª, 5.ª, 7.ª) y $S_2$ la de las pares (2.ª, 4.ª, 6.ª, 8.ª), entonces $S_1 + S_2 = 36$ y necesitamos $|S_1 - S_2| \in \{0, 11, 22, \dots\}$.

- $|S_1 - S_2| = 11$ es imposible (daría $S_1 = 12{,}5$).
- $|S_1 - S_2| = 22$ exigiría $S_1 = 29$ o $7$, imposible con 4 dígitos de 1–8 (máximo $8+7+6+5=26$).
- Por lo tanto $S_1 = S_2 = 18$.

## Subconjuntos de 4 dígitos que suman 18

Hallamos los subconjuntos de $\{1,\dots,8\}$ de tamaño 4 con suma 18:

$$\{1,2,7,8\},\ \{1,3,6,8\},\ \{1,4,5,8\},\ \{2,3,5,8\}$$
$$\{1,4,6,7\},\ \{2,3,6,7\},\ \{2,4,5,7\},\ \{3,4,5,6\}$$

Son 8, que forman **4 pares complementarios**:

1. $\{1,2,7,8\}$ y $\{3,4,5,6\}$
2. $\{1,3,6,8\}$ y $\{2,4,5,7\}$
3. $\{1,4,5,8\}$ y $\{2,3,6,7\}$
4. $\{2,3,5,8\}$ y $\{1,4,6,7\}$

## Conteo con el criterio del 2

Para cada par $\{A, B\}$ hay dos asignaciones (A en posiciones impares y B en pares, o viceversa). El último dígito (posición 8) pertenece al conjunto colocado en las posiciones pares, así que si ese conjunto tiene $e$ dígitos pares, el número de arreglos válidos es:

$$e \cdot 3! \cdot 4! = 72e$$

(en el conjunto par: $e$ opciones para la última posición y $3!$ para las demás; $4!$ para el conjunto impar).

En los cuatro pares, **ambos conjuntos tienen exactamente 2 dígitos pares**:

| Par | $e_A$ | $e_B$ |
|---|---|---|
| $\{1,2,7,8\},\{3,4,5,6\}$ | 2 | 2 |
| $\{1,3,6,8\},\{2,4,5,7\}$ | 2 | 2 |
| $\{1,4,5,8\},\{2,3,6,7\}$ | 2 | 2 |
| $\{2,3,5,8\},\{1,4,6,7\}$ | 2 | 2 |

Cada par contribuye $(2 + 2)\cdot 72 = 288$ números, así que:

$$N = 4 \times 288 = 1152$$

## Resultado

$$2025 - N = 2025 - 1152 = 873$$

$$\boxed{873}$$