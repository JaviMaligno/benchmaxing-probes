## Razonamiento

La cuadrícula tiene 3 filas y $n$ columnas. Con solo 3 filas de puntos, los tamaños posibles de cuadrados son tres:

**1. Cuadrados $1\times 1$ (alineados con los ejes):** hay 2 posiciones verticales y $n-1$ horizontales:
$$2(n-1)$$

**2. Cuadrados $2\times 2$ (alineados con los ejes):** solo cabe 1 verticalmente, y $n-2$ horizontalmente:
$$n-2$$

**3. Cuadrados inclinados de lado $\sqrt2$:** cada uno se inscribe en un bloque $2\times 2$ uniendo los puntos medios de sus lados, uno por bloque:
$$n-2$$

(No hay inclinados mayores, pues requerirían más de 3 filas.)

**Total:**
$$2(n-1)+(n-2)+(n-2)=4n-6=70$$
$$4n=76 \quad\Longrightarrow\quad n=19$$

Verificación con $n=19$: $2\cdot 18 = 36$ cuadrados de lado 1, $17$ de lado 2, y $17$ inclinados, es decir $36+17+17=70$. ✓

\boxed{19}