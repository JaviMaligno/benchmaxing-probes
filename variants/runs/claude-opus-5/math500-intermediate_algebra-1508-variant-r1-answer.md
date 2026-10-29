## Razonamiento

**Paso 1.** Calculamos $b_2$ y $b_3$ en términos de $b_1$:

$$b_2 = -\frac{1}{1+b_1}, \qquad b_3 = -\frac{1}{1+b_2} = -\frac{1}{1-\frac{1}{1+b_1}} = -\frac{1+b_1}{b_1}$$

**Paso 2.** Imponemos $b_3 = b_1$:

$$-\frac{1+b_1}{b_1} = b_1 \implies b_1^2 + b_1 + 1 = 0$$

Es decir, $b_1$ es una raíz cúbica primitiva de la unidad, por lo que $b_1^3 = 1$.

**Paso 3.** Determinamos $b_9$. Como $b_3 = b_1$, se tiene $b_4 = -\frac{1}{1+b_3} = -\frac{1}{1+b_1} = b_2$, y por inducción la sucesión es periódica de periodo 2:

$$b_1, b_2, b_1, b_2, \dots$$

Al ser $9$ impar, $b_9 = b_1$.

**Paso 4.** Por tanto $(b_9)^9 = b_1^9 = (b_1^3)^3 = 1^3 = 1$.

\boxed{1}