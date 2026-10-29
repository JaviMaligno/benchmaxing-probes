## Planteamiento

Sea $a=\log_x y$, $b=\log_y z$, $c=\log_z x$. Entonces $abc=1$.

**Primera ecuación:** $a+b+c=10$.

**Segunda ecuación:** $\log_y x = 1/a$, así que
$$\log_{1/a} z=-3 \iff z=\left(\tfrac1a\right)^{-3}=a^3.$$

**Tercera ecuación:** $\log_z y = \dfrac1b = ac$ y $\log_x z=\dfrac1c=ab$ (usando $abc=1$), luego
$$ac+ab=a(b+c)=25.$$

## Resolución

Sustituyendo $b+c=10-a$:
$$a(10-a)=25 \implies a^2-10a+25=0 \implies (a-5)^2=0 \implies a=5.$$

Por tanto $z=a^3=125$.

**Verificación de existencia:** con $a=5$ se tiene $b+c=5$ y $bc=\frac{1}{a}=\frac15$, cuyo discriminante es $25-\frac45>0$, de modo que $b,c$ son reales; además la base $\log_y x=\frac15$ es positiva y distinta de 1, y los valores $x=y^{1/5}$, $y=125^{1/b}$ son admisibles.

\boxed{125}