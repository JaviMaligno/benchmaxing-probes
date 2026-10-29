Vamos a resolver el problema paso a paso.

## Paso 1: Factorizar 2025

\[
2025 = 3^4 \cdot 5^2
\]

Los divisores positivos de \(2025\) son de la forma \(3^a 5^b\), con \(0 \le a \le 4\) y \(0 \le b \le 2\).

Entonces \(A\) tiene \(5 \cdot 3 = 15\) elementos.

## Paso 2: Condición sobre el mínimo común múltiplo

Queremos que el mcm de los elementos de \(B\) sea \(2025 = 3^4 5^2\). Esto requiere que:

1. Algún elemento de \(B\) tenga factor \(3^4\).
2. Algún elemento de \(B\) tenga factor \(5^2\).

Es decir, el mcm debe alcanzar la potencia máxima en ambos primos.

## Paso 3: Contar subconjuntos válidos

Consideremos todos los \(2^{15}\) subconjuntos de \(A\).

Para que el mcm sea \(2025\), debe cumplirse:

- No todos los elementos deben tener \(a \le 3\) (necesitamos al menos uno con \(a=4\)).
- No todos los elementos deben tener \(b \le 1\) (necesitamos al menos uno con \(b=2\)).

Los elementos con \(a=4\) son de la forma \(3^4 5^b\), con \(b \in \{0,1,2\}\): son 3 elementos.

Los elementos con \(b=2\) son de la forma \(3^a 5^2\), con \(a \in \{0,1,2,3,4\}\): son 5 elementos.

Queremos subconjuntos que contengan al menos un elemento con \(a=4\) y al menos uno con \(b=2\).

- Total de subconjuntos que contienen al menos un elemento con \(a=4\): \(2^{15} - 2^{12}\) (excluimos los que solo usan los 12 elementos con \(a \le 3\)).
- Total de subconjuntos que contienen al menos un elemento con \(b=2\): \(2^{15} - 2^{10}\) (excluimos los que solo usan los 10 elementos con \(b \le 1\)).

Por inclusión-exclusión, la cantidad de subconjuntos que cumplen ambas condiciones es:

\[
(2^{15} - 2^{12}) - (\text{subconjuntos con } b \le 1 \text{ y al menos un } a=4)
\]

El número de subconjuntos que no tienen \(b=2\) y tienen al menos un \(a=4\):

Los elementos con \(a=4\) y \(b \le 1\) son \(3^4\) y \(3^4 5\): 2 elementos. Los elementos con \(a \le 3\) y \(b \le 1\) son \(4 \cdot 2 = 8\) elementos. En total, 10 elementos con \(b \le 1\).

Los que tienen al menos un \(a=4\) entre esos 10: hay 2 elementos con \(a=4\) y 8 sin \(a=4\), entonces: \(2^{10} - 2^8\).

Por lo tanto:

\[
N = (2^{15} - 2^{12}) - (2^{10} - 2^8)
\]

\[
N = 2^{15} - 2^{12} - 2^{10} + 2^8
\]

\[
2^{15} = 32768,\quad 2^{12} = 4096,\quad 2^{10} = 1024,\quad 2^8 = 256
\]

\[
N = 32768 - 4096 - 1024 + 256 = 27904
\]

## Paso 4: Excluir el conjunto vacío

Pedimos que \(B\) sea **no vacío**. El conjunto vacío no tiene mcm, así que no lo contamos. Pero \(N\) ya cuenta solo subconjuntos que cumplen las condiciones, y el vacío no cumple tener al menos un \(a=4\), así que no está incluido. Entonces \(N\) ya es el número de subconjuntos **no vacíos** válidos.

## Paso 5: Probabilidad

\[
P = \frac{27904}{2^{15}} = \frac{27904}{32768}
\]

Simplificamos. Ambos son divisibles por 256:

\[
\frac{27904}{256} = 109, \quad \frac{32768}{256} = 128
\]

Entonces:

\[
P = \frac{109}{128}
\]

Aquí \(m = 109\), \(n = 128\), que son coprimos.

\[
m + n = 109 + 128 = 237
\]

\[
\boxed{237}
\]