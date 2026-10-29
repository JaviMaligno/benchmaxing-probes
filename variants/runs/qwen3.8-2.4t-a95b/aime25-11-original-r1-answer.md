

Sea \((x,y)\) un punto de intersección. Entonces

\[
y=f(x), \qquad x=34y^2.
\]

Como \(|f(x)|\le 1\), necesariamente \(0\le x\le 34\).

La función es una onda triangular de periodo \(4\). En cada periodo hay dos tramos lineales.

**Tramos ascendentes.** Para \(k\in\mathbb Z\), en

\[
[4k-1,4k+1), \qquad f(x)=x-4k.
\]

Sea \(t=f(x)\). Entonces \(x=t+4k\), y la intersección cumple

\[
t+4k=34t^2 \quad\Longrightarrow\quad 34t^2-t-4k=0.
\]

Los tramos relevantes para \(0\le x\le 34\) son \(k=0,1,\dots,8\). En cada uno de ellos las dos raíces son válidas; por Vieta, la suma de las dos raíces es

\[
\frac{1}{34}.
\]

Por tanto, la contribución total de los tramos ascendentes es

\[
S_{\text{asc}}=9\cdot \frac1{34}=\frac9{34}.
\]

**Tramos descendentes.** Para \(k\in\mathbb Z\), en

\[
[4k+1,4k+3), \qquad f(x)=4k+2-x.
\]

Sea \(y=f(x)\). Entonces \(x=4k+2-y\), y la intersección cumple

\[
4k+2-y=34y^2 \quad\Longrightarrow\quad 34y^2+y-(4k+2)=0.
\]

Los tramos relevantes son \(k=0,1,\dots,8\). Para \(k=0,1,\dots,7\), ambas raíces están en el rango válido \((-1,1]\), y su suma es

\[
-\frac1{34}.
\]

Así que estos ocho tramos contribuyen con

\[
-\frac8{34}.
\]

Para \(k=8\), la ecuación es

\[
34y^2+y-34=0,
\]

cuyas raíces son

\[
y=\frac{-1\pm\sqrt{4625}}{68}.
\]

La raíz negativa es menor que \(-1\), por lo que no está en el tramo. Solo es válida la raíz positiva:

\[
y=\frac{-1+\sqrt{4625}}{68}=\frac{-1+5\sqrt{185}}{68}.
\]

Por tanto, la suma total de las coordenadas \(y\) es

\[
S=\frac9{34}-\frac8{34}+\frac{-1+5\sqrt{185}}{68}
=\frac1{34}+\frac{-1+5\sqrt{185}}{68}
=\frac{1+5\sqrt{185}}{68}.
\]

Así,

\[
a=1,\quad b=5,\quad c=185,\quad d=68.
\]

Como \(185=5\cdot 37\) es libre de cuadrados y \(\gcd(1,5,68)=1\), se pide

\[
a+b+c+d=1+5+185+68=259.
\]

\[
\boxed{259}
\]