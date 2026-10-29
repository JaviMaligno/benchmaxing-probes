## Planteamiento

Coloco los vértices: $D=(0,0)$, $C=(130,0)$, $A=(0,33)$, $B=(18,33)$.

Cónica general: $ax^2+bxy+cy^2+dx+ey+f=0$.

- $D$: $f=0$
- $A$: $1089c+33e=0 \Rightarrow e=-33c$
- $C$: $16900a+130d=0 \Rightarrow d=-130a$
- $B$: $324a+594b+1089c+18d+33e=0 \Rightarrow -2016a+594b=0 \Rightarrow b=\tfrac{112}{33}a$

Normalizando $a=1$ y llamando $t=c$, la familia es
$$x^2+\tfrac{112}{33}xy+t\,y^2-130x-33t\,y=0 .$$

## Minimizar la razón

Con $p=\tfrac{56}{33}$, la forma cuadrática es $M=\begin{pmatrix}1&p\\p&t\end{pmatrix}$, y la razón de ejes cumple
$$\text{razón}^2=\frac{\lambda_{\max}}{\lambda_{\min}}=\frac{1+u}{1-u},\qquad u=\frac{\sqrt{(t-1)^2+4p^2}}{t+1}.$$

Minimizando $u^2=\dfrac{(t-1)^2+4p^2}{(t+1)^2}$: la derivada se anula en $2t-2-4p^2=0$, es decir $t=1+2p^2=\tfrac{7361}{1089}$ (que cumple $t>p^2$, así que es elipse).

Ahí: $u=\dfrac{p}{\sqrt{1+p^2}}$. Como $1+p^2=\dfrac{4225}{1089}$ y $\sqrt{1+p^2}=\dfrac{65}{33}$, resulta $u=\dfrac{56}{65}$.

$$\text{razón}^2=\frac{1+56/65}{1-56/65}=\frac{121}{9}\quad\Longrightarrow\quad \text{razón}=\frac{11}{3}.$$

\boxed{\dfrac{11}{3}}