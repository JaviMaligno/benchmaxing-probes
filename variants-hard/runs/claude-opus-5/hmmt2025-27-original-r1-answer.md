## Planteamiento

Sean $a=BC=7$, $b=CA=8$, $c=AB=6$, y $\theta=\angle ABP=\angle ACP$.

**Cosenos y senos del triángulo:**
$$\cos B=\frac{49+36-64}{84}=\frac14,\qquad \cos C=\frac{49+64-36}{112}=\frac{11}{16}$$
$$\sin B=\frac{\sqrt{15}}4,\qquad \sin C=\frac{3\sqrt{15}}{16},\qquad [ABC]=\frac{21\sqrt{15}}4$$

**Condición sobre $\theta$.** En $\triangle BPC$ los ángulos en $B$ y $C$ son $B-\theta$ y $C-\theta$, así que por el teorema de los senos:
$$\frac{BP}{PC}=\frac{\sin(C-\theta)}{\sin(B-\theta)}=\frac12\ \Longrightarrow\ 2\sin(C-\theta)=\sin(B-\theta)$$

Desarrollando:
$$\cot\theta=\frac{2\cos C-\cos B}{2\sin C-\sin B}=\frac{\frac{22}{16}-\frac4{16}}{\frac{6\sqrt{15}}{16}-\frac{4\sqrt{15}}{16}}=\frac{18}{2\sqrt{15}}=\frac9{\sqrt{15}}$$

Luego $\tan\theta=\frac{\sqrt{15}}9$. Como $\tan\frac C2=\frac{\sin C}{1+\cos C}=\frac{3\sqrt{15}/16}{27/16}=\frac{\sqrt{15}}9$, resulta $\theta=\frac C2$.

**Consecuencias.** Con $\sin\theta=\frac{\sqrt{15}}{\sqrt{96}}$, $\cos\theta=\frac9{\sqrt{96}}$:
$$\sin(C-\theta)=\sin\theta=\frac{\sqrt{15}}{\sqrt{96}},\qquad \angle BPC=180^\circ-(B+C-2\theta)=180^\circ-B$$

Entonces $\sin\angle BPC=\sin B=\frac{\sqrt{15}}4$ y
$$BP=\frac{BC\sin(C-\theta)}{\sin\angle BPC}=\frac{7\cdot\frac{\sqrt{15}}{\sqrt{96}}}{\frac{\sqrt{15}}4}=\frac{28}{\sqrt{96}}$$

**Área.** Con $PC=2BP$:
$$[BPC]=\tfrac12\cdot BP\cdot 2BP\cdot\sin B=BP^2\cdot\frac{\sqrt{15}}4=\frac{784}{96}\cdot\frac{\sqrt{15}}4=\frac{49\sqrt{15}}{24}$$

$$\frac{[BPC]}{[ABC]}=\frac{49\sqrt{15}/24}{21\sqrt{15}/4}=\frac{7}{18}$$

**Verificación:** $[ABP]:[ACP]=\tfrac12\cdot 6\cdot BP\sin\theta:\tfrac12\cdot 8\cdot 2BP\sin\theta=3:8$, y $\tfrac{3}{11}\cdot\tfrac{11}{18}+\tfrac{8}{11}\cdot\tfrac{11}{18}+\tfrac7{18}=1$ ✓

\boxed{\dfrac{7}{18}}