**Paso 1 — Contar los enteros impares positivos menores que 2010.**

Son: 1, 3, 5, …, 2009. Su cantidad es (2009 + 1)/2 = **1005** enteros posibles.

**Paso 2 — Condición para que 1/n tenga decimal terminante.**

1/n es un decimal finito si y solo si la factorización de n contiene únicamente los primos 2 y 5; es decir, n = 2^α · 5^β.

**Paso 3 — Aplicar la restricción de que n es impar.**

Como n es impar, no puede contener el factor 2, así que α = 0 y necesariamente n = 5^β (incluyendo β = 0, que da n = 1).

Buscamos las potencias de 5 menores que 2010:
- 5^0 = 1
- 5^1 = 5
- 5^2 = 25
- 5^3 = 125
- 5^4 = 625
- 5^5 = 3125 > 2010 ✗

Esto da **5** valores favorables: {1, 5, 25, 125, 625}.

**Paso 4 — Calcular la probabilidad y simplificar.**

$$\frac{a}{b} = \frac{5}{1005} = \frac{1}{201}$$

Como mcd(1, 201) = 1, la fracción ya está en términos mínimos: a = 1, b = 201.

**Paso 5 — Resultado.**

$$a + b = 1 + 201 = 202$$

\boxed{202}