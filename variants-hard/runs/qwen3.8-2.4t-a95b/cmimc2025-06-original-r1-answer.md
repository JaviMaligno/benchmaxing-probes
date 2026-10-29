

Sea \(A\) el área del conjunto de puntos \((x,y)\in[-1,1]^2\) que cumplen la desigualdad. Como el área total del cuadrado es \(4\), la probabilidad pedida será \(A/4\).

Dividimos el cuadrado en los cuatro cuadrantes.

### 1. Primer cuadrante: \(x,y\ge 0\)

Sea \(t=x+y\), con \(0\le t\le 2\). Entonces \(|x|+|y|=t\), y

\[
\min\{|t+1|,|t-1|\}=
\begin{cases}
1-t, & 0\le t\le 1,\\
t-1, & 1\le t\le 2.
\end{cases}
\]

La desigualdad es

\[
t+1\le 3\min\{|t+1|,|t-1|\}.
\]

Si \(0\le t\le 1\):

\[
t+1\le 3(1-t)\implies 4t\le 2\implies t\le \frac12.
\]

Si \(1\le t\le 2\):

\[
t+1\le 3(t-1)\implies t\ge 2,
\]

lo cual solo da el punto \((1,1)\), de área nula.

Por tanto, en el primer cuadrante la región favorable es \(x+y\le \frac12\), un triángulo de área

\[
\frac12\cdot \frac12\cdot \frac12=\frac18.
\]

### 2. Tercer cuadrante: \(x,y\le 0\)

Por simetría bajo \((x,y)\mapsto(-x,-y)\), se obtiene la misma área:

\[
\frac18.
\]

### 3. Segundo cuadrante: \(x\le 0,\ y\ge 0\)

Escribimos \(a=-x\ge 0\), \(b=y\ge 0\). Entonces \(|x|+|y|=a+b\), y \(x+y=b-a\), con \(|b-a|\le 1\). Por tanto,

\[
\min\{|b-a+1|,|b-a-1|\}=1-|b-a|.
\]

La desigualdad se convierte en

\[
a+b+1\le 3(1-|b-a|),
\]

es decir,

\[
a+b+3|a-b|\le 2.
\]

Consideremos la mitad \(a\ge b\). Entonces \(|a-b|=a-b\), y la condición es

\[
a+b+3(a-b)\le 2\implies 4a-2b\le 2\implies b\ge 2a-1.
\]

Dentro de \(0\le b\le a\le 1\), el área es

\[
\int_0^{1/2} a\,da+\int_{1/2}^1 \bigl(a-(2a-1)\bigr)\,da
=
\frac18+\int_{1/2}^1(1-a)\,da
=
\frac18+\frac18=\frac14.
\]

Por simetría entre \(a\) y \(b\), la otra mitad \(b\ge a\) aporta otro \(\frac14\). Así, el área favorable en el segundo cuadrante es

\[
\frac14+\frac14=\frac12.
\]

### 4. Cuarto cuadrante: \(x\ge 0,\ y\le 0\)

Por simetría con el segundo cuadrante, el área favorable también es

\[
\frac12.
\]

### Área total favorable

\[
A=\frac18+\frac18+\frac12+\frac12=\frac54.
\]

Por tanto, la probabilidad es

\[
\frac{A}{4}=\frac{5/4}{4}=\frac{5}{16}.
\]

\[
\boxed{\frac{5}{16}}
\]