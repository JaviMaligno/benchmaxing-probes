## Planteamiento

Aplico AM-GM dividiendo cada variable según su exponente: $p$ en 1 parte, $q$ en 2, $r$ en 2, $s$ en 3 (total 8 términos).

$$16 = p + \frac{q}{2}+\frac{q}{2} + \frac{r}{2}+\frac{r}{2} + \frac{s}{3}+\frac{s}{3}+\frac{s}{3} \ge 8\sqrt[8]{p\left(\frac{q}{2}\right)^2\left(\frac{r}{2}\right)^2\left(\frac{s}{3}\right)^3}$$

De aquí:

$$2 \ge \sqrt[8]{\frac{p\,q^2r^2s^3}{4\cdot 4\cdot 27}} \quad\Longrightarrow\quad p q^2 r^2 s^3 \le 432\cdot 2^8 = 110592$$

## Caso de igualdad

La igualdad requiere que los ocho términos sean iguales a $16/8 = 2$:

$$p = 2,\qquad q = 4,\qquad r = 4,\qquad s = 6$$

Verificación: $2+4+4+6 = 16$ y $2\cdot 4^2\cdot 4^2\cdot 6^3 = 2\cdot 16\cdot 16\cdot 216 = 110592$.

\boxed{110592}