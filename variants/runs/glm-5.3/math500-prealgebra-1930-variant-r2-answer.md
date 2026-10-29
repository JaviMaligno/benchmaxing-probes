# Resolución paso a paso

## Planteamiento

En un cuadrado mágico, todas las filas, columnas y diagonales principales suman lo mismo. Escribo las sumas de cada fila en función de $n$:

**Fila superior:**
$$(n+1) + 3 + (n-1) = 2n + 3$$

**Fila central:**
$$5 + (2n-11) + n = 3n - 6$$

**Fila inferior:**
$$(n-3) + (n+2) + 4 = 2n + 3$$

## Ecuación

Igualo la fila superior con la fila central, ya que deben tener la misma suma:

$$2n + 3 = 3n - 6$$

Resolviendo:

$$3 + 6 = 3n - 2n \implies n = 9$$

## Verificación con $n = 9$

El cuadrado queda:

| 10 | 3 | 8 |
|:--:|:-:|:-:|
| **5** | **7** | **9** |
| **6** | **11** | **4** |

- **Filas:** $10+3+8 = 21$, $\quad 5+7+9 = 21$, $\quad 6+11+4 = 21$ ✓
- **Columnas:** $10+5+6 = 21$, $\quad 3+7+11 = 21$, $\quad 8+9+4 = 21$ ✓
- **Diagonales:** $10+7+4 = 21$, $\quad 8+7+6 = 21$ ✓

Todas las sumas coinciden, así que el valor de $n$ es:

$$\boxed{9}$$