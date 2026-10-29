Queremos contar los pares de enteros $(a,b)$ con $\sqrt{a^2+b^2} \le 5$, es decir, $a^2+b^2 \le 25$.

Para cada valor de $a$ entre $-5$ y $5$, cuento los $b$ enteros con $b^2 \le 25 - a^2$:

- $a = 0$: $b^2 \le 25$, así que $b \in \{-5,\dots,5\}$: **11** valores.
- $a = \pm 1$: $b^2 \le 24$, así que $b \in \{-4,\dots,4\}$: 9 valores cada uno → **18**.
- $a = \pm 2$: $b^2 \le 21$, de nuevo $b \in \{-4,\dots,4\}$: **18**.
- $a = \pm 3$: $b^2 \le 16$, así que $b \in \{-4,\dots,4\}$: **18**.
- $a = \pm 4$: $b^2 \le 9$, así que $b \in \{-3,\dots,3\}$: 7 valores cada uno → **14**.
- $a = \pm 5$: $b^2 \le 0$, solo $b = 0$: **2**.

Sumando: $11 + 18 + 18 + 18 + 14 + 2 = 81$.

$$\boxed{81}$$