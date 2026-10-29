Los ceros al final de $42!$ provienen de los factores 10, es decir, de los pares de factores $2 \times 5$. Como en un factorial hay muchos más factores 2 que factores 5, basta contar cuántas veces aparece el factor 5 en $42!$.

**Paso 1: múltiplos de 5 hasta 42.**
$\lfloor 42/5 \rfloor = 8$ (que son 5, 10, 15, 20, 25, 30, 35 y 40), aportando un factor 5 cada uno.

**Paso 2: múltiplos de 25 hasta 42.**
$\lfloor 42/25 \rfloor = 1$ (solo el 25), que aporta un factor 5 adicional.

**Paso 3: múltiplos de 125.**
$\lfloor 42/125 \rfloor = 0$, así que no hay más contribuciones.

El total de factores 5 es $8 + 1 = 9$, y como hay factores 2 de sobra, $42!$ termina en 9 ceros.

$$\boxed{9}$$