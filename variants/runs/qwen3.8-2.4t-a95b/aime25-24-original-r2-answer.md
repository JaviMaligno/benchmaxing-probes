

Sea
\[
f(x)=\sin\left(7\pi\sin(5x)\right).
\]

Para que \(f(x)=0\), necesitamos
\[
7\pi\sin(5x)=k\pi \quad\Longleftrightarrow\quad \sin(5x)=\frac{k}{7},
\]
donde \(k\) es un entero. Como \(\sin(5x)\in[-1,1]\), debemos tener
\[
k=-7,-6,\dots,6,7.
\]

Ahora contamos cuántas soluciones hay en \(0<x<2\pi\). Si \(u=5x\), entonces \(u\in(0,10\pi)\), que son 5 periodos completos de la función seno.

- Para \(k=0\), \(\sin u=0\). Las soluciones son \(u=j\pi\). En \((0,10\pi)\), esto da \(j=1,2,\dots,9\), así que hay \(9\) soluciones.

- Para \(k=\pm 7\), \(\sin u=\pm 1\). Hay una solución por periodo, así que hay \(5+5=10\) soluciones.

- Para \(k=\pm1,\pm2,\dots,\pm6\), hay 12 valores posibles de \(k\), cada uno con \(\sin u\in(-1,1)\setminus\{0\}\). En cada periodo hay 2 soluciones, así que cada uno aporta \(10\) soluciones. En total:
\[
12\cdot 10=120.
\]

Por lo tanto,
\[
n=9+10+120=139.
\]

Ahora determinamos cuándo la gráfica es tangente al eje \(x\). Calculamos
\[
f'(x)=35\pi\cos\left(7\pi\sin(5x)\right)\cos(5x).
\]

En un cero de \(f\), tenemos \(\sin(5x)=k/7\), por lo que
\[
\cos\left(7\pi\sin(5x)\right)=\cos(k\pi)=\pm1\neq 0.
\]

Así que \(f'(x)=0\) ocurre exactamente cuando
\[
\cos(5x)=0,
\]
lo cual implica
\[
\sin(5x)=\pm1.
\]

Estos son precisamente los casos \(k=\pm7\), que ya contamos con \(10\) soluciones. En esos puntos, \(f\) tiene un cero de multiplicidad par, por lo que la gráfica es tangente al eje \(x\). Así,
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