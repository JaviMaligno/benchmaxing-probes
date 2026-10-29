## Planteamiento

Sea $n$ el número de monedas en cada una de las nueve bolsas iniciales. Entonces:

- Monedas antes de encontrar la bolsa: $9n$
- Monedas después: $9n + 47$

## Condición de divisibilidad

Para repartir todo en diez bolsas iguales, se necesita que $10 \mid 9n + 47$:

$$9n + 47 \equiv 0 \pmod{10}$$
$$9n \equiv -47 \equiv 3 \pmod{10}$$

Como $9 \equiv -1 \pmod{10}$, esto da $-n \equiv 3$, es decir:

$$n \equiv 7 \pmod{10}$$

Así que $n \in \{7, 17, 27, 37, 47, \dots\}$.

## Condición del total

Se exige más de 300 monedas, así que $9n > 300$, o sea $n > 33{,}33$. El menor valor admisible es $n = 37$.

(La condición resulta igual de restrictiva si se interpreta sobre el total posterior: $9n + 47 > 300$ obliga a $n > 28{,}1$, y el candidato $n = 27$ da $243 + 47 = 290 < 300$, por lo que también queda descartado y se llega a $n = 37$.)

## Verificación

- Antes: $9 \times 37 = 333$ monedas, y $333 > 300$ ✓
- Después: $333 + 47 = 380$ monedas
- Reparto: $380 / 10 = 38$ monedas por bolsa ✓

\boxed{333}