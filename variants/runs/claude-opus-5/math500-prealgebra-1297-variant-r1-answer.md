## Razonamiento

El número de ceros finales de $47!$ está determinado por la cantidad de factores 10 en su descomposición, es decir, por $\min(v_2, v_5)$, donde $v_p$ es el exponente del primo $p$. Como los factores 2 son mucho más abundantes que los factores 5, basta contar los factores 5.

Usando la fórmula de Legendre:

$$v_5(47!) = \left\lfloor \frac{47}{5} \right\rfloor + \left\lfloor \frac{47}{25} \right\rfloor + \left\lfloor \frac{47}{125} \right\rfloor$$

- $\left\lfloor 47/5 \right\rfloor = 9$ → los múltiplos de 5: $5, 10, 15, 20, 25, 30, 35, 40, 45$
- $\left\lfloor 47/25 \right\rfloor = 1$ → el 25 aporta un factor 5 adicional
- $\left\lfloor 47/125 \right\rfloor = 0$

Total: $9 + 1 = 10$ factores de 5.

Verificación de que el 2 no es el limitante: $v_2(47!) = 23 + 11 + 5 + 2 + 1 = 42$, muy superior a 10.

Por tanto, $\min(42, 10) = 10$.

\boxed{10}