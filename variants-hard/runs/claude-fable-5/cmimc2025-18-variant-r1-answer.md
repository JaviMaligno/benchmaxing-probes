**Respuesta: 1680.**

Razonamiento:

**Cota inferior.** Un 6720-ágono regular es un zonógono: sus lados vienen en 3360 direcciones distintas (cada dirección aparece en un par de lados opuestos). En cualquier disección en paralelogramos funciona el argumento de las "cintas" (líneas de de Bruijn): cada lado del polígono inicia una cinta de paralelogramos que tienen un par de lados paralelos a ese lado, y la cinta debe cruzar el polígono hasta terminar en el lado opuesto. Cuando una cinta de dirección $u$ cruza una cinta de dirección $v$, el cruce es un paralelogramo con lados en las direcciones $u$ y $v$.

Como $6720 \equiv 0 \pmod 4$, para cada dirección de lado existe otra dirección de lado exactamente perpendicular a ella: las 3360 direcciones se agrupan en $3360/2 = 1680$ pares perpendiculares. Para cada par perpendicular $(u, v)$, toda cinta de dirección $u$ debe cruzar toda cinta de dirección $v$ (una separa los dos lados opuestos de dirección $u$, la otra los de dirección $v$, y sus extremos se alternan en el borde), y ese cruce es un paralelogramo con lados perpendiculares, es decir, un **rectángulo**. Por lo tanto hay al menos un rectángulo por cada uno de los 1680 pares, o sea $R \ge 1680$.

**Construcción.** La cota se alcanza: un $4n$-ágono regular puede disecarse en paralelogramos de modo que cada par de direcciones perpendiculares aporte exactamente un rectángulo (la disección estándar de un zonógono en $\binom{2n}{2}$ paralelogramos, uno por cada par de direcciones, usa exactamente un paralelogramo por par, y solo los $n$ pares perpendiculares dan rectángulos). Con $n = 1680$ se consiguen exactamente 1680 rectángulos.

$$\boxed{1680}$$