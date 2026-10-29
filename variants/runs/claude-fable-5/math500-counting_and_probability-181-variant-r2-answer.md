Contemos los cuadrados posibles en una malla de 3 filas y $n$ columnas (altura 2 unidades):

**Cuadrados alineados a los ejes:**
- Lado 1: hay 2 filas de celdas y $n-1$ columnas de celdas → $2(n-1)$ cuadrados.
- Lado 2: solo caben en una posición vertical, con $n-2$ posiciones horizontales → $n-2$ cuadrados.
- Lado 3 o mayor: imposible, la altura es solo 2.

**Cuadrados inclinados:**
- Lado $\sqrt{2}$ (vector $(1,1)$): su caja envolvente es $2\times 2$, y en cada caja cabe exactamente un "diamante". Hay $n-2$ cajas → $n-2$ cuadrados.
- Lado $\sqrt{5}$ (vector $(2,1)$): requiere caja $3\times 3$, que no cabe en altura 2. Imposible.

Esto da exactamente tres tamaños ($1$, $2$ y $\sqrt{2}$), como pide el enunciado. El total es:

$$2(n-1) + (n-2) + (n-2) = 4n - 6 = 86$$

$$4n = 92 \quad\Rightarrow\quad n = 23$$

Verificación: con $n=23$ hay $44$ cuadrados de lado 1, $21$ de lado 2 y $21$ de lado $\sqrt{2}$, y $44+21+21=86$. ✓

$$\boxed{23}$$