Sea  
\[
S=\zeta^a+\zeta^b+\zeta^c+\zeta^d,\qquad \zeta=e^{2\pi i/13}.
\]

### 1. Una condición combinatoria fuerte

Escribe los exponentes como residuos \(r_1,r_2,r_3,r_4\in \mathbb Z/13\mathbb Z\). Para cada \(t\pmod{13}\), define
\[
N_t=\#\{(i,j):r_i-r_j\equiv t\pmod{13}\}.
\]
Entonces
\[
S\overline S=\sum_{i,j}\zeta^{r_i-r_j}
=\sum_{t=0}^{12}N_t\zeta^t.
\]
Como \(|S|^2=3\), tenemos
\[
\sum_{t=0}^{12}N_t\zeta^t=3.
\]

Aplicando cada automorfismo \(\zeta\mapsto \zeta^k\), con \(k=1,\dots,12\), obtenemos
\[
\sum_{t=0}^{12}N_t\zeta^{kt}=3.
\]
Además \(\sum_t N_t=16\). Por inversión discreta de Fourier,
\[
N_0=4,\qquad N_t=1\quad(t\neq 0).
\]

Así los cuatro residuos son distintos, y cada diferencia no nula módulo \(13\) ocurre exactamente una vez.

### 2. Una solución con valor \(7521\)

Toma
\[
(a,b,c,d)=(7,5,2,1).
\]
Los residuos son \(\{1,2,5,7\}\). Sus seis diferencias absolutas son
\[
1,4,6,3,5,2,
\]
es decir, exactamente \(1,2,3,4,5,6\). Por lo tanto las diferencias ordenadas cubren todos los residuos no nulos módulo \(13\). Entonces
\[
|S|^2=4+\sum_{t=1}^{12}\zeta^t=4-1=3,
\]
así que \(|S|=\sqrt3\). El valor correspondiente es
\[
1000(7)+100(5)+10(2)+1=7521.
\]

### 3. Minimalidad

Si \(a\ge 8\), entonces \(b\ge3\), \(c\ge2\), \(d\ge1\), y
\[
1000a+100b+10c+d\ge 8000+300+20+1=8321>7521.
\]
Así que solo hay que revisar \(a\le7\).

En ese caso los cuatro exponentes están en \(\{1,\dots,7\}\). Sus seis diferencias absolutas deben ser exactamente \(1,2,3,4,5,6\). La diferencia \(6\) obliga a que el conjunto contenga \(1\) y \(7\). Los únicos subconjuntos posibles son
\[
\{1,2,5,7\},\qquad \{1,3,6,7\}.
\]
Ordenados de mayor a menor, dan
\[
(7,5,2,1)\quad\text{y}\quad(7,6,3,1).
\]
Sus valores son
\[
7521,\qquad 7631.
\]
Luego el mínimo es \(7521\).

\[
\boxed{7521}
\]