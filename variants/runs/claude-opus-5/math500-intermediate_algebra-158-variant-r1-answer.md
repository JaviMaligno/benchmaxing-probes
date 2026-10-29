## Planteamiento

Aplico AM-GM dividiendo cada variable en tantas partes iguales como su exponente:

$$p + \underbrace{\frac{q}{2}+\frac{q}{2}}_{2} + \underbrace{\frac{r}{2}+\frac{r}{2}}_{2} + \underbrace{\frac{s}{3}+\frac{s}{3}+\frac{s}{3}}_{3} = 16$$

Son 8 términos en total, así que:

$$\frac{16}{8} \ge \sqrt[8]{p\cdot\left(\frac{q}{2}\right)^2\left(\frac{r}{2}\right)^2\left(\frac{s}{3}\right)^3}$$

## Despeje

$$2^8 \ge \frac{p\,q^2 r^2 s^3}{4\cdot 4\cdot 27} \quad\Longrightarrow\quad p\,q^2r^2s^3 \le 256 \cdot 432 = 110592$$

## Caso de igualdad

Se alcanza cuando todos los términos son iguales a 2:

$$p = 2,\qquad \frac{q}{2}=2 \Rightarrow q = 4,\qquad \frac{r}{2}=2 \Rightarrow r = 4,\qquad \frac{s}{3}=2 \Rightarrow s = 6$$

Verificación: $2+4+4+6 = 16$ ✓ y $2 \cdot 4^2 \cdot 4^2 \cdot 6^3 = 2 \cdot 16 \cdot 16 \cdot 216 = 110592$ ✓

$$\boxed{110592}$$