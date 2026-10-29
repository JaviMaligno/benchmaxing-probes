## Solución

Renombro $W=A,\;X=B,\;Y=C,\;Z=D$ para abreviar (así $QA=3$, $QB=5$, $QC=10$).

**Interpretación tangencial.** La condición $\angle QAB=\angle QDA$ es exactamente el ángulo inscrito‑tangente: $AB$ es tangente en $A$ a la circunferencia $\omega_1=(AQD)$. Análogamente $DC$ es tangente a $\omega_1$ en $D$, y $BA$, $CD$ son tangentes a $\omega_2=(BQC)$ en $B$ y $C$.

Luego $AB$ y $CD$ son las dos tangentes comunes a $\omega_1,\omega_2$; se cortan en el centro de homotecia $P$, con $PA=PD=a$, $PB=PC=b$, y la homotecia manda $A\mapsto B$, $D\mapsto C$. Por tanto $AD\parallel BC$ y $AB=CD$: **trapecio isósceles**.

**Relaciones métricas.** Con los ángulos $\alpha=\angle QAB=\angle QDA$, etc., la suma alrededor de $Q$ da $\alpha+\beta+\gamma+\delta=\pi$, y las leyes de senos en los cuatro triángulos dan
$$\sin\alpha:\sin\beta:\sin\gamma:\sin\delta=5:3:6:10,\qquad QD=6 .$$
Además, como $h^{-1}(Q)\in\omega_1$ está en la recta $PQ$, la potencia de $P$ da $PQ^2=ab$, de donde $\sqrt{a/b}=QA/QB=3/5$, es decir $b=\tfrac{25}{9}a$, $PQ=\tfrac53 a$.

**Posición de $Q$.** Con $P$ en el origen, eje de simetría vertical, semiángulo $\theta$ y $Q$ a ángulo $\eta$ del eje, la condición $Q\in\omega_1$ (centro $(0,-a/\cos\theta)$, radio $a\tan\theta$) se reduce a
$$\cos\eta=\cos\theta\cdot\frac{a+b}{2\sqrt{ab}}=\frac{17}{15}\cos\theta .$$
Los cosenos en $\triangle PAQ$ y $\triangle PDQ$ ($QA=3$, $QD=6$) dan $15\cos\theta\cos\eta-25\sin\theta\sin\eta=17$. Sustituyendo y resolviendo con $u=\cos^2\theta$:
$$1-\tfrac{289}{225}u=\tfrac{289}{625}(1-u)\;\Longrightarrow\;u=\tfrac{189}{289}.$$
Así $\sin\theta=\tfrac{10}{17}$, $\cos\eta=\tfrac{\sqrt{21}}5$, $\sin\eta=-\tfrac25$, luego $\cos\angle QPA=\tfrac{83}{85}$ y de $9=a^2\!\left(\tfrac{34}9-\tfrac{10}3\cdot\tfrac{83}{85}\right)=\tfrac{80}{153}a^2$:
$$a^2=\frac{1377}{80},\qquad a=\frac{9\sqrt{85}}{20}.$$

**Perímetro.**
$$AD=2a\sin\theta=\frac{20a}{17},\quad BC=\frac{500a}{153},\quad AB=CD=b-a=\frac{16a}{9},$$
$$P=\frac{180a+500a+544a}{153}=8a=\frac{18\sqrt{85}}{5}\approx 33.19 .$$

Verificación numérica: $AD\approx4.881$, $BC\approx13.558$, $AB=CD\approx7.376$, y existe $Q$ con $(3,5,10,6)$ como distancias.

$$\boxed{\dfrac{18\sqrt{85}}{5}}$$