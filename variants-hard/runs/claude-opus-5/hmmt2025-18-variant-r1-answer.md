## Planteamiento

Tras $t$ minutos, cada posición contiene el máximo de una ventana de radio $t$:
$$x_i^{(t)} = \max(x_{i-t},\dots,x_{i+t}),$$
es decir, una ventana de $2t+1 = 121$ elementos consecutivos ($t=60$).

Como los valores iniciales son distintos casi seguramente, cada ventana tiene un único argmax, y dos ventanas dan el mismo valor exactamente cuando comparten el argmax. Por tanto:

$$\#\text{valores distintos} = \#\{j : x_j \text{ es el máximo de alguna ventana de 121 posiciones consecutivas}\}.$$

## Condición local

Para el índice $j$ definamos
- $L_j$ = cantidad de vecinos consecutivos a la izquierda menores que $x_j$,
- $R_j$ = cantidad de vecinos consecutivos a la derecha menores que $x_j$.

El bloque maximal alrededor de $j$ formado por elementos $< x_j$ tiene longitud $L_j + 1 + R_j$. Existe una ventana de 121 posiciones que contiene a $j$ donde $x_j$ es máximo si y solo si ese bloque cabe la ventana:
$$L_j + R_j + 1 \ge 121 \quad\Longleftrightarrow\quad L_j + R_j \ge 120.$$

## Distribución de $L+R$

Sea $m = a+b+1$. El evento $\{L=a, R=b\}$ involucra $m+2$ variables: las $m$ de la racha y las dos que la cortan. Se requiere que $x_j$ supere a las $m-1$ restantes de la racha y quede por debajo de las dos exteriores, o sea que las dos exteriores sean las mayores de las $m+2$ y $x_j$ la tercera:
$$P(L=a,R=b) = \frac{2!\,(m-1)!}{(m+2)!} = \frac{2}{m(m+1)(m+2)}.$$

Como hay $s+1$ pares con $a+b=s$ (y $m=s+1$):
$$P(L+R=s) = \frac{2(s+1)}{(s+1)(s+2)(s+3)} = \frac{2}{(s+2)(s+3)}.$$

(Suma total: $2\sum_{s\ge0}\left(\frac1{s+2}-\frac1{s+3}\right)=1$ ✓.)

## Probabilidad y esperanza

$$P(L+R\le 119) = 2\sum_{s=0}^{119}\left(\frac{1}{s+2}-\frac{1}{s+3}\right) = 2\left(\frac12-\frac1{122}\right) = 1-\frac1{61}.$$

Luego $P(L+R\ge 120) = \dfrac{1}{61}$ (válido porque $122 \le 1011$, así que el borde circular no interviene).

Por linealidad de la esperanza sobre los 1011 índices:
$$E = 1011\cdot\frac{1}{61} = \frac{1011}{61}.$$

\boxed{\dfrac{1011}{61}}