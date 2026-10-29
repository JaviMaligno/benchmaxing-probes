El área de un paralelogramo definido por las rectas

\[
y=a x+c,\quad y=a x+d,\quad y=b x+c,\quad y=b x+d
\]

se calcula como el valor absoluto de

\[
\frac{(d-c)^2}{|a-b|}
\]

(o equivalentemente con el determinante correspondiente). En efecto, las rectas horizontales en el «espacio transformado» \(u=y-ax\) y \(v=y-bx\) quedan en \(u=c\), \(u=d\), \(v=c\), \(v=d\), y el área es

\[
\left|\frac{(d-c)^2}{a-b}\right|.
\]

### Primer paralelogramo

Líneas: \(y=ax+c\), \(y=ax+d\), \(y=bx+c\), \(y=bx+d\).  
Área \(=18\):

\[
\frac{(d-c)^2}{|a-b|}=18.
\]

### Segundo paralelogramo

Líneas: \(y=ax+c\), \(y=ax-d\), \(y=bx+c\), \(y=bx-d\).  
Aquí los intervalos verticales van de \(c\) a \(-d\), con longitud \(|c-(-d)|=c+d\).  
Área \(=72\):

\[
\frac{(c+d)^2}{|a-b|}=72.
\]

Sea \(k=|a-b|\), con \(k\ge 1\). Entonces:

\[
(d-c)^2=18k,\qquad (c+d)^2=72k.
\]

Dividiendo:

\[
\frac{(c+d)^2}{(d-c)^2}=4
\implies \frac{c+d}{d-c}=2
\]

(pues todas las cantidades son positivas, y \(c+d>d-c\) requiere esta elección de signo).

Entonces

\[
c+d=2(d-c)\implies c+d=2d-2c\implies 3c=d.
\]

Sustituyendo \(d=3c\):

\[
(d-c)^2=(2c)^2=4c^2=18k
\implies 2c^2=9k.
\]

Como \(k=a-b\) es entero y \(k\ge 1\), \(2c^2\) debe ser múltiplo de \(9\):

\[
2c^2=9k \implies 9\mid 2c^2 \implies 9\mid c^2 \implies 3\mid c.
\]

Escribimos \(c=3t\), con \(t\) entero positivo. Entonces:

\[
2(3t)^2=18t^2=9k\implies k=2t^2.
\]

Luego \(a-b=2t^2\), con \(t\ge 1\). Como \(a,b\) son enteros positivos y distintos, la diferencia mínima es \(2t^2\). Los valores de \(a,b\) que minimizan \(a+b\) para una diferencia fija \(2t^2\) son

\[
b=1,\quad a=1+2t^2.
\]

Entonces:

\[
a+b+c+d = (1+2t^2)+1+3t+9t = 2+2t^2+12t.
\]

Minimizamos \(2t^2+12t+2\) sobre \(t\ge 1\). La función crece para \(t\ge 1\) (su mínimo en números reales está en \(t=-3\)), así que el mínimo se da en \(t=1\).

Para \(t=1\):

\[
a=3,\quad b=1,\quad c=3,\quad d=9.
\]

Comprobamos:

\[
(d-c)^2=(9-3)^2=36,\quad |a-b|=2,\quad \frac{36}{2}=18.
\]

\[
(c+d)^2=(3+9)^2=144,\quad |a-b|=2,\quad \frac{144}{2}=72.
\]

Todo cuadra. Por tanto,

\[
a+b+c+d=3+1+3+9=16.
\]

\[
\boxed{16}
\]