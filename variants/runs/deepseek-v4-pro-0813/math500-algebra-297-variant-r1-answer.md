Voy a resolver el sistema paso a paso.

Tenemos

\[
y=x^2-7 \tag{1}
\]

y

\[
y^2=-9x+45 \tag{2}
\]

Sustituyo \(y=x^2-7\) en la segunda ecuación:

\[
(x^2-7)^2=-9x+45
\]

Desarrollo el cuadrado:

\[
x^4-14x^2+49=-9x+45
\]

Llevo todo a un lado:

\[
x^4-14x^2+49+9x-45=0
\]

\[
x^4-14x^2+9x+4=0
\]

Probamos raíces enteras. Para \(x=1\):

\[
1-14+9+4=0
\]

Así que \(x=1\) es una solución. Dividimos el polinomio entre \(x-1\).

Usando división sintética sobre coeficientes \(1,0,-14,9,4\):

\[
\begin{array}{c|cccc}
1 & 1 & 0 & -14 & 9 & 4 \\
  &   & 1 & 1 & -13 & -4 \\
\hline
  & 1 & 1 & -13 & -4 & 0
\end{array}
\]

El cociente es

\[
x^3+x^2-13x-4
\]

Probamos de nuevo raíces. Para \(x=4\):

\[
64+16-52-4=24\ne 0
\]

Para \(x=-4\):

\[
-64+16+52-4=0
\]

Así que \(x=-4\) también es raíz. Dividimos el cúbico entre \(x+4\):

\[
\begin{array}{c|cccc}
-4 & 1 & 1 & -13 & -4 \\
   &   & -4 & 12 & 4 \\
\hline
   & 1 & -3 & -1 & 0
\end{array}
\]

El cociente queda

\[
x^2-3x-1
\]

Resolvemos:

\[
x=\frac{3\pm\sqrt{9+4}}{2}
\]

\[
x=\frac{3\pm\sqrt{13}}{2}
\]

Por tanto, las soluciones para \(x\) son:

\[
x=1,\quad x=-4,\quad x=\frac{3+\sqrt{13}}{2},\quad x=\frac{3-\sqrt{13}}{2}
\]

Ahora calculamos las \(y\)-coordenadas con \(y=x^2-7\).

- Para \(x=1\):

\[
y=1-7=-6
\]

- Para \(x=-4\):

\[
y=16-7=9
\]

- Para \(x=\frac{3+\sqrt{13}}{2}\):

\[
x^2=\frac{(3+\sqrt{13})^2}{4}
\]

\[
(3+\sqrt{13})^2=9+6\sqrt{13}+13=22+6\sqrt{13}
\]

\[
x^2=\frac{22+6\sqrt{13}}{4}=\frac{11+3\sqrt{13}}{2}
\]

Entonces

\[
y=\frac{11+3\sqrt{13}}{2}-7
\]

\[
y=\frac{11+3\sqrt{13}-14}{2}
\]

\[
y=\frac{-3+3\sqrt{13}}{2}
\]

\[
y=\frac{3(\sqrt{13}-1)}{2}
\]

- Para \(x=\frac{3-\sqrt{13}}{2}\):

\[
(3-\sqrt{13})^2=9-6\sqrt{13}+13=22-6\sqrt{13}
\]

\[
x^2=\frac{22-6\sqrt{13}}{4}=\frac{11-3\sqrt{13}}{2}
\]

Entonces

\[
y=\frac{11-3\sqrt{13}}{2}-7
\]

\[
y=\frac{11-3\sqrt{13}-14}{2}
\]

\[
y=\frac{-3-3\sqrt{13}}{2}
\]

\[
y=-\frac{3(\sqrt{13}+1)}{2}
\]

Las \(y\)-coordenadas de las soluciones son:

\[
-6,\quad 9,\quad \frac{3(\sqrt{13}-1)}{2},\quad -\frac{3(\sqrt{13}+1)}{2}
\]

Calculamos el producto:

\[
(-6)(9)\left(\frac{3(\sqrt{13}-1)}{2}\right)\left(-\frac{3(\sqrt{13}+1)}{2}\right)
\]

Primero,

\[
(-6)(9)=-54
\]

Luego los otros dos factores:

\[
\frac{3(\sqrt{13}-1)}{2}\cdot \left(-\frac{3(\sqrt{13}+1)}{2}\right)
\]

\[
=-\frac{9(\sqrt{13}-1)(\sqrt{13}+1)}{4}
\]

\[
=-\frac{9(13-1)}{4}
\]

\[
=-\frac{9\cdot 12}{4}
\]

\[
=-\frac{108}{4}=-27
\]

Finalmente:

\[
(-54)(-27)=1458
\]

\[
\boxed{1458}
\]