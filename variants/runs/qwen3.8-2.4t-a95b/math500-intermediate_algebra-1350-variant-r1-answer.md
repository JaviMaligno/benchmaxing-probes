Sean las raíces enteras y distintas \(r_1,\dots,r_n\). Como el coeficiente principal es \(2\),

\[
g(x)=2\prod_{i=1}^n (x-r_i).
\]

Por Vieta,

\[
c_0=2(-1)^n\prod_{i=1}^n r_i=78,
\]

así que

\[
\prod_{i=1}^n (-r_i)=39.
\]

Definamos \(s_i=-r_i\). Entonces los \(s_i\) son enteros distintos cuyo producto es \(39\). Además,

\[
c_{n-1}= -2\sum_{i=1}^n r_i = 2\sum_{i=1}^n s_i,
\]

por lo que queremos minimizar

\[
|c_{n-1}|=2\left|\sum s_i\right|.
\]

Como \(39=3\cdot 13\), los valores absolutos de los \(s_i\) solo pueden involucrar \(1,3,13,39\), y a lo sumo podemos usar \(1\) y \(-1\).

Casos posibles con producto positivo \(39\):

- \(\{39\}\): suma \(39\).
- \(\{1,39\}\) o \(\{-1,-39\}\): suma \(\pm 40\).
- \(\{1,-1,-39\}\): suma \(-39\).
- \(\{3,13\}\) o \(\{-3,-13\}\): suma \(\pm 16\).
- Con \(\{1,3,13\}\), las combinaciones de signo válidas dan sumas \(17,-15,-11,9\). La menor en valor absoluto es \(9\), lograda con \(\{-1,-3,13\}\).
- Con \(\{1,-1,3,13\}\), las combinaciones válidas dan sumas \(\pm 10\).

Por tanto, el mínimo posible de \(\left|\sum s_i\right|\) es \(9\). Luego

\[
\min |c_{n-1}|=2\cdot 9=18.
\]

Esto se alcanza, por ejemplo, con raíces \(1,3,-13\):

\[
g(x)=2(x-1)(x-3)(x+13)=2x^3+18x^2-98x+78.
\]

\[
\boxed{18}
\]