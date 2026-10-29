Vamos a contar los cuadrados de cada tamaño en una cuadrícula de puntos de 3 filas y $n$ columnas (es decir, de dimensiones $2 \times (n-1)$ en unidades).

Con solo 3 filas de puntos, los únicos cuadrados posibles son de tres tamaños:

**Cuadrados $1\times 1$ (alineados):** caben en 2 filas de celdas y $n-1$ columnas de celdas, así que hay $2(n-1)$.

**Cuadrados $2\times 2$ (alineados):** ocupan toda la altura y hay $n-2$ posiciones horizontales, así que hay $n-2$.

**Cuadrados inclinados de lado $\sqrt{2}$:** tienen vértices del tipo $(x,1),(x+1,0),(x+2,1),(x+1,2)$; necesitan un ancho de 2 unidades, así que hay $n-2$.

(No caben cuadrados de lado $\sqrt{5}$ ni mayores, porque requerirían al menos 4 filas de puntos.)

Sumando:
$$2(n-1) + (n-2) + (n-2) = 4n - 6 = 70$$

Entonces $4n = 76$, es decir $n = 19$.

$$\boxed{19}$$