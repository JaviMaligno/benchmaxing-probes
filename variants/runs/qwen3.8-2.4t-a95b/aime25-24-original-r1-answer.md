

Sea

\[
f(x)=\sin\left(7\pi\sin(5x)\right).
\]

Queremos contar los \(x\in(0,2\pi)\) tales que \(f(x)=0\).

### 1. Condición para que \(f(x)=0\)

\[
\sin\left(7\pi\sin(5x)\right)=0
\]

si y solo si

\[
7\pi\sin(5x)=k\pi
\]

para algún entero \(k\). Por tanto,

\[
\sin(5x)=\frac{k}{7}.
\]

Como \(\sin(5x)\in[-1,1]\), debemos tener

\[
k=-7,-6,\dots,6,7.
\]

### 2. Contar soluciones para cada \(k\)

Hagamos \(u=5x\). Como \(0<x<2\pi\), tenemos

\[
0<u<10\pi,
\]

que son 5 periodos completos de la función seno, pero con extremos abiertos.

- Para \(k=\pm 7\), tenemos \(\sin(5x)=\pm 1\). En cada periodo hay una solución, así que hay

\[
5+5=10
\]

soluciones.

- Para \(k=\pm1,\pm2,\dots,\pm6\), hay 12 valores de \(k\), y cada uno corresponde a un valor en \((-1,1)\setminus\{0\}\). En cada periodo hay 2 soluciones, y ningún problema en los extremos. Así, cada uno aporta 10 soluciones:

\[
12\cdot 10=120.
\]

- Para \(k=0\), necesitamos \(\sin(5x)=0\), es decir,

\[
5x=m\pi.
\]

Como \(0<x<2\pi\), esto da \(0<m<10\), luego \(m=1,2,\dots,9\). Hay

\[
9
\]

soluciones.

Por lo tanto,

\[
n=10+120+9=139.
\]

### 3. Contar cuándo la gráfica es tangente al eje \(x\)

La gráfica es tangente al eje \(x\) en un cero si además \(f'(x)=0\). Calculamos:

\[
f'(x)=35\pi\cos(5x)\cos\left(7\pi\sin(5x)\right).
\]

En un cero, \(\sin(5x)=k/7\), así que

\[
\cos\left(7\pi\sin(5x)\right)=\cos(k\pi)=\pm1\neq 0.
\]

Por tanto, \(f'(x)=0\) si y solo si

\[
\cos(5x)=0,
\]

lo cual ocurre exactamente cuando

\[
\sin(5x)=\pm1.
\]

Esos son los casos \(k=\pm7\), que ya contamos, y aportan

\[
t=10.
\]

Finalmente,

\[
n+t=139+10=149.
\]

\[
\boxed{149}
\]