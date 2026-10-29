## Configuración de coordenadas

**Paso 1 — P, Q y el primer par.**
Tomo $P=(-1,0)$, $Q=(1,0)$, de modo que $\overline{PQ}=2$. Los círculos de radio $2$ centrados en $P$ y $Q$ se cortan en $x=0$, $y^2=4-1=3$:
$$R=(0,\sqrt3),\qquad S=(0,-\sqrt3),\qquad \overline{RS}=2\sqrt3 .$$

**Paso 2 — T y U.**
Círculos de radio $2\sqrt3$ centrados en $R$ y $S$: por simetría se cortan en $y=0$, con $x^2+3=12$, es decir $x=\pm 3$:
$$T=(-3,0),\qquad U=(3,0),\qquad \overline{TU}=6 .$$
El orden en el eje $x$ es $-3<-1<1<3$, o sea $T,P,Q,U$, como se pide.

**Paso 3 — V y W.**
Círculos de radio $6$ centrados en $T$ y $U$: se cortan en $x=0$, $y^2=36-9=27$:
$$V=(0,3\sqrt3),\qquad W=(0,-3\sqrt3),$$
y se elige $V$ con $y>0$, el mismo lado que $R$.

## Área del pentágono $PRUVT$

Vértices en orden: $P(-1,0)$, $R(0,\sqrt3)$, $U(3,0)$, $V(0,3\sqrt3)$, $T(-3,0)$. Los cinco lados no se cruzan (las aristas $PR$ y $VT$ son paralelas, ambas de pendiente $\sqrt3$), así que el polígono es simple y vale la fórmula del cordón:

$$\begin{aligned}
P\to R&: (-1)(\sqrt3)-(0)(0)=-\sqrt3\\
R\to U&: (0)(0)-(3)(\sqrt3)=-3\sqrt3\\
U\to V&: (3)(3\sqrt3)-(0)(0)=9\sqrt3\\
V\to T&: (0)(0)-(-3)(3\sqrt3)=9\sqrt3\\
T\to P&: (-3)(0)-(-1)(0)=0
\end{aligned}$$

Suma $=14\sqrt3$, luego el área es $\tfrac12\,|14\sqrt3|=7\sqrt3$.

**Verificación por descomposición:** el triángulo $TUV$ tiene área $\tfrac12\cdot 6\cdot 3\sqrt3=9\sqrt3$, y el cuadrilátero $TPRU$ (la zona que el camino $T\to P\to R\to U$ recorta por abajo) tiene área $2\sqrt3$. Diferencia: $9\sqrt3-2\sqrt3=7\sqrt3$. ✓

\boxed{7\sqrt{3}}