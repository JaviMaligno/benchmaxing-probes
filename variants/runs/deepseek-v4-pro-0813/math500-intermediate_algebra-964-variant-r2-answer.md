Voy a analizar la función recursiva paso a paso.

## Paso 1: Entender los casos base

Para $i=0$, la función es:
$$g(0,j) = \text{rem}_5(j+1)$$

Para $i \geq 1$:
- Si $j=0$: $g(i,0) = g(i-1,2)$
- Si $1 \leq j \leq 4$: $g(i,j) = g(i-1, g(i,j-1))$

## Paso 2: Calcular valores para $i=0$

| $j$ | $g(0,j)$ |
|-----|----------|
| 0   | $\text{rem}_5(1) = 1$ |
| 1   | $\text{rem}_5(2) = 2$ |
| 2   | $\text{rem}_5(3) = 3$ |
| 3   | $\text{rem}_5(4) = 4$ |
| 4   | $\text{rem}_5(5) = 0$ |

## Paso 3: Calcular valores para $i=1$

- $g(1,0) = g(0,2) = 3$
- $g(1,1) = g(0, g(1,0)) = g(0,3) = 4$
- $g(1,2) = g(0, g(1,1)) = g(0,4) = 0$
- $g(1,3) = g(0, g(1,2)) = g(0,0) = 1$
- $g(1,4) = g(0, g(1,3)) = g(0,1) = 2$

## Paso 4: Calcular valores para $i=2$

Comencemos con $g(2,0) = g(1,2) = 0$.

- $g(2,1) = g(1, g(2,0)) = g(1,0) = 3$
- $g(2,2) = g(1, g(2,1)) = g(1,3) = 1$
- $g(2,3) = g(1, g(2,2)) = g(1,1) = 4$
- $g(2,4) = g(1, g(2,3)) = g(1,4) = 2$

## Paso 5: Calcular valores para $i=3$

- $g(3,0) = g(2,2) = 1$
- $g(3,1) = g(2, g(3,0)) = g(2,1) = 3$
- $g(3,2) = g(2, g(3,1)) = g(2,3) = 4$
- $g(3,3) = g(2, g(3,2)) = g(2,4) = 2$
- $g(3,4) = g(2, g(3,3)) = g(2,2) = 1$

## Paso 6: Identificar un patrón

Observemos la fila $i$ como $(g(i,0), g(i,1), g(i,2), g(i,3), g(i,4))$:

- $i=0$: $(1, 2, 3, 4, 0)$
- $i=1$: $(3, 4, 0, 1, 2)$
- $i=2$: $(0, 3, 1, 4, 2)$
- $i=3$: $(1, 3, 4, 2, 1)$

Parece que hay una estructura, pero quizás es más útil buscar un ciclo.

## Paso 7: Continuar calculando para encontrar periodicidad

Calculemos con un programa mental más sistemático. La recursión para $i$ depende de la fila $i-1$ y de los valores previos en la fila $i$.

Continuemos:

**Fila $i=4$:**
- $g(4,0) = g(3,2) = 4$
- $g(4,1) = g(3, g(4,0)) = g(3,4) = 1$
- $g(4,2) = g(3, g(4,1)) = g(3,1) = 3$
- $g(4,3) = g(3, g(4,2)) = g(3,3) = 2$
- $g(4,4) = g(3, g(4,3)) = g(3,2) = 4$

**Fila $i=5$:**
- $g(5,0) = g(4,2) = 3$
- $g(5,1) = g(4, g(5,0)) = g(4,3) = 2$
- $g(5,2) = g(4, g(5,1)) = g(4,2) = 3$
- $g(5,3) = g(4, g(5,2)) = g(4,3) = 2$
- $g(5,4) = g(4, g(5,3)) = g(4,2) = 3$

**Fila $i=6$:**
- $g(6,0) = g(5,2) = 3$
- $g(6,1) = g(5, g(6,0)) = g(5,3) = 2$
- $g(6,2) = g(5, g(6,1)) = g(5,2) = 3$
- $g(6,3) = g(5, g(6,2)) = g(5,3) = 2$
- $g(6,4) = g(5, g(6,3)) = g(5,2) = 3$

¡Interesante! A partir de $i=5$, la fila es estable: $(3, 2, 3, 2, 3)$.

## Paso 8: Buscar periodicidad o estabilización

Parece que desde $i=5$ en adelante, la fila se repite: $(3, 2, 3, 2, 3)$.

Dado que $2024$ es muy grande, si la estabilización comienza en $i=5$, entonces $g(2024, 3) = 2$.

## Paso 9: Verificar la estabilización

Sea una fila $F = (3, 2, 3, 2, 3)$. Calculemos la siguiente fila:

- $g_{t+1}(0) = F(2) = 3$
- $g_{t+1}(1) = F(g_{t+1}(0)) = F(3) = 2$
- $g_{t+1}(2) = F(g_{t+1}(1)) = F(2) = 3$
- $g_{t+1}(3) = F(g_{t+1}(2)) = F(3) = 2$
- $g_{t+1}(4) = F(g_{t+1}(3)) = F(2) = 3$

La fila es punto fijo. Por lo tanto, para todo $i \geq 5$, $g(i,3) = 2$.

## Paso 10: Conclusión

Dado que $2024 \geq 5$, tenemos:
$$g(2024, 3) = 2$$

\boxed{2}