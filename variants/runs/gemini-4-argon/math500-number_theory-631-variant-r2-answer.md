Para determinar después de cuántos segundos ambos puntos volverán a apuntar hacia arriba al mismo tiempo, debemos calcular el tiempo que tarda cada rueda en dar una vuelta completa (su período) en segundos y luego hallar el mínimo común múltiplo de ambos tiempos.

**Paso 1: Calcular el período de la primera rueda en segundos.**
La primera rueda da $37\frac{1}{2} = \frac{75}{2}$ vueltas por minuto (60 segundos).
Su velocidad en vueltas por segundo es:
$$\frac{75/2\text{ vueltas}}{60\text{ segundos}} = \frac{75}{120} = \frac{5}{8}\text{ vueltas por segundo}$$

Por lo tanto, el tiempo que tarda en dar una vuelta completa es el inverso de esta fracción:
$$T_1 = \frac{8}{5}\text{ segundos}$$

**Paso 2: Calcular el período de la segunda rueda en segundos.**
La segunda rueda da $54$ vueltas por minuto (60 segundos).
Su velocidad en vueltas por segundo es:
$$\frac{54\text{ vueltas}}{60\text{ segundos}} = \frac{9}{10}\text{ vueltas por segundo}$$

Por lo tanto, el tiempo que tarda en dar una vuelta completa es:
$$T_2 = \frac{10}{9}\text{ segundos}$$

**Paso 3: Encontrar el mínimo común múltiplo (MCM) de ambos períodos.**
Para que ambos puntos apunten hacia arriba al mismo tiempo, el tiempo transcurrido $t$ debe ser un múltiplo entero tanto de $T_1$ como de $T_2$. El mínimo común múltiplo de dos fracciones irreducibles $\frac{a}{b}$ y $\frac{c}{d}$ se calcula como:
$$\text{MCM}\left(\frac{a}{b}, \frac{c}{d}\right) = \frac{\text{MCM}(a, c)}{\text{MCD}(b, d)}$$

Sustituyendo nuestros valores:
- $\text{MCM}(8, 10) = 40$
- $\text{MCD}(5, 9) = 1$

Por lo tanto:
$$t = \frac{40}{1} = 40\text{ segundos}$$

*(Comprobación: En 40 segundos, la primera rueda da $40 \times \frac{5}{8} = 25$ vueltas completas y la segunda rueda da $40 \times \frac{9}{10} = 36$ vueltas completas).*

\boxed{40}