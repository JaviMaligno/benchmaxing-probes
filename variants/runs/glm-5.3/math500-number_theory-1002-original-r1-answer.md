# Resolución paso a paso

## Paso 1: Agrupar las dos congruencias iguales

Observo que $n \equiv 10 \pmod{11}$ y $n \equiv 10 \pmod{13}$. Como $\text{mcm}(11, 13) = 143$, tengo:

$$n \equiv 10 \pmod{143}$$

Es decir, $n = 143k + 10$ para algún entero $k \geq 0$.

## Paso 2: Aplicar la condición módulo 7

Sustituyo en $n \equiv 5 \pmod 7$:

$$143k + 10 \equiv 5 \pmod 7$$

Como $143 = 7 \cdot 20 + 3$, tengo $143 \equiv 3 \pmod 7$, y también $10 \equiv 3 \pmod 7$:

$$3k + 3 \equiv 5 \pmod 7 \implies 3k \equiv 2 \pmod 7$$

## Paso 3: Resolver para $k$

El inverso de $3$ módulo $7$ es $5$ (pues $3 \cdot 5 = 15 \equiv 1 \pmod 7$):

$$k \equiv 2 \cdot 5 = 10 \equiv 3 \pmod 7$$

Así que $k = 7m + 3$.

## Paso 4: Encontrar la forma general de $n$

$$n = 143(7m + 3) + 10 = 1001m + 429 + 10 = 1001m + 439$$

## Paso 5: Buscar el mayor $n < 2010$

$$1001m + 439 < 2010 \implies 1001m < 1571 \implies m \leq 1$$

Con $m = 1$: $\quad n = 1001 + 439 = 1440$

## Paso 6: Verificación

- $1440 = 7 \cdot 205 + 5$ → residuo $5$ ✓
- $1440 = 11 \cdot 130 + 10$ → residuo $10$ ✓
- $1440 = 13 \cdot 110 + 10$ → residuo $10$ ✓

$$\boxed{1440}$$