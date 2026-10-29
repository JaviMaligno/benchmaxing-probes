

Tomemos $PQ=1$; la razón pedida es invariante por escala. Sea $G$ el centroide de $\triangle PQR$, y sean $v_P,v_Q,v_R$ los vectores de los vértices desde $G$. Entonces

\[
|v_P|=|v_Q|=|v_R|=\frac1{\sqrt3},\qquad v_i\cdot v_j=-\frac16\quad(i\neq j).
\]

### 1. Puntos de intersección de las elipses

Si $X\in \mathcal E_{PQ}\cap \mathcal E_{PR}$, entonces

\[
XP+XQ=XP+XR=\frac32,
\]

por lo que $XQ=XR$. Así, $X$ está en la mediana desde $P$, es decir, $X=\lambda v_P$.

Además,

\[
XP=\frac{|\lambda-1|}{\sqrt3},\qquad
XQ=\frac{\sqrt{\lambda^2+\lambda+1}}{\sqrt3}.
\]

La condición $XP+XQ=\frac32$ equivale a

\[
|\lambda-1|+\sqrt{\lambda^2+\lambda+1}=\frac{3\sqrt3}{2}.
\]

Resolviendo los dos casos del valor absoluto:

\[
\lambda=\tau_+:=\frac{3+5\sqrt3}{8}>1,
\qquad
\lambda=\tau_-:=\frac{3-5\sqrt3}{8}<0.
\]

Por simetría, cada par de elipses da dos puntos sobre la mediana correspondiente. Para cada vértice $v_i$, hay un punto

\[
A_i=\tau_+ v_i
\]

más allá del vértice, y un punto

\[
B_i=\tau_- v_i
\]

más allá del lado opuesto. En total hay seis puntos.

### 2. Qué aristas pueden formar $\triangle XYZ$

Las coordenadas baricéntricas de $\lambda v_i$ respecto a $\triangle PQR$ son

\[
\left(\frac{1+2\lambda}{3},\frac{1-\lambda}{3},\frac{1-\lambda}{3}\right).
\]

Para $A_i$, la coordenada propia es positiva y las otras dos negativas. Para $B_i$, la coordenada propia es negativa y las otras dos positivas.

Un segmento corta a $\triangle PQR$ si alguna combinación convexa de sus extremos tiene las tres coordenadas baricéntricas no negativas.

- $A_iA_j$ con $i\neq j$: la tercera coordenada es negativa en ambos extremos, luego no corta.
- $A_iB_j$ con $i\neq j$: la coordenada $j$ es negativa en ambos extremos, luego no corta.
- $A_iB_i$: como $\tau_-<1<\tau_+$, el segmento contiene al vértice $v_i$, así que corta.
- $B_iB_j$: el punto medio tiene las tres coordenadas positivas, luego atraviesa $\triangle PQR$.

Por tanto, los triángulos válidos son el triángulo exterior $A_PA_QA_R$ y los tres triángulos de la forma $A_iA_jB_k$, con $\{i,j,k\}=\{P,Q,R\}$.

### 3. Lado mayor

El triángulo $A_PA_QA_R$ es homotético a $\triangle PQR$ con factor $\tau_+$, así que sus lados miden

\[
\tau_+\cdot 1=\tau_+.
\]

En un triángulo $A_iA_jB_k$, el lado $A_iA_j$ también mide $\tau_+$. Los otros lados miden

\[
|A_i-B_k|^2
=
|\tau_+ v_i-\tau_- v_k|^2
=
\frac{\tau_+^2+\tau_-^2+\tau_+\tau_-}{3}.
\]

Usando

\[
\tau_++\tau_-=\frac34,\qquad
\tau_+\tau_-=-\frac{33}{32},
\]

se obtiene

\[
|A_i-B_k|^2
=
\frac{(\tau_++\tau_-)^2-\tau_+\tau_-}{3}
=
\frac{\frac{9}{16}+\frac{33}{32}}{3}
=
\frac{17}{32}<1<\tau_+^2.
\]

Así, en cualquier triángulo válido, el lado mayor es $\tau_+$.

Como el lado mayor de $\triangle PQR$ es $1$, la razón pedida es

\[
\boxed{\frac{3+5\sqrt3}{8}}
\]