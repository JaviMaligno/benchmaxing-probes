# Solución paso a paso

**Tiempos de llegada de los otros corredores:**
- Alice (8 mph): $t = 1/8$ h
- Bob (4 mph): $t = 1/4$ h
- Charlie (2 mph): $t = 1/2$ h

**Dave** empieza a la mitad de la velocidad de Charlie: $1$ mph, y duplica su velocidad cada vez que alguien termina.

**Distancia recorrida por Dave por tramos:**

1. **De $t=0$ a $t=1/8$** (llega Alice), a $1$ mph:
$$d_1 = 1 \cdot \frac{1}{8} = \frac{1}{8} \text{ milla}$$
Dave duplica a $2$ mph.

2. **De $t=1/8$ a $t=1/4$** (llega Bob), a $2$ mph:
$$d_2 = 2 \cdot \frac{1}{8} = \frac{1}{4} \text{ milla}$$
Total hasta aquí: $\frac{1}{8} + \frac{1}{4} = \frac{3}{8}$ millas. Dave duplica a $4$ mph.

3. **Tramo final:** le faltan $1 - \frac{3}{8} = \frac{5}{8}$ millas a $4$ mph:
$$t_{\text{final}} = \frac{5/8}{4} = \frac{5}{32} \text{ h}$$

**Verificación:** Dave termina en $\frac{1}{4} + \frac{5}{32} = \frac{13}{32} \approx 0.406$ h, antes de que Charlie termine ($1/2$ h), así que no hay más duplicaciones que considerar.

**Tiempo total:**
$$\frac{1}{8} + \frac{1}{4} + \frac{5}{32} = \frac{4 + 8 + 5}{32} = \frac{13}{32} \text{ horas}$$

\boxed{\dfrac{13}{32}}