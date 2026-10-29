## Solución

**Suma de áreas.** Los cuatro triángulos cubren el cuadrado, así que el área del cuadrado es $1+2+3+4=10$ y el lado es $s=\sqrt{10}$.

**Alturas desde $P$.** Cada triángulo tiene base $s$, de modo que sus alturas (distancias de $P$ a los lados) son $\frac{2}{\sqrt{10}}, \frac{4}{\sqrt{10}}, \frac{6}{\sqrt{10}}, \frac{8}{\sqrt{10}}$ para las áreas $1,2,3,4$ respectivamente. Las distancias a lados opuestos deben sumar $s=\sqrt{10}$, lo que obliga a emparejar las áreas opuestas como $\{1,4\}$ y $\{2,3\}$ (pues $\frac{2+8}{\sqrt{10}}=\frac{4+6}{\sqrt{10}}=\sqrt{10}$).

**Coordenadas.** Con $t=\frac{1}{\sqrt{10}}$, coloco el cuadrado con vértices $(0,0),(10t,0),(10t,10t),(0,10t)$ y $P=(2t,4t)$ (cualquier otra asignación válida da el mismo producto por simetría). Las áreas resultan $1,2,3,4$ en algún orden, como se pide.

**Distancias al cuadrado** (usando $t^2=\tfrac{1}{10}$):

$$PA^2 = (2t)^2+(4t)^2 = 20t^2 = 2$$
$$PB^2 = (8t)^2+(4t)^2 = 80t^2 = 8$$
$$PC^2 = (8t)^2+(6t)^2 = 100t^2 = 10$$
$$PD^2 = (2t)^2+(6t)^2 = 40t^2 = 4$$

**Producto.**

$$(PA\cdot PB\cdot PC\cdot PD)^2 = 2\cdot 8\cdot 10\cdot 4 = 640 \implies PA\cdot PB\cdot PC\cdot PD = \sqrt{640} = 8\sqrt{10}$$

$$\boxed{8\sqrt{10}}$$