Queremos maximizar

\[
f(x,y)=\frac{x-y}{x^4+y^4+6}.
\]

El denominador siempre es positivo, así que el signo de \(f\) es el de \(x-y\). Para un máximo necesitamos \(x>y\).

**Puntos críticos.** Derivando:

\[
\frac{\partial f}{\partial x}=0
\quad\Longrightarrow\quad
x^4+y^4+6=4x^3(x-y),
\]

\[
\frac{\partial f}{\partial y}=0
\quad\Longrightarrow\quad
x^4+y^4+6=-4y^3(x-y).
\]

Igualando ambas expresiones:

\[
4x^3(x-y)=-4y^3(x-y).
\]

Si \(x\neq y\), esto da

\[
x^3=-y^3 \quad\Longrightarrow\quad y=-x.
\]

Entonces

\[
f(x,-x)=\frac{x-(-x)}{x^4+x^4+6}
=\frac{2x}{2x^4+6}
=\frac{x}{x^4+3}.
\]

Maximizamos

\[
g(x)=\frac{x}{x^4+3}.
\]

Su derivada es

\[
g'(x)=\frac{3-3x^4}{(x^4+3)^2}
=\frac{3(1-x^4)}{(x^4+3)^2},
\]

que se anula en \(x=\pm 1\). Como \(g(1)=\frac14\) y \(g(-1)=-\frac14\), el máximo es \(\frac14\), alcanzado en \(x=1,\ y=-1\).

Para confirmar que es máximo global, basta notar la desigualdad

\[
x^4+y^4+6-4(x-y)
=(x^4-4x+3)+(y^4+4y+3)
\ge 0,
\]

pues

\[
x^4-4x+3=(x-1)^2(x^2+2x+3)\ge 0
\]

y

\[
y^4+4y+3=(y+1)^2(y^2-2y+3)\ge 0.
\]

Por lo tanto,

\[
4(x-y)\le x^4+y^4+6
\quad\Longrightarrow\quad
\frac{x-y}{x^4+y^4+6}\le \frac14,
\]

con igualdad en \(x=1,\ y=-1\).

\[
\boxed{\frac14}
\]