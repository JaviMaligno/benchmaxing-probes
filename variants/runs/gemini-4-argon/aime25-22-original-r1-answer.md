Para hallar la probabilidad deseada, primero determinamos la factorización en números primos de $2025$:
$$2025 = 45^2 = (3^2 \times 5)^2 = 3^4 \times 5^2$$

Cualquier divisor entero positivo de $2025$ es de la forma $3^a \times 5^b$, donde $a \in \{0, 1, 2, 3, 4\}$ y $b \in \{0, 1, 2\}$. Por lo tanto, el número total de divisores en el conjunto $A$ es:
$$|A| = (4 + 1)(2 + 1) = 5 \times 3 = 15$$

El número total de subconjuntos posibles $B \subseteq A$ es $2^{15}$.

Para que un subconjunto no vacío $B$ tenga como mínimo común múltiplo a $2025 = 3^4 \times 5^2$, debe cumplir dos condiciones simultáneamente:
1. $B$ debe contener al menos un elemento que sea múltiplo de $3^4$ (es decir, con $a = 4$).
2. $B$ debe contener al menos un elemento que sea múltiplo de $5^2$ (es decir, con $b = 2$).

(Notemos que si $B$ cumple ambas condiciones, automáticamente es no vacío).

Contemos cuántos elementos de $A$ cumplen estas propiedades:
- **Múltiplos de $3^4$:** Son de la forma $3^4 \times 5^b$ con $b \in \{0, 1, 2\}$, por lo que hay $3$ elementos.
- **Múltiplos de $5^2$:** Son de la forma $3^a \times 5^2$ con $a \in \{0, 1, 2, 3, 4\}$, por lo que hay $5$ elementos.
- **Múltiplos tanto de $3^4$ como de $5^2$:** Solo existe $1$ elemento, que es el propio $3^4 \times 5^2 = 2025$.

Definamos los eventos complementarios para un subconjunto $B$:
- Sea $E_1$ la propiedad de que $B$ **no** contiene ningún múltiplo de $3^4$. Como hay $15 - 3 = 12$ elementos restantes, existen $|E_1| = 2^{12}$ subconjuntos de este tipo.
- Sea $E_2$ la propiedad de que $B$ **no** contiene ningún múltiplo de $5^2$. Como hay $15 - 5 = 10$ elementos restantes, existen $|E_2| = 2^{10}$ subconjuntos de este tipo.
- La intersección $E_1 \cap E_2$ corresponde a los subconjuntos que no contienen ni múltiplos de $3^4$ ni múltiplos de $5^2$. El número de elementos prohibidos es $3 + 5 - 1 = 7$, dejando $15 - 7 = 8$ elementos posibles. Por tanto, $|E_1 \cap E_2| = 2^8$.

Por el Principio de Inclusión-Exclusión, el número de subconjuntos $B$ cuyo mínimo común múltiplo es $2025$ es:
$$N = 2^{15} - |E_1| - |E_2| + |E_1 \cap E_2| = 2^{15} - 2^{12} - 2^{10} + 2^8$$

La probabilidad buscada es:
$$P = \frac{2^{15} - 2^{12} - 2^{10} + 2^8}{2^{15}}$$

Dividiendo el numerador y el denominador entre $2^8$, obtenemos:
$$P = \frac{2^7 - 2^4 - 2^2 + 1}{2^7} = \frac{128 - 16 - 4 + 1}{128} = \frac{109}{128}$$

Dado que $128 = 2^7$ y $109$ es impar, $m = 109$ y $n = 128$ son primos relativos. Finalmente, calculamos $m + n$:
$$m + n = 109 + 128 = 237$$

\boxed{237}