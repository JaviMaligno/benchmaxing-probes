Para resolver el problema paso a paso, primero hallamos la factorización en números primos de $675$:
$$675 = 27 \times 25 = 3^3 \times 5^2$$

Cualquier divisor positivo de $675$ tiene la forma $3^a 5^b$, donde $a \in \{0, 1, 2, 3\}$ y $b \in \{0, 1, 2\}$. Por lo tanto, el número total de elementos en el conjunto $S$ de divisores de $675$ es:
$$|S| = (3 + 1)(2 + 1) = 4 \times 3 = 12$$

El número total de subconjuntos $T \subseteq S$ posibles es $2^{12}$.

Para que un subconjunto no vacío $T \subseteq S$ tenga como mínimo común múltiplo ($\text{mcm}$) a $675 = 3^3 5^2$, el máximo exponente de $3$ entre los elementos de $T$ debe ser $3$, y el máximo exponente de $5$ entre los elementos de $T$ debe ser $2$. Es decir, $T$ debe cumplir simultáneamente dos condiciones:
1. Contener al menos un múltiplo de $3^3$.
2. Contener al menos un múltiplo de $5^2$.

(Nota: Si $T$ cumple ambas condiciones, automáticamente es no vacío).

Definamos dos subconjuntos dentro de $S$:
- Sea $A$ el conjunto de divisores en $S$ que son múltiplos de $3^3$:
  $$A = \{3^3 5^0, 3^3 5^1, 3^3 5^2\} \implies |A| = 3$$
- Sea $B$ el conjunto de divisores en $S$ que son múltiplos de $5^2$:
  $$B = \{3^0 5^2, 3^1 5^2, 3^2 5^2, 3^3 5^2\} \implies |B| = 4$$

Observamos que la intersección de ambos conjuntos es $A \cap B = \{3^3 5^2\} = \{675\}$, por lo que $|A \cap B| = 1$. Entonces, por el principio de inclusión-exclusión, el tamaño de su unión es:
$$|A \cup B| = |A| + |B| - |A \cap B| = 3 + 4 - 1 = 6$$

Buscamos el número de subconjuntos $T \subseteq S$ tales que $T \cap A \neq \emptyset$ y $T \cap B \neq \emptyset$. Aplicando nuevamente el principio de inclusión-exclusión sobre todos los $2^{12}$ subconjuntos de $S$:
- El número de subconjuntos que no contienen elementos de $A$ ($T \cap A = \emptyset$) es $2^{12 - |A|} = 2^{12 - 3} = 2^9$.
- El número de subconjuntos que no contienen elementos de $B$ ($T \cap B = \emptyset$) es $2^{12 - |B|} = 2^{12 - 4} = 2^8$.
- El número de subconjuntos que no contienen elementos ni de $A$ ni de $B$ ($T \cap (A \cup B) = \emptyset$) es $2^{12 - |A \cup B|} = 2^{12 - 6} = 2^6$.

Por lo tanto, el número de subconjuntos $T$ válidos es:
$$N = 2^{12} - 2^9 - 2^8 + 2^6$$

Factorizando $2^6$:
$$N = 2^6(2^6 - 2^3 - 2^2 + 1) = 2^6(64 - 8 - 4 + 1) = 2^6 \times 53$$

La probabilidad de elegir uno de estos subconjuntos al azar es:
$$\frac{m}{n} = \frac{2^6 \times 53}{2^{12}} = \frac{53}{2^6} = \frac{53}{64}$$

Como $53$ es primo y $64 = 2^6$, los enteros positivos $m = 53$ y $n = 64$ son coprimos. Finalmente, calculamos $m + n$:
$$m + n = 53 + 64 = 117$$

\boxed{117}