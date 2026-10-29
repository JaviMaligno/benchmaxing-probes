Sea
\[
f(x)=px^2+qx+r.
\]
Como \(0,1,2\in[0,2]\), se cumple
\[
|f(0)|\le 1,\qquad |f(1)|\le 1,\qquad |f(2)|\le 1.
\]

Definamos
\[
y_0=f(0)=r,\quad y_1=f(1)=p+q+r,\quad y_2=f(2)=4p+2q+r.
\]
Resolviendo para \(p,q,r\):
\[
p=\frac{y_0-2y_1+y_2}{2},\qquad
q=\frac{-3y_0+4y_1-y_2}{2},\qquad
r=y_0.
\]

Ahora acotamos las cuatro posibles combinaciones de signos:

1. 
\[
p+q+r=y_1,
\]
luego
\[
|p+q+r|\le 1.
\]

2. 
\[
p+q-r=y_1-2y_0,
\]
luego
\[
|p+q-r|\le |y_1|+2|y_0|\le 3.
\]

3. 
\[
p-q+r=3y_0-3y_1+y_2,
\]
luego
\[
|p-q+r|\le 3|y_0|+3|y_1|+|y_2|\le 7.
\]

4. 
\[
p-q-r=y_0-3y_1+y_2,
\]
luego
\[
|p-q-r|\le |y_0|+3|y_1|+|y_2|\le 5.
\]

Como
\[
|p|+|q|+|r|
=
\max\{|p+q+r|,\ |p+q-r|,\ |p-q+r|,\ |p-q-r|\},
\]
se obtiene
\[
|p|+|q|+|r|\le 7.
\]

Este valor se alcanza con
\[
f(x)=2x^2-4x+1=2(x-1)^2-1.
\]
Para \(0\le x\le 2\), se tiene \((x-1)^2\in[0,1]\), así que \(|f(x)|\le 1\). Sus coeficientes son \(p=2\), \(q=-4\), \(r=1\), y
\[
|p|+|q|+|r|=2+4+1=7.
\]

Por lo tanto, el máximo valor posible es
\[
\boxed{7}.
\]