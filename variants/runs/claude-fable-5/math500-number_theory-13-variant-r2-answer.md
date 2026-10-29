Resolvamos la congruencia paso a paso.

**Paso 1: Simplificar.** Como $\gcd(22, 100) = 2$ y $2 \mid 38$, la congruencia tiene solución y podemos dividir todo entre 2:
$$11x \equiv 19 \pmod{50}$$

**Paso 2: Hallar el inverso de 11 módulo 50.** Buscamos $y$ tal que $11y \equiv 1 \pmod{50}$. Probando: $11 \cdot 41 = 451 = 9 \cdot 50 + 1$, así que el inverso es $41$.

**Paso 3: Despejar $x$.**
$$x \equiv 41 \cdot 19 = 779 \equiv 779 - 750 = 29 \pmod{50}$$

**Paso 4: Las dos soluciones positivas más pequeñas.** Como $x \equiv 29 \pmod{50}$, las dos menores son $x = 29$ y $x = 79$ (ambas verifican la congruencia original módulo 100, pues $22 \cdot 29 = 638 \equiv 38$ y $22 \cdot 79 = 1738 \equiv 38 \pmod{100}$).

**Paso 5: Promedio.**
$$\frac{29 + 79}{2} = 54$$

$$\boxed{54}$$