Queremos maximizar $pq^2r^2s^3$ sujeto a $p+q+r+s=16$, con todas las variables positivas.

**Aplicando AM-GM con una partición adecuada:** escribimos la suma como 8 términos, repartiendo cada variable según su exponente en el producto:

$$16 = p + \frac{q}{2} + \frac{q}{2} + \frac{r}{2} + \frac{r}{2} + \frac{s}{3} + \frac{s}{3} + \frac{s}{3}.$$

Por la desigualdad entre la media aritmética y la geométrica (AM-GM) sobre estos 8 términos:

$$\frac{16}{8} = 2 \ \ge\ \sqrt[8]{\,p \cdot \frac{q^2}{4} \cdot \frac{r^2}{4} \cdot \frac{s^3}{27}\,}.$$

Elevando a la octava potencia:

$$\frac{pq^2r^2s^3}{4 \cdot 4 \cdot 27} \le 2^8 = 256 \quad\Longrightarrow\quad pq^2r^2s^3 \le 256 \cdot 432 = 110592.$$

**Verificación de la igualdad:** se alcanza cuando todos los términos son iguales, es decir $p = \frac{q}{2} = \frac{r}{2} = \frac{s}{3} = 2$, lo que da $p=2$, $q=4$, $r=4$, $s=6$. Comprobamos: $2+4+4+6 = 16$ ✓, y el producto es $2 \cdot 16 \cdot 16 \cdot 216 = 110592$ ✓.

$$\boxed{110592}$$