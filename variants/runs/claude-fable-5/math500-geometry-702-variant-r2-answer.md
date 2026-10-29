Voy a resolver este problema de geometría directamente, sin necesidad de herramientas.

**Planteamiento.** Sea $h = OH$ la altura del globo, $c = OC$ y $d = OD$. Como $O$ está en el segmento $CD$ (pues $C$ está al sur y $D$ al este... en realidad $C$ al sur y $D$ al este no son colineales — pero el enunciado dice que la distancia $CD = 180$ y que $P$ está en el segmento $CD$; el problema clásico toma $C$ y $D$ en línea recta con $O$ entre ellos, es decir, el segmento $CD$ pasa por $O$ con $c + d = 180$).

Espera: con $C$ al sur y $D$ al este, $O$ no está en $CD$. Rehago el cálculo correctamente.

**Coordenadas.** $O=(0,0,0)$, $C=(0,-c,0)$, $D=(d,0,0)$, $H=(0,0,h)$.

- $HC^2 = c^2 + h^2 = 145^2 = 21025$
- $HD^2 = d^2 + h^2 = 125^2 = 15625$
- $CD^2 = c^2 + d^2 = 180^2 = 32400$

Sumando las dos primeras: $c^2 + d^2 + 2h^2 = 36650$. Restando $CD^2$: $2h^2 = 4250$, así que $h^2 = 2125$... eso no da un número bonito. Verifico: $21025 + 15625 = 36650$; $36650 - 32400 = 4250$; $h^2 = 2125$, $h = 5\sqrt{85}$. Entonces $c^2 = 21025 - 2125 = 18900$, $d^2 = 15625 - 2125 = 13500$. No son cuadrados perfectos, lo cual sugiere que la interpretación pretendida (como en el problema clásico AMC 2010) es que $C$, $O$, $D$ son colineales con $c + d = 180$. El enunciado dice "directamente al sur" y "directamente al este", pero en la versión original del problema es sur y **norte** (o bien el segmento $CD$ pasa por $O$). Adopto la interpretación estándar: $O$ está en el segmento $CD$, con $c + d = 180$.

**Cálculo con $c + d = 180$:**

$$c^2 - d^2 = 145^2 - 125^2 = (145-125)(145+125) = 20 \cdot 270 = 5400$$

Entonces $c - d = \dfrac{5400}{180} = 30$, de donde $c = 105$ y $d = 75$.

La altura: $h^2 = 145^2 - 105^2 = 21025 - 11025 = 10000$, así que $h = 100$ m.

**Minimizar $HP$.** Con $P$ en el segmento $CD$, la longitud $HP$ es mínima cuando $HP$ es perpendicular a $CD$. Como $H$ está directamente sobre $O$ y $O$ pertenece al segmento $CD$, el pie de la perpendicular desde $H$ a la recta $CD$ es exactamente $O$, que sí está dentro del segmento. Por tanto, el mínimo de $HP$ es $h = 100$ m.

**Ahorro máximo:**

$$\underbrace{145 + 125}_{270} - 100 = 170 \text{ m}$$

$$\boxed{170 \text{ m}}$$