## Planteamiento

La serie es geométrica con primer término $a_1 = 3$ y razón
$$r = \frac{15/a}{3} = \frac{5}{a}.$$

**Convergencia:** se requiere $|5/a| < 1$, es decir $a > 5$ (con $a$ entero positivo).

**Suma:**
$$S = \frac{3}{1 - \frac{5}{a}} = \frac{3a}{a-5}.$$

## Condición de cuadrado perfecto

Reescribimos:
$$S = \frac{3(a-5) + 15}{a-5} = 3 + \frac{15}{a-5}.$$

Para que $S$ sea entero, $(a-5)$ debe dividir a 15: $a-5 \in \{1, 3, 5, 15\}$, o sea $a \in \{6, 8, 10, 20\}$.

| $a$ | $S = 3 + \frac{15}{a-5}$ | ¿Cuadrado? |
|---|---|---|
| 6 | 18 | no |
| 8 | 8 | no |
| 10 | 6 | no |
| 20 | 4 | sí ($2^2$) |

Verificando además los valores no enteros intermedios ($a = 7, 9, 11, \dots, 19$), ninguno da un cuadrado racional: por ejemplo $a=9 \Rightarrow 27/4$, $a=17 \Rightarrow 17/4$, $a=15 \Rightarrow 9/2$.

El único caso válido, y por tanto el menor, es $a = 20$, donde la serie es $3 + \frac{3}{4} + \frac{3}{16} + \cdots = 4 = 2^2$.

\boxed{20}