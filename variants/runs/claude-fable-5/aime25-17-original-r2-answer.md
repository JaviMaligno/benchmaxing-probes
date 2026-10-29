Trabajando módulo $n+2$: como $n \equiv -2 \pmod{n+2}$, tenemos:

- $n+3 \equiv 1 \pmod{n+2}$
- $n^2+9 \equiv (-2)^2+9 = 13 \pmod{n+2}$

Por lo tanto, $3(n+3)(n^2+9) \equiv 3 \cdot 1 \cdot 13 = 39 \pmod{n+2}$.

Así que $n+2$ debe dividir a $39$. Los divisores de $39$ son $1, 3, 13, 39$. Como $n$ es un entero positivo, $n+2 \geq 3$, de modo que $n+2 \in \{3, 13, 39\}$, es decir, $n \in \{1, 11, 37\}$.

Verificación rápida:
- $n=1$: $3 \mid 3\cdot 4\cdot 10 = 120$ ✓
- $n=11$: $13 \mid 3\cdot 14\cdot 130$ ✓
- $n=37$: $39 \mid 3\cdot 40\cdot 1378$ (pues $3\mid 3$ y $13\mid 1378 = 13\cdot 106$) ✓

La suma es $1 + 11 + 37 = 49$.

$\boxed{49}$