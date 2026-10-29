## Solución

**Simplificación de las desigualdades.** Con la primera desigualdad:
$$x - yz < y - zx \iff (x-y) + z(x-y) < 0 \iff (x-y)(1+z) < 0$$

Con la segunda:
$$y - zx < z - xy \iff (y-z) + x(y-z) < 0 \iff (y-z)(1+x) < 0$$

**Análisis de casos.** Cada condición da dos opciones; la región finita resulta del caso:
$$x < y,\quad z > -1,\quad y < z,\quad x > -1$$

es decir $-1 < x < y < z$ con $x+y+z = 75$ (nótese que $z > y > x > -1$ hace redundante $z > -1$). Los otros casos producen regiones no acotadas.

**Parametrización.** Con $z = 75 - x - y$, las condiciones son:
- $x > -1$
- $x < y$
- $y < z \iff 2y + x < 75$

Esto define en el plano $(x,y)$ un triángulo con vértices:
- Intersección de $x=-1$ con $y=x$: $(-1,-1)$
- Intersección de $x=-1$ con $2y+x=75$: $(-1, 38)$
- Intersección de $y=x$ con $2y+x=75$: $(25, 25)$

**Área proyectada.** Base sobre $x=-1$ de longitud $38-(-1) = 39$; altura horizontal $25-(-1) = 26$:
$$\text{Área}_{xy} = \tfrac{1}{2} \cdot 39 \cdot 26 = 507$$

**Factor de corrección.** El plano $x+y+z=75$ tiene normal $(1,1,1)$; al proyectar sobre el plano $xy$ el área se reduce por el factor $\frac{|n_z|}{|n|} = \frac{1}{\sqrt{3}}$, así que el área real es:
$$507\sqrt{3}$$

Entonces $a = 507$, $b = 3$, y $a + b = 510$.

$$\boxed{510}$$