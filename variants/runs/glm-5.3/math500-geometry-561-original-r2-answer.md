**Razonamiento.** En un octágono equiangular cada ángulo exterior mide $45^\circ$. Coloquemos los lados en direcciones $0^\circ, 45^\circ, 90^\circ, \dots, 315^\circ$, alternando longitudes $1$ y $\frac{\sqrt{2}}{2}$.

Los vectores de los lados son:

- $s_1=(1,0)$, $\quad s_2=\frac{\sqrt2}{2}(\cos45^\circ,\sin45^\circ)=\left(\tfrac12,\tfrac12\right)$
- $s_3=(0,1)$, $\quad s_4=\left(-\tfrac12,\tfrac12\right)$
- $s_5=(-1,0)$, $\quad s_6=\left(-\tfrac12,-\tfrac12\right)$
- $s_7=(0,-1)$, $\quad s_8=\left(\tfrac12,-\tfrac12\right)$

La suma de componentes es $0$ en ambos ejes, así que el octágono se cierra. Los vértices, partiendo de $(0,0)$, son:

$$(0,0),\ (1,0),\ \left(\tfrac32,\tfrac12\right),\ \left(\tfrac32,\tfrac32\right),\ (1,2),\ (0,2),\ \left(-\tfrac12,\t32\right),\ \left(-\tfrac12,\tfrac12\right)$$

**Verificación geométrica:** estos vértices caben en un cuadrado de lado $2$ (coordenadas $x$ de $-\tfrac12$ a $\tfrac32$, e $y$ de $0$ a $2$). El octágono es ese cuadrado con cuatro triángulos rectángulos isósceles de catetos $\tfrac12$ recortados en las esquinas (área $4\cdot\tfrac12\cdot\tfrac12\cdot\tfrac12=\tfrac12$). Por tanto:

$$\text{Área}=4-\tfrac12=\tfrac72.$$

(El mismo resultado se obtiene con la fórmula del shoelace: la suma de productos cruzados da $7$, y $7/2$.)

$$\boxed{\dfrac{7}{2}}$$