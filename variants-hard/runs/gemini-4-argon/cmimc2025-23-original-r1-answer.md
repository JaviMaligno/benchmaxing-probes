Para calcular el área del pentágono $ACFHE$, podemos establecer un sistema de coordenadas cartesianas.

### Paso 1: Coordenadas de $A$, $B$, $C$ y $D$
Situemos el segmento $AB$ sobre el eje $x$ con su punto medio en el origen $(0,0)$. Dado que la longitud de $AB$ es $1$, las coordenadas de $A$ y $B$ son:
$$A = \left(-\frac{1}{2}, 0\right), \quad B = \left(\frac{1}{2}, 0\right)$$

Las circunferencias $\odot A$ y $\odot B$ tienen radio $r_1 = AB = 1$. Sus puntos de intersección $C$ y $D$ se encuentran sobre la mediatriz de $AB$ (el eje $y$, donde $x = 0$). Sustituyendo en la ecuación de $\odot A$:
$$\left(0 - \left(-\frac{1}{2}\right)\right)^2 + y^2 = 1^2 \implies \frac{1}{4} + y^2 = 1 \implies y = \pm\frac{\sqrt{3}}{2}$$

Sin pérdida de generalidad, elegimos $C$ en el semiplano superior y $D$ en el inferior:
$$C = \left(0, \frac{\sqrt{3}}{2}\right), \quad D = \left(0, -\frac{\sqrt{3}}{2}\right)$$

La distancia entre $C$ y $D$ es:
$$CD = \frac{\sqrt{3}}{2} - \left(-\frac{\sqrt{3}}{2}\right) = \sqrt{3}$$

---

### Paso 2: Coordenadas de $E$ y $F$
Las circunferencias $\odot C$ y $\odot D$ tienen radio $r_2 = CD = \sqrt{3}$. Por simetría, sus puntos de intersección $E$ y $F$ se encuentran sobre la mediatriz de $CD$, que es el eje $x$ ($y = 0$). Sustituyendo en la ecuación de $\odot C$:
$$x^2 + \left(0 - \frac{\sqrt{3}}{2}\right)^2 = (\sqrt{3})^2 \implies x^2 + \frac{3}{4} = 3 \implies x^2 = \frac{9}{4} \implies x = \pm\frac{3}{2}$$

Para que los puntos $E, A, B, F$ aparezcan en ese orden sobre la recta común (el eje $x$), asignamos:
$$E = \left(-\frac{3}{2}, 0\right), \quad F = \left(\frac{3}{2}, 0\right)$$

La distancia entre $E$ y $F$ es:
$$EF = \frac{3}{2} - \left(-\frac{3}{2}\right) = 3$$

---

### Paso 3: Coordenadas de $G$ y $H$
Las circunferencias $\odot E$ y $\odot F$ tienen radio $r_3 = EF = 3$. Sus puntos de intersección $G$ y $H$ se encuentran sobre la mediatriz de $EF$ (el eje $y$, donde $x = 0$). Sustituyendo en la ecuación de $\odot E$:
$$\left(0 - \left(-\frac{3}{2}\right)\right)^2 + y^2 = 3^2 \implies \frac{9}{4} + y^2 = 9 \implies y^2 = \frac{27}{4} \implies y = \pm\frac{3\sqrt{3}}{2}$$

Como $C$ y $H$ están en lados opuestos de la recta $AB$ y $C$ tiene coordenada $y > 0$, el punto $H$ debe tener coordenada $y < 0$:
$$H = \left(0, -\frac{3\sqrt{3}}{2}\right)$$

---

### Paso 4: Cálculo del área del pentágono $ACFHE$
Los vértices del pentágono $ACFHE$ son:
- $A\left(-\frac{1}{2}, 0\right)$
- $C\left(0, \frac{\sqrt{3}}{2}\right)$
- $F\left(\frac{3}{2}, 0\right)$
- $H\left(0, -\frac{3\sqrt{3}}{2}\right)$
- $E\left(-\frac{3}{2}, 0\right)$

Dado que los puntos $E$, $A$ y $F$ son colineales y están sobre el eje $x$, el eje $x$ divide el pentágono $ACFHE$ en dos triángulos: $\triangle ACF$ (en el semiplano superior) y $\triangle EFH$ (en el semiplano inferior).

1. **Área de $\triangle ACF$:**
   - Base $AF = \frac{3}{2} - \left(-\frac{1}{2}\right) = 2$
   - Altura desde $C = \frac{\sqrt{3}}{2}$
   $$\text{Área}(\triangle ACF) = \frac{1}{2} \times 2 \times \frac{\sqrt{3}}{2} = \frac{\sqrt{3}}{2}$$

2. **Área de $\triangle EFH$:**
   - Base $EF = \frac{3}{2} - \left(-\frac{3}{2}\right) = 3$
   - Altura desde $H = \frac{3\sqrt{3}}{2}$
   $$\text{Área}(\triangle EFH) = \frac{1}{2} \times 3 \times \frac{3\sqrt{3}}{2} = \frac{9\sqrt{3}}{4}$$

Sumando ambas áreas obtenemos el área total del pentágono $ACFHE$:
$$\text{Área}(ACFHE) = \frac{\sqrt{3}}{2} + \frac{9\sqrt{3}}{4} = \frac{2\sqrt{3} + 9\sqrt{3}}{4} = \frac{11\sqrt{3}}{4}$$

\boxed{\frac{11\sqrt{3}}{4}}