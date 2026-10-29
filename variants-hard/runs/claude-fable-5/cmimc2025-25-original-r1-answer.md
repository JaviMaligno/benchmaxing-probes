## Planteamiento

Tomo el triángulo equilátero de lado 1 con $A=(0,0)$, $B=(1,0)$, $C=(1/2,\sqrt3/2)$. Cada elipse tiene suma de distancias igual a $CA+CB = 2$ (semieje mayor $a=1$, $c=1/2$).

## Intersecciones de las elipses

Cada par de elipses comparte un foco. Por ejemplo, $E_{AB}$ y $E_{AC}$ comparten $A$: si $P$ está en ambas, entonces $PA+PB=2$ y $PA+PC=2$, luego $PB=PC$, es decir, **todas sus intersecciones están en la mediatriz de $BC$**, que es la recta por $A$ y el punto medio de $BC$.

Parametrizo esa recta como $P = t\,(\tfrac{\sqrt3}{2}, \tfrac12)$ y sustituyo en $E_{AB}$: $(x-\tfrac12)^2 + \tfrac{y^2}{3/4} = 1$:

$$\left(\tfrac{\sqrt3}{2}t-\tfrac12\right)^2 + \tfrac{t^2/4}{3/4} = 1 \;\Longrightarrow\; 13t^2 - 6\sqrt3\,t - 9 = 0 \;\Longrightarrow\; t = \frac{3\sqrt3 \pm 12}{13}.$$

Hay dos puntos: uno con $t_+\approx 1.323$ (más allá del punto medio de $BC$, fuera del triángulo) y otro con $t_-\approx -0.523$ (detrás del vértice $A$). Por simetría, lo mismo ocurre para los otros dos pares de elipses, sobre las otras dos medianas.

## Elección del triángulo $GHI$

- Tomando los tres puntos "exteriores" ($t_+$): se forma un triángulo invertido cuyo inradio ($\approx 0.373$) es menor que el circunradio de $\triangle ABC$ ($\approx 0.577$), así que sus lados **cruzan** los de $\triangle ABC$ (configuración tipo estrella). Descartado.
- Tomando puntos "detrás de los vértices" ($t_-$): por ejemplo
$$P_A^- = \left(\tfrac{9-12\sqrt3}{26},\, \tfrac{3\sqrt3-12}{26}\right)\approx(-0.453,\,-0.262), \qquad P_B^- \approx (1.453,\,-0.262).$$
Las combinaciones válidas (sin cruce de aristas) siempre incluyen al menos dos de estos puntos, y el lado mayor del triángulo resultante es el que une dos puntos tipo $P^-$ (por ejemplo, el triángulo con $P_A^-,P_B^-$ y $P_C^+=(1/2,-0.457)$, que queda completamente debajo de la recta $AB$, o bien el triángulo homotético grande $P_A^-P_B^-P_C^-$ que contiene a $\triangle ABC$).

Verificación de que $P_A^-$ está en ambas elipses: $P_A^-A \approx 0.5234$, $P_A^-B = P_A^-C \approx 1.4766$, y en efecto $0.5234+1.4766 = 2$. ✓

## Lado mayor

$$|P_A^- P_B^-| = \frac{17+12\sqrt3}{26} - \frac{9-12\sqrt3}{26} = \frac{8+24\sqrt3}{26} = \frac{4+12\sqrt3}{13} \approx 1.9066.$$

Como el lado de $\triangle ABC$ es 1, la razón pedida es:

$$\boxed{\dfrac{12\sqrt{3}+4}{13}}$$