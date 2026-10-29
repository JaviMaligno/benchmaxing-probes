Para encontrar el valor máximo de $ab^2 c^3 d^4$ sujeto a la condición $a + b + c + d = 10$ con $a, b, c, d > 0$, podemos utilizar la desigualdad entre la media aritmética y la media geométrica (MA-MG).

Reescribimos la suma $a + b + c + d$ dividiendo cada variable en partes iguales según su exponente en el producto:
$$a + b + c + d = a + \frac{b}{2} + \frac{b}{2} + \frac{c}{3} + \frac{c}{3} + \frac{c}{3} + \frac{d}{4} + \frac{d}{4} + \frac{d}{4} + \frac{d}{4}$$

Aplicando la desigualdad MA-MG a estos $1 + 2 + 3 + 4 = 10$ términos positivos, obtenemos:
$$\frac{a + 2\left(\frac{b}{2}\right) + 3\left(\frac{c}{3}\right) + 4\left(\frac{d}{4}\right)}{10} \ge \sqrt[10]{a \left(\frac{b}{2}\right)^2 \left(\frac{c}{3}\right)^3 \left(\frac{d}{4}\right)^4}$$

Dado que $a + b + c + d = 10$, el lado izquierdo de la desigualdad es igual a $\frac{10}{10} = 1$. Sustituyendo y elevando ambos lados a la décima potencia:
$$1^{10} \ge \frac{ab^2 c^3 d^4}{1^1 \cdot 2^2 \cdot 3^3 \cdot 4^4}$$

Despejando el producto $ab^2 c^3 d^4$:
$$ab^2 c^3 d^4 \le 1^1 \cdot 2^2 \cdot 3^3 \cdot 4^4$$

Calculamos el valor del lado derecho:
$$1 \cdot 4 \cdot 27 \cdot 256 = 108 \cdot 256 = 27648$$

La igualdad se alcanza cuando todos los términos son iguales, es decir:
$$a = \frac{b}{2} = \frac{c}{3} = \frac{d}{4} = 1$$
lo que corresponde a $a = 1$, $b = 2$, $c = 3$ y $d = 4$, valores que cumplen $1 + 2 + 3 + 4 = 10$.

\boxed{27648}