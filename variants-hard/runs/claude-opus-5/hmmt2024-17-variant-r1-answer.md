Voy a resolverlo analíticamente y luego verifico con una simulación.

**Planteamiento.** Columnas $1,2,3,\dots$; $V_i$ = puerta vertical de la columna $i$ (abierta con prob. $3/4$), $T_i,B_i$ = puertas horizontales entre columnas $i$ e $i+1$ en la fila superior/inferior (abiertas con prob. $1/2$).

Proceso de izquierda a derecha con estados sobre $(\text{arriba}_i,\text{abajo}_i)$:

- **A**: ambas celdas en la componente del inicio.
- **B/C**: una en la componente del inicio, la otra en una componente "colgante" viva de tamaño $L$ (se demuestra, por planaridad del ladder, que esa componente colgante es siempre un tramo contiguo de una sola fila, luego $L$ basta como descriptor).
- **muerto**: ninguna de las dos; la componente ya no crece.

Déjame verificar el resultado numéricamente.

**Transiciones.** Desde A: $\to$A con $5/8$, $\to$B/C con $1/8$ ($L=1$), muerto con $1/4$; celdas añadidas en esperanza $11/8$.
Desde B/C: si la puerta horizontal del lado "vivo" está cerrada ($1/2$) $\to$ muerto; si abierta: con $3/4$ se abre $V_{i+1}$ y pasa a A añadiendo $2+\tfrac L2$ en esperanza; con $1/4$ sigue en B/C añadiendo $1$ celda y $L'=\tfrac L2+1$ en esperanza.