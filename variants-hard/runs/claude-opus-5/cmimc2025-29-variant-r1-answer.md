## Planteamiento

Coloco coordenadas usando el ángulo recto en $S$:

- $S=(0,0)$, $R=(110,0)$, $P=(0,28)$, y como $PQ\parallel SR$ con $PQ=20$: $Q=(20,28)$.

Cónica general: $ax^2+bxy+cy^2+dx+ey+f=0$.

- $S$: $f=0$.
- $R$: $12100a+110d=0 \Rightarrow d=-110a$.
- $P$: $784c+28e=0 \Rightarrow e=-28c$.
- $Q$: $400a+560b+784c-2200a-784c=0 \Rightarrow b=\tfrac{45}{14}a$.

Con $a\neq 0$ (si $a=0$ la cónica degenera), normalizo $a=1$, $c=t$:
$$x^2+\tfrac{45}{14}xy+t\,y^2-110x-28t\,y=0.$$

## La razón depende solo de la parte cuadrática

La razón de ejes es $\sqrt{\lambda_{\max}/\lambda_{\min}}$, con $\lambda$ los autovalores de
$$M=\begin{pmatrix}1 & 45/28\\ 45/28 & t\end{pmatrix},\qquad \lambda=\frac{(1+t)\pm\sqrt{(t-1)^2+k}}{2},\quad k=\Big(\tfrac{45}{14}\Big)^2=\tfrac{2025}{196}.$$

Con $s=t+1$ y $D=\sqrt{(t-1)^2+k}$, se tiene $\dfrac{\lambda_{\max}}{\lambda_{\min}}=\dfrac{s+D}{s-D}$, que es creciente en $D/s$. Basta minimizar
$$f(t)=\frac{(t-1)^2+k}{(t+1)^2}.$$

$$f'(t)=\frac{2\,(2t-2-k)}{(t+1)^3}=0\ \Longrightarrow\ t=1+\frac{k}{2}=\frac{2417}{392},$$

valor admisible, pues exige $t>k/4=2025/784$ para que sea elipse (forma definida positiva), y $2417/392\approx 6.17>2.58$.

Sustituyendo $t-1=k/2$, $t+1=(k+4)/2$:
$$f=\frac{k(k+4)/4}{(k+4)^2/4}=\frac{k}{k+4}=\frac{2025/196}{2809/196}=\frac{2025}{2809}=\Big(\frac{45}{53}\Big)^2.$$

Luego $D/s=45/53$ y
$$\text{razón}^2=\frac{1+45/53}{1-45/53}=\frac{98}{8}=\frac{49}{4}\ \Longrightarrow\ \text{razón}=\frac72.$$

La cónica es una elipse real no degenerada (forma definida positiva pasando por cuatro puntos distintos en posición convexa).

$$\boxed{\dfrac{7}{2}}$$