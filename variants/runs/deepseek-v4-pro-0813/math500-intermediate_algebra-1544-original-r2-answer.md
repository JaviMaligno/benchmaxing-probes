Voy a razonar paso a paso.

Sea la ecuación cuadrática

\[
x^2+ax+b=0.
\]

Llamemos \(r\) y \(s\) a sus raíces. Como es cuadrática mónica, sus raíces son las dos que determinan el polinomio.

La condición dice: para toda raíz \(c\), el número \(c^2-2\) también es raíz.

---

## 1. Entender la condición

Dado que la ecuación tiene a lo más dos raíces, aplicar \(c\mapsto c^2-2\) a cualquier raíz debe producir una raíz. Esto significa que el conjunto

\[
R=\{r,s\}
\]

es invariante bajo la función

\[
f(c)=c^2-2.
\]

Hay dos posibilidades:

1. \(f(c)=c\), es decir, \(c^2-2=c\), o
2. las dos raíces se intercambian: \(f(r)=s\) y \(f(s)=r\).

---

## 2. Caso 1: una raíz fija bajo \(f\)

Si \(c\) es raíz y \(c^2-2=c\), entonces

\[
c^2-c-2=0
\]

\[
(c-2)(c+1)=0.
\]

Así, \(c=2\) o \(c=-1\).

### Subcaso 1a: ambas raíces son fijas

Las raíces de la ecuación son \(2\) y \(-1\). Entonces el polinomio es

\[
(x-2)(x+1)=x^2-x-2.
\]

Luego

\[
a=-1,\qquad b=-2.
\]

Esto da una ecuación:

\[
x^2-x-2=0.
\]

### Subcaso 1b: una raíz es fija y la otra se transforma en sí misma

Veamos si es posible tener una raíz fija y la otra que se intercambie. La condición \(f(c)=c\) fuerza \(c\in\{-1,2\}\).

Si una raíz es, digamos, \(c=-1\) y la otra es \(d\), entonces \(f(d)\) debe ser otra raíz. Para que solo haya dos raíces, \(f(d)\in\{-1,d\}\). Si \(f(d)=d\), entonces \(d\in\{-1,2\}\), y volvemos al caso de dos raíces fijas: las raíces serían \(\{-1,2\}\), porque si \(d=-1\) habría una raíz repetida.

Si \(d=-1\), entonces la ecuación tendría raíz doble \(-1\):

\[
(x+1)^2=x^2+2x+1,
\]

es decir, \(a=2\), \(b=1\). Comprobemos: \(f(-1)=1-2=-1\), que es raíz. Funciona.

---

## 3. Caso 2: las dos raíces se intercambian

Si \(f(r)=s\) y \(f(s)=r\), entonces \(f(f(r))=r\). Es decir, aplicar dos veces la función \(f\) devuelve la raíz original.

Esto significa que \(r\) satisface

\[
f(f(r))=r.
\]

Calculemos \(f\circ f\):

\[
f(f(c))=(c^2-2)^2-2=c^4-4c^2+4-2=c^4-4c^2+2.
\]

Igualamos a \(c\):

\[
c^4-4c^2+2=c
\]

\[
c^4-4c^2-c+2=0.
\]

Factoricemos. Probamos \(c=1\):

\[
1-4-1+2=-2\neq 0.
\]

Probamos \(c=-1\):

\[
1-4+1+2=0.
\]

Entonces \(c=-1\) es raíz. Dividimos por \(c+1\):

\[
c^4-4c^2-c+2=(c+1)(c^3-c^2-3c+2).
\]

Probamos \(c=2\) en el cúbico:

\[
8-4-6+2=0.
\]

Entonces

\[
c^3-c^2-3c+2=(c-2)(c^2+c-1).
\]

Luego

\[
c^4-4c^2-c+2=(c+1)(c-2)(c^2+c-1).
\]

Las raíces de \(c^2+c-1=0\) son

\[
c=\frac{-1\pm\sqrt{5}}2.
\]

Entonces los posibles valores de las raíces \(r,s\) que se intercambian son dos de estas cuatro soluciones de \(f(f(c))=c\), siempre que \(f\) las intercambie de verdad y no las deje fijas.

Los valores fijos \(c=-1\) y \(c=2\) ya los consideramos. Para valores no fijos, tenemos:

\[
\alpha=\frac{-1+\sqrt5}{2},\qquad \beta=\frac{-1-\sqrt5}{2}.
\]

Calculamos

\[
f(\alpha)=\alpha^2-2.
\]

Como \(\alpha^2=1-\alpha\), porque \(\alpha^2+\alpha-1=0\),

\[
f(\alpha)=1-\alpha-2=-1-\alpha.
\]

Pero \(-1-\alpha=\beta\), ya que \(\alpha+\beta=-1\). Por tanto,

\[
f(\alpha)=\beta,\qquad f(\beta)=\alpha.
\]

Entonces las raíces \(\alpha\) y \(\beta\) se intercambian.

