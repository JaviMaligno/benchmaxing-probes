## Planteamiento

Nombro los ángulos del siguiente modo: $\alpha=\angle PAD=\angle PDC$, $\delta=\angle PDA=\angle PAB$, $\beta=\angle PBC=\angle PCD$, $\gamma=\angle PCB=\angle PBA$.

**Suma de ángulos.** Los ángulos del cuadrilátero son $\angle A=\angle D=\alpha+\delta$ y $\angle B=\angle C=\beta+\gamma$, de modo que $2(\alpha+\delta)+2(\beta+\gamma)=360^\circ$, es decir
$$\alpha+\beta+\gamma+\delta=180^\circ.$$

**Ley de senos en los cuatro triángulos.** Con $P$ como vértice común:

- $\triangle APB$: $\dfrac{PA}{PB}=\dfrac{\sin\gamma}{\sin\delta}=\dfrac45$
- $\triangle BPC$: $\dfrac{PB}{PC}=\dfrac{\sin\gamma}{\sin\beta}=\dfrac12$
- $\triangle APD$: $\dfrac{PD}{PA}=\dfrac{\sin\alpha}{\sin\delta}$
- $\triangle DPC$: $\dfrac{PD}{PC}=\dfrac{\sin\beta}{\sin\alpha}$

Multiplicando las dos últimas: $PD^2=PA\cdot PC\cdot\dfrac{\sin\beta}{\sin\delta}=4\cdot 10\cdot\dfrac{8}{5}=64$, luego $\boxed{PD=8}$ (valor intermedio). Poniendo $\sin\delta=s$: $\sin\gamma=\tfrac{4s}{5}$, $\sin\beta=\tfrac{8s}{5}$, $\sin\alpha=2s$.

**Clave: $AB=CD$.** La condición $\angle PAB=\angle PDA$ dice (ángulo semiinscrito) que $AB$ es tangente en $A$ al circuncírculo de $\triangle APD$, y $\angle PDC=\angle PAD$ dice que $CD$ es tangente en $D$ a ese mismo círculo. Análogamente, $AB$ y $CD$ son tangentes en $B$ y $C$ al circuncírculo de $\triangle BPC$. Así, $AB$ y $CD$ son las dos tangentes comunes a dos círculos que se cortan en $P$, y por simetría $AB=CD$.

**Cálculo de $AB$.** Como $\angle APB=180^\circ-\gamma-\delta$ y $\angle DPC=180^\circ-\alpha-\beta$, la ley de cosenos da, con $c=\cos(\gamma+\delta)=-\cos(\alpha+\beta)$ (pues $(\alpha+\beta)+(\gamma+\delta)=180^\circ$):
$$AB^2=41+40c,\qquad CD^2=164-160c.$$
Igualando: $200c=123$, o sea $c=\tfrac{123}{200}$, y entonces
$$AB=CD=\sqrt{41+\tfrac{123}{5}}=\sqrt{\tfrac{328}{5}}=\tfrac{2\sqrt{410}}{5}.$$

**Cálculo de $BC$ y $DA$.** De $\cos(\gamma+\delta)=\tfrac{123}{200}$ con los senos de arriba se obtiene (desarrollando $\cos\gamma\cos\delta-\sin\gamma\sin\delta$ y usando $\alpha+\beta+\gamma+\delta=180^\circ$) $t=s^2=\tfrac{24871}{104960}$. Con esto:
$$\cos\beta\cos\gamma=\frac{127\cdot 373}{82000}=\frac{47371}{82000},\qquad \sin\beta\sin\gamma=\frac{32t}{25}=\frac{24871}{82000},$$
$$\cos(\beta+\gamma)=\frac{22500}{82000}=\frac{45}{164}.$$
Como $\angle BPC=180^\circ-(\beta+\gamma)$ y $\angle APD=\beta+\gamma$:
$$BC^2=125+100\cdot\tfrac{45}{164}=\tfrac{6250}{41}\ \Rightarrow\ BC=\tfrac{25\sqrt{410}}{41},$$
$$DA^2=80-64\cdot\tfrac{45}{164}=\tfrac{2560}{41}\ \Rightarrow\ DA=\tfrac{16\sqrt{410}}{41}.$$

**Perímetro.** $BC+DA=\tfrac{41\sqrt{410}}{41}=\sqrt{410}$, de modo que
$$AB+BC+CD+DA=\frac{4\sqrt{410}}{5}+\sqrt{410}=\frac{9\sqrt{410}}{5}.$$

(Verificación numérica: $8.099+12.345+8.099+7.903\approx 36.447=\tfrac{9\sqrt{410}}{5}$.)

$$\boxed{\dfrac{9\sqrt{410}}{5}}$$