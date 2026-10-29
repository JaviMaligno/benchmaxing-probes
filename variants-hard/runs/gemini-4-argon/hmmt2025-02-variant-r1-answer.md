Para encontrar todos los números de cinco dígitos $\underline{a b c d e}$ que cumplen la condición dada, expresemos el número en función de su primer dígito $a \in \{1, 2, \dots, 9\}$ y el número de cuatro dígitos restante $x = \underline{b c d e}$, donde $0 \le x \le 9999$:

$$\underline{a b c d e} = 10000a + x$$

La ecuación planteada en el problema es:

$$\sqrt{10000a + x} = a\sqrt{x}$$

Elevando ambos lados al cuadrado, obtenemos:

$$10000a + x = a^2 x$$

Reorganizando los términos para despejar $x$:

$$10000a = (a^2 - 1)x \implies x = \frac{10000a}{a^2 - 1}$$

Si $a = 1$, el denominador es $0$, lo cual no produce solución. Para $a \in \{2, 3, \dots, 9\}$, como $\text{mcd}(a, a^2 - 1) = 1$, para que $x$ sea un número entero es necesario que $a^2 - 1$ divida a $10000 = 2^4 \cdot 5^4$.

Analicemos cada valor posible de $a$:
- **$a = 2$:** $a^2 - 1 = 3$ (no divide a $10000$).
- **$a = 3$:** $a^2 - 1 = 8 = 2^3$, que sí divide a $10000$. Entonces:
  $$x = \frac{10000 \cdot 3}{8} = 3750$$
  Esto nos da el número de cinco dígitos **$33750$**.
- **$a = 4$:** $a^2 - 1 = 15 = 3 \cdot 5$ (no divide a $10000$).
- **$a = 5$:** $a^2 - 1 = 24 = 2^3 \cdot 3$ (no divide a $10000$).
- **$a = 6$:** $a^2 - 1 = 35 = 5 \cdot 7$ (no divide a $10000$).
- **$a = 7$:** $a^2 - 1 = 48 = 2^4 \cdot 3$ (no divide a $10000$).
- **$a = 8$:** $a^2 - 1 = 63 = 3^2 \cdot 7$ (no divide a $10000$).
- **$a = 9$:** $a^2 - 1 = 80 = 2^4 \cdot 5$, que sí divide a $10000$. Entonces:
  $$x = \frac{10000 \cdot 9}{80} = 1125$$
  Esto nos da el número de cinco dígitos **$91125$**.

Ambos valores de $x$ tienen cuatro dígitos ($3750$ y $1125$), por lo que los únicos números posibles son $33750$ y $91125$.

Finalmente, calculamos la suma de todos los números posibles:

$$33750 + 91125 = 124875$$

\boxed{124875}