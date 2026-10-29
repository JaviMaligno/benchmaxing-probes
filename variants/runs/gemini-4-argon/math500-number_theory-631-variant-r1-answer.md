Para determinar después de cuántos segundos ambos puntos volverán a apuntar hacia arriba al mismo tiempo, debemos calcular el período de rotación (el tiempo que tarda en dar una vuelta completa) de cada rueda en segundos y luego hallar su mínimo común múltiplo.

1. **Primera rueda:**
   Da $37\frac{1}{2} = \frac{75}{2}$ vueltas por minuto ($60\text{ segundos}$).
   La cantidad de vueltas por segundo es:
   $$\frac{75/2}{60} = \frac{75}{120} = \frac{5}{8}\text{ vueltas por segundo}$$
   Por lo tanto, el tiempo que tarda la primera rueda en dar una vuelta completa es:
   $$T_1 = \frac{8}{5}\text{ segundos}$$

2. **Segunda rueda:**
   Da $54$ vueltas por minuto ($60\text{ segundos}$).
   La cantidad de vueltas por segundo es:
   $$\frac{54}{60} = \frac{9}{10}\text{ vueltas por segundo}$$
   Por lo tanto, el tiempo que tarda la segunda rueda en dar una vuelta completa es:
   $$T_2 = \frac{10}{9}\text{ segundos}$$

3. **Tiempo hasta que coincidan nuevamente:**
   Para que ambos puntos apunten hacia arriba simultáneamente, el tiempo transcurrido $t$ debe ser un múltiplo entero tanto de $T_1$ como de $T_2$. Buscamos el mínimo común múltiplo de ambas fracciones irreducibles:
   $$\text{mcm}\left(\frac{8}{5}, \frac{10}{9}\right) = \frac{\text{mcm}(8, 10)}{\text{mcd}(5, 9)} = \frac{40}{1} = 40\text{ segundos}$$

*(Comprobación: en $40\text{ segundos}$, la primera rueda da $40 \times \frac{5}{8} = 25$ vueltas completas y la segunda rueda da $40 \times \frac{9}{10} = 36$ vueltas completas; como $\text{mcd}(25, 36) = 1$, este es el menor tiempo posible).*

\boxed{40}