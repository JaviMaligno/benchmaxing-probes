Aplicamos la desigualdad AM-GM dividiendo la suma en 10 términos iguales según los exponentes:

$$a + b + c + d = a + \frac{b}{2} + \frac{b}{2} + \frac{c}{3} + \frac{c}{3} + \frac{c}{3} + \frac{d}{4} + \frac{d}{4} + \frac{d}{4} + \frac{d}{4} = 10.$$

Por AM-GM sobre estos 10 términos:

$$\frac{10}{10} \ge \sqrt[10]{a \cdot \left(\frac{b}{2}\right)^2 \left(\frac{c}{3}\right)^3 \left(\frac{d}{4}\right)^4} \;\Longrightarrow\; a \cdot \frac{b^2}{4} \cdot \frac{c^3}{27} \cdot \frac{d^4}{256} \le 1.$$

Por lo tanto:

$$ab^2c^3d^4 \le 4 \cdot 27 \cdot 256 = 27648.$$

La igualdad se alcanza cuando todos los términos son iguales: $a = \frac{b}{2} = \frac{c}{3} = \frac{d}{4}$, es decir $a=1,\ b=2,\ c=3,\ d=4$, cuya suma es efectivamente $10$. Verificando: $1 \cdot 4 \cdot 27 \cdot 256 = 27648$.

$$\boxed{27648}$$