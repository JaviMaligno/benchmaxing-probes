Para encontrar el valor máximo de $ab^2 c^3 d^4$ sujeto a la condición $a + b + c + d = 10$ para números reales positivos $a, b, c, d$, podemos utilizar la desigualdad entre las medias aritmética y geométrica (MA-MG).

Primero, reescribimos la suma $a + b + c + d$ dividiendo cada variable en tantas partes iguales como indique su exponente en el producto:
$$a + b + c + d = a + \frac{b}{2} + \frac{b}{2} + \frac{c}{3} + \frac{c}{3} + \frac{c}{3} + \frac{d}{4} + \frac{d}{4} + \frac{d}{4} + \frac{d}{4} = 10$$

Observamos que tenemos un total de $1 + 2 + 3 + 4 = 10$ términos positivos. Aplicando la desigualdad MA-MG a estos $10$ términos, obtenemos:
$$\frac{a + 2\left(\frac{b}{2}\right) + 3\left(\frac{c}{3}\right) + 4\left(\frac{d}{4}\right)}{10} \ge \sqrt[10]{a \left(\frac{b}{2}\right)^2 \left(\frac{c}{3}\right)^3 \left(\frac{d}{4}\right)^4}$$

Sustituyendo $a + b + c + d = 10$ en el lado izquierdo:
$$\frac{10}{10} \ge \sqrt[10]{\frac{ab^2 c^3 d^4}{2^2 \cdot 3^3 \cdot 4^4}}$$
$$1 \ge \sqrt[10]{\frac{ab^2 c^3 d^4}{4 \cdot 27 \cdot 256}}$$

Elevando ambos lados a la décima potencia:
$$1 \ge \frac{ab^2 c^3 d^4}{4 \cdot 27 \cdot 256}$$

Despejando el producto y calculando el denominador:
$$ab^2 c^3 d^4 \le 4 \cdot 27 \cdot 256 = 108 \cdot 256 = 27648$$

La igualdad se alcanza cuando todos los términos son iguales:
$$a = \frac{b}{2} = \frac{c}{3} = \frac{d}{4} = 1$$
lo que ocurre cuando $a = 1, b = 2, c = 3$ y $d = 4$ (cumpliendo que $1 + 2 + 3 + 4 = 10$).

\boxed{27648}