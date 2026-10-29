Sea \(r_1,\dots,r_n\) las raíces. Entonces
\[
f(x)=2\prod_{i=1}^n(x-r_i),
\]
por lo que
\[
|a_0|=2\prod_{i=1}^n|r_i|=66
\quad\Longrightarrow\quad
\prod_{i=1}^n|r_i|=33=3\cdot11.
\]
Además,
\[
a_{n-1}=-2\sum_{i=1}^n r_i,
\]
así que debemos minimizar el valor absoluto de la suma de las raíces.

Como las raíces son enteras, distintas y no nulas, solo pueden aparecer una o dos raíces de valor absoluto mayor que \(1\):

- Si aparecen \(3\) y \(11\) en valor absoluto, sus signos pueden hacer que su suma sea \(\pm8\) o \(\pm14\). Añadir una raíz \(1\) o \(-1\) permite obtener una suma total de valor absoluto mínimo \(7\).
- Si solo aparece una raíz no unitaria, su valor absoluto es \(33\), y las posibles raíces \(\pm1\) no pueden reducir la suma por debajo de \(32\) en valor absoluto.

El mínimo se alcanza con las raíces \(1,3,-11\), cuya suma es \(-7\) y cuyo producto es \(-33\). En efecto,
\[
f(x)=2(x-1)(x-3)(x+11)
\]
cumple las condiciones y tiene \(a_{n-1}=14\). Por tanto, el valor mínimo es
\[
\boxed{14}
\]