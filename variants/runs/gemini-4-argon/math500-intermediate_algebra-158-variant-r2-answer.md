Para encontrar el valor máximo de $p q^2 r^2 s^3$ sujeto a la condición $p + q + r + s = 16$ para números reales positivos $p, q, r, s,$ podemos utilizar la desigualdad entre la media aritmética y la media geométrica (MA-MG).

Primero, descomponemos la suma $p + q + r + s$ en $1 + 2 + 2 + 3 = 8$ términos de manera que coincidan con los exponentes del producto que queremos maximizar:
$$p + q + r + s = p + \frac{q}{2} + \frac{q}{2} + \frac{r}{2} + \frac{r}{2} + \frac{s}{3} + \frac{s}{3} + \frac{s}{3} = 16$$

Aplicando la desigualdad MA-MG a estos 8 términos positivos, obtenemos:
$$\frac{p + \frac{q}{2} + \frac{q}{2} + \frac{r}{2} + \frac{r}{2} + \frac{s}{3} + \frac{s}{3} + \frac{s}{3}}{8} \ge \sqrt[8]{p \cdot \left(\frac{q}{2}\right)^2 \cdot \left(\frac{r}{2}\right)^2 \cdot \left(\frac{s}{3}\right)^3}$$

Sustituyendo la suma por $16$:
$$\frac{16}{8} \ge \sqrt[8]{\frac{p q^2 r^2 s^3}{2^2 \cdot 2^2 \cdot 3^3}}$$
$$2 \ge \sqrt[8]{\frac{p q^2 r^2 s^3}{4 \cdot 4 \cdot 27}}$$

Elevando ambos lados a la octava potencia:
$$2^8 \ge \frac{p q^2 r^2 s^3}{432}$$
$$256 \ge \frac{p q^2 r^2 s^3}{432}$$

Multiplicando ambos lados por $432$:
$$p q^2 r^2 s^3 \le 256 \cdot 432 = 110592$$

La igualdad se alcanza cuando todos los términos son iguales:
$$p = \frac{q}{2} = \frac{r}{2} = \frac{s}{3} = 2$$
es decir, cuando $p = 2,$ $q = 4,$ $r = 4$ y $s = 6.$

\boxed{110592}