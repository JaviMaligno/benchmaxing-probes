

Tomamos un hexágono regular de lado \(1\). Su área es

\[
A=6\cdot \frac{\sqrt3}{4}=\frac{3\sqrt3}{2},
\]

y la distancia entre cualquier par de lados opuestos es

\[
D=\sqrt3.
\]

Ignoramos casos de medida nula: puntos coincidentes o rectas que pasan exactamente por vértices.

---

### 1. Densidad inducida por dos puntos aleatorios

Parametricemos una recta no orientada por \((\theta,p)\), donde \(\theta\) es la dirección de su normal y \(p\) su distancia firmada al origen. Para una recta \(L\), sea \(\ell(L)\) la longitud de la cuerda \(L\cap H\).

Si dos puntos \(X,Y\) están sobre una misma recta \(L\), con coordenadas \(s,t\) a lo largo de la cuerda, el cambio de variables da

\[
dX\,dY = |s-t|\,d\theta\,dp\,ds\,dt.
\]

Integrando sobre todas las posiciones posibles de \(X,Y\) dentro de la cuerda de longitud \(\ell\),

\[
\int_0^\ell\int_0^\ell |s-t|\,ds\,dt=\frac{\ell^3}{3}.
\]

Por tanto, la probabilidad de que la recta determinada por dos puntos uniformes pertenezca a un conjunto de rectas \(S\) es

\[
\mathbb P(L\in S)=\frac{1}{A^2}\int_S \frac{\ell^3}{3}\,d\theta\,dp
=\frac{\int_S \ell^3\,d\theta\,dp}{3A^2}.
\]

Así, el peso de una recta es proporcional a \(\ell^3\).

---

### 2. Peso de las rectas que cortan un par fijo de lados opuestos

Colocamos el hexágono con centro en el origen y consideramos el par de lados opuestos horizontales:

\[
E_+: y=\frac{D}{2},\quad x\in\left[-\frac12,\frac12\right],
\]
\[
E_-: y=-\frac{D}{2},\quad x\in\left[-\frac12,\frac12\right].
\]

Una recta que corta ambos lados queda determinada por sus puntos de corte

\[
(u,D/2)\in E_+,\qquad (v,-D/2)\in E_-,
\]

con \(u,v\in[-1/2,1/2]\). Su longitud de cuerda es

\[
\ell=\sqrt{(u-v)^2+D^2}.
\]

Escribimos la recta como \(y=mx+c\). Entonces

\[
m=\frac{D}{u-v},\qquad
c=-\frac{D(u+v)}{2(u-v)}.
\]

Además, en coordenadas de recta no orientada,

\[
d\theta\,dp=\frac{dc\,dm}{(1+m^2)^{3/2}}.
\]

El jacobiano del cambio \((u,v)\mapsto (m,c)\) es

\[
\left|\frac{\partial(m,c)}{\partial(u,v)}\right|
=\frac{D^2}{|u-v|^3}.
\]

Y como

\[
1+m^2=1+\frac{D^2}{(u-v)^2}
=\frac{\ell^2}{(u-v)^2},
\]

tenemos

\[
(1+m^2)^{3/2}=\frac{\ell^3}{|u-v|^3}.
\]

Por tanto,

\[
\ell^3\,d\theta\,dp
=
\ell^3\cdot
\frac{D^2/|u-v|^3}{\ell^3/|u-v|^3}
\,du\,dv
=
D^2\,du\,dv.
\]

Luego, para este par de lados opuestos,

\[
\int \ell^3\,d\theta\,dp
=
D^2\int_{-1/2}^{1/2}\int_{-1/2}^{1/2}du\,dv
=
D^2\cdot 1\cdot 1
=
3.
\]

---

### 3. Sumar los tres pares opuestos

Hay \(3\) pares de lados opuestos, simétricos y disjuntos salvo conjuntos de medida nula. Así, el peso total favorable es

\[
3\cdot 3=9.
\]

El peso total es

\[
3A^2
=
3\left(\frac{3\sqrt3}{2}\right)^2
=
3\cdot \frac{27}{4}
=
\frac{81}{4}.
\]

Por tanto, la probabilidad pedida es

\[
\frac{9}{81/4}
=
\frac{36}{81}
=
\frac{4}{9}.
\]

\[
\boxed{\frac{4}{9}}
\]