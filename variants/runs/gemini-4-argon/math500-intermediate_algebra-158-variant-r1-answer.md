Para encontrar el valor máximo de la expresión $p q^2 r^2 s^3$ sujeto a la restricción $p + q + r + s = 16$ para números reales positivos $p, q, r, s,$ podemos utilizar la desigualdad entre la media aritmética y la media geométrica (MA-MG).

Observamos que los exponentes de $p, q, r$ y $s$ en el producto son $1, 2, 2$ y $3,$ respectivamente, cuya suma es $1 + 2 + 2 + 3 = 8.$ Por lo tanto, dividimos cada variable en tantas partes iguales como indique su exponente:

$$p + q + r + s = p + \frac{q}{2} + \frac{q}{2} + \frac{r}{2} + \frac{r}{2} + \frac{s}{3} + \frac{s}{3} + \frac{s}{3} = 16$$

Aplicando la desigualdad MA-MG a estos $8$ términos positivos, obtenemos:

$$\frac{p + \frac{q}{2} + \frac{q}{2} + \frac{r}{2} + \frac{r}{2} + \frac{s}{3} + \frac{s}{3} + \frac{s}{3}}{8} \ge \sqrt[8]{p \cdot \left(\frac{q}{2}\right)^2 \cdot \left(\frac{r}{2}\right)^2 \cdot \left(\frac{s}{3}\right)^3}$$

Sustituyendo la suma conocida en el lado izquierdo:

$$\frac{16}{8} \ge \sqrt[8]{\frac{p q^2 r^2 s^3}{2^2 \cdot 2^2 \cdot 3^3}}$$

$$2 \ge \sqrt[8]{\frac{p q^2 r^2 s^3}{4 \cdot 4 \cdot 27}}$$

Elevando ambos lados a la octava potencia:

$$2^8 \ge \frac{p q^2 r^2 s^3}{432}$$

$$256 \ge \frac{p q^2 r^2 s^3}{432}$$

Multiplicando ambos lados por $432$:

$$p q^2 r^2 s^3 \le 256 \cdot 432 = 110592$$

La igualdad se alcanza cuando todos los términos de la media son iguales, es decir, cuando:
$$p = \frac{q}{2} = \frac{r}{2} = \frac{s}{3} = 2$$
lo que corresponde a $p = 2,$ $q = 4,$ $r = 4$ y $s = 6$ (cuya suma es $2 + 4 + 4 + 6 = 16$).

\boxed{110592}