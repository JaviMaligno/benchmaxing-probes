**Paso 1: Suma de los divisores de 500.**

Factorizamos $500 = 2^2 \cdot 5^3$.

La función sigma para un número $p^a \cdot q^b$ es $\frac{p^{a+1}-1}{p-1}\cdot\frac{q^{b+1}-1}{q-1}$:

$$A = \sigma(500) = (1 + 2 + 4)(1 + 5 + 25 + 125) = 7 \cdot 156 = 1092$$

**Paso 2: Factorización de $A = 1092$.**

$$1092 = 4 \cdot 273 = 2^2 \cdot 3 \cdot 91 = 2^2 \cdot 3 \cdot 7 \cdot 13$$

**Paso 3: Suma de los primos distintos.**

Los divisores primos distintos de $A$ son $2$, $3$, $7$ y $13$:

$$2 + 3 + 7 + 13 = 25$$

\boxed{25}