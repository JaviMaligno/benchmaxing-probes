Aplico la desigualdad AM-GM dividiendo la suma en 8 términos acordes a los exponentes:

$$p + q + r + s = p + \frac{q}{2} + \frac{q}{2} + \frac{r}{2} + \frac{r}{2} + \frac{s}{3} + \frac{s}{3} + \frac{s}{3} = 16$$

Por AM-GM con estos 8 términos:

$$\frac{16}{8} = 2 \ge \sqrt[8]{p \cdot \frac{q^2}{4} \cdot \frac{r^2}{4} \cdot \frac{s^3}{27}}$$

Elevando a la octava potencia:

$$2^8 = 256 \ge \frac{p\,q^2 r^2 s^3}{4 \cdot 4 \cdot 27} = \frac{p\,q^2 r^2 s^3}{432}$$

Por lo tanto $p\,q^2 r^2 s^3 \le 256 \cdot 432 = 110592$.

La igualdad se alcanza cuando todos los términos son iguales: $p = \frac{q}{2} = \frac{r}{2} = \frac{s}{3} = 2$, es decir, $p=2$, $q=4$, $r=4$, $s=6$ (que suman 16). Verificación: $2 \cdot 16 \cdot 16 \cdot 216 = 110592$. ✓

$$\boxed{110592}$$