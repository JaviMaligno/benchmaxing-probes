## Razonamiento

**Cuadrados alineados con los ejes:**

- Lado 1: hay $2$ posiciones verticales (3 filas → 2 franjas) y $n-1$ horizontales: $2(n-1)$.
- Lado 2: solo $1$ posición vertical (altura total = 2) y $n-2$ horizontales: $n-2$.
- Lado 3 o más: imposible, la altura máxima es 2.

**Cuadrados inclinados:**

Un cuadrado inclinado con vector de lado $(a,b)$ ocupa una caja envolvente de $(a+b)\times(a+b)$. Como la altura disponible es 2, se necesita $a+b\le 2$, lo que fuerza $(a,b)=(1,1)$, es decir lado $\sqrt2$.

Dentro de cada caja $2\times 2$ cabe exactamente un cuadrado de ese tipo, y hay $1\cdot(n-2)$ cajas: $n-2$ cuadrados.

Esto da justamente **tres tamaños** distintos: $1$, $\sqrt2$ y $2$ (consistente con el enunciado).

**Total:**

$$2(n-1) + (n-2) + (n-2) = 4n - 6 = 86 \implies n = 23$$

Verificación con $n=23$: $44 + 21 + 21 = 86$. ✓

\boxed{23}