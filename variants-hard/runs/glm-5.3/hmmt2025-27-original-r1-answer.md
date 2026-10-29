## Planteamiento

Sea $\theta = \angle ABP = \angle ACP$, y escribamos $t = BP$, de modo que $PC = 2t$.

**Paso 1: ángulos de $\triangle ABC$.** Con $AB=6$, $AC=8$, $BC=7$, la ley de cosenos da:
$$\cos B = \frac{36+49-64}{84}=\frac14,\qquad \sin B=\frac{\sqrt{15}}{4},\qquad \cos C=\frac{77}{112}=\frac{11}{16},\qquad \sin C=\frac{3\sqrt{15}}{16},$$
$$\sin A = \sin(B+C)=\frac{7\sqrt{15}}{32},\qquad \cos A = \frac{17}{32}.$$

**Paso 2: ángulos en $\triangle BPC$.** Como $P$ es interior, los rayos $BP$ y $CP$ dividen los ángulos en $B$ y en $C$:
$$\angle PBC = B-\theta,\qquad \angle BCP = C-\theta,\qquad \angle BPC = A+2\theta.$$

**Paso 3: ley de senos en $\triangle BPC$.** De $\dfrac{t}{\sin(C-\theta)}=\dfrac{2t}{\sin(B-\theta)}$ se obtiene $\sin(B-\theta)=2\sin(C-\theta)$. Expandiendo:
$$\frac{\sqrt{15}}4\cos\theta-\frac14\sin\theta=\frac{3\sqrt{15}}8\cos\theta-\frac{11}8\sin\theta \;\Longrightarrow\; 9\sin\theta=\sqrt{15}\cos\theta \;\Longrightarrow\; \tan\theta=\frac{\sqrt{15}}9.$$

(Esta raíz es única en $(0,\min(B,C))$, pues la función es creciente ahí.) Entonces
$$\sin\theta=\frac{\sqrt{10}}8,\qquad \cos\theta=\frac{3\sqrt6}8,$$
y por lo tanto
$$\sin(B-\theta)=\sin B\cos\theta-\cos B\sin\theta=\frac{3\sqrt{90}-\sqrt{10}}{32}=\frac{\sqrt{10}}4,\qquad \sin(C-\theta)=\frac{\sqrt{10}}8 \;(\checkmark).$$

**Paso 4: hallar $t$.** Usando el lado $BC=7$ en la ley de senos de $\triangle BPC$:
$$\sin 2\theta=\frac{3\sqrt{15}}{16},\quad \cos 2\theta=\frac{11}{16},\qquad \sin(A+2\theta)=\frac{7\sqrt{15}}{32}\cdot\frac{11}{16}+\frac{17}{32}\cdot\frac{3\sqrt{15}}{16}=\frac{\sqrt{15}}4,$$
$$t=\frac{7\sin(C-\theta)}{\sin(A+2\theta)}=\frac{7\cdot\sqrt{10}/8}{\sqrt{15}/4}=\frac{7}{\sqrt6}.$$

**Paso 5: áreas y razón.**
$$[BPC]=\tfrac12\cdot BP\cdot PC\cdot\sin(A+2\theta)=t^2\cdot\frac{\sqrt{15}}4=\frac{49}{6}\cdot\frac{\sqrt{15}}4=\frac{49\sqrt{15}}{24},$$
$$[ABC]=\tfrac12\cdot AB\cdot AC\cdot\sin A=24\cdot\frac{7\sqrt{15}}{32}=\frac{21\sqrt{15}}4.$$
$$\frac{[BPC]}{[ABC]}=\frac{49\sqrt{15}}{24}\cdot\frac{4}{21\sqrt{15}}=\frac{196}{504}=\frac{7}{18}.$$

**Verificación (numérica):** con $B=(0,0)$, $C=(7,0)$, $A=(1.5,\,5.809)$, resulta $P\approx(1.75,\,2.259)$, dentro del triángulo; ambos ángulos dan $\approx 23.3^\circ$; $|BP|\approx2.858$, $|PC|\approx5.715$; y la razón de alturas es $2.259/5.809\approx0.3889=\tfrac{7}{18}$ ✓.

$$\boxed{\dfrac{7}{18}}$$