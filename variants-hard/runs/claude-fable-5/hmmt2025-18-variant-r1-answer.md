## Planteamiento

Tras $t$ minutos, el valor en la posición $i$ es el máximo de la ventana $\{x_{i-t},\dots,x_{i+t}\}$. Con $t=60$, los valores presentes en el círculo son exactamente los máximos de todas las ventanas de longitud $121$. Como los $x_i$ son casi seguramente distintos, el número de valores distintos es el número de índices $j$ tales que $x_j$ es el máximo de **alguna** ventana de longitud $121$ que lo contiene.

## Criterio de supervivencia

Sea $L$ la longitud de la racha de valores consecutivos menores que $x_j$ a su izquierda, y $R$ la análoga a la derecha. Una ventana de longitud $121$ que contiene a $j$ tiene la forma $[j-a,\,j+b]$ con $a+b=120$; en ella $x_j$ es máximo si y solo si $L\ge a$ y $R\ge b$. Existe tal elección de $a,b$ si y solo si
$$L+R\ge 120.$$
Como $240 < 1011$, las rachas relevantes no se solapan ni dan la vuelta al círculo, así que el cálculo local es exacto.

## Cálculo de la probabilidad

Condicionando en $x_j=x$, los vecinos son uniformes independientes, de modo que $P(L=l)=x^l(1-x)$ y análogamente para $R$. Entonces
$$P(L+R=s\mid x)=(s+1)\,x^s(1-x)^2,$$
y con $m=120$:
$$P(L+R\ge m\mid x)=\sum_{s\ge m}(s+1)x^s(1-x)^2=x^m\big((m+1)-mx\big).$$

Integrando sobre $x\in[0,1]$:
$$P(\text{sobrevive})=\int_0^1 x^m\big((m+1)-mx\big)\,dx=\frac{m+1}{m+1}-\frac{m}{m+2}=\frac{2}{m+2}=\frac{2}{122}=\frac{1}{61}.$$

## Resultado

Por linealidad de la esperanza, el número esperado de valores distintos es
$$1011\cdot\frac{1}{61}=\frac{1011}{61}.$$

$$\boxed{\dfrac{1011}{61}}$$