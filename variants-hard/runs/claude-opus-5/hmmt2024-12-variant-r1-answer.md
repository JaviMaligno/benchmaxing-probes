## Razonamiento

**Modelo del movimiento.** Con coordenadas (fila, columna), el rey cojo puede moverse a una celda vecina (de las 8 del rey) salvo las de su misma columna. Es decir, se eliminan los movimientos vertical arriba/abajo, y quedan: izquierda, derecha y las cuatro diagonales. En **todos** los casos la columna cambia exactamente en ±1.

**Cota superior.** Como cada movimiento cambia la columna en ±1, la paridad de la columna se alterna en cada paso. Las columnas impares (1, 3, 5, 7, 9) contienen 5·9 = 45 celdas y las pares (2, 4, 6, 8) contienen 4·9 = 36 celdas.

La casilla inicial (1,1) está en columna impar, así que el recorrido tiene la forma I, P, I, P, … En un camino de $n$ celdas hay $\lfloor n/2 \rfloor$ celdas en columnas pares, luego

$$\left\lfloor \frac{n}{2} \right\rfloor \le 36 \quad\Longrightarrow\quad n \le 73.$$

**Construcción de 73 celdas.** Recorremos las columnas por parejas en zigzag:

1. Columnas 1–2 hacia abajo: (1,1), (1,2), (2,1), (2,2), (3,1), (3,2), …, (9,1), (9,2) — 18 celdas. Los pasos (r,1)→(r,2) son horizontales y (r,2)→(r+1,1) son diagonales: todos válidos.
2. Paso (9,2)→(9,3) (horizontal).
3. Columnas 3–4 hacia arriba: (9,3), (9,4), (8,3), (8,4), …, (1,3), (1,4) — 18 celdas.
4. Paso (1,4)→(1,5); columnas 5–6 hacia abajo hasta (9,6) — 18 celdas.
5. Paso (9,6)→(9,7); columnas 7–8 hacia arriba hasta (1,8) — 18 celdas.
6. Paso final (1,8)→(1,9).

Esto cubre las 72 celdas de las columnas 1 a 8 más una celda de la columna 9: 73 celdas, todas distintas, y se alcanza exactamente la cota (36 pares + 37 impares).

\boxed{73}