Vamos a resolver el problema paso a paso.

Queremos minimizar

\[
f(x,y,z)=x^4+4y^2+4z^4
\]

sujeto a \(xyz=2\), con \(x,y,z>0\).

## 1. Aplicamos la desigualdad AM-GM

Idea: repartir cada término en varios términos iguales para que, al aplicar AM-GM, el producto sea constante.

- \(x^4\): un solo término.
- \(4y^2\): lo separamos como \(2y^2+2y^2\).
- \(4z^4\): lo separamos como \(z^4+z^4+z^4+z^4\).

Así tenemos 7 términos:

\[
x^4,\; 2y^2,\; 2y^2,\; z^4,\; z^4,\; z^4,\; z^4.
\]

Por AM-GM:

\[
\frac{x^4+2y^2+2y^2+z^4+z^4+z^4+z^4}{7}
\ge \sqrt[7]{x^4\cdot (2y^2)^2 \cdot (z^4)^4}.
\]

El producto interior es

\[
x^4\cdot 4y^4\cdot z^{16}=4x^4y^4z^{16}.
\]

Usando \(xyz=2\):

\[
x^4y^4z^{16}=(xyz)^4 z^{12}=2^4 z^{12}=16z^{12}.
\]

Esto no es constante, pues depende de \(z\). El AM-GM directo con estos pesos no iguala términos de forma que el producto sea constante. Necesitamos pesos diferentes.

## 2. Método con multiplicadores de Lagrange

Minimizamos \(f\) sujeto a \(g=xyz-2=0\).

Las derivadas parciales son:

\[
\frac{\partial f}{\partial x}=4x^3,\qquad
\frac{\partial f}{\partial y}=8y,\qquad
\frac{\partial f}{\partial z}=16z^3.
\]

Y

\[
\frac{\partial g}{\partial x}=yz,\qquad
\frac{\partial g}{\partial y}=xz,\qquad
\frac{\partial g}{\partial z}=xy.
\]

Las condiciones de Lagrange:

\[
4x^3=\lambda yz,\qquad 8y=\lambda xz,\qquad 16z^3=\lambda xy.
\]

Multiplicando cada ecuación respectivamente por \(x,y,z\):

\[
4x^4=\lambda xyz=2\lambda,
\]

\[
8y^2=\lambda xyz=2\lambda,
\]

\[
16z^4=\lambda xyz=2\lambda.
\]

Entonces:

\[
4x^4=8y^2=16z^4.
\]

Sea este valor común \(k=2\lambda\). Así:

\[
x^4=\frac{k}{4},\qquad y^2=\frac{k}{8},\qquad z^4=\frac{k}{16}.
\]

Por tanto:

\[
x=\left(\frac{k}{4}\right)^{1/4},\quad
y=\left(\frac{k}{8}\right)^{1/2},\quad
z=\left(\frac{k}{16}\right)^{1/4}.
\]

## 3. Imponemos la restricción \(xyz=2\)

Entonces:

\[
\left(\frac{k}{4}\right)^{1/4}
\left(\frac{k}{8}\right)^{1/2}
\left(\frac{k}{16}\right)^{1/4}=2.
\]

Sumando exponentes de \(k\):

\[
\frac14+\frac12+\frac14=1.
\]

Luego:

\[
k^1\cdot \frac{1}{4^{1/4}}\cdot \frac{1}{8^{1/2}}\cdot \frac{1}{16^{1/4}}=2.
\]

Calculamos el denominador. Escribimos todo en potencias de 2:

- \(4^{1/4}=(2^2)^{1/4}=2^{1/2}\).
- \(8^{1/2}=(2^3)^{1/2}=2^{3/2}\).
- \(16^{1/4}=(2^4)^{1/4}=2\).

El producto es:

\[
2^{1/2}\cdot 2^{3/2}\cdot 2=2^{1/2+3/2+1}=2^3=8.
\]

Así:

\[
\frac{k}{8}=2 \implies k=16.
\]

## 4. Valor mínimo

El valor común es \(k=16\). Por tanto:

\[
4x^4=16 \implies x^4=4,
\]

\[
8y^2=16 \implies y^2=2,
\]

\[
16z^4=16 \implies z^4=1.
\]

Así:

\[
x=\sqrt[4]{4}=\sqrt{2},\qquad y=\sqrt{2},\qquad z=1.
\]

Comprobamos:

\[
xyz=\sqrt2\cdot \sqrt2\cdot 1=2.
\]

La suma es:

\[
x^4+4y^2+4z^4=4+4\cdot 2+4\cdot 1=4+8+4=16.
\]

El mínimo es

\[
\boxed{16}.
\]

Nota: se puede justificar que efectivamente es mínimo porque la función tiende a infinito cuando alguna variable tiende a \(0\) o a infinito sobre la restricción, y el punto crítico único es el encontrado.