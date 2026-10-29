Para determinar cuántos ceros hay al final de $47!$, debemos contar cuántas veces aparece el factor $10$ en su descomposición prima. Como $10 = 2 \times 5$ y en cualquier factorial siempre hay más factores de $2$ que de $5$, la cantidad de ceros al final está determinada por el número total de factores de $5$ en la descomposición prima de $47!$.

Podemos calcular el número de factores de $5$ utilizando la fórmula de Legendre:

1. Contamos los múltiplos de $5$ menores o iguales a $47$:
   $$\left\lfloor \frac{47}{5} \right\rfloor = 9$$
   (Estos son: $5, 10, 15, 20, 25, 30, 35, 40, 45$, cada uno aportando al menos un factor de $5$).

2. Contamos los múltiplos de $5^2 = 25$ menores o iguales a $47$, ya que aportan un factor adicional de $5$:
   $$\left\lfloor \frac{47}{25} \right\rfloor = 1$$
   (Este es el número $25$).

3. Como $5^3 = 125 > 47$, no hay múltiplos de potencias mayores de $5$.

Sumando las contribuciones:
$$9 + 1 = 10$$

\boxed{10}