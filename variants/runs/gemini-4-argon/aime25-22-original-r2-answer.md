Para resolver el problema paso a paso, primero hallamos la factorización en números primos de $2025$:
$$2025 = 45^2 = (3^2 \cdot 5)^2 = 3^4 \cdot 5^2$$

El conjunto $A$ de los divisores enteros positivos de $2025$ está formado por todos los números de la forma $3^a \cdot 5^b$, donde $a \in \{0, 1, 2, 3, 4\}$ y $b \in \{0, 1, 2\}$. Por lo tanto, el número total de elementos en $A$ es:
$$|A| = (4 + 1)(2 + 1) = 5 \times 3 = 15$$

Elegir un subconjunto $B \subseteq A$ de manera uniforme y aleatoria equivale a decidir, de forma independiente y con probabilidad $\frac{1}{2}$ para cada elemento de $A$, si dicho elemento pertenece o no a $B$.

Para que $B$ sea no vacío y el mínimo común múltiplo de sus elementos sea $2025 = 3^4 \cdot 5^2$, deben cumplirse simultáneamente dos condiciones:
1. $B$ debe contener al menos un múltiplo de $3^4$ (es decir, un elemento con $a = 4$).
2. $B$ debe contener al menos un múltiplo de $5^2$ (es decir, un elemento con $b = 2$).

*(Nota: si se cumplen ambas condiciones, $B$ es automáticamente no vacío).*

Definamos los siguientes subconjuntos de $A$:
- $E_1 = \{3^4 \cdot 5^0, 3^4 \cdot 5^1, 3^4 \cdot 5^2\}$, que tiene $|E_1| = 3$ elementos.
- $E_2 = \{3^0 \cdot 5^2, 3^1 \cdot 5^2, 3^2 \cdot 5^2, 3^3 \cdot 5^2, 3^4 \cdot 5^2\}$, que tiene $|E_2| = 5$ elementos.

Observamos que $E_1 \cap E_2 = \{3^4 \cdot 5^2\} = \{2025\}$, por lo que $|E_1 \cup E_2| = 3 + 5 - 1 = 7$.

Queremos calcular la probabilidad de que $B \cap E_1 \neq \emptyset$ y $B \cap E_2 \neq \emptyset$. Aplicando el principio de inclusión-exclusión con los eventos complementarios:
- La probabilidad de que $B \cap E_1 = \emptyset$ es $\left(\frac{1}{2}\right)^3 = \frac{1}{8}$.
- La probabilidad de que $B \cap E_2 = \emptyset$ es $\left(\frac{1}{2}\right)^5 = \frac{1}{32}$.
- La probabilidad de que $B \cap E_1 = \emptyset$ y $B \cap E_2 = \emptyset$ (es decir, $B \cap (E_1 \cup E_2) = \emptyset$) es $\left(\frac{1}{2}\right)^7 = \frac{1}{128}$.

Por lo tanto, la probabilidad buscada es:
$$P(B \cap E_1 \neq \emptyset \text{ y } B \cap E_2 \neq \emptyset) = 1 - \left(\frac{1}{8} + \frac{1}{32} - \frac{1}{128}\right) = 1 - \frac{16 + 4 - 1}{128} = 1 - \frac{19}{128} = \frac{109}{128}$$

Como $109$ y $128 = 2^7$ son primos relativos, tenemos $m = 109$ y $n = 128$. Finalmente, calculamos $m + n$:
$$m + n = 109 + 128 = 237$$

\boxed{237}