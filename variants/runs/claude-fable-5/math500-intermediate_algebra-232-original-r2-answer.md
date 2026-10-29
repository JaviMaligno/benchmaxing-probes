Queremos contar los pares ordenados de enteros $(a,b)$ tales que $|a+bi| \le 5$, es decir, $\sqrt{a^2+b^2} \le 5$, lo que equivale a $a^2 + b^2 \le 25$.

Contamos, para cada valor entero de $a$ con $-5 \le a \le 5$, cuántos enteros $b$ cumplen $b^2 \le 25 - a^2$:

- $a = 0$: $b^2 \le 25$, así que $b \in \{-5,\dots,5\}$: **11** valores.
- $a = \pm 1$: $b^2 \le 24$, así que $b \in \{-4,\dots,4\}$: **9** valores cada uno.
- $a = \pm 2$: $b^2 \le 21$: $b \in \{-4,\dots,4\}$: **9** valores cada uno.
- $a = \pm 3$: $b^2 \le 16$: $b \in \{-4,\dots,4\}$: **9** valores cada uno.
- $a = \pm 4$: $b^2 \le 9$: $b \in \{-3,\dots,3\}$: **7** valores cada uno.
- $a = \pm 5$: $b^2 \le 0$: solo $b = 0$: **1** valor cada uno.

Sumando:
$$11 + 2(9 + 9 + 9 + 7 + 1) = 11 + 2 \cdot 35 = 11 + 70 = 81.$$

$$\boxed{81}$$