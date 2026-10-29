El número de ceros al final de $n!$ es igual a la cantidad de factores de $10$ que contiene. Como $10 = 2 \cdot 5$, y en $n!$ siempre hay más factores de $2$ que de $5$, basta con contar cuántas veces aparece el factor $5$.

Para $47!$, contamos los múltiplos de $5$, de $25$, de $125$, etc., hasta que el cociente sea menor que $1$:

$$
\left\lfloor \frac{47}{5} \right\rfloor = 9
$$

$$
\left\lfloor \frac{47}{25} \right\rfloor = 1
$$

$$
\left\lfloor \frac{47}{125} \right\rfloor = 0
$$

Sumamos: $9 + 1 = 10$.

Por lo tanto, $47!$ termina en $10$ ceros.

\boxed{10}