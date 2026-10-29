## Planteamiento

Aplicamos AM-GM dividiendo cada variable según su exponente: $a$ en 1 parte, $b$ en 2, $c$ en 3 y $d$ en 4 (total: 10 términos).

$$10 = a + b + c + d = a + 2\cdot\frac{b}{2} + 3\cdot\frac{c}{3} + 4\cdot\frac{d}{4}$$

Por AM-GM sobre esos 10 términos:

$$\frac{a + \frac{b}{2}+\frac{b}{2} + \frac{c}{3}+\frac{c}{3}+\frac{c}{3} + \frac{d}{4}+\frac{d}{4}+\frac{d}{4}+\frac{d}{4}}{10} \ge \sqrt[10]{a\left(\frac{b}{2}\right)^2\left(\frac{c}{3}\right)^3\left(\frac{d}{4}\right)^4}$$

El lado izquierdo vale $\frac{10}{10} = 1$, por lo que:

$$1 \ge \frac{ab^2c^3d^4}{2^2\cdot 3^3\cdot 4^4} \quad\Longrightarrow\quad ab^2c^3d^4 \le 4\cdot 27\cdot 256 = 27648$$

## Igualdad

Se alcanza cuando todos los términos son iguales:

$$a = \frac{b}{2} = \frac{c}{3} = \frac{d}{4} = 1 \quad\Longrightarrow\quad (a,b,c,d) = (1,2,3,4)$$

que efectivamente suma $10$, y da $1\cdot 4\cdot 27\cdot 256 = 27648$.

$$\boxed{27648}$$