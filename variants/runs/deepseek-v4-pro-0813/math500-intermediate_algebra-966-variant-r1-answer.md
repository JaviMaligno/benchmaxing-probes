Vamos a resolver el problema paso a paso.

Queremos minimizar

\[
F(a,b,c)=a^4+6b^2+9c^4
\]

sujeto a \(a,b,c>0\) y \(abc=3\).

---

**Paso 1: Aplicar la desigualdad AM-GM**

Inspirándonos en la condición \(abc=3\), buscamos coeficientes que se ajusten. Una forma directa es usar la desigualdad de la media aritmética y la media geométrica:

\[
\frac{a^4+6b^2+9c^4}{4}
\ge \sqrt[4]{a^4\cdot 6b^2\cdot 9c^4}
\]

Pero AM-GM con 4 términos no encaja directamente, porque tenemos tres sumandos y 6 y 9 son coeficientes, no repeticiones.

Mejor escribimos los términos de modo que el número de sumandos sea 4 y sus exponentes se igualen. Notemos que:

\[
6b^2 = b^2+b^2+b^2+b^2+b^2+b^2
\]

y

\[
9c^4 = c^4+c^4+\cdots+c^4\quad (9\ \text{veces}).
\]

Eso da demasiados términos. En su lugar, buscamos pesos.

---

**Paso 2: Método de multiplicadores de Lagrange**

Definimos

\[
L(a,b,c,\lambda)=a^4+6b^2+9c^4+\lambda(abc-3).
\]

Las condiciones de primer orden son:

\[
\frac{\partial L}{\partial a}=4a^3+\lambda bc=0
\]

\[
\frac{\partial L}{\partial b}=12b+\lambda ac=0
\]

\[
\frac{\partial L}{\partial c}=36c^3+\lambda ab=0.
\]

Multiplicando la primera por \(a\), la segunda por \(b\) y la tercera por \(c\):

\[
4a^4+\lambda abc=0
\]

\[
12b^2+\lambda abc=0
\]

\[
36c^4+\lambda abc=0.
\]

Como \(\lambda abc\) es común, tenemos

\[
4a^4=12b^2=36c^4.
\]

Dividiendo por 4:

\[
a^4=3b^2=9c^4.
\]

---

**Paso 3: Expresar \(a,b,c\) en términos de un parámetro**

Sea

\[
a^4=3b^2=9c^4=t.
\]

Entonces

\[
a=t^{1/4}
\]

\[
b=\sqrt{\frac{t}{3}}
\]

\[
c=\left(\frac{t}{9}\right)^{1/4}.
\]

Usamos la restricción \(abc=3\):

\[
t^{1/4}\cdot \left(\frac{t}{3}\right)^{1/2}\cdot \left(\frac{t}{9}\right)^{1/4}=3.
\]

Calculamos el lado izquierdo:

Exponente total de \(t\):

\[
\frac14+\frac12+\frac14=1.
\]

Así que

\[
abc=t\cdot 3^{-1/2}\cdot 9^{-1/4}.
\]

Pero \(9^{-1/4}=3^{-1/2}\), luego

\[
abc=t\cdot 3^{-1/2}\cdot 3^{-1/2}=t\cdot 3^{-1}=\frac{t}{3}.
\]

Por tanto,

\[
\frac{t}{3}=3
\]

y

\[
t=9.
\]

---

**Paso 4: Hallar el valor mínimo**

Con \(t=9\):

\[
a=9^{1/4}=\sqrt{3}
\]

\[
b=\sqrt{\frac{9}{3}}=\sqrt{3}
\]

\[
c=\left(\frac{9}{9}\right)^{1/4}=1.
\]

Entonces

\[
F(\sqrt3,\sqrt3,1)=(\sqrt3)^4+6(\sqrt3)^2+9\cdot 1^4.
\]

\[
(\sqrt3)^4=9
\]

\[
6(\sqrt3)^2=6\cdot 3=18
\]

\[
9\cdot 1^4=9.
\]

Sumando:

\[
9+18+9=36.
\]

---

**Conclusión.** El valor mínimo es

\[
\boxed{36}
\]