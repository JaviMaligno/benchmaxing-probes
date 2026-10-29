## Razonamiento paso a paso

**Paso 1: Expreso la suma de cada fila.**

- Fila superior: $(n+1) + 3 + (n-1) = 2n + 3$
- Fila del medio: $5 + (2n-11) + n = 3n - 6$
- Fila inferior: $(n-3) + (n+2) + 4 = 2n + 3$

**Paso 2: Igualo las sumas (todas deben coincidir).**

Las filas superior e inferior ya coinciden ($2n+3$). Igualo con la fila del medio:

$$2n + 3 = 3n - 6$$
$$9 = n$$

**Paso 3: Verifico con $n = 9$.**

El cuadrado queda:

$$\begin{matrix} 10 & 3 & 8 \\ 5 & 7 & 9 \\ 6 & 11 & 4 \end{matrix}$$

- Filas: $21$, $21$, $21$ ✓
- Columnas: $10+5+6=21$, $\ 3+7+11=21$, $\ 8+9+4=21$ ✓
- Diagonal principal: $10+7+4=21$ ✓
- Diagonal secundaria: $8+7+6=21$ ✓

Todas las condiciones del cuadrado mágico se cumplen.

$$\boxed{9}$$