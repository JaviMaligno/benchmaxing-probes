El paralelogramo está delimitado por dos rectas de pendiente $a$ y dos rectas de pendiente $b$. La distancia vertical entre las rectas de pendiente $a$ es $|d-c|$ y entre las de pendiente $b$ es $|d-c|$ (la misma diferencia vertical). En general, el área de un paralelogramo formado por estas rectas es $\dfrac{(d-c)^2}{|b-a|}$.

En el primer caso, las rectas son:
- $y=ax+c$ y $y=ax+d$ (separación vertical $d-c$)
- $y=bx+c$ y $y=bx+d$ (separación vertical $d-c$)

El área es $\dfrac{(d-c)^2}{|b-a|}=18$.

En el segundo caso:
- $y=ax+c$ y $y=ax-d$ (separación vertical $c+d$)
- $y=bx+c$ y $y=bx-d$ (separación vertical $c+d$)

El área es $\dfrac{(c+d)^2}{|b-a|}=72$.

Dividiendo la segunda ecuación entre la primera:
$$\frac{(c+d)^2}{(d-c)^2}=\frac{72}{18}=4$$
$$\frac{c+d}{d-c}=2$$

Despejando: $c+d=2(d-c)$, luego $c+d=2d-2c$, así que $3c=d$.

Sustituyendo $d=3c$ en la primera ecuación:
$$\frac{(3c-c)^2}{|b-a|}=18 \implies \frac{4c^2}{|b-a|}=18 \implies |b-a|=\frac{2c^2}{9}.$$

Buscamos enteros positivos que minimicen $a+b+c+d=a+b+c+3c=a+b+4c$. Como $|b-a|=\frac{2c^2}{9}$, para que sea entero, $c$ debe ser múltiplo de $3$. Sea $c=3k$, con $k$ entero positivo. Entonces:
$$|b-a|=\frac{2(3k)^2}{9}=2k^2.$$

Queremos minimizar $a+b+4c=a+b+12k$. Dado que $a$ y $b$ son enteros positivos con diferencia $2k^2$, la suma $a+b$ se minimiza con $a=1$ y $b=1+2k^2$ (o viceversa), lo que da $a+b=2+2k^2$.

Entonces la suma total es $2+2k^2+12k=2(k^2+6k+1)$, que crece con $k$. El mínimo se da para $k=1$:
$$a+b+c+d=2+2+12=16.$$

Verificamos: con $k=1$, $c=3$, $d=9$, $|b-a|=2$. Si $a=1$, $b=3$ (o intercambiados), la suma es $1+3+3+9=16$.

La respuesta final es:
\boxed{16}