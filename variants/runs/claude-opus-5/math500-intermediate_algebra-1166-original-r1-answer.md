## Planteamiento

Sea $s = a+b$. Para $s$ fijo, el numerador solo depende de $s$ y $c$, mientras que el denominador crece con $ab$. Por AM–GM, $ab \le s^2/4$ con igualdad si $a=b$. Entonces

$$\frac{(a+b+c)\left[(a+b)^2+(a+b+4c)^2\right]}{abc} \ge \frac{4(s+c)\left[s^2+(s+4c)^2\right]}{s^2c}.$$

## Reducción a una variable

La expresión es homogénea de grado 0, así que tomamos $s=1$ y $c=t>0$:

$$(1+4t)^2+1 = 16t^2+8t+2,$$
$$(1+t)(16t^2+8t+2) = 16t^3+24t^2+10t+2,$$

de donde

$$f(t) = \frac{4\left(16t^3+24t^2+10t+2\right)}{t} = 4\left(16t^2+24t+10+\frac{2}{t}\right).$$

## Minimización

$$f'(t) = 4\left(32t+24-\frac{2}{t^2}\right)=0 \iff 16t^3+12t^2-1=0.$$

Como $t=\tfrac14$ da $\tfrac14+\tfrac34-1=0$, es raíz (y factorizando, $16t^3+12t^2-1=(4t-1)(4t^2+4t+1)=(4t-1)(2t+1)^2$, por lo que es la única raíz positiva, con $f'<0$ antes y $f'>0$ después: es mínimo).

En $t=\tfrac14$:

$$16\cdot\tfrac1{16}+24\cdot\tfrac14+10+8 = 1+6+10+8 = 25 \implies f\left(\tfrac14\right)=100.$$

La igualdad se alcanza con $a=b$ y $c=\tfrac{a+b}{4}=\tfrac{a}{2}$, por ejemplo $(a,b,c)=(2,2,1)$:
$$\frac{5\,[16+64]}{4}=\frac{400}{4}=100. \checkmark$$

$$\boxed{100}$$