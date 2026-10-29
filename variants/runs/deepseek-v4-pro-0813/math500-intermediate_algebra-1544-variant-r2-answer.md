Vamos a razonar paso a paso.

Sea la ecuación

\[
x^2+px+q=0.
\]

Queremos que siempre que \(t\) sea raíz, entonces

\[
f(t)=t^2-4t+6
\]

también sea raíz.

Cuando una cuadrática cumple esta propiedad, las raíces deben formar conjuntos cerrados bajo la aplicación \(f\). Como \(f\) aplica el conjunto de raíces en sí mismo, y el conjunto de raíces tiene a lo sumo 2 elementos, debemos analizar los casos posibles.

---

## 1. Raíz doble

Si la ecuación tiene una raíz doble \(r\), entonces:

\[
x^2+px+q=(x-r)^2,
\]

así que

\[
p=-2r,\qquad q=r^2.
\]

La condición es que \(f(r)\) también sea raíz. Como la única raíz es \(r\), debe cumplirse:

\[
f(r)=r.
\]

Entonces:

\[
r^2-4r+6=r,
\]

\[
r^2-5r+6=0,
\]

\[
(r-2)(r-3)=0.
\]

Por lo tanto \(r=2\) o \(r=3\).

- Si \(r=2\):

\[
p=-4,\qquad q=4.
\]

- Si \(r=3\):

\[
p=-6,\qquad q=9.
\]

Obtenemos dos ecuaciones válidas.

---

## 2. Dos raíces distintas

Sean las raíces \(a\) y \(b\), con \(a\neq b\).

Como \(f(a)\) debe ser raíz, tenemos:

\[
f(a)=a \quad\text{o}\quad f(a)=b.
\]

Análogamente para \(b\).

### Caso 2.1: \(f(a)=a\) y \(f(b)=b\)

Entonces \(a\) y \(b\) son puntos fijos de \(f\). Los puntos fijos son los que ya calculamos:

\[
f(t)=t \iff t^2-5t+6=0 \iff t=2 \text{ o } t=3.
\]

Los únicos puntos fijos son \(2\) y \(3\). Por tanto, como las raíces deben ser distintas, las raíces serían \(2\) y \(3\). Esto da la ecuación:

\[
(x-2)(x-3)=x^2-5x+6,
\]

es decir,

\[
p=-5,\qquad q=6.
\]

Esta es una ecuación válida.

### Caso 2.2: una raíz se aplica en la otra y viceversa

Supongamos

\[
f(a)=b,\qquad f(b)=a.
\]

Entonces \(a\) y \(b\) forman un 2-ciclo de \(f\).

Calculamos \(f(f(t))\). Tenemos:

\[
f(t)=t^2-4t+6.
\]

Entonces:

\[
f(f(t))=(t^2-4t+6)^2-4(t^2-4t+6)+6.
\]

Un 2-ciclo cumple \(f(f(t))=t\) y \(f(t)\neq t\).

Desarrollamos:

\[
(t^2-4t+6)^2 = t^4-8t^3+28t^2-48t+36.
\]

Luego:

\[
-4(t^2-4t+6)=-4t^2+16t-24.
\]

Y sumamos \(6\):

\[
f(f(t)) = t^4-8t^3+28t^2-48t+36-4t^2+16t-24+6,
\]

\[
f(f(t))=t^4-8t^3+24t^2-32t+18.
\]

Igualamos a \(t\):

\[
t^4-8t^3+24t^2-33t+18=0.
\]

Factoricemos. Observemos que los puntos fijos \(t=2\) y \(t=3\) son también soluciones de \(f(f(t))=t\), pero queremos soluciones distintas de los puntos fijos.

Factorizamos:

\[
t^4-8t^3+24t^2-33t+18.
\]

Probamos \(t=2\):

\[
16-64+96-66+18=0.
\]

Probamos \(t=3\):

\[
81-216+216-99+18=0.
\]

Así que \((t-2)(t-3)=t^2-5t+6\) divide al polinomio.

Dividimos:

\[
t^4-8t^3+24t^2-33t+18
\]

entre \(t^2-5t+6\).

Primer término: \(t^2\), restamos:

\[
t^4-5t^3+6t^2,
\]

queda:

\[
-3t^3+18t^2-33t+18.
\]

Segundo término: \(-3t\), restamos:

\[
-3t^3+15t^2-18t,
\]

queda:

\[
3t^2-15t+18.
\]

Tercer término: \(3\), restamos:

\[
3t^2-15t+18,
\]

queda \(0\).

Por tanto:

\[
f(f(t))-t=(t^2-5t+6)(t^2-3t+3).
\]

El 2-ciclo corresponde a las raíces de:

\[
t^2-3t+3=0.
\]

Pero su discriminante es:

\[
\Delta=(-3)^2-4\cdot 1\cdot 3=9-12=-3<0.
\]

Por tanto, no hay raíces reales. Como estamos trabajando con ecuaciones cuadráticas usuales con raíces reales o complejas, estas soluciones serían complejas. Sin embargo, el problema no dice explícitamente que \(p,q\) sean reales. Analicemos con cuidado.

Si permitimos raíces complejas, las dos raíces de \(t^2-3t+3=0\) son:

\[
t=\frac{3\pm i\sqrt{3}}{2}.
\]

Estas dos raíces forman un 2-ciclo de \(f\), es decir:

\[
a=\frac{3+i\sqrt{3}}{2},\qquad b=\frac{3-i\sqrt{3}}{2}.
\]

La ecuación cuadrática con esas raíces es:

\[
t^2-3t+3=0,
\]

es decir,

\[
p=-3,\qquad q=3.
\]

Esta también cumple la propiedad, porque al evaluar \(f\) en cualquiera de las dos raíces se obtiene la otra.

Si el problema se restringe a \(p,q\) reales, \(p=-3,\ q=3\) sigue siendo admisible porque la cuadrática tiene coeficientes reales, aunque sus raíces sean complejas. La propiedad pedida no exige que las raíces sean reales.

### Caso 2.3: una raíz es fija y la otra se aplica sobre sí misma

Este caso ya quedó cubierto en 2.1, porque si ambas son fijas, son exactamente \(2\) y \(3\).

No hay otras posibilidades, pues:

- Si \(f(a)=a\) y \(f(b)=a\), entonces la raíz \(b\) se aplica a \(a\), pero \(f\) debe restringirse biyectivamente sobre el conjunto de raíces, lo que obligaría a \(b=a\), contradiciendo que son distintas. Igualmente para casos mixtos.

---

## 3. Recuento final

Las ecuaciones válidas son:

1. \(x^2-4x+4=0\), raíz doble \(2\).  
   Coeficientes: \(p=-4,\ q=4\).

2. \(x^2-6x+9=0\), raíz doble \(3\).  
   Coeficientes: \(p=-6,\ q=9\).

3. \(x^2-5x+6=0\), raíces \(2\) y \(3\).  
   Coeficientes: \(p=-5,\ q=6\).

4. \(x^2-3x+3=0\), raíces \(a=\frac{3+i\sqrt{3}}2\), \(b=\frac{3-i\sqrt{3}}2\).  
   Coeficientes: \(p=-3,\ q=3\).

Por tanto, hay

\[
\boxed{4}
\]

ecuaciones cuadráticas.