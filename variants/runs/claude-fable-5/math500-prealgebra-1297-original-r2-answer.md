Para contar los ceros al final de $42!$, hay que contar cuántas veces aparece el factor 10 en el producto, es decir, cuántos pares de factores $2 \times 5$ hay. Como los factores 2 abundan mucho más que los factores 5, basta contar los factores 5.

Usando la fórmula de Legendre:

- Múltiplos de 5 hasta 42: $\lfloor 42/5 \rfloor = 8$ (que son 5, 10, 15, 20, 25, 30, 35, 40), cada uno aporta al menos un factor 5.
- Múltiplos de 25 hasta 42: $\lfloor 42/25 \rfloor = 1$ (el 25), que aporta un factor 5 adicional.
- Múltiplos de 125: $\lfloor 42/125 \rfloor = 0$, así que no hay más contribuciones.

Total de factores 5: $8 + 1 = 9$. Como hay factores 2 de sobra para emparejarlos, $42!$ termina en 9 ceros.

$$\boxed{9}$$