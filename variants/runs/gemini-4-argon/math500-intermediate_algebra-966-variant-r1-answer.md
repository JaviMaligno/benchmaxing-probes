Para encontrar el valor mínimo de la expresión $a^4 + 6b^2 + 9c^4$, podemos utilizar la desigualdad entre la media aritmética y la media geométrica (MA-MG).

Primero, separamos el término $6b^2$ en dos partes iguales para que al multiplicar todos los términos obtengamos una potencia de $abc$:
\[a^4 + 6b^2 + 9c^4 = a^4 + 3b^2 + 3b^2 + 9c^4.\]

Aplicando la desigualdad MA-MG a estos cuatro términos positivos, obtenemos:
\[\frac{a^4 + 3b^2 + 3b^2 + 9c^4}{4} \ge \sqrt[4]{a^4 \cdot (3b^2) \cdot (3b^2) \cdot (9c^4)}.\]

Simplificamos el interior de la raíz cuarta:
\[a^4 \cdot 3b^2 \cdot 3b^2 \cdot 9c^4 = 81 a^4 b^4 c^4 = 81(abc)^4.\]

Dado que $abc = 3$, sustituimos este valor:
\[81(abc)^4 = 3^4 \cdot 3^4 = 3^8.\]

Por lo tanto, la desigualdad se convierte en:
\[a^4 + 6b^2 + 9c^4 \ge 4 \sqrt[4]{3^8} = 4 \cdot 3^2 = 4 \cdot 9 = 36.\]

Para verificar que este mínimo se puede alcanzar, comprobamos la condición de igualdad en MA-MG, la cual ocurre cuando todos los términos son iguales:
\[a^4 = 3b^2 = 9c^4 = 9.\]

De aquí obtenemos:
- $a^4 = 9 \implies a = \sqrt{3}$
- $3b^2 = 9 \implies b^2 = 3 \implies b = \sqrt{3}$
- $9c^4 = 9 \implies c^4 = 1 \implies c = 1$

Estos valores son reales positivos y cumplen que $abc = \sqrt{3} \cdot \sqrt{3} \cdot 1 = 3$.

\boxed{36}