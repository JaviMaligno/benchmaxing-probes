## Solución

**Paso 1: las direcciones de los paralelogramos están determinadas por el polígono.**

Si un polígono convexo se tesela con paralelogramos, se puede demostrar por inducción (quitando la pieza que cubre un vértice, que debe tener sus lados sobre los dos lados del polígono que se cortan ahí, y observando que el resto sigue siendo convexo) que cada lado de cada paralelogramo es paralelo a algún lado del polígono original.

Un 6720-gono regular tiene lados en pares opuestos paralelos, es decir, hay **3360 direcciones distintas** (módulo π), separadas por ángulos de 2π/6720.

**Paso 2: estructura de zonas.**

En una teselación de un polígono centralmente simétrico por paralelogramos, las piezas se organizan en *zonas* (franjas) paralelas a cada par de lados opuestos. Si la dirección *i* tiene $m_i$ zonas, todo par de direcciones $i,j$ distintas genera exactamente $m_i \cdot m_j$ paralelogramos con esas dos direcciones (cada par de zonas se cruza exactamente una vez, por convexidad).

Como cada lado del polígono toca al menos una pieza con esa dirección, se cumple $m_i \ge 1$ para cada una de las 3360 direcciones.

**Paso 3: cuándo un paralelogramo es un rectángulo.**

Un paralelogramo es un rectángulo exactamente cuando sus dos direcciones son perpendiculares. Las direcciones se indexan módulo 3360; dos direcciones $k$ y $k+1680$ forman un ángulo de $\pi/2$. Como $k \mapsto k+1680 \pmod{3360}$ es una involución sin puntos fijos, hay exactamente $3360/2 = 1680$ pares de direcciones perpendiculares.

**Paso 4: cota inferior.**

Cada par perpendicular $\{k, k+1680\}$ produce al menos $m_k \cdot m_{k+1680} \ge 1$ rectángulos. Por lo tanto:

$$R \ge 1680.$$

**Paso 5: construcción que alcanza la cota.**

El 6720-gono regular es un zonógono, y admite la teselación canónica con **una sola zona por dirección** ($m_i = 1$ para todo $i$). Ésta produce un paralelogramo por cada par de direcciones, y los rectángulos son exactamente los de pares de direcciones perpendiculares, es decir, exactamente $1680$ rectángulos.

Por lo tanto, el mínimo posible es:

$$\boxed{1680}$$