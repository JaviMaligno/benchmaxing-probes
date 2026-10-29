

Sea \(Q=(x,y)\) el punto de intersección en el cuarto cuadrante, con \(x>0\) y \(y<0\). Como está en la parábola original,

\[
y=x^2-4 \quad\Longrightarrow\quad x^2=y+4.
\]

Como \(Q\) también está en la imagen de la parábola rotada \(60^\circ\) en sentido antihorario, su preimagen bajo la rotación de \(-60^\circ\) debe estar en la parábola original. La rotación de \(-60^\circ\) da

\[
(X,Y)=\left(\frac{x+\sqrt3\,y}{2},\frac{-\sqrt3\,x+y}{2}\right).
\]

Este punto debe cumplir \(Y=X^2-4\):

\[
\frac{-\sqrt3 x+y}{2}=\left(\frac{x+\sqrt3 y}{2}\right)^2-4.
\]

Multiplicando por \(4\),

\[
2(-\sqrt3 x+y)=x^2+2\sqrt3 xy+3y^2-16.
\]

Usando \(x^2=y+4\),

\[
-2\sqrt3 x+2y=3y^2+2\sqrt3 xy+y-12.
\]

Reordenando,

\[
3y^2-y-12+2\sqrt3 x(y+1)=0,
\]

es decir,

\[
2\sqrt3 x(y+1)=-3y^2+y+12.
\]

Como \(x>0\), al elevar al cuadrado y usar \(x^2=y+4\),

\[
12(y+4)(y+1)^2=(-3y^2+y+12)^2.
\]

Al expandir y simplificar,

\[
9y^4-18y^3-143y^2-84y+96=0.
\]

Este polinomio se factoriza como

\[
(9y^2+9y-8)(y^2-3y-12)=0.
\]

Las raíces son

\[
y=\frac{3\pm\sqrt{57}}{2},\qquad y=\frac{-3\pm\sqrt{41}}{6}.
\]

En el cuarto cuadrante necesitamos \(y<0\). Las dos raíces negativas son

\[
y=\frac{3-\sqrt{57}}{2},\qquad y=\frac{-3-\sqrt{41}}{6}.
\]

Ahora debemos verificar la ecuación sin cuadrar,

\[
2\sqrt3 x(y+1)=-3y^2+y+12.
\]

Para \(y=\frac{3-\sqrt{57}}{2}\), se tiene \(y+1<0\) y además

\[
-3y^2+y+12=-8(y+3)<0,
\]

por lo que \(x>0\). Esta raíz sí corresponde al cuarto cuadrante.

Para \(y=\frac{-3-\sqrt{41}}{6}\), se tiene \(y+1<0\), pero

\[
-3y^2+y+12=\frac{22-2\sqrt{41}}{3}>0,
\]

lo cual forzará \(x<0\), así que no está en el cuarto cuadrante.

Por tanto, la coordenada \(y\) es

\[
y=\frac{3-\sqrt{57}}{2}.
\]

Así,

\[
a=3,\qquad b=57,\qquad c=2,
\]

y

\[
a+b+c=3+57+2=62.
\]

\[
\boxed{62}
\]