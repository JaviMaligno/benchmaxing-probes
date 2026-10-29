## Planteamiento

Sea el array con filas $y\in\{0,1,2\}$ y columnas $x\in\{0,1,\dots,n-1\}$.

**Cuadrados alineados con los ejes de lado 1:** hay $2$ posiciones verticales y $n-1$ horizontales → $2(n-1)$.

**Cuadrados alineados de lado 2:** solo $1$ posición vertical (ocupa las 3 filas) y $n-2$ horizontales → $n-2$.

**Cuadrados inclinados:** todo cuadrado inclinado con vector de lado $(a,b)$ se inscribe en una caja cuadrada de lado $a+b$. Como la altura disponible es solo $2$, debe ser $a+b=2$, es decir $(a,b)=(1,1)$: el cuadrado de lado $\sqrt{2}$ girado 45°. Hay exactamente uno por cada caja $2\times 2$, y hay $n-2$ cajas → $n-2$.

Esto da justamente **tres tamaños distintos**: $1$, $2$ y $\sqrt{2}$. ✓

## Conteo total

$$2(n-1) + (n-2) + (n-2) = 4n - 6$$

$$4n - 6 = 86 \implies 4n = 92 \implies n = 23$$

Verificación con $n=23$: $44 + 21 + 21 = 86$. ✓

\boxed{23}