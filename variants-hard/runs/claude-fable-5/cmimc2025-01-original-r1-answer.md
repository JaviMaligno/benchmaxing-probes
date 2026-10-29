Primero establezco las velocidades y los momentos clave:

- Alice: 8 mph → termina 1 milla en **1/8 h**.
- Bob: 4 mph → termina en **1/4 h**.
- Charlie: 2 mph → terminaría en 1/2 h.
- Dave: empieza a la mitad de la velocidad de Charlie, es decir, **1 mph**, y duplica su velocidad cada vez que alguien termina.

Ahora sigo el progreso de Dave por tramos:

**Tramo 1** (de $t=0$ a $t=1/8$, velocidad 1 mph):
$$d_1 = 1 \cdot \tfrac{1}{8} = \tfrac{1}{8} \text{ mi}$$

Alice termina en $t = 1/8$, así que Dave pasa a 2 mph.

**Tramo 2** (de $t=1/8$ a $t=1/4$, velocidad 2 mph):
$$d_2 = 2 \cdot \tfrac{1}{8} = \tfrac{1}{4} \text{ mi} \quad\Rightarrow\quad \text{total} = \tfrac{1}{8} + \tfrac{1}{4} = \tfrac{3}{8} \text{ mi}$$

Bob termina en $t = 1/4$, así que Dave pasa a 4 mph.

**Tramo 3** (velocidad 4 mph): a Dave le faltan $1 - \tfrac{3}{8} = \tfrac{5}{8}$ millas. A 4 mph tardaría:
$$\frac{5/8}{4} = \frac{5}{32} \text{ h}$$

Hay que verificar que Dave termina antes de que Charlie (quien acabaría en $t = 1/2 = 16/32$ h) provoque otra duplicación. Dave terminaría en:
$$t = \frac{1}{4} + \frac{5}{32} = \frac{8}{32} + \frac{5}{32} = \frac{13}{32} \text{ h}$$

Como $\tfrac{13}{32} < \tfrac{16}{32}$, Dave efectivamente cruza la meta antes que Charlie, y no hay más duplicaciones que considerar.

$$\boxed{\dfrac{13}{32}}$$