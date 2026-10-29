Para encontrar el valor mínimo de la expresión $x^4 + 4y^2 + 4z^4$ sabiendo que $x, y, z$ son números reales positivos tales que $xyz = 2$, podemos utilizar la desigualdad entre la media aritmética y la media geométrica (MA-MG).

Primero, separamos el término $4y^2$ en dos partes iguales para que al multiplicar todos los términos las potencias de $x$, $y$ y $z$ sean iguales a $4$:
\[x^4 + 4y^2 + 4z^4 = x^4 + 2y^2 + 2y^2 + 4z^4.\]

Aplicando la desigualdad MA-MG a estos cuatro términos positivos, obtenemos:
\[\frac{x^4 + 2y^2 + 2y^2 + 4z^4}{4} \ge \sqrt[4]{x^4 \cdot (2y^2) \cdot (2y^2) \cdot (4z^4)}.\]

Simplificamos el interior de la raíz cuarta:
\[\sqrt[4]{16x^4y^4z^4} = 2xyz.\]

Sustituyendo la condición dada $xyz = 2$:
\[\frac{x^4 + 4y^2 + 4z^4}{4} \ge 2(2) = 4.\]

Multiplicando ambos lados por $4$, resulta:
\[x^4 + 4y^2 + 4z^4 \ge 16.\]

Finalmente, verificamos que la igualdad se alcanza cuando los cuatro términos son iguales entre sí, es decir, cuando $x^4 = 2y^2 = 4z^4 = 4$. Esto ocurre para los valores positivos $x = \sqrt{2}$, $y = \sqrt{2}$ y $z = 1$, los cuales cumplen que $xyz = \sqrt{2} \cdot \sqrt{2} \cdot 1 = 2$.

\boxed{16}