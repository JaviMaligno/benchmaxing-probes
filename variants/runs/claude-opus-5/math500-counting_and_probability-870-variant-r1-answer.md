## Planteamiento

Lo único que importa es el **orden cíclico** de los seis puntos en la circunferencia, junto con el emparejamiento inducido: los puntos se agrupan en las parejas $\{P,Q\}$, $\{R,S\}$, $\{T,U\}$.

Dos cuerdas se cortan **si y solo si** sus extremos se alternan alrededor del círculo (cada cuerda separa los dos extremos de la otra).

## Conteo

Etiquetemos las posiciones según el orden cíclico como $1,2,3,4,5,6$. Por simetría, las tres parejas se distribuyen entre estas posiciones de manera uniforme: el número de formas de partir 6 posiciones en 3 parejas (sin orden) es

$$\frac{6!}{2^3\cdot 3!}=15,$$

y los 15 emparejamientos son equiprobables.

Ahora: ¿cuántos de esos 15 tienen las tres cuerdas cortándose dos a dos? Si una cuerda une las posiciones $1$ y $k$, para que las otras dos cuerdas la crucen ambas deben tener un extremo en cada uno de los arcos que determina, es decir cada arco debe contener exactamente 2 puntos, lo que fuerza $k=4$. Quedan las posiciones $\{2,3\}$ y $\{5,6\}$, y las dos cuerdas restantes deben además cruzarse entre sí, lo que obliga a $2\!-\!5$ y $3\!-\!6$.

Por tanto hay **un único** emparejamiento válido:

$$1\!-\!4,\qquad 2\!-\!5,\qquad 3\!-\!6,$$

el patrón "alternado" en el que cada cuerda es una especie de diámetro combinatorio.

## Probabilidad

$$\frac{1}{15}$$

\boxed{\dfrac{1}{15}}