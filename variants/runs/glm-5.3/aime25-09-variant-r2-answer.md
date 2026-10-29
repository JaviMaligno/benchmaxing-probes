## Resolución

**Planteamiento.** Un punto $P=(t,\,t^2-5)$ de la parábola original pertenece también a la imagen rotada si y solo si su preimagen bajo la rotación de $60^\circ$ sigue en la parábola original, es decir, $R_{-60^\circ}(P)=(u,\,u^2-5)$ para algún $u$ real.

Con $\cos 60^\circ=\tfrac12$, $\sin 60^\circ=\tfrac{\sqrt3}{2}$, la preimagen de $P$ es:
$$X=\frac{t+\sqrt3\,(t^2-5)}{2}=\frac{t+\sqrt3\,y}{2},\qquad Y=\frac{(t^2-5)-\sqrt3\,t}{2}=\frac{y-\sqrt3\,t}{2},$$
donde escribí $y=t^2-5$. Exigiendo $Y=X^2-5$ y multiplicando por $4$:
$$2(y-\sqrt3\,t)+20=(t+\sqrt3\,y)^2=(y+5)+2\sqrt3\,ty+3y^2,$$
que se simplifica a la ecuación clave
$$y+15-3y^2=2\sqrt3\,t\,(y+1).\qquad(\ast)$$

**Ecuación en $y$.** Elevando $(\ast)$ al cuadrado y usando $t^2=y+5$:
$$(3y^2-y-15)^2=12\,(y+5)(y+1)^2,$$
es decir,
$$9y^4-18y^3-173y^2-102y+165=0=(y^2-3y-15)(9y^2+9y-11).$$
Las cuatro raíces son
$$y=\frac{3\pm\sqrt{69}}{2},\qquad y=\frac{-3\pm\sqrt{53}}{6}.$$

**Cuadrantes.** El signo de $t$ queda fijado por $(\ast)$ (con $t^2=y+5$):

- $y=\frac{3+\sqrt{69}}{2}\approx 5.65$: exige $t=-\sqrt{\tfrac{13+\sqrt{69}}{2}}\approx -3.26$ → **segundo cuadrante**.
- $y=\frac{-3+\sqrt{53}}{6}\approx 0.71$: exige $t=+\sqrt{\tfrac{27+\sqrt{53}}{6}}\approx 2.39$ → **primer cuadrante**.
- $y=\frac{-3-\sqrt{53}}{6}\approx -1.71$: exige $t=-\sqrt{\tfrac{27-\sqrt{53}}{6}}\approx -1.81$ → **tercer cuadrante**.
- $y=\frac{3-\sqrt{69}}{2}\approx -2.65$: como $3y^2-y-15=42-4\sqrt{69}>0$ y $y+1=\tfrac{5-\sqrt{69}}{2}<0$, se necesita $t>0$, con $t=\sqrt{\tfrac{13-\sqrt{69}}{2}}\approx 1.53$ → **cuarto cuadrante**. ✓

Comprobación numérica: la preimagen de $\left(1.53189,\,-2.65331\right)$ es $\left(-1.53189,\,-2.65331\right)$, que cumple $(-1.53189)^2-5=-2.65331$. ✓ Como $f(t)=3t^4-31t^2+65+2\sqrt3\,t(t^2-4)$ es una cuártica y ya encontramos sus cuatro raíces reales, no hay más intersecciones: hay exactamente una en el cuarto cuadrante.

**Conclusión.** El punto pedido tiene ordenada
$$y=\frac{3-\sqrt{69}}{2}=\frac{a-\sqrt b}{c}\quad\text{con }(a,b,c)=(3,69,2),\ \gcd(3,2)=1,$$
donde $69=3\cdot 23$ es libre de cuadrados, así que la representación es única.

$$a+b+c=3+69+2=74$$

\boxed{74}