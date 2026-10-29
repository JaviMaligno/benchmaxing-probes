## Planteamiento

Coloco coordenadas: $x$ a lo largo de los 12 pies, $y$ a lo ancho de los 10 pies, $z$ en altura (8 pies).

- Paredes laterales ($10\times 8$): $x=0$ y $x=12$.
- Pared trasera: $y=0$; pared frontal: $y=10$. Techo: $z=8$.

**Gecko:** pared $x=0$, a 1 pie del techo y 1 pie de la pared trasera → $(0,\,1,\,7)$.
**Mosca:** pared $x=12$, a 1 pie del piso y 1 pie de la pared frontal → $(12,\,9,\,1)$.

Como no puede usar el piso, hay que desplegar (desdoblar) las caras permitidas y buscar la recta más corta.

## Caminos candidatos

**1) Pared → techo → pared opuesta:**
Subir 1 (hasta el techo) + 12 (techo) + bajar 7 = 20; desplazamiento lateral $9-1=8$:
$$\sqrt{20^2+8^2}=\sqrt{464}=4\sqrt{29}\approx 21.54$$

**2) Pared → pared trasera (o frontal) → pared opuesta:**
$1+12+9=22$ y $7-1=6$: $\sqrt{484+36}=\sqrt{520}\approx 22.80$

**3) Pared → techo → pared frontal → pared opuesta:**
En el desdoblamiento, un cateto recorre: 1 (hasta el techo) + 12 (techo) + 1 (desde la arista frontal hasta la mosca) $=14$; el otro cateto: 9 (de $y=1$ a $y=10$) + 7 (bajar de $z=8$ a $z=1$) $=16$:
$$\sqrt{14^2+16^2}=\sqrt{452}=2\sqrt{113}\approx 21.26$$

Verifico que la recta sí atraviesa las cuatro caras en orden: cruza al techo en $(0,\,2.14,\,8)$, pasa a la pared frontal en $(6.875,\,10,\,8)$ y entra a la pared $x=12$ en $(12,\,10,\,2.14)$ — todos puntos interiores de sus aristas, así que el camino es válido.

Las demás secuencias (trasera+techo: $\sqrt{500}$; techo+trasera: $\sqrt{548}$; frontal+techo: $\sqrt{788}$; trasera+techo+frontal: $\sqrt{520}$) son todas mayores.

El mínimo es $2\sqrt{113}\approx 21.26 < 4\sqrt{29}\approx 21.54$.

$$\boxed{2\sqrt{113}}$$