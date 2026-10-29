## Razonamiento

**Observación clave sobre los movimientos.** El rey cojo puede moverse a cualquier celda que comparta un vértice con la suya, excepto las de su misma columna. Las celdas vecinas por vértice están a distancia a lo más 1 en fila y columna; al excluir la misma columna, **todo movimiento cambia la columna exactamente en ±1** (movimientos horizontales o diagonales).

**Cota superior.** Numeremos las columnas del 1 al 9. Como cada movimiento cambia la columna en ±1, la paridad de la columna alterna en cada paso. Hay 5 columnas impares (45 celdas) y 4 columnas pares (36 celdas). El rey empieza en la columna 1 (impar), así que su recorrido tiene la forma I, P, I, P, …, donde las celdas de columna impar y par se alternan. Por tanto:

$$\#\text{impares} \le \#\text{pares} + 1 \le 36 + 1 = 37,$$

y el total de celdas visitadas es a lo más $36 + 37 = 73$.

**Construcción que alcanza 73.** Usamos zigzags por pares de columnas (cada paso es horizontal o diagonal, nunca dentro de una misma columna):

1. Bajar por las columnas 1–2: $(1,1)\to(1,2)\to(2,1)\to(2,2)\to\cdots\to(9,1)\to(9,2)$ — 18 celdas.
2. Paso horizontal a $(9,3)$ y subir por las columnas 3–4: $(9,3)\to(9,4)\to(8,3)\to(8,4)\to\cdots\to(1,3)\to(1,4)$ — 18 celdas.
3. Paso a $(1,5)$ y bajar por las columnas 5–6 igual que antes, terminando en $(9,6)$ — 18 celdas.
4. Paso a $(9,7)$ y subir por las columnas 7–8, terminando en $(1,8)$ — 18 celdas.
5. Paso horizontal final a $(1,9)$ — 1 celda.

Todos los movimientos son válidos (horizontales o diagonales) y ninguna celda se repite. Total: $18 \times 4 + 1 = 73$ celdas, que coincide con la cota.

$$\boxed{73}$$