

Sean las raíces enteras distintas \(r_1,\dots,r_n\). Como el coeficiente principal es \(2\),

\[
g(x)=2\prod_{i=1}^n (x-r_i).
\]

Por Vieta,

\[
c_0=2(-1)^n\prod_{i=1}^n r_i=78
\quad\Longrightarrow\quad
(-1)^n\prod_{i=1}^n r_i=39.
\]

Definiendo \(s_i=-r_i\), los \(s_i\) son enteros distintos no nulos y

\[
\prod_{i=1}^n s_i=39.
\]

Además,

\[
c_{n-1}=-2\sum_{i=1}^n r_i=2\sum_{i=1}^n s_i,
\]

por lo que queremos minimizar \(\left|\sum s_i\right|\).

Como \(39=3\cdot 13\) es libre de cuadrados, los valores absolutos posibles de los factores son \(1,3,13,39\). A lo sumo podemos usar \(1\) y \(-1\) como factores de valor absoluto \(1\).

Consideramos los casos:

- Si usamos el factor \(39\), la suma tiene valor absoluto al menos \(39\).
- Si usamos \(3\) y \(13\) por separado, probamos signos y posibles factores \(\pm1\):
  \[
  -3+13-1=9,
  \]
  con producto
  \[
  (-3)(13)(-1)=39.
  \]
  Esto da \(\left|\sum s_i\right|=9\), y no hay ninguna combinación válida con suma absoluta menor.

Por tanto,

\[
\min |c_{n-1}|=2\cdot 9=18.
\]

De hecho, se alcanza con raíces \(3,-13,1\):

\[
g(x)=2(x-3)(x-1)(x+13)=2x^3+18x^2-98x+78.
\]

\[
\boxed{18}
\]