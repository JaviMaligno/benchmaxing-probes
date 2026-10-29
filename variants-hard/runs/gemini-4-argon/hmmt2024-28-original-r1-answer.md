Para hallar el área del triángulo $TAD$, analizamos paso a paso la configuración geométrica alrededor del vértice $T$:

### 1. Posición de las circunferencias circunscritas y ángulos en $T$
Dado que las circunferencias circunscritas $\omega_1 = \odot(TAB)$ y $\omega_2 = \odot(TCD)$ pasan ambas por el punto $T$ y son tangentes interiormente, su único punto común debe ser el punto de tangencia $T$. 

Sea $\ell$ la recta tangente común a $\omega_1$ y $\omega_2$ en $T$. Como ambas circunferencias son tangentes interiormente en $T$, ambas se encuentran en el mismo semiplano determinado por $\ell$. Al ser $ABTCD$ un pentágono convexo, las semirrectas que parten de $T$ hacia los demás vértices aparecen ordenadas como $TB, TA, TD, TC$, formando ángulos $0^\circ < \phi_B < \phi_A < \phi_D < \phi_C < 180^\circ$ con respecto a la semirrecta de $\ell$ del lado de $B$.

Definimos $\alpha = \angle BTA = \phi_A - \phi_B$ y $\beta = \angle DTC = \phi_C - \phi_D$. Como $\angle BTC = 120^\circ$ y $\angle ATD = 90^\circ$, tenemos:
$$\alpha + \beta = \angle BTC - \angle ATD = 120^\circ - 90^\circ = 30^\circ.$$

### 2. Expresión de las longitudes mediante coordenadas polares
Sean $R_1$ y $R_2$ los circunradios de $\triangle TAB$ y $\triangle TCD$, respectivamente. Cualquier punto $P$ sobre una circunferencia de radio $R$ tangente a $\ell$ en $T$ cumple $TP = 2R\sin\phi_P$. 

Por el teorema del seno en $\triangle TAB$ y $\triangle TCD$, haciendo $x = AB = CD$, tenemos:
$$x = 2R_1\sin\alpha = 2R_2\sin\beta \implies 2R_1 = \frac{x}{\sin\alpha}, \quad 2R_2 = \frac{x}{\sin\beta}.$$

Sea $\theta = \phi_A$. Entonces $\phi_B = \theta - \alpha$, $\phi_D = \theta + 90^\circ$ y $\phi_C = \theta + 90^\circ + \beta$. Las distancias desde $T$ a los otros cuatro vértices son:
$$\begin{aligned}
TA &= 2R_1\sin\theta = \frac{x\sin\theta}{\sin\alpha}, \\
TD &= 2R_2\sin(\theta + 90^\circ) = \frac{x\cos\theta}{\sin\beta}, \\
BT &= 2R_1\sin(\theta - \alpha) = x\sin\theta\cot\alpha - x\cos\theta, \\
CT &= 2R_2\sin(\theta + 90^\circ + \beta) = x\cos\theta\cot\beta - x\sin\theta.
\end{aligned}$$

### 3. Relación entre las áreas
Definimos $u = x\sin\theta$ y $v = x\cos\theta$, y denotamos $b = BT = 4$ y $c = CT = 5$. De las expresiones anteriores obtenemos:
$$u\cot\alpha = b + v, \qquad v\cot\beta = c + u.$$

Calculamos ahora las áreas de los tres triángulos que componen el pentágono $ABTCD$:
$$\begin{aligned}
[TAB] &= \frac{1}{2} BT \cdot TA \sin\alpha = \frac{1}{2} b u, \\
[TCD] &= \frac{1}{2} CT \cdot TD \sin\beta = \frac{1}{2} c v, \\
[TAD] &= \frac{1}{2} TA \cdot TD = \frac{uv}{2\sin\alpha\sin\beta}.
\end{aligned}$$

Multiplicando las ecuaciones $u\cot\alpha = b + v$ y $v\cot\beta = c + u$, resulta:
$$uv\cot\alpha\cot\beta = (b + v)(c + u) = bc + bu + cv + uv \implies uv(\cot\alpha\cot\beta - 1) = bc + 2([TAB] + [TCD]).$$

Usando la identidad trigonométrica $\cot\alpha\cot\beta - 1 = \frac{\cos(\alpha + \beta)}{\sin\alpha\sin\beta}$, el miembro izquierdo se transforma en:
$$uv(\cot\alpha\cot\beta - 1) = \frac{uv}{\sin\alpha\sin\beta}\cos(\alpha + \beta) = 2[TAD]\cos 30^\circ = \sqrt{3}[TAD].$$

### 4. Cálculo de $[TAD]$
Sabemos que $[TAB] + [TCD] + [TAD] = 22$, por lo que $[TAB] + [TCD] = 22 - [TAD]$. Sustituyendo $b = 4$, $c = 5$ y esta relación en la ecuación obtenida:
$$4 \cdot 5 + 2(22 - [TAD]) = \sqrt{3}[TAD] \implies 64 - 2[TAD] = \sqrt{3}[TAD].$$

Despejando $[TAD]$:
$$[TAD] = \frac{64}{2 + \sqrt{3}} = 64(2 - \sqrt{3}) = 128 - 64\sqrt{3}.$$

\boxed{128 - 64\sqrt{3}}