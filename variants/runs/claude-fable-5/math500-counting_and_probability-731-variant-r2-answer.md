## Planteamiento

Coloco el centro $O$ en el origen con circunradio $1$, de modo que los vértices son:
$$P = (0, 1), \quad Q = \left(-\tfrac{\sqrt{3}}{2}, -\tfrac{1}{2}\right), \quad R = \left(\tfrac{\sqrt{3}}{2}, -\tfrac{1}{2}\right)$$

El área del triángulo es $\frac{3\sqrt{3}}{4}$ y su inradio es $\frac{1}{2}$.

## Región más cercana a $O$

Un punto está más cerca de $O$ que de un vértice $V$ si está del lado de $O$ respecto a la mediatriz del segmento $OV$. Cada mediatriz es una recta a distancia $\frac{1}{2}$ de $O$, perpendicular a la dirección del vértice correspondiente:

- Mediatriz de $OP$: $y = \tfrac{1}{2}$, región: $y < \tfrac{1}{2}$
- Mediatriz de $OQ$: $\sqrt{3}x + y = -1$, región: $\sqrt{3}x + y > -1$
- Mediatriz de $OR$: $\sqrt{3}x - y = 1$, región: $\sqrt{3}x - y < 1$

Estas tres rectas son tangentes al círculo de radio $\frac{1}{2}$ centrado en $O$, con normales apuntando **hacia** los vértices (ángulos $90°$, $210°$, $330°$). La intersección de los tres semiplanos es un triángulo equilátero con inradio $\frac{1}{2}$ y centro $O$ — es decir, un triángulo **congruente** al original pero rotado $180°$ respecto a $O$ (las normales de los lados del triángulo original apuntan en las direcciones opuestas: $270°$, $30°$, $150°$).

## Cálculo del área

La región buscada es la intersección del triángulo original con su imagen bajo rotación de $180°$ alrededor del centroide. Esta intersección es un hexágono (la figura tipo "estrella de David"): cada esquina del triángulo original que queda cortada es un triángulo pequeño semejante con razón $\frac{1}{3}$, es decir, con área $\frac{1}{9}$ del total. Se cortan tres esquinas:

$$\text{Área del hexágono} = \left(1 - 3 \cdot \tfrac{1}{9}\right) \cdot [\triangle PQR] = \tfrac{2}{3} \, [\triangle PQR]$$

**Verificación:** el punto medio de $QR$, $(0, -\tfrac{1}{2})$, dista $\tfrac{1}{2}$ de $O$ y $\tfrac{\sqrt{3}}{2}$ de $Q$ y de $R$, así que está más cerca de $O$, y en efecto satisface las tres desigualdades.

## Probabilidad

$$\frac{\text{área favorable}}{\text{área total}} = \frac{2}{3}$$

$$\boxed{\dfrac{2}{3}}$$