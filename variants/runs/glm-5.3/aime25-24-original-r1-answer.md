Sea \(\theta=5x\). Como \(0<x<2\pi\), tenemos \(0<\theta<10\pi\), y cada \(\theta\) corresponde a un único \(x\).

Los ceros cumplen
\[
\sin(7\pi\sin\theta)=0
\iff 7\sin\theta\in\mathbb Z
\iff \sin\theta=\frac{k}{7},
\]
con \(k=-7,-6,\dots,7\).

Contamos soluciones \(\theta\in(0,10\pi)\):

- Si \(k\neq0\) y \(|k|\le6\), hay \(12\) valores de \(k\), y cada ecuación tiene \(2\) soluciones por periodo \(2\pi\), o sea \(10\) soluciones cada una.
- Si \(k=0\), entonces \(\theta=m\pi\), con \(m=1,\dots,9\), así que hay \(9\) soluciones.
- Si \(k=\pm7\), hay \(1\) solución por periodo, es decir \(5\) soluciones para cada signo.

Por tanto,
\[
n=12\cdot 10+9+2\cdot 5=139.
\]

Además,
\[
f'(x)=35\pi\cos(7\pi\sin(5x))\cos(5x).
\]
En un cero, \(\cos(7\pi\sin(5x))=\cos(k\pi)\neq0\), así que la tangencia al eje \(x\) ocurre exactamente cuando \(\cos(5x)=0\). Esto corresponde a \(\sin(5x)=\pm1\), es decir \(k=\pm7\), dando
\[
t=10.
\]

Así,
\[
n+t=139+10=149.
\]

\(\boxed{149}\)