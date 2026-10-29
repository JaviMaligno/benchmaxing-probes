Para resolver esto, primero factorizo $10!$ en primos:

$$10! = 2^8 \cdot 3^4 \cdot 5^2 \cdot 7$$

(Los exponentes: para el 2, $\lfloor 10/2\rfloor + \lfloor 10/4\rfloor + \lfloor 10/8\rfloor = 5+2+1 = 8$; para el 3, $3+1 = 4$; para el 5, $2$; para el 7, $1$.)

**Condición de positividad:** como $x^3$ debe ser positivo y el cubo conserva el signo, $x$ tiene que ser un entero positivo.

**Condición de divisibilidad:** si $x = 2^a \cdot 3^b \cdot 5^c \cdot 7^d$, entonces $x^3 = 2^{3a} \cdot 3^{3b} \cdot 5^{3c} \cdot 7^{3d}$ debe dividir a $10!$, lo que exige:

- $3a \le 8 \Rightarrow a \in \{0, 1, 2\}$ — 3 opciones
- $3b \le 4 \Rightarrow b \in \{0, 1\}$ — 2 opciones
- $3c \le 2 \Rightarrow c = 0$ — 1 opción
- $3d \le 1 \Rightarrow d = 0$ — 1 opción

El total de valores posibles es $3 \cdot 2 \cdot 1 \cdot 1 = 6$ (corresponden a $x \in \{1, 2, 3, 4, 6, 12\}$).

$$\boxed{6}$$