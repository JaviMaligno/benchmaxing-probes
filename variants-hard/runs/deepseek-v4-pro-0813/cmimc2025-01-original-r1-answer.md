Vamos a razonar paso a paso.

**1. Velocidades iniciales**

- Alice: 8 mph
- Bob: 4 mph
- Charlie: 2 mph
- Dave: inicialmente la mitad de Charlie, es decir, 1 mph.

**2. Tiempos de llegada de los otros corredores**

La carrera es de 1 milla, así que el tiempo de cada corredor es $1 / \text{velocidad}$.

- Alice: $1/8$ h = $0{,}125$ h
- Bob: $1/4$ h = $0{,}25$ h
- Charlie: $1/2$ h = $0{,}5$ h

**3. Efecto del superpoder de Dave**

Cada vez que un corredor termina, Dave duplica su velocidad. Los momentos en que esto ocurre son:

- En $t = 1/8$ h termina Alice → Dave pasa de 1 mph a 2 mph.
- En $t = 1/4$ h termina Bob → Dave pasa de 2 mph a 4 mph.
- En $t = 1/2$ h termina Charlie → Dave pasa de 4 mph a 8 mph.

**4. Distancia recorrida por Dave**

- De $t = 0$ a $t = 1/8$ h, a 1 mph:
  distancia $= 1 \cdot \frac18 = \frac18$ milla.

- De $t = 1/8$ a $t = 1/4$ h, a 2 mph:
  intervalo $= \frac14 - \frac18 = \frac18$ h,
  distancia $= 2 \cdot \frac18 = \frac14$ milla.

- De $t = 1/4$ a $t = 1/2$ h, a 4 mph:
  intervalo $= \frac12 - \frac14 = \frac14$ h,
  distancia $= 4 \cdot \frac14 = 1$ milla.

Distancia total hasta $t = 1/2$ h:

$$
\frac18 + \frac14 + 1 = \frac18 + \frac28 + \frac88 = \frac{11}{8} \text{ millas}.
$$

Dave ya ha superado la milla antes de que Charlie termine. Veamos cuándo exactamente.

**5. Momento en que Dave completa la milla**

Después de $t = 1/4$ h, Dave va a 4 mph y le falta:

$$
1 - \left(\frac18 + \frac14\right) = 1 - \frac38 = \frac58 \text{ milla}.
$$

A 4 mph, el tiempo adicional es:

$$
\frac{5/8}{4} = \frac{5}{32} \text{ h}.
$$

Entonces el tiempo total es:

$$
\frac14 + \frac{5}{32} = \frac{8}{32} + \frac{5}{32} = \frac{13}{32} \text{ h}.
$$

Verificamos que $\frac{13}{32} \approx 0{,}40625$ h, que es menor que $0{,}5$ h, así que Charlie aún no ha terminado y no hay más duplicaciones antes de que Dave cruce la meta.

**Respuesta final:**

$$
\boxed{\frac{13}{32}}
$$