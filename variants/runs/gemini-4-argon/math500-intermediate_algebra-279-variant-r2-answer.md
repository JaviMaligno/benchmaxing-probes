Para encontrar el valor de $q_1(1) + q_2(1) + \dots + q_m(1)$, primero factorizamos completamente el polinomio $x^8 + 63x^4 - 64$ en polinomios mónicos irreducibles sobre los enteros.

**Paso 1: Factorización inicial tratando el polinomio como cuadrático en $x^4$.**
Haciendo el cambio de variable $y = x^4$, tenemos:
\[y^2 + 63y - 64 = (y - 1)(y + 64)\]
Sustituyendo $y = x^4$ de vuelta, obtenemos:
\[x^8 + 63x^4 - 64 = (x^4 - 1)(x^4 + 64)\]

**Paso 2: Factorizar $x^4 - 1$.**
Usando la diferencia de cuadrados:
\[x^4 - 1 = (x^2 - 1)(x^2 + 1) = (x - 1)(x + 1)(x^2 + 1)\]
Los polinomios $x - 1$, $x + 1$ y $x^2 + 1$ no se pueden factorizar más sobre los enteros, por lo que son irreducibles.

**Paso 3: Factorizar $x^4 + 64$.**
Utilizamos la identidad de Sophie Germain completando el cuadrado:
\[x^4 + 64 = (x^4 + 16x^2 + 64) - 16x^2 = (x^2 + 8)^2 - (4x)^2\]
Aplicando la diferencia de cuadrados:
\[(x^2 + 8)^2 - (4x)^2 = (x^2 - 4x + 8)(x^2 + 4x + 8)\]
El discriminante de ambos polinomios cuadráticos es $\Delta = (\pm 4)^2 - 4(1)(8) = 16 - 32 = -16 < 0$. Como son de grado $2$ y no tienen raíces reales (y por ende tampoco enteras), ambos son irreducibles sobre los enteros.

**Paso 4: Evaluación en $x = 1$ y suma.**
La factorización completa en polinomios mónicos irreducibles es:
\[x^8 + 63x^4 - 64 = (x - 1)(x + 1)(x^2 + 1)(x^2 - 4x + 8)(x^2 + 4x + 8)\]

Evaluamos cada factor $q_i(x)$ en $x = 1$:
- $q_1(1) = 1 - 1 = 0$
- $q_2(1) = 1 + 1 = 2$
- $q_3(1) = 1^2 + 1 = 2$
- $q_4(1) = 1^2 - 4(1) + 8 = 5$
- $q_5(1) = 1^2 + 4(1) + 8 = 13$

Sumando estos resultados:
\[0 + 2 + 2 + 5 + 13 = 22\]

\boxed{22}