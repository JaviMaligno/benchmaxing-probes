

Sea \(s=a+b\). Entonces la expresión es

\[
F=\frac{(s+c)\left[s^2+(s+4c)^2\right]}{abc}.
\]

Para \(s\) y \(c\) fijos, el numerador depende solo de \(s\) y \(c\), mientras que el denominador contiene \(ab\). Como \(a,b>0\) y \(a+b=s\),

\[
ab\le \left(\frac{s}{2}\right)^2,
\]

con igualdad cuando \(a=b\). Por tanto, el mínimo se alcanza cuando \(a=b\).

Sea entonces \(a=b=x\) y \(c=y\). La expresión se convierte en

\[
F=\frac{(2x+y)\left[(2x)^2+(2x+4y)^2\right]}{x^2y}.
\]

Por homogeneidad, depende solo de \(r=\frac{y}{x}>0\). Así,

\[
F(r)=\frac{(2+r)\left[4+(2+4r)^2\right]}{r}.
\]

Simplificando:

\[
4+(2+4r)^2=8+16r+16r^2,
\]

\[
F(r)=\frac{8(r+2)(2r^2+2r+1)}{r}
=16r^2+48r+40+\frac{16}{r}.
\]

Derivamos:

\[
F'(r)=32r+48-\frac{16}{r^2}.
\]

Para un punto crítico,

\[
32r+48-\frac{16}{r^2}=0
\]

\[
2r+3-\frac{1}{r^2}=0
\]

\[
2r^3+3r^2-1=0.
\]

Factorizando,

\[
2r^3+3r^2-1=(r+1)^2(2r-1).
\]

Como \(r>0\), la única raíz positiva es

\[
r=\frac12.
\]

Además,

\[
F''(r)=32+\frac{32}{r^3}>0,
\]

así que es un mínimo global. Evaluando:

\[
F\left(\frac12\right)
=16\left(\frac14\right)+48\left(\frac12\right)+40+\frac{16}{1/2}
=4+24+40+32=100.
\]

La igualdad ocurre cuando \(a=b\) y \(c=\frac{a}{2}\), es decir, \(a=b=2c\).

\[
\boxed{100}
\]