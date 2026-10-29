## Planteamiento

Sea $n$ el número de monedas por bolsa en las nueve bolsas iniciales.

**Total inicial:** $9n$
**Total después de encontrar la bolsa:** $9n + 47$

## Condición de divisibilidad

Para repartir todo en diez bolsas iguales, $10 \mid 9n + 47$:

$$9n + 47 \equiv 0 \pmod{10} \;\Longrightarrow\; 9n \equiv -47 \equiv 3 \pmod{10}$$

Como $9 \equiv -1 \pmod{10}$:

$$-n \equiv 3 \pmod{10} \;\Longrightarrow\; n \equiv 7 \pmod{10}$$

Es decir, $n$ debe terminar en 7: $n \in \{7, 17, 27, 37, \dots\}$

## Condición de tamaño

Con más de 300 monedas: $9n > 300 \Rightarrow n > 33{,}33$

El menor valor admisible es $n = 37$.

## Verificación

- Antes: $9 \times 37 = 333$ monedas (y $333 > 300$ ✓)
- Después: $333 + 47 = 380$
- Reparto: $380 / 10 = 38$ monedas por bolsa ✓

(El candidato anterior, $n = 27$, da $243$ monedas, que no supera 300 — y tampoco lo haría el total de $290$ tras añadir la bolsa.)

\boxed{333}