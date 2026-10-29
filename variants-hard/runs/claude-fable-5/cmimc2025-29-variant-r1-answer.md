## Planteamiento

Coloco coordenadas: $S=(0,0)$, $R=(110,0)$, $P=(0,28)$, $Q=(20,28)$ (ya que $\angle PSR = 90^\circ$ y $PQ \parallel SR$).

## Familia de cónicas por los cuatro puntos

El haz de cónicas por los 4 vértices se genera con dos cónicas degeneradas: el par de rectas $y(y-28)=0$ (rectas $SR$ y $PQ$) y el par $x\cdot(14x+45y-1540)=0$ (rectas $PS$ y $QR$, pues $QR$ pasa por $(20,28)$ y $(110,0)$ con pendiente $-14/45$).

$$y(y-28) + t\,x(14x+45y-1540)=0$$

La parte cuadrática es $14t\,x^2 + 45t\,xy + y^2$, con matriz
$$M=\begin{pmatrix}14t & \tfrac{45t}{2}\\ \tfrac{45t}{2} & 1\end{pmatrix},\qquad T=14t+1,\quad \Delta = 14t-\tfrac{2025}{4}t^2.$$

Es elipse cuando $\Delta>0$, es decir $0<t<\tfrac{56}{2025}$. Si $r=a/b$ es la razón de ejes y $\lambda_1\le\lambda_2$ los autovalores de $M$, entonces $r^2=\lambda_2/\lambda_1$ y
$$\frac{T^2}{\Delta}=\frac{(\lambda_1+\lambda_2)^2}{\lambda_1\lambda_2}=r^2+2+\frac{1}{r^2}\cdot r^0 \;=\; k+2+\frac1k,\quad k=r^2,$$
que es creciente en $k\ge 1$. Basta minimizar $f(t)=\dfrac{(14t+1)^2}{14t-\tfrac{2025}{4}t^2}$.

## Minimización

$f'(t)=0$ da, tras cancelar $(14t+1)$:
$$28t\left(14-\tfrac{2025}{4}t\right)=(14t+1)\left(14-\tfrac{2025}{2}t\right)$$
$$392t - 14175t^2 = 14 - \tfrac{1633}{2}t - 14175t^2 \;\Longrightarrow\; \tfrac{2417}{2}t = 14 \;\Longrightarrow\; t^*=\frac{28}{2417},$$
que cae dentro del intervalo de elipses.

Evaluando:
- $T = 1+\dfrac{392}{2417}=\dfrac{2809}{2417}$ (y $2809=53^2$),
- $\Delta = \dfrac{28}{2417}\left(14-\dfrac{14175}{2417}\right)=\dfrac{28\cdot 19663}{2417^2}=\dfrac{196\cdot 2809}{2417^2}$.

Entonces
$$\frac{T^2}{\Delta}=\frac{2809}{196}\;\Longrightarrow\; \left(r+\frac1r\right)^2=\frac{2809}{196}\;\Longrightarrow\; r+\frac1r=\frac{53}{14}.$$

Resolviendo $14r^2-53r+14=0$: $r=\dfrac{53\pm 45}{28}$, y tomando $r\ge 1$ se obtiene $r=\dfrac{98}{28}=\dfrac{7}{2}$.

$$\boxed{\dfrac{7}{2}}$$