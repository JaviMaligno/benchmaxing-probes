Esta es una pregunta puramente matemática, así que la resuelvo directamente.

**Reescritura de la suma.** Como $j + 0.5 = \frac{2j+1}{2}$, cada término es

$$\left\lfloor \frac{2025}{j+0.5} \right\rfloor = \left\lfloor \frac{4050}{2j+1} \right\rfloor.$$

Cuando $j$ recorre $-1000, \dots, 1000$, el número $k = 2j+1$ recorre todos los impares desde $-1999$ hasta $2001$. La suma es entonces

$$S = \sum_{\substack{k \text{ impar} \\ -1999 \le k \le 2001}} \left\lfloor \frac{4050}{k} \right\rfloor.$$

**Emparejamiento $k \leftrightarrow -k$.** Para cada impar $k$ con $1 \le k \le 1999$, emparejo el término de $k$ con el de $-k$. Se usa la identidad:

$$\lfloor x \rfloor + \lfloor -x \rfloor = \begin{cases} 0 & \text{si } x \in \mathbb{Z}, \\ -1 & \text{si } x \notin \mathbb{Z}. \end{cases}$$

Así que cada par contribuye $-1$, salvo cuando $k \mid 4050$, en cuyo caso contribuye $0$.

**Divisores impares de 4050.** Como $4050 = 2 \cdot 3^4 \cdot 5^2$, sus divisores impares son los divisores de $2025 = 3^4 \cdot 5^2$:

$$1, 3, 5, 9, 15, 25, 27, 45, 75, 81, 135, 225, 405, 675, 2025.$$

Son 15 en total, pero $2025 > 1999$, así que dentro del rango de emparejamiento hay **14** divisores.

**Suma de los pares.** Hay 1000 impares entre 1 y 1999, luego 1000 pares. De ellos, $1000 - 14 = 986$ contribuyen $-1$ cada uno, y 14 contribuyen $0$:

$$\text{pares} = -986.$$

**Término sin pareja.** Queda $k = 2001$ (correspondiente a $j = 1000$), cuyo opuesto $-2001$ no está en el rango:

$$\left\lfloor \frac{4050}{2001} \right\rfloor = 2.$$

**Total.**

$$S = -986 + 2 = -984.$$

$$\boxed{-984}$$