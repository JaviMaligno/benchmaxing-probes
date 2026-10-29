

Tomemos coordenadas con

\[
P=(-10,0),\qquad Q=(10,0),\qquad O=(0,0),
\]

de modo que \(\Gamma\) es

\[
x^2+y^2=100.
\]

Como \(R\) y \(S\) están del mismo lado de \(PQ\), los tomamos con \(y>0\).

---

### 1. Coordenadas de \(R\) y \(S\)

Para \(R\), usando \(QR=12\):

\[
(x-10)^2+y^2=144,\qquad x^2+y^2=100.
\]

Restando,

\[
200-20x=144 \implies x=\frac{14}{5}.
\]

Luego

\[
y^2=100-\frac{196}{25}=\frac{2304}{25}\implies y=\frac{48}{5}.
\]

Así,

\[
R=\left(\frac{14}{5},\frac{48}{5}\right).
\]

Para \(S\), usando \(PS=8\):

\[
(x+10)^2+y^2=64,\qquad x^2+y^2=100.
\]

Restando,

\[
200+20x=64 \implies x=-\frac{34}{5}.
\]

Luego

\[
y^2=100-\frac{1156}{25}=\frac{1344}{25}\implies y=\frac{8\sqrt{21}}{5}.
\]

Así,

\[
S=\left(-\frac{34}{5},\frac{8\sqrt{21}}{5}\right).
\]

---

### 2. Punto de intersección \(T\)

La recta \(QR\) tiene pendiente

\[
\frac{48/5}{14/5-10}=-\frac{4}{3},
\]

por lo que su ecuación es

\[
4x+3y=40.
\]

La recta \(PS\) tiene pendiente

\[
\frac{8\sqrt{21}/5}{-34/5+10}=\frac{\sqrt{21}}{2},
\]

por lo que su ecuación es

\[
y=\frac{\sqrt{21}}{2}(x+10).
\]

Resolviendo el sistema, si \(u=\sqrt{21}\), se obtiene

\[
T=\left(\frac{96u-506}{25},\frac{1008-128u}{25}\right).
\]

---

### 3. Lados del triángulo \(TRS\)

Calculamos las distancias.

\[
TR=\frac{32}{5}(6-u),
\]

\[
TS=\frac{24}{5}(2u-7),
\]

y

\[
RS=\frac{8}{5}\sqrt{36+(6-u)^2}
=\frac{8}{5}\sqrt{93-12u}.
\]

Pero

\[
(2u-3)^2=4u^2+9-12u=84+9-12u=93-12u,
\]

así que

\[
RS=\frac{8}{5}(2u-3).
\]

Sea

\[
a=RS,\qquad b=TS,\qquad c=TR,
\]

donde \(a\) es el lado opuesto a \(T\). Entonces

\[
a=\frac{16u-24}{5},\qquad
b=\frac{48u-168}{5},\qquad
c=\frac{192-32u}{5}.
\]

---

### 4. Excentro relativo a \(T\)

El centro del excírculo opuesto a \(T\) tiene coordenadas baricéntricas

\[
J=\frac{-aT+bR+cS}{-a+b+c}.
\]

El denominador es

\[
-a+b+c=\frac{48}{5}.
\]

Sustituyendo las coordenadas de \(T,R,S\) y simplificando,

\[
J_x
=
\frac{-(16u-24)(96u-506)+70(48u-168)-170(192-32u)}{1200}
=16u-74,
\]

y

\[
J_y
=
\frac{-(16u-24)(1008-128u)+240(48u-168)+40u(192-32u)}{1200}
=0.
\]

Por tanto,

\[
J=(16\sqrt{21}-74,0).
\]

Como \(16\sqrt{21}<74\), la distancia desde \(O=(0,0)\) hasta \(J\) es

\[
OJ=74-16\sqrt{21}.
\]

\[
\boxed{74-16\sqrt{21}}
\]