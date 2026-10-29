

Como \(f(x)\in[-1,1]\), en cualquier intersección con \(x=34y^2\) se tiene
\[
-1\le y\le 1,\qquad 0\le x\le 34.
\]

En \([0,34]\), la función es una sucesión de tramos lineales.

**Tramos ascendentes.** Para \(n=0,1,\dots,8\),
\[
y=x-4n,
\]
con \(x\in[0,1]\) cuando \(n=0\), y \(x\in[4n-1,4n+1]\) para \(n\ge1\).

Sustituyendo \(x=34y^2\):
\[
34y^2=y+4n \quad\Longrightarrow\quad 34y^2-y-4n=0.
\]

Para \(n=0\), las raíces son \(y=0\) y \(y=\frac1{34}\), ambas válidas.  
Para \(n=1,\dots,8\), se comprueba que hay una raíz en \((-1,0)\) y otra en \((0,1)\), pues
\[
34(-1)^2-(-1)-4n=35-4n>0,
\]
\[
34(0)^2-0-4n=-4n<0,
\]
\[
34(1)^2-1-4n=33-4n>0.
\]
Así, cada \(n=0,1,\dots,8\) aporta dos intersecciones válidas. Por Vieta, la suma de las dos raíces de cada ecuación es \(\frac1{34}\). Entonces la suma total de los tramos ascendentes es
\[
S_{\text{asc}}=9\cdot \frac1{34}=\frac9{34}.
\]

**Tramos descendentes.** Para \(n=0,1,\dots,7\),
\[
y=4n+2-x,
\]
con \(x\in[4n+1,4n+3]\). Para \(n=8\), el tramo queda truncado en \(x\in[33,34]\).

Sustituyendo \(x=34y^2\):
\[
34y^2=4n+2-y \quad\Longrightarrow\quad 34y^2+y-(4n+2)=0.
\]

Para \(n=0,1,\dots,7\), hay una raíz en \((-1,0)\) y otra en \((0,1)\), ya que
\[
34(-1)^2-1-(4n+2)=31-4n>0,
\]
\[
-(4n+2)<0,
\]
\[
34(1)^2+1-(4n+2)=33-4n>0.
\]
Cada una aporta suma de raíces \(-\frac1{34}\), así que
\[
S_{\text{desc},0\le n\le 7}=8\left(-\frac1{34}\right)=-\frac8{34}.
\]

Para \(n=8\), la ecuación es
\[
34y^2+y-34=0.
\]
En el tramo truncado solo importa \(y\in[0,1]\). La raíz positiva es válida:
\[
y=\frac{-1+\sqrt{1+4\cdot34\cdot34}}{68}
=\frac{-1+\sqrt{4625}}{68}
=\frac{-1+5\sqrt{185}}{68}.
\]
La raíz negativa es menor que \(-1\), por lo que no corresponde a ningún punto de la gráfica en \(x\le34\).

Por tanto, la suma total de coordenadas \(y\) es
\[
S=\frac9{34}-\frac8{34}+\frac{-1+5\sqrt{185}}{68}
=\frac1{34}+\frac{-1+5\sqrt{185}}{68}
=\frac{1+5\sqrt{185}}{68}.
\]

Así,
\[
a=1,\quad b=5,\quad c=185,\quad d=68.
\]
Como \(185=5\cdot37\) es libre de cuadrados y \(\gcd(1,5,68)=1\), tenemos
\[
a+b+c+d=1+5+185+68=259.
\]

\[
\boxed{259}
\]