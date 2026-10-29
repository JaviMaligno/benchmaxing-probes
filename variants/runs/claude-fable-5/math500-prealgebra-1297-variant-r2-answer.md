Para contar los ceros finales de $47!$, hay que contar cuántos factores de 10 contiene, es decir, cuántas parejas de factores 2 y 5 hay. Como los factores 2 abundan mucho más que los 5, basta contar los factores 5.

Usando la fórmula de Legendre:

- Múltiplos de 5 hasta 47: $\lfloor 47/5 \rfloor = 9$ (que son 5, 10, 15, 20, 25, 30, 35, 40, 45)
- Múltiplos de 25 hasta 47: $\lfloor 47/25 \rfloor = 1$ (el 25 aporta un factor 5 adicional)
- Múltiplos de 125: $\lfloor 47/125 \rfloor = 0$

Total de factores 5: $9 + 1 = 10$. Como hay más que suficientes factores 2 para emparejarlos, $47!$ termina en 10 ceros.

$$\boxed{10}$$