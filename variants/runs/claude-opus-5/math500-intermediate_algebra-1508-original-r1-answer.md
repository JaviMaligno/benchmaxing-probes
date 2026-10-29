## Razonamiento

**La recurrencia es periódica de periodo 3.**

Con $a_2 = \dfrac{1}{1-a_1}$:

$$a_3 = \frac{1}{1-a_2} = \frac{1}{1-\frac{1}{1-a_1}} = \frac{1-a_1}{-a_1} = \frac{a_1-1}{a_1}$$

Y se verifica que $a_4 = a_1$, así que la sucesión tiene periodo 3.

**Condición $a_3 = a_1$:**

$$\frac{a_1-1}{a_1} = a_1 \implies a_1 - 1 = a_1^2 \implies a_1^2 - a_1 + 1 = 0$$

**Cálculo de $a_9$:**

Como $9 \equiv 3 \pmod 3$ y el periodo es 3, tenemos $a_9 = a_3 = a_1$.

**Elevando a la novena:**

De $a_1^2 = a_1 - 1$ se obtiene
$$a_1^3 = a_1^2 - a_1 = (a_1-1) - a_1 = -1$$

Por lo tanto:
$$(a_9)^9 = a_1^9 = (a_1^3)^3 = (-1)^3 = -1$$

\boxed{-1}