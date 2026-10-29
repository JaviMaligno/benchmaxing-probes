## Solución

**Planteamiento.** Sea $h$ la altura de la cueva. Colocamos coordenadas con el suelo en $y=0$. Las puntas de las cuatro estructuras están a las alturas:

- Estalactitas (desde el techo): $y = h-16$ y $y = h-36$
- Estalagmitas (desde el suelo): $y = 25$ y $y = 49$

**Usando las diagonales del cuadrado.** En un cuadrado, las diagonales se bisecan mutuamente, así que los dos pares de vértices opuestos comparten el mismo punto medio, en particular la misma coordenada $y$ media. Probamos el emparejamiento donde las dos puntas del techo son vértices opuestos entre sí:

$$\frac{(h-16)+(h-36)}{2} = \frac{25+49}{2} \implies h - 26 = 37 \implies h = 63.$$

**Verificación.** Con $h = 63$, las alturas de las puntas son $47, 27, 25, 49$. Las diagonales serían:

- Diagonal 1: entre puntos de alturas $47$ y $27$, con vector $(p, -20)$
- Diagonal 2: entre puntos de alturas $25$ y $49$, con vector $(q, 24)$

Para que formen un cuadrado, las diagonales deben ser perpendiculares y de igual longitud:

$$pq = 480 \quad\text{(perpendicularidad: } pq - 20\cdot 24 = 0\text{)}$$
$$p^2 + 400 = q^2 + 576 \implies p^2 - q^2 = 176$$

Sustituyendo $q = 480/p$: $p^4 - 176p^2 - 230400 = 0$, cuya solución es $p^2 = \frac{176 + \sqrt{30976 + 921600}}{2} = \frac{176 + 976}{2} = 576$, es decir $p = 24$ y $q = 20$.

Ambas diagonales miden $\sqrt{576 + 400} = \sqrt{976}$, son iguales y perpendiculares, y se bisecan (podemos centrarlas en el mismo punto eligiendo las coordenadas horizontales). Por tanto el cuadrado existe.

(Los otros emparejamientos de diagonales llevan a contradicciones: por ejemplo, exigirían que una diagonal vertical de longitud distinta coincidiera, o dan $h$ que no permite diagonales iguales y perpendiculares.)

$$\boxed{63}$$