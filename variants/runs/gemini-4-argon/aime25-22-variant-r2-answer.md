Para encontrar la probabilidad deseada, primero determinamos la factorización en números primos de $675$:
$$675 = 27 \times 25 = 3^3 \times 5^2$$

Cualquier divisor positivo $d \in S$ de $675$ tiene la forma $d = 3^a 5^b$, donde $a \in \{0, 1, 2, 3\}$ y $b \in \{0, 1, 2\}$. Por lo tanto, el número total de divisores en $S$ es:
$$|S| = (3 + 1)(2 + 1) = 4 \times 3 = 12$$

El número total de subconjuntos posibles $T \subseteq S$ es $2^{12}$.

Para que un subconjunto $T$ sea no vacío y el mínimo común múltiplo de sus elementos sea $675 = 3^3 \times 5^2$, el máximo exponente de $3$ entre los elementos de $T$ debe ser $3$, y el máximo exponente de $5$ entre los elementos de $T$ debe ser $2$. 

Definimos dos conjuntos dentro de $S$:
- Sea $A$ el conjunto de divisores en $S$ que son múltiplos de $3^3$: $A = \{3^3 5^0, 3^3 5^1, 3^3 5^2\}$, por lo que $|A| = 3$.
- Sea $B$ el conjunto de divisores en $S$ que son múltiplos de $5^2$: $B = \{3^0 5^2, 3^1 5^2, 3^2 5^2, 3^3 5^2\}$, por lo que $|B| = 4$.

La condición $\text{mcm}(T) = 675$ se cumple si y solo si $T \cap A \neq \emptyset$ y $T \cap B \neq \emptyset$ (lo cual garantiza automáticamente que $T$ sea no vacío).

Contamos el número de subconjuntos $T$ que **no** cumplen la condición usando el principio de inclusión-exclusión:
1. Subconjuntos donde $T \cap A = \emptyset$: estos son subconjuntos de $S \setminus A$. Como $|S \setminus A| = 12 - 3 = 9$, hay $2^9$ tales subconjuntos.
2. Subconjuntos donde $T \cap B = \emptyset$: estos son subconjuntos de $S \setminus B$. Como $|S \setminus B| = 12 - 4 = 8$, hay $2^8$ tales subconjuntos.
3. Subconjuntos donde $T \cap A = \emptyset$ y $T \cap B = \emptyset$: estos son subconjuntos de $S \setminus (A \cup B)$. Como $A \cap B = \{3^3 5^2\}$, tenemos $|A \cup B| = 3 + 4 - 1 = 6$, y por tanto $|S \setminus (A \cup B)| = 12 - 6 = 6$. Hay $2^6$ tales subconjuntos.

Así, el número de subconjuntos favorables es:
$$2^{12} - (2^9 + 2^8 - 2^6) = 2^6(2^6 - 2^3 - 2^2 + 1) = 2^6(64 - 8 - 4 + 1) = 53 \times 2^6$$

La probabilidad de elegir uno de estos subconjuntos al azar es:
$$\frac{53 \times 2^6}{2^{12}} = \frac{53}{2^6} = \frac{53}{64}$$

Como $53$ y $64$ son coprimos, tenemos $m = 53$ y $n = 64$. Por lo tanto, $m + n = 53 + 64 = 117$.

\boxed{117}