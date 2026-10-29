Contemos los cuadrados posibles en una malla de 3 filas y $n$ columnas de puntos (es decir, de altura 2 unidades):

**Cuadrados alineados con los ejes:**
- Lado 1: hay 2 filas de celdas y $n-1$ posiciones horizontales, o sea $2(n-1)$.
- Lado 2: solo caben en una posición vertical, con $n-2$ posiciones horizontales, o sea $n-2$.

**Cuadrados inclinados:**
- Lado $\sqrt{2}$ (vector $(1,1)$): su caja envolvente es de $2\times 2$, así que caben en $n-2$ posiciones.

No cabe ningún otro tamaño, pues cualquier cuadrado con vector $(a,b)$ necesita una caja de lado $a+b \le 2$. Esto da exactamente los tres tamaños mencionados.

**Total:**
$$2(n-1) + (n-2) + (n-2) = 4n - 6 = 86 \implies 4n = 92 \implies n = 23$$

Verificación: con $n=23$ hay $2\cdot22 = 44$ de lado 1, $21$ de lado 2 y $21$ de lado $\sqrt2$, y $44+21+21 = 86$. ✓

$$\boxed{23}$$