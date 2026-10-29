Para encontrar el número de ceros al final de $42!$, debemos determinar cuántas veces es divisible por $10$. Como $10 = 2 \times 5$ y en el desarrollo de un factorial siempre hay más factores de $2$ que de $5$, basta con contar cuántos factores de $5$ hay en la factorización prima de $42!$.

Utilizando la fórmula de Legendre para contar los factores de $5$ en $42!$:

1. Dividimos $42$ entre $5$ y tomamos la parte entera para contar los múltiplos de $5$:
   $$\left\lfloor \frac{42}{5} \right\rfloor = 8$$
   (Estos corresponden a $5, 10, 15, 20, 25, 30, 35, 40$).

2. Dividimos $42$ entre $5^2 = 25$ y tomamos la parte entera para contar el factor adicional de $5$ que aportan los múltiplos de $25$:
   $$\left\lfloor \frac{42}{25} \right\rfloor = 1$$
   (Este corresponde al número $25$).

3. Como $5^3 = 125 > 42$, no hay más potencias de $5$ que debamos considerar.

Sumamos las cantidades obtenidas:
$$8 + 1 = 9$$

\boxed{9}