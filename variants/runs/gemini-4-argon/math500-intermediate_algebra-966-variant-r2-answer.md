Para encontrar el valor mínimo de la expresión $a^4 + 6b^2 + 9c^4$ sabiendo que $a, b, c$ son números reales positivos tales que $abc = 3$, podemos utilizar la desigualdad entre la media aritmética y la media geométrica (MA-MG).

Primero, separamos el término $6b^2$ en dos términos iguales para que, al multiplicarlos todos, las potencias de $a$, $b$ y $c$ sean iguales:
\[a^4 + 6b^2 + 9c^4 = a^4 + 3b^2 + 3b^2 + 9c^4\]

Aplicando la desigualdad MA-MG a estos cuatro términos positivos:
\[\frac{a^4 + 3b^2 + 3b^2 + 9c^4}{4} \ge \sqrt[4]{a^4 \cdot 3b^2 \cdot 3b^2 \cdot 9c^4}\]

Simplificando el lado derecho:
\[a^4 + 6b^2 + 9c^4 \ge 4 \sqrt[4]{81 a^4 b^4 c^4} = 4 \cdot 3abc = 12abc\]

Como sabemos que $abc = 3$, sustituimos este valor en la desigualdad:
\[a^4 + 6b^2 + 9c^4 \ge 12(3) = 36\]

Para verificar que este valor mínimo se puede alcanzar, comprobamos la condición de igualdad de la desigualdad MA-MG, que ocurre cuando los cuatro términos son iguales:
\[a^4 = 3b^2 = 9c^4 = \frac{36}{4} = 9\]

De aquí obtenemos:
- $a^4 = 9 \implies a = \sqrt{3}$
- $3b^2 = 9 \implies b^2 = 3 \implies b = \sqrt{3}$
- $9c^4 = 9 \implies c^4 = 1 \implies c = 1$

Estos valores son reales positivos y cumplen que $abc = \sqrt{3} \cdot \sqrt{3} \cdot 1 = 3$. Por lo tanto, el valor mínimo es $36$.

\boxed{36}