## Planteamiento

Coloco coordenadas: largo 12 en $x$, ancho 10 en $y$, alto 8 en $z$.

- Paredes laterales ($10\times 8$): $x=0$ y $x=12$.
- Paredes frontal/posterior ($12\times 8$): $y=0$ (frontal) y $y=10$ (posterior).
- Gecko: pared $x=0$, a 1 pie del techo y 1 del fondo → $G=(0,9,7)$.
- Mosca: pared $x=12$, a 1 pie del suelo y 1 de la frontal → $M=(12,1,1)$.

El suelo está prohibido, así que hay que comparar desarrollos planos (unfoldings).

## Candidatos

**1) Lateral → techo → lateral:** recorrido longitudinal $1+12+7=20$, transversal $|9-1|=8$:
$$\sqrt{20^2+8^2}=\sqrt{464}=4\sqrt{29}\approx 21.54$$

**2) Lateral → pared frontal (o posterior) → lateral:** longitudinal $9+12+1=22$, transversal $7-1=6$:
$$\sqrt{22^2+6^2}=\sqrt{520}\approx 22.80$$

**3) Lateral → techo → pared frontal → lateral:** tomo el techo como plano base $(x,y)$.
- Pared $x=0$: $(0,y,z)\mapsto(z-8,\;y)$, luego $G\mapsto(-1,9)$.
- Pared $y=0$: $(x,0,z)\mapsto(x,\;z-8)$.
- Pared $x=12$ desplegada sobre el borde $x=12$ de la frontal: $(12,y,z)\mapsto(12+y,\;z-8)$, luego $M\mapsto(13,-7)$.

$$\sqrt{14^2+16^2}=\sqrt{452}=2\sqrt{113}\approx 21.26$$

**Verificación de validez:** la recta $y'=9-\tfrac87(x'+1)$ cruza los bordes en $(0,\tfrac{55}{7})$, $(\tfrac{55}{8},0)$ y $(12,-\tfrac{41}{7})$, todos dentro de los bordes reales ($0\le \tfrac{55}{7}\le 10$, $0\le\tfrac{55}{8}\le12$, $0\le 8-\tfrac{41}{7}\le 8$). La trayectoria es legítima y sus cuatro tramos suman $\sqrt{113}\left(\tfrac{8+55+41+8}{56}\right)=2\sqrt{113}$.

Otros desarrollos (lateral→frontal→techo→lateral: $\sqrt{788}$; lateral→posterior→techo→lateral: $\sqrt{500}$; lateral→techo→posterior→lateral: $\sqrt{548}$) son más largos.

El mínimo es $2\sqrt{113}\approx 21.26$ pies, menor que $4\sqrt{29}$.

\boxed{2\sqrt{113}}