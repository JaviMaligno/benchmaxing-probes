## Planteamiento

**1. Coordenadas.** Como $\angle PSR = 90^\circ$ y $PQ \parallel SR$, es un trapecio rectángulo. Pongo:
$$S=(0,0),\qquad R=(110,0),\qquad P=(0,28),\qquad Q=(20,28).$$

**2. Haz de cónicas por los cuatro puntos.** Sea $ax^2+bxy+cy^2+dx+ey+f=0$:

- Por $S(0,0)$: $f=0$.
- Por $P(0,28)$: $784c+28e=0\Rightarrow e=-28c$.
- Por $R(110,0)$: $12100a+110d=0\Rightarrow d=-110a$.
- Por $Q(20,28)$: $400a+560b+784c+20d+28e=0$. Sustituyendo $d$ y $e$: $-1800a+560b=0\Rightarrow b=\tfrac{45}{14}a$.

Dividiendo entre $a$ y escribiendo $t=c/a$, toda cónica por los cuatro puntos es:
$$x^2+\tfrac{45}{14}xy+ty^2-110x-28ty=0,\qquad t\in\mathbb{R}.$$

**3. Condición de elipse.** Se necesita $b^2-4ac<0$, es decir $\left(\tfrac{45}{14}\right)^2-4t<0$, o sea
$$t>t_0:=\frac{2025}{784}=\left(\frac{45}{28}\right)^2 .$$
(Además, completando el cuadrado se obtiene un centro $x_0=-\tfrac12M^{-1}L$ con $x_0^TMx_0=\tfrac14L^TML>0$, así que cada $t>t_0$ da una elipse real no degenerada.)

**4. La razón de ejes.** La parte cuadrática tiene matriz $M=\begin{pmatrix}1&45/28\\45/28&t\end{pmatrix}$, con traza $T=1+t$ y determinante $D=t-t_0$. Los semiejes son $\sqrt{k/\lambda_i}$ (autovalores de $M$), así que la razón $\rho\ge 1$ (mayor/menor) es $\sqrt{\lambda_{\max}/\lambda_{\min}}$, y:
$$\left(\rho+\frac1\rho\right)^2=\frac{(\lambda_{\max}+\lambda_{\min})^2}{\lambda_{\max}\lambda_{\min}}=\frac{T^2}{D}.$$
Como $\rho\mapsto \rho+1/\rho$ es creciente para $\rho\ge1$, basta minimizar
$$h(t)=\frac{1+t}{\sqrt{t-t_0}},\qquad t>t_0.$$

**5. Minimización.** 
$$h'(t)\propto (t-t_0)-\tfrac12(1+t)=0\;\Longrightarrow\; t^\ast=1+2t_0=\frac{2417}{392}.$$
(En los extremos $t\to t_0^+$ y $t\to\infty$, $h\to\infty$, así que es un mínimo global.)

En $t^\ast$:
$$t^\ast - t_0 = 1+t_0=\frac{2809}{784}=\left(\frac{53}{28}\right)^2,\qquad 1+t^\ast=2(1+t_0),$$
$$h(t^\ast)=\frac{2(1+t_0)}{\sqrt{1+t_0}}=2\sqrt{1+t_0}=2\cdot\frac{53}{28}=\frac{53}{14}.$$

**6. Cálculo de $\rho$.** Con $\rho+\dfrac1\rho=\dfrac{53}{14}$:
$$\rho^2-\frac{53}{14}\rho+1=0\;\Longrightarrow\;\rho=\frac{53\pm 45}{28},$$
y tomando la raíz $\rho\ge1$:
$$\rho=\frac{98}{28}=\frac72 .$$

**Verificación:** con $t^\ast=\frac{2417}{392}$, la elipse $x^2+\frac{45}{14}xy+\frac{2417}{392}y^2-110x-\frac{2417}{14}y=0$ pasa por los cuatro vértices, sus autovalores son $\lambda_{\max}=\frac{2597}{212}$, $\lambda_{\min}=\frac{53}{212}$, y $\sqrt{\lambda_{\max}/\lambda_{\min}}=\sqrt{49/4}=\frac72$. ✓

\boxed{\dfrac{7}{2}}