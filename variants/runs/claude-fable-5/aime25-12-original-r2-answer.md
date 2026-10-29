## Resolución

**Simplificar las desigualdades.** Con $x+y+z=75$:

- $x - yz < y - zx \iff (x-y) + z(x-y) < 0 \iff (x-y)(1+z) < 0$
- $y - zx < z - xy \iff (y-z) + x(y-z) < 0 \iff (y-z)(1+x) < 0$

**Análisis de casos.** Cada condición da dos opciones de signo, lo que produce tres regiones disjuntas en el plano. La región acotada surge cuando:

$$1+z > 0,\; x < y \qquad \text{y} \qquad 1+x > 0,\; y < z$$

es decir, $-1 < x < y < z$ con $x+y+z=75$ (las otras combinaciones dan regiones no acotadas).

**Vértices de la región.** Es un triángulo con vértices donde las desigualdades se vuelven igualdades:

- $x=y=z$: punto $(25,25,25)$
- $x=-1,\; y=z$: punto $(-1,38,38)$
- $x=y=-1$: punto $(-1,-1,77)$

**Área.** Desde $A=(25,25,25)$:

$$\vec{AB} = (-26,-26,52), \qquad \vec{AC} = (-26,13,13)$$

$$\vec{AB}\times\vec{AC} = (-1014,\,-1014,\,-1014), \qquad \|\vec{AB}\times\vec{AC}\| = 1014\sqrt{3}$$

$$\text{Área} = \frac{1014\sqrt{3}}{2} = 507\sqrt{3}$$

Entonces $a=507$, $b=3$, y $a+b = 510$.

$$\boxed{510}$$