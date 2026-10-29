# Análisis del problema

**Movimientos permitidos.** Una casilla comparte al menos un vértice con las 8 casillas vecinas (adyacentes por lado o por esquina). De estas, las que están en la misma columna son la casilla directamente arriba y la directamente abajo, que quedan prohibidas. Por tanto, desde \((r,c)\) el rey cojo solo puede moverse a:
- \((r, c\pm 1)\) (movimientos horizontales),
- \((r\pm 1, c\pm 1)\) (movimientos diagonales).

**Observación clave:** en todo movimiento la columna cambia exactamente en \(1\). Nunca se puede permanecer en la misma columna ni saltar más de una columna.

# Cota superior

Coloreamos las casillas según la paridad de su columna:
- Columnas impares \(1,3,5,7,9\): \(5 \times 9 = 45\) casillas.
- Columnas pares \(2,4,6,8\): \(4 \times 9 = 36\) casillas.

Como cada movimiento cambia la columna en \(1\), cada movimiento cambia la paridad de la columna. Así, cualquier camino alterna entre casillas de columna impar y casillas de columna par.

El camino empieza en \((1,1)\), que está en una columna impar. Un camino que visite \(L\) casillas contiene \(\lceil L/2\rceil\) casillas de columnas impares y \(\lfloor L/2\rfloor\) de columnas pares. Como solo hay 36 casillas de columnas pares:
\[
\lfloor L/2\rfloor \le 36 \implies L \le 73.
\]

# Construcción que alcanza 73

Serpenteamos por pares de columnas (usando movimientos horizontales y diagonales, todos válidos):

1. **Columnas 1–2 (bajando):** \((1,1)\to(1,2)\to(2,1)\to(2,2)\to\cdots\to(9,1)\to(9,2)\). Cada paso es horizontal o diagonal: válido. Termina en \((9,2)\). (18 casillas.)
2. **Paso a columna 3:** \((9,2)\to(9,3)\) (horizontal).
3. **Columnas 3–4 (subiendo):** \((9,3)\to(9,4)\to(8,3)\to(8,4)\to\cdots\to(1,3)\to(1,4)\). Termina en \((1,4)\). (18 casillas.)
4. **Paso a columna 5:** \((1,4)\to(1,5)\).
5. **Columnas 5–6 (bajando):** \((1,5)\to(1,6)\to(2,5)\to(2,6)\to\cdots\to(9,5)\to(9,6)\). Termina en \((9,6)\). (18 casillas.)
6. **Paso a columna 7:** \((9,6)\to(9,7)\).
7. **Columnas 7–8 (subiendo):** \((9,7)\to(9,8)\to(8,7)\to(8,8)\to\cdots\to(1,7)\to(1,8)\). Termina en \((1,8)\). (18 casillas.)
8. **Paso a columna 9:** \((1,8)\to(1,9)\). (1 casilla; los únicos vecinos de \((1,9)\), namely \((1,8)\) y \((2,8)\), ya fueron visitados, así que el camino termina aquí.)

Total: \(18+18+18+18+1 = 73\) casillas, todas distintas, comenzando en la esquina superior izquierda.

Como la cota superior (73) coincide con la construcción, el máximo es:

\[
\boxed{73}
\]