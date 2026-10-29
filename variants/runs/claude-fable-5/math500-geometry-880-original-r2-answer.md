## Planteamiento

Coloco coordenadas: la habitación tiene largo 12 (eje $x$), ancho 10 (eje $y$) y altura 8 (eje $z$).

- **Gecko**: en la pared lateral $x=0$, a 1 pie del techo y a 1 pie de la pared trasera ($y=0$): $G=(0,\,1,\,7)$.
- **Mosca**: en la pared lateral opuesta $x=12$, a 1 pie del piso y a 1 pie de la pared frontal ($y=10$): $F=(12,\,9,\,1)$.

El camino más corto sobre superficies se encuentra "desplegando" las paredes en un plano y midiendo la línea recta. Como el piso está prohibido, pruebo las rutas posibles:

**Ruta 1: pared lateral → techo → pared lateral opuesta.**
Al desplegar, las distancias en la dirección del recorrido suman $1+12+7=20$, y en la dirección transversal $|9-1|=8$:
$$\sqrt{20^2+8^2}=\sqrt{464}\approx 21.54$$

**Ruta 2: pared lateral → pared trasera (o frontal) → pared lateral opuesta.**
Horizontal: $1+12+9=22$; vertical: $7-1=6$:
$$\sqrt{22^2+6^2}=\sqrt{520}\approx 22.80$$

**Ruta 3: pared lateral → techo → pared frontal → pared lateral opuesta.**
Despliego manteniendo el techo fijo con coordenadas $(u,v)=(x,y)$:
- La pared del gecko gira sobre la arista $x=0,\ z=8$: $G \to (-(8-7),\ 1) = (-1,\ 1)$.
- La pared frontal gira sobre la arista $y=10,\ z=8$: un punto $(x,10,z)\to(x,\ 10+(8-z))$.
- La pared de la mosca gira sobre la arista vertical $x=12,\ y=10$: $F=(12,9,1)\to(12+(10-9),\ 10+(8-1))=(13,\ 17)$.

Distancia en línea recta:
$$\sqrt{(13-(-1))^2+(17-1)^2}=\sqrt{14^2+16^2}=\sqrt{196+256}=\sqrt{452}=2\sqrt{113}\approx 21.26$$

Verifico que la recta de $(-1,1)$ a $(13,17)$ cruza las regiones desplegadas en orden válido: entra al techo en $v\approx 2.14$, pasa a la pared frontal en $u\approx 6.88$, y cruza a la pared de la mosca en $v\approx 15.86$ — todo dentro de los rangos correctos. ✓

Las demás combinaciones (pared trasera + techo da $\sqrt{500}$; techo + pared trasera da $\sqrt{548}$, etc.) resultan más largas.

## Conclusión

La ruta más corta cruza la pared lateral, el techo, la pared frontal y la pared lateral opuesta:

$$\boxed{2\sqrt{113}}$$