El número de ceros al final de un factorial depende de cuántas veces aparece el factor 10, es decir, el producto de 2 y 5. Como hay más factores 2 que 5, basta contar los factores 5.

Contamos los múltiplos de 5 hasta 42:

$$\left\lfloor \frac{42}{5} \right\rfloor = 8$$

Contamos los múltiplos de 25 (que aportan un factor 5 adicional):

$$\left\lfloor \frac{42}{25} \right\rfloor = 1$$

Como $25^2 = 625 > 42$, no hay más potencias de 5 que considerar.

Total de factores 5:

$$8 + 1 = 9$$

Por lo tanto, $42!$ termina en 9 ceros.

\boxed{9}