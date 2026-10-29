Para encontrar la suma de los divisores primos distintos de $A$, seguimos estos pasos:

**Paso 1: Encontrar la factorización prima de $500$.**
$$500 = 5 \times 100 = 2^2 \times 5^3$$

**Paso 2: Calcular $A$, la suma de los divisores positivos de $500$.**
Usando la fórmula para la suma de divisores a partir de la factorización prima:
$$A = \sigma(500) = (1 + 2^1 + 2^2)(1 + 5^1 + 5^2 + 5^3)$$
$$A = (1 + 2 + 4)(1 + 5 + 25 + 125)$$
$$A = 7 \times 156$$

**Paso 3: Encontrar los divisores primos distintos de $A$.**
No necesitamos multiplicar $7 \times 156$; en su lugar, factorizamos $156$ en números primos:
$$156 = 2 \times 78 = 2 \times 2 \times 39 = 2^2 \times 3 \times 13$$

Por lo tanto, la factorización prima de $A$ es:
$$A = 2^2 \times 3 \times 7 \times 13$$

Los divisores primos distintos de $A$ son $2$, $3$, $7$ y $13$.

**Paso 4: Sumar los divisores primos distintos de $A$.**
$$2 + 3 + 7 + 13 = 25$$

\boxed{25}