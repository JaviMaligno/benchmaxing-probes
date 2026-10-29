## Planteamiento

Sea $n$ el número de monedas en cada una de las 7 bolsas originales.

**Total tras encontrar la bolsa:** $7n + 53$

## Condición de divisibilidad

Para repartir todo en 8 bolsas iguales:

$$7n + 53 \equiv 0 \pmod 8$$

Como $7 \equiv -1 \pmod 8$ y $53 \equiv 5 \pmod 8$:

$$-n + 5 \equiv 0 \pmod 8 \quad\Longrightarrow\quad n \equiv 5 \pmod 8$$

Así que $n \in \{5, 13, 21, 29, 37, \dots\}$

## Condición del total

El total debe superar las 200 monedas: $7n + 53 > 200$, es decir $n > 21$.

Probamos los candidatos:

- $n = 21$: total $= 147 + 53 = 200$. Es divisible entre 8 ($200/8 = 25$), pero **no** es *más* de 200. Se descarta.
- $n = 29$: total $= 203 + 53 = 256$, y $256 / 8 = 32$ ✓, con $256 > 200$ ✓

## Verificación

Con $n = 29$: siete bolsas de 29 monedas dan **203 monedas**. Al sumar las 53 se obtienen 256, que se reparten en 8 bolsas de 32 monedas cada una. (También $203 > 200$, por lo que la respuesta no cambia si la condición se interpreta sobre el total inicial.)

\boxed{203}