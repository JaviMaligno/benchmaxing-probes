Sea \(H(x,y)\) la probabilidad de que la etiqueta \(x\) llegue a la raíz antes que \(7\), cuando \(x\) está en el vértice \(x\) y \(7\) en el vértice \(y\). Solo necesitamos seguir estas dos etiquetas. Además,
\[
H(\text{raíz},y)=1,\qquad H(x,\text{raíz})=0,\qquad H(y,x)=1-H(x,y).
\]

Denotemos los vértices por \(r,l,m,\alpha,\beta,\gamma,\delta\), correspondientes a las posiciones iniciales de \(4,2,6,1,3,5,7\). Definimos
\[
\begin{aligned}
&A=H(l,\delta),\quad B=H(m,\delta),\quad
C=H(\alpha,\delta)=H(\beta,\delta),\quad E=H(\gamma,\delta),\\
&U=H(l,m),\quad W=H(\gamma,m),\quad S=H(\alpha,m),\\
&T=H(l,\gamma),\quad Q=H(\alpha,\gamma).
\end{aligned}
\]
Al promediar sobre las seis aristas, cancelando las que no mueven ninguna de las dos etiquetas, obtenemos
\[
\begin{gathered}
4A=1+2C+U,\qquad 4B=2+E,\qquad 2E=B+W,\qquad 2C=A+S,\\
6U=1+2S+T+A,\qquad 4W=1+E,\\
4S=U+Q+C,\qquad 4T=1+2Q+U,\qquad 2Q=T+S.
\end{gathered}
\]

Las ecuaciones en \(B,E,W\) dan
\[
E=\frac12,\qquad B=\frac58,\qquad W=\frac38.
\]
Resolviendo las restantes,
\[
A=\frac58,\qquad C=\frac12
\]
(junto con \(U=Q=\frac12\), \(S=\frac38\) y \(T=\frac58\)).

Por tanto,
\[
p(2)=p(6)=\frac58,\qquad p(1)=p(3)=p(5)=\frac12,
\]
y la suma pedida es
\[
\frac12+\frac58+\frac12+\frac12+\frac58=\boxed{\frac{11}{4}}.
\]