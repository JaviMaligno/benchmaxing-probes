Sea \(\theta=6x\). Como \(0<x<2\pi\), entonces \(0<\theta<12\pi\).

La condición \(g(x)=0\) equivale a
\[
\sin(8\pi\sin\theta)=0
\]
es decir,
\[
8\pi\sin\theta=k\pi \quad\Longrightarrow\quad \sin\theta=\frac{k}{8},
\]
con \(k\) entero y \(-8\le k\le 8\).

Contamos las soluciones \(\theta\in(0,12\pi)\):

- Para \(k=0\): \(\sin\theta=0\). Las soluciones son \(\pi,2\pi,\dots,11\pi\): hay \(11\).
- Para \(k=\pm1,\dots,\pm7\): hay \(14\) valores de \(k\), y cada ecuación \(\sin\theta=\frac{k}{8}\) tiene \(2\) soluciones por período. En \(6\) períodos hay \(14\cdot 12=168\) soluciones.
- Para \(k=\pm8\): \(\sin\theta=\pm1\). Cada una tiene \(6\) soluciones, luego \(12\) en total.

Por tanto,
\[
n=11+168+12=191.
\]

Para la tangencia, derivamos:
\[
g'(x)=\cos(8\pi\sin(6x))\cdot 48\pi\cos(6x).
\]
En una raíz, \(8\pi\sin(6x)=k\pi\), así que
\[
\cos(8\pi\sin(6x))=\cos(k\pi)=\pm1\neq0.
\]
Luego \(g'(x)=0\) exactamente cuando \(\cos(6x)=0\), lo cual ocurre solo si \(\sin(6x)=\pm1\). Esto corresponde a los casos \(k=\pm8\), que son las \(12\) soluciones ya contadas. Así,
\[
t=12.
\]

Finalmente,
\[
n+t=191+12=203.
\]

\[
\boxed{203}
\]