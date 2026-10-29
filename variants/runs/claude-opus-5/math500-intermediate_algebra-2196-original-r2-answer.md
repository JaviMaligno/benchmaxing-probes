## Planteamiento

Queremos maximizar $f(x,y)=\dfrac{x-y}{x^4+y^4+6}$. El denominador es siempre positivo (≥ 6), así que conviene buscar una cota del tipo $x-y \le \frac{1}{4}(x^4+y^4+6)$.

## Cota por AM-GM

Para todo real $x$:
$$x^4 + 3 - 4x = (x-1)^2(x^2+2x+3) = (x-1)^2\big[(x+1)^2+2\big] \ge 0,$$
luego $x^4+3 \ge 4x$.

Análogamente, para todo real $y$ (aplicando lo anterior a $-y$):
$$y^4 + 3 \ge -4y.$$

Sumando ambas desigualdades:
$$x^4+y^4+6 \ge 4(x-y).$$

Como $x^4+y^4+6>0$, se obtiene
$$\frac{x-y}{x^4+y^4+6} \le \frac{1}{4}.$$

## Igualdad

La igualdad requiere $x=1$ y $y=-1$. Comprobación:
$$\frac{1-(-1)}{1+1+6} = \frac{2}{8} = \frac{1}{4}.$$

El valor $1/4$ se alcanza, por lo que es el máximo.

\boxed{\dfrac{1}{4}}