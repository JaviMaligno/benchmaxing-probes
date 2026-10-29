Vamos a razonar paso a paso.

Sea el cuadrado $PQRS$, con los vértices en orden $P \to Q \to R \to S$. Coloquemos coordenadas de forma conveniente.

Sea $P=(0,0)$, $Q=(s,0)$, $R=(s,s)$, $S=(0,s)$, donde $s$ es el lado del cuadrado.

El punto medio de $\overline{PQ}$ es $M=\left(\frac{s}{2},0\right)$.

La recta $m$ pasa por $M$ e interseca al segmento $\overline{QR}$, que es el lado derecho. Como $QR$ es la recta $x=s$ con $0\le y\le s$, la recta $m$ tendrá pendiente positiva (para intersecar $QR$ desde $M$).

Sea $m$ la recta que pasa por $M$ con ecuación
\[
y = k\left(x-\frac{s}{2}\right).
\]

Distancia de un punto $(x_0,y_0)$ a la recta $ax+by+c=0$:
\[
\frac{|ax_0+by_0+c|}{\sqrt{a^2+b^2}}.
\]

Escribamos $m$ como
\[
kx - y - \frac{ks}{2}=0.
\]

Entonces:

- Distancia desde $P=(0,0)$:
\[
d_P=\frac{\left|k\cdot 0-0-\frac{ks}{2}\right|}{\sqrt{k^2+1}}
=\frac{|ks|/2}{\sqrt{k^2+1}}=5.
\]

- Distancia desde $R=(s,s)$:
\[
d_R=\frac{\left|k s - s - \frac{ks}{2}\right|}{\sqrt{k^2+1}}
=\frac{\left|\frac{ks}{2}-s\right|}{\sqrt{k^2+1}}.
\]

Como la recta interseca $QR$ con $x=s$, en el punto de intersección $y=k\left(s-\frac{s}{2}\right)=\frac{ks}{2}$. Para que este punto esté en el segmento $QR$, se necesita $0\le \frac{ks}{2}\le s$, es decir $0\le k\le 2$. Por tanto $k>0$.

Entonces:
\[
d_P=\frac{ks/2}{\sqrt{k^2+1}}=5,
\]
y
\[
d_R=\frac{s-\frac{ks}{2}}{\sqrt{k^2+1}}=8
\]
(pues $k\le 2$ implica $\frac{ks}{2}\le s$).

Sumando:
\[
d_P+d_R=\frac{ks/2+s-ks/2}{\sqrt{k^2+1}}
=\frac{s}{\sqrt{k^2+1}}=13.
\]

Así:
\[
\frac{s}{\sqrt{k^2+1}}=13.
\]

Por otro lado, de $d_P=5$:
\[
\frac{ks/2}{\sqrt{k^2+1}}=5.
\]

Dividiendo esta última por la anterior:
\[
\frac{ks/2}{s}=\frac{k}{2}=\frac{5}{13},
\]
luego
\[
k=\frac{10}{13}.
\]

Ahora sustituimos:
\[
\frac{s}{\sqrt{\left(\frac{10}{13}\right)^2+1}}=13.
\]

Calculamos:
\[
k^2+1=\frac{100}{169}+1=\frac{269}{169}.
\]
Entonces:
\[
\frac{s}{\frac{\sqrt{269}}{13}}=13
\quad\Rightarrow\quad
\frac{13s}{\sqrt{269}}=13
\quad\Rightarrow\quad
s=\sqrt{269}.
\]

Por tanto el área del cuadrado es:
\[
s^2=269.
\]

\[
\boxed{269}
\]