**Respuesta: 139**

**Razonamiento:**

La condición "ningún invitado está sentado junto a otros dos invitados" significa que ningún asiento ocupado puede tener ambos vecinos ocupados. Eso equivale a prohibir **tres asientos ocupados consecutivos**: los bloques de asientos ocupados solo pueden tener tamaño 1 o 2.

Con 9 ocupados y 8 vacíos, descompongo los 9 ocupados en bloques de tamaño 1 o 2. Si hay $t$ bloques de tamaño 2 y $s$ de tamaño 1, entonces $s + 2t = 9$ y el total de bloques es $b = s + t = 9 - t$, con $t = 0, 1, 2, 3, 4$.

Los 8 asientos vacíos crean 9 huecos (incluyendo los extremos) donde colocar los bloques, de modo que queden separados. Las formas de hacerlo son $\binom{9}{b}$, y las formas de elegir cuáles bloques son dobles son $\binom{b}{t}$:

| $t$ | $b = 9-t$ | $\binom{9}{b}\binom{b}{t}$ |
|---|---|---|
| 0 | 9 | $\binom{9}{9}\binom{9}{0} = 1$ |
| 1 | 8 | $\binom{9}{8}\binom{8}{1} = 72$ |
| 2 | 7 | $\binom{9}{7}\binom{7}{2} = 756$ |
| 3 | 6 | $\binom{9}{6}\binom{6}{3} = 1680$ |
| 4 | 5 | $\binom{9}{5}\binom{5}{4} = 630$ |

Sumando: $1 + 72 + 756 + 1680 + 630 = 3139$.

Por lo tanto $N = 3139$ y el residuo módulo 1000 es:

$$\boxed{139}$$