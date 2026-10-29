## Planteamiento

Coloco coordenadas: el eje $x$ a lo ancho (12 ft, desde la pared trasera $x=0$ hasta la delantera $x=12$), el eje $y$ a lo largo (15 ft, entre las dos paredes laterales $y=0$ y $y=15$) y $z$ la altura (0 a 9).

- **Araña**: pared lateral $y=0$, a 1 ft del techo y 1 ft de la pared trasera → $(x,z)=(1,\,8)$.
- **Polilla**: pared lateral $y=15$, a 1 ft del suelo y 1 ft de la pared delantera → $(x,z)=(11,\,1)$.

Como no puede usar el suelo, hay que comparar los desarrollos planos (desplegar las caras).

## Ruta por el techo (lateral → techo → lateral opuesta)

Al desplegar, la coordenada $x$ se conserva y los tramos se suman en línea recta:

- subir por la pared lateral hasta el techo: $9-8 = 1$
- cruzar el techo de lado a lado: $15$
- bajar por la pared opuesta hasta la polilla: $9-1 = 8$

Total en una dirección: $1+15+8 = 24$; en la perpendicular: $11-1 = 10$.

$$d=\sqrt{24^2+10^2}=\sqrt{576+100}=\sqrt{676}=26$$

La recta del desarrollo corta el borde del techo en $x\approx1.42$ y el otro borde en $x\approx7.67$, ambos dentro de $[0,12]$, así que el camino es válido.

## Otras rutas

- Por la pared trasera (lateral → trasera → lateral): $\sqrt{(1+15+11)^2+(8-1)^2}=\sqrt{27^2+7^2}=\sqrt{778}\approx27.9$
- Por la pared delantera: igualmente $\sqrt{778}\approx27.9$
- Lateral → trasera → techo → lateral: $\sqrt{24^2+12^2}=\sqrt{720}\approx26.8$
- Lateral → techo → trasera → lateral: $\sqrt{810}\approx28.5$
- Rutas por la pared delantera combinadas con el techo resultan mucho mayores.

El mínimo es la ruta por el techo, con $\sqrt{676}=26$ pies.

\boxed{26}