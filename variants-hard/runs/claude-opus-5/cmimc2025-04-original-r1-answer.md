## Planteamiento

Sea $a=\log_x y$, $b=\log_y z$, $c=\log_z x$. Por la cadena de logaritmos, $abc=1$.

**Ecuación 1:** $a+b+c=8$

**Ecuación 3:** $\log_z y=\dfrac1b$ y $\log_x z=\dfrac1c$. Como $abc=1$, se tiene $\dfrac1b=ac$ y $\dfrac1c=ab$, luego
$$ac+ab=a(b+c)=16$$

**Ecuación 2:** $\log_y x=\dfrac1a$, y $\log_{1/a} z=-3$ significa
$$z=\left(\tfrac1a\right)^{-3}=a^3$$

## Resolución

De la primera ecuación, $b+c=8-a$. Sustituyendo en la tercera:
$$a(8-a)=16\;\Longrightarrow\;a^2-8a+16=0\;\Longrightarrow\;(a-4)^2=0\;\Longrightarrow\;a=4$$

(Consistente: con $a=4$, $b+c=4$ y $bc=\tfrac1a=\tfrac14$, cuyas raíces $2\pm\tfrac{\sqrt{15}}{2}$ son reales.)

Por tanto $z=a^3=4^3$.

\boxed{64}