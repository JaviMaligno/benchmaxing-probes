Para encontrar el valor mínimo de la expresión $x^4 + 4y^2 + 4z^4$ sujeto a la condición $xyz = 2$ con $x, y, z > 0$, podemos utilizar la desigualdad entre la media aritmética y la media geométrica (MA-MG).

Primero, descomponemos el término $4y^2$ en dos términos iguales de $2y^2$ para que, al multiplicar todos los términos, los exponentes de $x, y$ y $z$ sean iguales:
\[x^4 + 4y^2 + 4z^4 = x^4 + 2y^2 + 2y^2 + 4z^4.\]

Aplicando la desigualdad MA-MG a estos cuatro términos positivos, obtenemos:
\[\frac{x^4 + 2y^2 + 2y^2 + 4z^4}{4} \ge \sqrt[4]{x^4 \cdot (2y^2) \cdot (2y^2) \cdot (4z^4)}.\]

Simplificamos el interior de la raíz cuarta:
\[x^4 \cdot 2y^2 \cdot 2y^2 \cdot 4z^4 = 16x^4y^4z^4 = 16(xyz)^4.\]

Dado que $xyz = 2$, sustituimos este valor:
\[16(xyz)^4 = 16(2)^4 = 16 \cdot 16 = 256 = 4^4.\]

Por lo tanto, la desigualdad se convierte en:
\[\frac{x^4 + 4y^2 + 4z^4}{4} \ge \sqrt[4]{4^4} = 4,\]
lo que implica:
\[x^4 + 4y^2 + 4z^4 \ge 16.\]

Para verificar que este valor mínimo se puede alcanzar, comprobamos la condición de igualdad de la desigualdad MA-MG, la cual ocurre cuando todos los términos son iguales a $4$:
\[x^4 = 2y^2 = 4z^4 = 4.\]
Resolviendo para $x, y, z > 0$:
- $x^4 = 4 \implies x = \sqrt{2}$
- $2y^2 = 4 \implies y^2 = 2 \implies y = \sqrt{2}$
- $4z^4 = 4 \implies z^4 = 1 \implies z = 1$

Verificamos que estos valores cumplen la restricción: $xyz = \sqrt{2} \cdot \sqrt{2} \cdot 1 = 2$.

\boxed{16}