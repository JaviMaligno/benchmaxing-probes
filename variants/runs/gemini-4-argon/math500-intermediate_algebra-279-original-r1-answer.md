Para encontrar los factores irreducibles de $x^8 + 3x^4 - 4$ sobre los enteros, comenzamos tratando el polinomio como una expresión cuadrática en términos de $x^4$:

\[x^8 + 3x^4 - 4 = (x^4 - 1)(x^4 + 4)\]

Ahora factorizamos cada uno de estos dos términos por separado:

1. **Factorización de $x^4 - 1$:**
   Aplicando diferencias de cuadrados sucesivamente:
   \[x^4 - 1 = (x^2 - 1)(x^2 + 1) = (x - 1)(x + 1)(x^2 + 1)\]
   Los polinomios $x - 1$, $x + 1$ y $x^2 + 1$ no pueden factorizarse más sobre los enteros.

2. **Factorización de $x^4 + 4$:**
   Utilizamos la identidad de Sophie Germain completando el cuadrado:
   \[x^4 + 4 = (x^4 + 4x^2 + 4) - 4x^2 = (x^2 + 2)^2 - (2x)^2 = (x^2 - 2x + 2)(x^2 + 2x + 2)\]
   Ambos factores cuadráticos tienen discriminante $\Delta = (\pm 2)^2 - 4(1)(2) = -4 < 0$, por lo que no tienen raíces reales y son irreducibles sobre los enteros.

Por lo tanto, la factorización completa en polinomios mónicos irreducibles sobre los enteros es:
\[x^8 + 3x^4 - 4 = (x - 1)(x + 1)(x^2 + 1)(x^2 - 2x + 2)(x^2 + 2x + 2)\]

Evaluamos cada factor $p_i(x)$ en $x = 1$:
* $p_1(1) = 1 - 1 = 0$
* $p_2(1) = 1 + 1 = 2$
* $p_3(1) = 1^2 + 1 = 2$
* $p_4(1) = 1^2 - 2(1) + 2 = 1$
* $p_5(1) = 1^2 + 2(1) + 2 = 5$

Sumando estos valores obtenemos:
\[p_1(1) + p_2(1) + p_3(1) + p_4(1) + p_5(1) = 0 + 2 + 2 + 1 + 5 = 10\]

\boxed{10}