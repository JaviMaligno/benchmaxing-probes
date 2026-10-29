

Sea \(f(t)=t^2-2\). Si \(R\) es el conjunto de raíces de la ecuación, la condición es \(f(R)\subseteq R\). Como una ecuación cuadrática tiene a lo sumo dos raíces distintas, las órbitas bajo \(f\) solo pueden ser puntos fijos, un ciclo de periodo \(2\), o un punto que cae en un punto fijo.

1. **Puntos fijos**:
\[
t^2-2=t \implies t^2-t-2=0 \implies t=2,\,-1.
\]
Esto da las ecuaciones con raíz doble:
\[
(x-2)^2=x^2-4x+4,\qquad (x+1)^2=x^2+2x+1.
\]

2. **Dos puntos fijos como raíces**:
\[
\{2,-1\}\implies (x-2)(x+1)=x^2-x-2.
\]

3. **Ciclo de periodo \(2\)**:
\[
f(f(t))=t \implies (t^2-2)^2-2=t
\]
\[
t^4-4t^2-t+2=0=(t-2)(t+1)(t^2+t-1).
\]
Excluyendo los puntos fijos, queda \(t^2+t-1=0\), cuyas dos raíces se intercambian bajo \(f\). Esto da:
\[
x^2+x-1=0.
\]

4. **Un punto fijo y otro punto que cae en él**:
- Si el punto fijo es \(2\): \(t^2-2=2\implies t=\pm2\). Además de \(2\), está \(-2\), dando raíces \(\{2,-2\}\):
\[
x^2-4=0.
\]
- Si el punto fijo es \(-1\): \(t^2-2=-1\implies t=\pm1\). Además de \(-1\), está \(1\), dando raíces \(\{-1,1\}\):
\[
x^2-1=0.
\]

En total hay \(6\) ecuaciones.

\[
\boxed{6}
\]