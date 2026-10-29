Sea \(O=(0,0)\), y sean los vértices \((\pm a,\pm b)\). El área del rectángulo es \(4ab\). Podemos suponer \(a\ge b\); el otro caso es simétrico.

Para que \(P=(x,y)\) esté más cerca de \(O\) que de \((a,b)\), debe cumplirse
\[
x^2+y^2<(x-a)^2+(y-b)^2
\quad\Longleftrightarrow\quad
ax+by<\frac{a^2+b^2}{2}.
\]
Aplicando esto a los cuatro vértices, obtenemos
\[
a|x|+b|y|<\frac{a^2+b^2}{2}.
\]

Sin considerar los límites del rectángulo, esta región es un rombo con semidiagonales
\[
\frac{a^2+b^2}{2a}\quad\text{y}\quad \frac{a^2+b^2}{2b},
\]
cuya área es \(\frac{(a^2+b^2)^2}{2ab}\). Como \(a\ge b\), el rombo sobresale por arriba y por abajo del rectángulo. Cada porción sobrante es un triángulo de área
\[
\frac{(a^2-b^2)^2}{4ab}.
\]
Por tanto, el área favorable dentro del rectángulo es
\[
\frac{(a^2+b^2)^2}{2ab}
-2\cdot\frac{(a^2-b^2)^2}{4ab}
=2ab.
\]
Dividiendo entre el área total \(4ab\), la probabilidad es

\[
\boxed{\frac12}
\]