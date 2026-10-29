**Configuración:** el arreglo tiene 3 filas y $n$ columnas de puntos.

**Cuadrados alineados con los ejes:**
- De tamaño $1\times 1$: hay $2$ posiciones verticales y $n-1$ horizontales → $2(n-1)$.
- De tamaño $2\times 2$: solo $1$ posición vertical y $n-2$ horizontales → $n-2$.

**Cuadrados inclinados:** un cuadrado con lado vector $(a,b)$, $a,b\ge 1$, tiene caja de tamaño $(a+b)\times(a+b)$ y necesita $(a+b+1)$ filas de puntos. Como solo hay $3$ filas, se exige $a+b\le 2$, así que la única posibilidad es $(a,b)=(1,1)$:
- De lado $\sqrt{2}$ (rombos): ocupan exactamente $3\times 3$ puntos, con $1$ posición vertical y $n-2$ horizontales → $n-2$.

**Total:**
$$2(n-1) + (n-2) + (n-2) = 4n - 6$$

Se cumplen las tres condiciones: para $n\ge 2$ hay exactamente tres tamaños ($1$, $2$, $\sqrt{2}$).

$$4n - 6 = 86 \implies 4n = 92 \implies n = 23$$

\boxed{23}