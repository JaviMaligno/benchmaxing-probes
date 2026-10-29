

Sea  
\[
P(x)=(x^2-1)(x^2-2)(x^2-3)(x^2-4).
\]

Multiplicamos la ecuación por \(P(x)\), fuera de los polos \(x^2=1,2,3,4\):

\[
\sum_{k=1}^4 k\prod_{j\ne k}(x^2-j)+(4-2022x)P(x)=0.
\]

Llamemos \(Q(x)\) al polinomio resultante. Cada término del sumatorio tiene grado a lo sumo \(6\), pues es un producto de tres factores cuadráticos. Por tanto, los términos de grado \(9\) y \(8\) provienen solo de \((4-2022x)P(x)\).

Como \(P(x)\) es mónico de grado \(8\) y solo tiene potencias pares,

\[
P(x)=x^8-10x^6+\cdots
\]

Entonces

\[
(4-2022x)P(x)=-2022x^9+4x^8+\cdots
\]

Así, \(Q(x)\) tiene grado \(9\), con coeficiente principal \(-2022\) y coeficiente de \(x^8\) igual a \(4\).

Además, si \(x^2=m\) con \(m\in\{1,2,3,4\}\), entonces

\[
Q(x)=m\prod_{j\ne m}(m-j)\ne 0,
\]

por lo que no se introducen raíces espurias en los polos.

Por las fórmulas de Vieta, la suma de todas las raíces complejas, contadas con multiplicidad, es

\[
-\frac{4}{-2022}=\frac{4}{2022}=\frac{2}{1011}.
\]

\[
\boxed{\frac{2}{1011}}
\]