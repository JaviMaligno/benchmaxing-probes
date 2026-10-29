Para determinar cuántos ceros hay al final de $47!$, debemos contar cuántas veces aparece el factor $10$ en su descomposición en factores primos. Como $10 = 2 \times 5$ y en el producto de los números del $1$ al $47$ hay muchos más factores de $2$ que de $5$, la cantidad de ceros al final estará determinada por la cantidad total de factores de $5$.

Podemos calcular el número de factores de $5$ en $47!$ utilizando la fórmula de Legendre:

1. Contamos cuántos múltiplos de $5$ hay del $1$ al $47$:
   $$\left\lfloor \frac{47}{5} \right\rfloor = 9$$
   (Estos son: $5, 10, 15, 20, 25, 30, 35, 40, 45$).

2. Contamos cuántos múltiplos de $5^2 = 25$ hay del $1$ al $47$, ya que cada uno aporta un factor adicional de $5$:
   $$\left\lfloor \frac{47}{25} \right\rfloor = 1$$
   (Este es el número $25$).

3. Como $5^3 = 125 > 47$, no hay múltiplos de potencias mayores de $5$.

Sumando las contribuciones obtenemos el total de factores de $5$:
$$9 + 1 = 10$$

\boxed{10}