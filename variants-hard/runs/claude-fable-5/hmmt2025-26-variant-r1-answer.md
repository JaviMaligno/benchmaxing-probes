## Solución

**Coordenadas del trapecio.** Coloco $S=(0,0)$, $R=(18,0)$, y como $PQ \parallel RS$, pongo $P=(x,h)$, $Q=(x+10,h)$.

- $SP=5$: $x^2+h^2=25$
- $QR=7$: $(x-8)^2+h^2=49$

Restando: $-16x+64=24 \Rightarrow x=\tfrac{5}{2}$, y entonces $h^2 = 25-\tfrac{25}{4}=\tfrac{75}{4}$, es decir $h=\tfrac{5\sqrt3}{2}$.

Así: $P=\left(\tfrac52, \tfrac{5\sqrt3}{2}\right)$, $Q=\left(\tfrac{25}{2}, \tfrac{5\sqrt3}{2}\right)$, $R=(18,0)$, $S=(0,0)$.

**Circuncentros.** Los triángulos que contienen el lado $PQ$ tienen circuncentro sobre $x=\tfrac{15}{2}$; los que contienen $RS$, sobre $x=9$. Igualando distancias al tercer vértice en cada caso:

- $O_1$ (de $\triangle PQR$): en $x=\tfrac{15}{2}$, equidistante de $Q$ y $R$: $O_1=\left(\tfrac{15}{2},\, -\tfrac{133\sqrt3}{30}\right)$
- $O_2$ (de $\triangle QRS$): en $x=9$, equidistante de $S$ y $Q$: $O_2=\left(9,\, -\tfrac{10\sqrt3}{3}\right)$
- $O_3$ (de $\triangle RSP$): en $x=9$, equidistante de $S$ y $P$: $O_3=\left(9,\, -\tfrac{4\sqrt3}{3}\right)$
- $O_4$ (de $\triangle SPQ$): en $x=\tfrac{15}{2}$, equidistante de $S$ y $P$: $O_4=\left(\tfrac{15}{2},\, -\tfrac{5\sqrt3}{6}\right)$

**Área.** El cuadrilátero $O_1O_2O_3O_4$ es un trapecio con dos lados verticales paralelos:

- Lado en $x=\tfrac{15}{2}$: $\left|-\tfrac{5\sqrt3}{6}+\tfrac{133\sqrt3}{30}\right| = \tfrac{108\sqrt3}{30} = \tfrac{18\sqrt3}{5}$
- Lado en $x=9$: $\left|-\tfrac{4\sqrt3}{3}+\tfrac{10\sqrt3}{3}\right| = 2\sqrt3$
- Distancia entre ellos: $9-\tfrac{15}{2}=\tfrac{3}{2}$

$$\text{Área} = \frac12\left(\frac{18\sqrt3}{5}+2\sqrt3\right)\cdot\frac32 = \frac34\cdot\frac{28\sqrt3}{5} = \frac{21\sqrt3}{5}$$

(Verificado también con la fórmula del polígono de Gauss: $\tfrac12\cdot\tfrac{42}{5}\sqrt3 = \tfrac{21\sqrt3}{5}$.)

$$\boxed{\dfrac{21\sqrt{3}}{5}}$$