## Razonamiento

El número de ceros finales de $47!$ está determinado por la cantidad de factores 10 en su descomposición, es decir, por $\min(\text{exponente de }2, \text{exponente de }5)$. Como los factores 2 son mucho más abundantes, basta contar los factores 5 (fórmula de Legendre):

$$\left\lfloor \frac{47}{5} \right\rfloor + \left\lfloor \frac{47}{25} \right\rfloor = 9 + 1 = 10$$

- Los 9 múltiplos de 5 hasta 47 son: 5, 10, 15, 20, 25, 30, 35, 40, 45.
- De ellos, el 25 aporta un factor 5 adicional (ya que $25 = 5^2$).

Total: 10 factores de 5. Y como los factores de 2 son claramente más de 10 ($\lfloor 47/2 \rfloor = 23$ ya solos), el mínimo es 10.

\boxed{10}