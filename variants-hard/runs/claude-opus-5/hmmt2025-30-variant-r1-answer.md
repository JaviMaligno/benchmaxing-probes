Voy a resolver el problema y verificarlo numéricamente.

**Planteamiento.** Si el plano corta la caja $[0,a]\times[0,b]\times[0,c]$ en un hexágono, escribimos el plano como $\frac{x}{X}+\frac{y}{Y}+\frac{z}{Z}=1$ con $X>a$, $Y>b$, $Z>c$. El hexágono es el triángulo $T$ de vértices $V_1=(X,0,0)$, $V_2=(0,Y,0)$, $V_3=(0,0,Z)$ **truncado** en cada vértice por los planos $x=a$, $y=b$, $z=c$. Cada recta de corte es paralela al lado opuesto (intersecciones con planos paralelos), así que los tres triángulos cortados son semejantes a $T$ con razones

$$\lambda_1=\tfrac{X-a}{X},\qquad \lambda_2=\tfrac{Y-b}{Y},\qquad \lambda_3=\tfrac{Z-c}{Z}.$$

Con $s_1=|V_2V_3|$, $s_2=|V_3V_1|$, $s_3=|V_1V_2|$, los lados del hexágono en orden son

$$s_3(1-\lambda_1-\lambda_2),\;\; \lambda_2 s_2,\;\; s_1(1-\lambda_2-\lambda_3),\;\; \lambda_3 s_3,\;\; s_2(1-\lambda_3-\lambda_1),\;\; \lambda_1 s_1.$$

**Resolución.** Igualando a $44,60,54,52,50,66$ y poniendo $m=1-(\lambda_1+\lambda_2+\lambda_3)=-k$:

$$s_3m=44-52=-8,\qquad s_2m=50-60=-10,\qquad s_1m=54-66=-12$$

luego $s_1=\frac{12}{k},\,s_2=\frac{10}{k},\,s_3=\frac{8}{k}$ (triángulo $6{:}5{:}4$, acutángulo ✓). Entonces $\lambda_1=5{,}5k$, $\lambda_2=6k$, $\lambda_3=6{,}5k$, y de $1-18k=-k$ sale $k=\frac1{17}$:

$$s_1=204,\; s_2=170,\; s_3=136,\qquad \lambda_1=\tfrac{11}{34},\;\lambda_2=\tfrac{6}{17},\;\lambda_3=\tfrac{13}{34}.$$

De $Y^2+Z^2=204^2$, $X^2+Z^2=170^2$, $X^2+Y^2=136^2$: $X^2=10\cdot289$, $Y^2=54\cdot 289$, $Z^2=90\cdot289$.

**Distancia.** Con $d_0=\left(\sum X^{-2}\right)^{-1/2}$ y centro $(a/2,b/2,c/2)$:

$$D=d_0\left|\tfrac{a}{2X}+\tfrac{b}{2Y}+\tfrac{c}{2Z}-1\right| = d_0\cdot\tfrac12|1-\textstyle\sum\lambda_i| = \frac{d_0}{34},$$

y como $\sum X^{-2}=\frac{1}{289}\left(\frac1{10}+\frac1{54}+\frac1{90}\right)=\frac{7}{289\cdot 54}$, resulta $d_0=17\sqrt{54/7}$ y

$$D=\tfrac12\sqrt{\tfrac{54}{7}}=\sqrt{\tfrac{27}{14}}=\frac{3\sqrt{42}}{14}\approx 1{,}3887.$$

Comprobación de consistencia: los lados reconstruidos son $136\cdot\frac{11}{34}=44$, $170\cdot\frac6{17}=60$, $204\cdot\frac9{34}=54$, $136\cdot\frac{13}{34}=52$, $170\cdot\frac{10}{34}=50$, $204\cdot\frac{11}{34}=66$ ✓ (caja $\approx 36{,}4\times80{,}8\times99{,}6$). Además, el desplazamiento cíclico alternativo de la asignación de lados da el mismo valor $27/14$.

\boxed{\dfrac{3\sqrt{42}}{14}}