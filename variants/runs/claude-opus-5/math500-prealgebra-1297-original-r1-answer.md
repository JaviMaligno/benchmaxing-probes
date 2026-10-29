## Razonamiento

El número de ceros finales de $42!$ está determinado por la cantidad de factores $10 = 2 \cdot 5$ en su descomposición. Como los factores 2 son mucho más abundantes que los factores 5, basta contar los factores 5.

Usando la fórmula de Legendre:

$$\left\lfloor \frac{42}{5} \right\rfloor + \left\lfloor \frac{42}{25} \right\rfloor = 8 + 1 = 9$$

- Los 8 múltiplos de 5 hasta 42 son: 5, 10, 15, 20, 25, 30, 35, 40.
- De ellos, el 25 aporta un factor 5 adicional (25 = 5²).

Total: 9 factores de 5, y hay sobrados factores 2 (por ejemplo, $\lfloor 42/2 \rfloor = 21$ ya supera 9), así que se forman exactamente 9 factores de 10.

\boxed{9}