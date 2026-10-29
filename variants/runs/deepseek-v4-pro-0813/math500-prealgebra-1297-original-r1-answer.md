Los ceros finales de un factorial provienen de factores de 10, es decir, de cada pareja de factores 2 y 5. Como en un factorial hay muchos más factores 2 que 5, basta con contar cuántas veces aparece el factor 5 en los números del 1 al 42.

Contamos los múltiplos de 5:

- Múltiplos de 5 hasta 42:  
  \(\left\lfloor \frac{42}{5} \right\rfloor = 8\)

- Múltiplos de 25 hasta 42 (aportan un 5 extra):  
  \(\left\lfloor \frac{42}{25} \right\rfloor = 1\)

- No hay múltiplos de 125, porque 125 > 42.

Total de factores 5:

\[
8 + 1 = 9
\]

Por lo tanto, \(42!\) tiene 9 ceros al final.

\[
\boxed{9}
\]