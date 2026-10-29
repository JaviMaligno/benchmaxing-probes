El problema es el clásico de la “araña y la polilla” en una habitación (caja). Hay que desdoblar (desarrollar) las caras por las que puede caminar la araña: paredes y techo, **sin** cruzar el suelo. La araña está sobre una pared lateral de 12′×9′ y la polilla sobre la pared lateral opuesta.

Ubico las coordenadas y luego desdoblo el recorrido mínimo.

**Sistema de coordenadas**

- Longitud de la habitación: 15′ (dirección “frente–fondo”).
- Anchura: 12′ (entre las dos paredes laterales).
- Altura: 9′.

La araña está en la pared lateral izquierda (por ejemplo), a 1′ del techo y 1′ de la pared trasera. La polilla está en la pared lateral derecha, a 1′ del suelo y 1′ de la pared frontal.

Por tanto:

- Araña: a 8′ del suelo (porque 9 − 1 = 8) y a 1′ de la pared trasera.
- Polilla: a 1′ del suelo y a 1′ de la pared frontal.

**Distancia más corta usando desdoblamiento**

El camino puede ir por las paredes y el techo. Conviene desdoblar una trayectoria que cruce el techo desde una pared lateral a la otra. Desplegamos las dos paredes laterales y el techo como una sola banda vertical de altura:

- pared lateral izquierda: 9′,
- techo: 12′ (la anchura del techo corresponde a la anchura de la habitación),
- pared lateral derecha: 9′.

Al desdoblar en línea recta (aplanando), las posiciones relevantes quedan así. Tomamos la coordenada horizontal total del desarrollo:

- ancho a lo largo del desarrollo: 12′ + 9′ + 9′ = 30′ (depende de cómo se pliegue; la coordenada útil es la suma de los tramos desde la araña hasta la polilla).

Una forma directa de calcularlo: al desdoblar las tres superficies, la separación horizontal entre araña y polilla es:

- De la araña (en pared izquierda) hasta el borde derecho de esa pared: 9′ horizontales en el desarrollo.
- A través del techo: 12′.
- Hasta la polilla (en pared derecha): 0′ (está en el borde correspondiente).

En realidad hay que tener cuidado con las posiciones en las paredes:

- La araña está a 1′ de la pared trasera, así que en la dirección “largo” (15′) su coordenada es 1′ desde atrás.
- La polilla está a 1′ de la pared frontal, así que en la dirección “largo” su coordenada es 14′ desde atrás.

Por tanto, la diferencia en la dirección del largo es:

$$14 - 1 = 13 \text{ pies}.$$

En la dirección del desarrollo (ancho + altura desplegada), la araña está a 8′ del suelo, y la polilla a 1′ del suelo. Al desdoblar las dos paredes laterales con el techo en medio, la separación “horizontal” del desarrollo entre ambos puntos es:

$$(9 - 8) + 12 + (9 - 1) = 1 + 12 + 8 = 21 \text{ pies}.$$

**Pitágoras**

$$d = \sqrt{13^2 + 21^2} = \sqrt{169 + 441} = \sqrt{610}.$$

**Forma radical simplificada**

$$610 = 2 \cdot 5 \cdot 61,$$

así que no se puede simplificar más:

$$\boxed{\sqrt{610}}$$