Voy a resolver el problema paso a paso.

## Planteamiento

Los ceros al final de un número provienen de factores de 10 = 2 × 5. Por lo tanto, necesito contar cuántas veces aparecen los factores 2 y 5 en la descomposición de 47!, y el número de ceros finales será el mínimo entre ambos conteos.

## Paso 1: Contar los factores de 5

Uso la fórmula de Legendre:

$$\left\lfloor \frac{47}{5} \right\rfloor + \left\lfloor \frac{47}{25} \right\rfloor = 9 + 1 = 10$$

- Los múltiplos de 5 hasta 47 son: 5, 10, 15, 20, 25, 30, 35, 40, 45 → **9 factores**
- El 25 (= 5²) aporta un factor adicional → **+1 factor**

Total de factores de 5: **10**

## Paso 2: Contar los factores de 2

$$\left\lfloor \frac{47}{2} \right\rfloor + \left\lfloor \frac{47}{4} \right\rfloor + \left\lfloor \frac{47}{8} \right\rfloor + \left\lfloor \frac{47}{16} \right\rfloor + \left\lfloor \frac{47}{32} \right\rfloor = 23 + 11 + 5 + 2 + 1 = 42$$

Los factores de 2 (42) superan ampliamente a los de 5 (10).

## Conclusión

El número de ceros al final de 47! está limitado por los factores de 5, que son exactamente 10.

$$\boxed{10}$$