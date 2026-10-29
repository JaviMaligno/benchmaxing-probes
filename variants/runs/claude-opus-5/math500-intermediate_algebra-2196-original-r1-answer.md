## Planteamiento

Hago el cambio $a = x$, $b = -y$. Entonces $x - y = a + b$ y $x^4 + y^4 = a^4 + b^4$, así que la expresión es
$$\frac{a+b}{a^4+b^4+6}.$$

## Cota superior

Por AM–GM, para todo real $a$ se cumple
$$a^4 + 1 + 1 + 1 \ge 4|a| \ge 4a,$$
es decir $a^4 + 3 \ge 4a$ (con igualdad en $a=1$). Lo mismo para $b$: $b^4 + 3 \ge 4b$.

Sumando:
$$a^4 + b^4 + 6 \ge 4(a+b).$$

Como el denominador es siempre positivo ($\ge 6$), esto da
$$\frac{a+b}{a^4+b^4+6} \le \frac{1}{4}.$$

## Igualdad

Se alcanza con $a = b = 1$, o sea $x = 1$, $y = -1$:
$$\frac{1-(-1)}{1^4+(-1)^4+6} = \frac{2}{8} = \frac{1}{4}.$$

(Coherente con Lagrange: optimizar $x-y$ con $x^4+y^4$ fijo exige $4\lambda x^3 = 1$, $4\lambda y^3 = -1$, luego $y = -x$; y maximizar $\frac{t}{t^4+3}$ da $t=1$.)

$$\boxed{\dfrac{1}{4}}$$