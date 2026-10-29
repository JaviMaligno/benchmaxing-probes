Voy a resolver la ecuación paso a paso.

Queremos hallar todas las soluciones complejas de
\[
\frac{1}{x^2-1}+\frac{2}{x^2-2}+\frac{3}{x^2-3}+\frac{4}{x^2-4}=2010x-4.
\]

Primero observamos que los denominadores se anulan en \(x=\pm 1,\pm \sqrt2,\pm \sqrt3,\pm 2\), así que esos valores quedan excluidos. Multiplicamos ambos lados por el producto de los denominadores:
\[
D(x)=(x^2-1)(x^2-2)(x^2-3)(x^2-4).
\]

Obtenemos una ecuación polinómica:
\[
\sum_{k=1}^4 k\prod_{\substack{j=1\\j\neq k}}^4 (x^2-j)=(2010x-4)D(x).
\]

Ahora determinamos el grado de la ecuación resultante. Cada producto \(\prod_{j\neq k}(x^2-j)\) tiene grado 6, así que el lado izquierdo tiene grado a lo sumo 6. En cambio, el lado derecho \((2010x-4)D(x)\) tiene grado \(1+8=9\).

La ecuación polinómica final es de la forma
\[
P(x)=0
\]
donde \(P\) tiene grado 9, con coeficiente principal proveniente del término \(2010x\cdot x^8=2010x^9\).

Nos piden la suma de todas las soluciones complejas de la ecuación polinómica. Para un polinomio
\[
a_9x^9+a_8x^8+\cdots+a_0,
\]
la suma de todas sus raíces complejas (contando multiplicidades) es
\[
-\frac{a_8}{a_9}.
\]

Aquí \(a_9=2010\). Para hallar \(a_8\), observamos que solo el término \(2010x\,D(x)\) contribuye a la potencia \(x^9\), y además \(-4D(x)\) contribuye a \(x^8\). Como \(D(x)\) contiene solamente potencias pares, su coeficiente de \(x^8\) es \(1\). Por tanto, la contribución del lado derecho al coeficiente de \(x^8\) es \(-4\).

El lado izquierdo tiene grado a lo sumo 6, de modo que no contribuye a los coeficientes de \(x^9\) ni \(x^8\).

Así,
\[
a_8=-4.
\]

Por lo tanto, la suma de todas las soluciones complejas es
\[
-\frac{a_8}{a_9}
=-\frac{-4}{2010}
=\frac{4}{2010}
=\frac{2}{1005}.
\]

La respuesta final es

\[
\boxed{\frac{2}{1005}}
\]