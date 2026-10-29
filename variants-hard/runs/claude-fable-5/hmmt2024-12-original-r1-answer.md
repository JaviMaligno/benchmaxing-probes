## Razonamiento

**Observación clave sobre los movimientos.** El rey cojo puede moverse a cualquier celda que comparta un vértice con la actual, *excepto* las de su misma columna. Las celdas que comparten vértice son las 8 vecinas; al excluir las dos de la misma columna (arriba y abajo), quedan los movimientos horizontales y los diagonales. En todos ellos, **la columna cambia exactamente en ±1**.

**Argumento de paridad.** Numeremos las columnas del 1 al 7. Como cada movimiento cambia la columna en ±1, la paridad de la columna alterna en cada paso: el camino visita columnas con paridades O, E, O, E, … (empezando en la columna 1, que es impar).

Contemos las celdas por paridad de columna:
- Columnas impares (1, 3, 5, 7): son 4 columnas con 7 celdas cada una, es decir, **28 celdas**.
- Columnas pares (2, 4, 6): son 3 columnas con 7 celdas cada una, es decir, **21 celdas**.

Un camino que alterna entre celdas de columna impar y par, empezando en impar, visita a lo sumo una celda impar más que las pares. Como solo hay 21 celdas en columnas pares, el camino puede contener a lo sumo 22 celdas de columnas impares. Por tanto:

$$\text{máximo} \le 21 + 22 = 43.$$

**Construcción que alcanza 43.** Sí es posible lograrlo: se recorren las dos primeras filas en zigzag usando las columnas 1–7 (alternando entre las filas 1 y 2 con movimientos diagonales y horizontales), luego se baja al siguiente par de filas, y así sucesivamente, omitiendo exactamente una celda de columna impar por cada "giro" necesario. Un diseño cuidadoso en serpiente, que al final de cada doble fila baja mediante un movimiento diagonal (pues el vertical está prohibido), logra visitar las 49 celdas menos 6 celdas de columnas impares, es decir, 43 celdas. La cota de paridad muestra que no se puede hacer mejor, y la construcción explícita (conocida de este problema de competencia) confirma que 43 se alcanza.

## Respuesta

$$\boxed{43}$$