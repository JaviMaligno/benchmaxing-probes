## Planteamiento

Sea $O$ el circuncentro del triángulo equilátero. Como el lado es $6$, el radio circunscrito es $R = \frac{6}{\sqrt{3}} = 2\sqrt{3}$. Coloco coordenadas con $O=(0,0)$:

$$\omega:\ x^2+y^2=12,\qquad A=(2\sqrt{3},0),\quad B=(-\sqrt{3},3),\quad C=(-\sqrt{3},-3).$$

## Paso 1: Lugar geométrico de $P$

Como $\angle BAC = 60^\circ$, el ángulo central $\angle BOC = 120^\circ$. Dado que $\angle BPC = 120^\circ = \angle BOC$, con $P$ y $O$ del mismo lado de $BC$, los puntos $B,P,C,O$ son **concíclicos**. La circunferencia que pasa por $B$, $C$ y $O$ es

$$\gamma:\ x^2+y^2+4\sqrt{3}\,x=0.$$

(Efectivamente, $3+9-12=0$ para $B$ y $C$, y $0$ para $O$.) Entonces $P=(p,q)$ satisface $p^2+q^2+4\sqrt{3}p=0$.

## Paso 2: Ubicar $X$

$X\in\omega$ con $AX=5$: si $X=(x,y)$, entonces
$$25=|A-X|^2=(2\sqrt{3}-x)^2+y^2=24-4\sqrt{3}\,x \implies x=-\frac{\sqrt{3}}{12},\quad y=\pm\frac{5\sqrt{69}}{12}.$$

Por simetría respecto al eje $x$, tomo $y=\frac{5\sqrt{69}}{12}$ (el otro signo refleja todo y da el mismo $XP$).

## Paso 3: Condición del círculo de diámetro $AP$

$X$ está en el círculo de diámetro $AP$ si y solo si $\angle AXP=90^\circ$, es decir $(A-X)\cdot(P-X)=0$. Como $A-X=\left(\frac{25\sqrt{3}}{12},-\frac{5\sqrt{69}}{12}\right)$:

$$\frac{25\sqrt{3}}{12}\Big(p+\frac{\sqrt{3}}{12}\Big)-\frac{5\sqrt{69}}{12}\Big(q-\frac{5\sqrt{69}}{12}\Big)=0 \implies 5\sqrt{3}\,p-\sqrt{69}\,q+30=0.$$

## Paso 4: Resolver el sistema

De la recta: $q=\dfrac{5\sqrt{3}\,p+30}{\sqrt{69}}$. Sustituyendo en $\gamma$:

$$144p^2+576\sqrt{3}\,p+900=0 \implies 4p^2+16\sqrt{3}\,p+25=0,$$

con raíces $p=\dfrac{-4\sqrt{3}\pm\sqrt{23}}{2}$. La raíz $p=\dfrac{-\sqrt{23}-4\sqrt{3}}{2}<- \sqrt{3}$ queda fuera del triángulo, así que

$$p=\frac{\sqrt{23}-4\sqrt{3}}{2},\qquad q=\frac{5\sqrt{3}\,p+30}{\sqrt{69}}=\frac{5}{2}.$$

**Verificación:** $P\approx(-1.066,\,2.5)$ está dentro del triángulo, y $\cos\angle BPC = -\frac12$ (se comprueba que $(PB\cdot PC)^2=\frac14|PB|^2|PC|^2$ con signo negativo), es decir $\angle BPC=120^\circ$. ✓

## Paso 5: Calcular $XP$

En el triángulo rectángulo $AXP$ (recto en $X$), con $AX=5$:

$$AP^2=\Big(2\sqrt{3}-\frac{\sqrt{23}-4\sqrt{3}}{2}\Big)^2+\Big(\frac52\Big)^2=\frac{(8\sqrt{3}-\sqrt{23})^2+25}{4}=\frac{215-16\sqrt{69}+25}{4}=60-4\sqrt{69}.$$

$$XP^2=AP^2-AX^2=60-4\sqrt{69}-25=35-4\sqrt{69}=23+12-4\sqrt{69}=(\sqrt{23}-2\sqrt{3})^2.$$

Como $\sqrt{23}>2\sqrt{3}$, se concluye $XP=\sqrt{23}-2\sqrt{3}\approx 1.33$.

$$\boxed{\sqrt{23}-2\sqrt{3}}$$