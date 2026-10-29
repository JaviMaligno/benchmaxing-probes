## Planteamiento con coordenadas

Pongo $S=(0,0)$, $R=(18,0)$. Como $PQ\parallel RS$, escribo $P=(u,h)$, $Q=(u+10,h)$.

- $SP=5$: $u^2+h^2=25$
- $QR=7$: $(u-8)^2+h^2=49$

Restando: $u=\tfrac52$, y luego $h=\tfrac{5\sqrt3}{2}$. Entonces:
$$P=\left(\tfrac52,\tfrac{5\sqrt3}{2}\right),\quad Q=\left(\tfrac{25}{2},\tfrac{5\sqrt3}{2}\right),\quad R=(18,0),\quad S=(0,0).$$

**Mediatrices clave:**
- de $PQ$: $x=\tfrac{15}{2}$;  de $RS$: $x=9$
- de $QR$: $11x-5\sqrt3\,y=149$
- de $SP$: $x+\sqrt3\,y=5$

## Circuncentros

Cada circuncentro es la intersección de dos mediatrices:

| Triángulo | Circuncentro |
|---|---|
| $PQR$ | $O_1=\left(\tfrac{15}{2},-\tfrac{133\sqrt3}{30}\right)$ |
| $QRS$ | $O_2=\left(9,-\tfrac{10\sqrt3}{3}\right)$ |
| $RSP$ | $O_3=\left(9,-\tfrac{4\sqrt3}{3}\right)$ |
| $SPQ$ | $O_4=\left(\tfrac{15}{2},-\tfrac{5\sqrt3}{6}\right)$ |

(Verifiqué cada uno: las distancias a los tres vértices coinciden; p. ej. $|O_1P|^2=|O_1Q|^2=|O_1R|^2=\tfrac{38073}{225}$.)

## Área del cuadrilátero

Como $PQ\parallel RS$, los lados $O_1O_4$ (sobre $x=\tfrac{15}{2}$) y $O_2O_3$ (sobre $x=9$) son **paralelos y verticales**; el cuadrilátero $O_1O_2O_3O_4$ es un trapecio (recorrido antihorario, convexo).

Longitudes de los lados paralelos:
$$|O_1O_4|=\frac{133\sqrt3}{30}-\frac{5\sqrt3}{6}=\frac{108\sqrt3}{30}=\frac{18\sqrt3}{5},\qquad |O_2O_3|=\frac{10\sqrt3}{3}-\frac{4\sqrt3}{3}=2\sqrt3,$$
con altura (separación horizontal) $\tfrac32$. Área:
$$\frac12\left(\frac{18\sqrt3}{5}+2\sqrt3\right)\cdot\frac32=\frac12\cdot\frac{28\sqrt3}{5}\cdot\frac32=\frac{42\sqrt3}{10}=\frac{21\sqrt3}{5}.$$

**Comprobación independiente** (shoelace con las cuatro coordenadas exactas, y también integrando $\int_{7.5}^{9}\frac{174-16x}{5\sqrt3}\,dx=\frac{63}{5\sqrt3}$): todo da $\tfrac{21\sqrt3}{5}\approx 7.275$.

$$\boxed{\dfrac{21\sqrt{3}}{5}}$$