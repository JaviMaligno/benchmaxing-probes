Para encontrar la suma $p_1(1) + p_2(1) + \dots + p_k(1)$, primero factorizamos completamente el polinomio $x^8 + 3x^4 - 4$ en polinomios mónicos irreducibles con coeficientes enteros.

1. **Factorización como cuadrática en $x^4$:**
   Podemos ver el polinomio como $(x^4)^2 + 3(x^4) - 4$, lo cual se factoriza como:
   $$x^8 + 3x^4 - 4 = (x^4 - 1)(x^4 + 4)$$

2. **Factorización de $x^4 - 1$:**
   Aplicando diferencia de cuadrados dos veces:
   $$x^4 - 1 = (x^2 - 1)(x^2 + 1) = (x - 1)(x + 1)(x^2 + 1)$$
   Los polinomios $x - 1$, $x + 1$ y $x^2 + 1$ no se pueden factorizar más sobre los enteros.

3. **Factorización de $x^4 + 4$ (identidad de Sophie Germain):**
   Completamos el cuadrado sumando y restando $4x^2$:
   $$x^4 + 4 = (x^4 + 4x^2 + 4) - 4x^2 = (x^2 + 2)^2 - (2x)^2 = (x^2 - 2x + 2)(x^2 + 2x + 2)$$
   Ambos factores cuadráticos tienen discriminante $\Delta = (\pm 2)^2 - 4(1)(2) = -4 < 0$, por lo que no tienen raíces reales y son irreducibles sobre los enteros.

4. **Factorización completa y evaluación en $x = 1$:**
   Por lo tanto, la factorización completa es:
   $$x^8 + 3x^4 - 4 = (x - 1)(x + 1)(x^2 + 1)(x^2 - 2x + 2)(x^2 + 2x + 2)$$

   Evaluando cada factor $p_i(x)$ en $x = 1$:
   - $p_1(1) = 1 - 1 = 0$
   - $p_2(1) = 1 + 1 = 2$
   - $p_3(1) = 1^2 + 1 = 2$
   - $p_4(1) = 1^2 - 2(1) + 2 = 1$
   - $p_5(1) = 1^2 + 2(1) + 2 = 5$

5. **Suma de los valores:**
   $$p_1(1) + p_2(1) + p_3(1) + p_4(1) + p_5(1) = 0 + 2 + 2 + 1 + 5 = 10$$

\boxed{10}