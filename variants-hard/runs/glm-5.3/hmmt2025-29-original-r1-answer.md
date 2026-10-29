# Solución

## Planteamiento con coordenadas

Sitúo el rectángulo como $A=(0,24)$, $B=(w,24)$, $C=(w,0)$, $D=(0,0)$, donde $w=AB$ es la incógnita (y $BC=24$). Escribo $X=(p,\,24-t)$ con $p,q>0$, $q=w-p$, $0<t<24$ (aquí $t$ es la distancia vertical de $X$ al lado $AB$).

**Condición $\angle AXB=90^\circ$:** los vectores $A-X=(-p,t)$ y $B-X=(q,t)$ deben ser perpendiculares:
$$-pq+t^2=0 \quad\Longrightarrow\quad t^2=pq. \tag{0}$$

## Radios circunscritos y ángulos en $X$

En $\triangle AXD$, el lado opuesto al ángulo en $X$ es $AD=24$, así que $\sin\angle AXD=\frac{24}{2\cdot13}=\frac{12}{13}$, y como el triángulo es **acutángulo** (por hipótesis), el ángulo en $X$ es agudo: $\cos\angle AXD=\frac{5}{13}$. Análogamente en $\triangle BXC$: $\sin\angle BXC=\frac{24}{30}=\frac45$, luego $\cos\angle BXC=\frac35$.

**Circunradio de $\triangle AXD$** con área $\frac{24p}{2}=12p$:
$$13=\frac{|AX|\cdot|DX|\cdot 24}{4\cdot 12p} \;\Longrightarrow\; |AX||DX|=26p. \tag{1}$$
De (0): $|AX|^2=p^2+t^2=p^2+pq=pw$, y $|DX|^2=p^2+(24-t)^2=p^2+576-48t+pq=576-48t+pw$.

Ley de cosenos con el lado $AD=24$ opuesto al ángulo en $X$:
$$576=pw+|DX|^2-2\cdot 26p\cdot\tfrac{5}{13}=pw+\underbrace{576-48t+pw}_{|DX|^2}-20p \;\Longrightarrow\; pw-24t=10p. \tag{2}$$

**Circunradio de $\triangle BXC$** con área $12q$: $15=\frac{|BX||CX|24}{48q}\Rightarrow|BX||CX|=30q$, y $\cos\angle BXC=\frac35$ da análogamente:
$$qw-24t=18q. \tag{3}$$

## Resolviendo el sistema

De (2) y (3): $24t=p(w-10)=q(w-18)$. Sustituyendo en (0):
$$\frac{p(w-10)^2}{576}=pq,\qquad \frac{q(w-18)^2}{576}=pq \;\Longrightarrow\; p(w-10)^2=576q,\quad q(w-18)^2=576p.$$

Multiplicando ambas (con $pq\neq0$): $(w-10)(w-18)=\pm576$. Como $t=\frac{p(w-10)}{24}>0$ obliga a $w>18$, se toma el signo positivo:
$$w^2-28w+180=576 \;\Longrightarrow\; w^2-28w-396=0 \;\Longrightarrow\; w=\frac{28\pm\sqrt{2368}}{2}=14\pm 4\sqrt{37}.$$

Solo $w=14+4\sqrt{37}\approx 38.33$ cumple $w>18$.

## Verificación

Con este $w$ queda $t=\frac{12w}{w-14}=12+\frac{42}{\sqrt{37}}\approx 18.90<24$ ✓, y $p=5+\frac{67}{\sqrt{37}}\approx16.01$, $q=9+\frac{81}{\sqrt{37}}\approx22.32$ (se comprueba $t^2=pq$ y $p+q=w$ exactamente). Numéricamente:
- $|AX|\approx24.78$, $|DX|\approx16.80$ ⟹ $R_1=\frac{|AX||DX|}{2p}\approx 13.00$ ✓
- $|BX|\approx29.25$, $|CX|\approx22.89$ ⟹ $R_2=\frac{|BX||CX|}{2q}\approx 15.00$ ✓

Acutangularidad: los ángulos en $A,B,C,D$ tienen cosenos $\frac{t}{|AX|},\frac{t}{|BX|},\frac{24-t}{|CX|},\frac{24-t}{|DX|}>0$ (agudos), y los ángulos en $X$ son agudos por construcción. La condición $t<24$ se cumple, así que la configuración existe y es única.

$$\boxed{14+4\sqrt{37}}$$