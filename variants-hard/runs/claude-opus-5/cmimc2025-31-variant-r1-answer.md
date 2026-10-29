## Planteamiento

Sea $m$ el mes y $d$ el día. El número formado es:
- $N = 10m + d$ si $d$ tiene una cifra,
- $N = 100m + d$ si $d$ tiene dos cifras.

Como $m$ divide a $10m$ y a $100m$, la condición $m \mid N$ equivale siempre a $m \mid d$.

La condición $d \mid N$ equivale a $d \mid 10m$ (día de una cifra) o $d \mid 100m$ (día de dos cifras).

## Junio ($m=6$, días 1–30)

- Una cifra: $6 \mid d \Rightarrow d=6$. Y $6 \mid 60$. ✓ **6 de junio**
- Dos cifras: $d \in \{12, 18, 24, 30\}$, hace falta $d \mid 600$:
  - $600/12 = 50$ ✓, $600/18$ no es entero ✗, $600/24 = 25$ ✓, $600/30 = 20$ ✓

Junio: 6, 12, 24, 30 → **4**

## Julio ($m=7$, días 1–31)

- Una cifra: $d=7$, y $7 \mid 70$. ✓
- Dos cifras: $d \in \{14, 21, 28\}$, hace falta $d \mid 700$:
  - $700/14 = 50$ ✓, $700/21$ no es entero ✗, $700/28 = 25$ ✓

Julio: 7, 14, 28 → **3**

## Agosto ($m=8$, días 1–31)

- Una cifra: $d=8$, y $8 \mid 80$. ✓
- Dos cifras: $d \in \{16, 24\}$, hace falta $d \mid 800$:
  - $800/16 = 50$ ✓, $800/24$ no es entero ✗

Agosto: 8, 16 → **2**

## Total

$4 + 3 + 2 = 9$

\boxed{9}