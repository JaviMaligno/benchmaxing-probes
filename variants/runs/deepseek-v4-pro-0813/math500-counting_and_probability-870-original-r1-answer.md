El problema clásico de dos cuerdas en una circunferencia.

**Razonamiento:**

1. Colocamos los cuatro puntos $A$, $B$, $C$, $D$ sobre la circunferencia.

2. Para que los segmentos $AB$ y $CD$ se intersecten (en el interior del círculo), los extremos deben estar **alternados** alrededor de la circunferencia. Es decir, al recorrerla en algún sentido, el orden debe ser $A, C, B, D$ o $A, D, B, C$.

3. Hay en total $4! = 24$ ordenamientos posibles de los cuatro puntos alrededor del círculo (considerando todas las formas de etiquetarlos).

4. De esos, ¿cuántos tienen los puntos alternados con $A$ y $B$ separados por $C$ y $D$?

   - Fijamos las posiciones alrededor del círculo (4 posiciones).
   - $A$ y $B$ deben ocupar posiciones opuestas (separadas por un punto intermedio): hay 4 formas de elegir la posición de $A$, y para $B$ deben quedar así separadas; en un arreglo circular, la otra posición "opuesta" queda determinada.
   - Una vez elegidas las posiciones de $A$ y $B$, $C$ y $D$ ocupan las otras dos posiciones de 2 formas distintas.
   
   Más sencillo: de los $4! = 24$ órdenes lineales (con un punto tomado como inicio), los que producen cuerdas que se cruzan son exactamente $8$.

5. Por lo tanto,

\[
P = \frac{8}{24} = \frac{1}{3}
\]

La probabilidad de que los segmentos $AB$ y $CD$ se intersecten es $\frac{1}{3}$.

\[
\boxed{\frac{1}{3}}
\]