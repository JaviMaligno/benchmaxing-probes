Para encontrar el valor de $q_1(1) + q_2(1) + \dots + q_m(1)$, primero factorizamos completamente el polinomio $P(x) = x^8 + 63x^4 - 64$ en polinomios mónicos irreducibles sobre los enteros.

**Paso 1: Factorización inicial como cuadrática en $x^4$**
Podemos tratar $x^8 + 63x^4 - 64$ como un polinomio cuadrático en términos de $u = x^4$:
$$u^2 + 63u - 64 = (u + 64)(u - 1)$$
Sustituyendo nuevamente $u = x^4$, obtenemos:
$$x^8 + 63x^4 - 64 = (x^4 + 64)(x^4 - 1)$$

**Paso 2: Factorizar $x^4 - 1$**
Usando la diferencia de cuadrados dos veces:
$$x^4 - 1 = (x^2 - 1)(x^2 + 1) = (x - 1)(x + 1)(x^2 + 1)$$
Los factores $x - 1$, $x + 1$ y $x^2 + 1$ son mónicos e irreducibles sobre los enteros.

**Paso 3: Factorizar $x^4 + 64$**
Aplicamos la identidad de Sophie Germain completando el cuadrado:
$$x^4 + 64 = (x^4 + 16x^2 + 64) - 16x^2 = (x^2 + 8)^2 - (4x)^2$$
Aplicando diferencia de cuadrados:
$$x^4 + 64 = (x^2 - 4x + 8)(x^2 + 4x + 8)$$
El discriminante de ambos factores cuadráticos es $\Delta = (\pm 4)^2 - 4(1)(8) = 16 - 32 = -16 < 0$. Como no tienen raíces reales, tampoco tienen raíces enteras ni racionales, por lo que ambos son irreducibles sobre los enteros.

**Paso 4: Evaluar en $x = 1$ y sumar**
La factorización completa en polinomios mónicos irreducibles es:
$$x^8 + 63x^4 - 64 = (x - 1)(x + 1)(x^2 + 1)(x^2 - 4x + 8)(x^2 + 4x + 8)$$

Evaluamos cada factor $q_i(x)$ en $x = 1$:
- $q_1(1) = 1 - 1 = 0$
- $q_2(1) = 1 + 1 = 2$
- $q_3(1) = 1^2 + 1 = 2$
- $q_4(1) = 1^2 - 4(1) + 8 = 5$
- $q_5(1) = 1^2 + 4(1) + 8 = 13$

Sumando todos los valores obtenidos:
$$0 + 2 + 2 + 5 + 13 = 22$$

\boxed{22}