La ecuación con esas raíces es

\[
(x-\alpha)(x-\beta)=x^2-(\alpha+\beta)x+\alpha\beta.
\]

Sabemos que

\[
\alpha+\beta=-1,\qquad \alpha\beta=-1.
\]

Por tanto,

\[
x^2+x-1=0.
\]

Es decir,

\[
a=1,\qquad b=-1.
\]

---

## 4. Considerar raíces dobles

Una ecuación cuadrática puede tener raíz doble. En ese caso, la única raíz \(c\) debe cumplir \(f(c)=c\), porque no hay otra raíz a la que transformarse.

Ya vimos que \(f(c)=c\) da \(c=-1\) o \(c=2\).

- Si \(c=-1\), la ecuación es \((x+1)^2=x^2+2x+1\).
- Si \(c=2\), la ecuación es \((x-2)^2=x^2-4x+4\).

Ambas cumplen la condición.

---

## 5. Recuento de ecuaciones válidas

Tenemos las siguientes ecuaciones:

1. \(x^2-x-2=0\), raíces \(2\) y \(-1\): ambas fijas.
2. \(x^2+2x+1=0\), raíz doble \(-1\): fija.
3. \(x^2-4x+4=0\), raíz doble \(2\): fija.
4. \(x^2+x-1=0\), raíces \(\alpha,\beta\) que se intercambian.

¿Hay alguna más? Revisemos si alguna raíz fija puede aparecer junto a una raíz no fija.

Si una raíz es fija, digamos \(c=-1\), y la otra es \(d\), debe ocurrir \(f(d)\in\{-1,d\}\).

- Si \(f(d)=-1\), entonces \(d^2-2=-1\), luego \(d^2=1\), así \(d=\pm1\). Si \(d=1\), sus raíces serían \(-1\) y \(1\). Verifiquemos \(f(1)=1-2=-1\), que es raíz. Pero ¿\(f(-1)=-1\), raíz? Sí. Entonces \(x^2-1=0\), es decir, \(a=0\), \(b=-1\), ¿cumple?

Comprobemos con más cuidado: raíces \(-1\) y \(1\). Para \(c=-1\), \(f(c)=-1\), raíz. Para \(c=1\), \(f(1)=-1\), raíz. Entonces sí cumple.

Espera, me faltó este caso. Veamos.

Si una raíz es \(c=-1\) fija y la otra \(d\) cumple \(f(d)=-1\), obtuvimos \(d=\pm1\). Si \(d=-1\), es la raíz doble ya considerada. Si \(d=1\), la ecuación es

\[
(x+1)(x-1)=x^2-1,
\]

con \(a=0\), \(b=-1\).

- Si \(f(d)=d\), entonces \(d\in\{-1,2\}\). Si \(d=2\), la ecuación tiene raíces \(-1\) y \(2\), ya considerada.

Análogamente, si la raíz fija es \(c=2\):

- Si \(f(d)=2\), entonces \(d^2-2=2\), luego \(d^2=4\), \(d=\pm2\). Si \(d=-2\), las raíces son \(2\) y \(-2\). La ecuación sería

\[
(x-2)(x+2)=x^2-4,
\]

con \(a=0\), \(b=-4\). Verifiquemos: \(f(2)=2\), raíz; \(f(-2)=4-2=2\), raíz. Cumple.

- Si \(f(d)=d\), entonces \(d\in\{-1,2\}\). El caso \(d=-1\) da raíces \(-1\) y \(2\), ya considerada; \(d=2\) da raíz doble, ya considerada.

---

## 6. Lista final

Las ecuaciones válidas parecen ser:

1. \(x^2-x-2=0\), \(a=-1\), \(b=-2\).
2. \(x^2-1=0\), \(a=0\), \(b=-1\).
3. \(x^2+2x+1=0\), \(a=2\), \(b=1\).
4. \(x^2-4=0\), \(a=0\), \(b=-4\).
5. \(x^2-4x+4=0\), \(a=-4\), \(b=4\).
6. \(x^2+x-1=0\), \(a=1\), \(b=-1\).

Verifiquemos cada una:

1. Raíces \(-1,2\). \(f(-1)=-1\), \(f(2)=2\).
2. Raíces \(-1,1\). \(f(-1)=-1\), \(f(1)=-1\).
3. Raíz doble \(-1\). \(f(-1)=-1\).
4. Raíces \(-2,2\). \(f(-2)=2\), \(f(2)=2\).
5. Raíz doble \(2\). \(f(2)=2\).
6. Raíces \(\alpha,\beta\). \(f(\alpha)=\beta\), \(f(\beta)=\alpha\).

Todas cumplen.

Además, los pares \((a,b)\) son todos distintos:

\[
(-1,-2),\ (0,-1),\ (2,1),\ (0,-4),\ (-4,4),\ (1,-1).
\]

Por tanto, hay \(6\) ecuaciones.

\[
\boxed{6}
\]