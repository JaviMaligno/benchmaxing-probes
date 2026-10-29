Para encontrar el mayor valor posible de la expresión dada, primero podemos simplificarla utilizando la identidad de la diferencia de cuadrados:

$$\left(a+\frac{1}{b}\right)\left(\frac{1}{b}-a\right) = \left(\frac{1}{b}+a\right)\left(\frac{1}{b}-a\right) = \frac{1}{b^2} - a^2$$

Para maximizar el valor de $\frac{1}{b^2} - a^2$, debemos maximizar el primer término $\left(\frac{1}{b^2}\right)$ y minimizar el segundo término $\left(a^2\right)$, dado que $a$ y $b$ son variables independientes.

1. **Maximizar $\frac{1}{b^2}$:**
   Sabemos que $3 \leq b \leq 5$. Como $b$ es positivo, para que la fracción $\frac{1}{b^2}$ sea lo más grande posible, el denominador $b^2$ debe ser lo más pequeño posible. Esto ocurre cuando $b = 3$:
   $$\frac{1}{b^2} \leq \frac{1}{3^2} = \frac{1}{9}$$

2. **Minimizar $a^2$:**
   Sabemos que $-6 \leq a \leq -2$. Al elevar al cuadrado números negativos, el orden de la desigualdad se invierte, por lo que $(-2)^2 \leq a^2 \leq (-6)^2$, es decir, $4 \leq a^2 \leq 36$. El menor valor posible de $a^2$ ocurre cuando $a = -2$:
   $$a^2 \geq (-2)^2 = 4$$

3. **Calcular el valor máximo:**
   Sustituyendo estos valores extremos en nuestra expresión simplificada, obtenemos:
   $$\frac{1}{9} - 4 = \frac{1}{9} - \frac{36}{9} = -\frac{35}{9}$$

\boxed{-\frac{35}{9}}