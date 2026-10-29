Para encontrar la cantidad de ceros al final de $42!$, debemos determinar cuántas veces es divisible por $10$. Como $10 = 2 \times 5$ y en el desarrollo de un factorial siempre hay más factores de $2$ que de $5$, la cantidad de ceros finales está determinada por el número de veces que el factor primo $5$ aparece en la factorización de $42!$.

Utilizando la fórmula de Legendre, contamos los múltiplos de las potencias de $5$ menores o iguales a $42$:

1. Múltiplos de $5$: $\lfloor \frac{42}{5} \rfloor = 8$ (que corresponden a $5, 10, 15, 20, 25, 30, 35, 40$).
2. Múltiplos de $25$ ($5^2$), que aportan un factor de $5$ adicional: $\lfloor \frac{42}{25} \rfloor = 1$ (que corresponde a $25$).
3. Múltiplos de $125$ ($5^3$): $\lfloor \frac{42}{125} \rfloor = 0$.

Sumando todos los factores de $5$:
$$8 + 1 = 9$$

\boxed{9}