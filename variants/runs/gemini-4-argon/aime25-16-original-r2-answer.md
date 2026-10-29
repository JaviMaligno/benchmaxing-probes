Para encontrar el área del triángulo $\triangle BGE$, podemos seguir los siguientes pasos:

**Paso 1: Determinar la longitud de los segmentos sobre la recta.**
Como los puntos $A, B, C, D, E$ y $F$ están alineados en ese orden, el segmento total $AF$ es la suma de los segmentos disjuntos $AC$, $CD$ y $DF$:
$$AF = AC + CD + DF$$

Sustituyendo los valores dados ($AF = 73$, $AC = 26$, $DF = 33$):
$$73 = 26 + CD + 33$$
$$CD = 73 - 59 = 14$$

Ahora podemos hallar la longitud de la base $BE$ del triángulo $\triangle BGE$. Observamos que los segmentos $BD$ y $CE$ se solapan precisamente en el segmento $CD$:
$$BE = BD + CE - CD$$
$$BE = 22 + 31 - 14 = 39$$

**Paso 2: Calcular el área y la altura del triángulo $\triangle CGD$.**
Conocemos los tres lados del triángulo $\triangle CGD$: $CD = 14$, $DG = 30$ y $CG = 40$.
Calculamos su semiperímetro $s$:
$$s = \frac{14 + 30 + 40}{2} = 42$$

Aplicando la fórmula de Herón para hallar el área de $\triangle CGD$:
$$\text{Área}(\triangle CGD) = \sqrt{s(s - CD)(s - DG)(s - CG)}$$
$$\text{Área}(\triangle CGD) = \sqrt{42(42 - 14)(42 - 30)(42 - 40)} = \sqrt{42 \cdot 28 \cdot 12 \cdot 2}$$
$$\text{Área}(\triangle CGD) = \sqrt{(6 \cdot 7) \cdot (4 \cdot 7) \cdot (2 \cdot 6) \cdot 2} = 6 \cdot 7 \cdot 4 = 168$$

**Paso 3: Calcular el área de $\triangle BGE$.**
Dado que los puntos $B, C, D$ y $E$ están en la misma recta, los triángulos $\triangle BGE$ y $\triangle CGD$ comparten la misma altura $h$ trazada desde el punto $G$ hacia la recta $AF$. Por lo tanto, la razón entre sus áreas es igual a la razón entre sus bases:
$$\frac{\text{Área}(\triangle BGE)}{\text{Área}(\triangle CGD)} = \frac{BE}{CD}$$

Sustituyendo los valores obtenidos:
$$\text{Área}(\triangle BGE) = 168 \cdot \frac{39}{14} = 12 \cdot 39 = 468$$

\boxed{468}