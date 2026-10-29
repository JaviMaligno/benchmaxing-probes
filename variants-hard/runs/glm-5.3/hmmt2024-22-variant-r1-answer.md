**Configuración.** Coloco $Q=(0,0)$, $R=(c,0)$ con $c=QR$, y $P=(a,b)$. La condición $\angle QPR=90^\circ$ equivale a $(Q-P)\cdot(R-P)=0$, es decir

$$b^2=a(c-a).$$

Entonces:
- **Altura:** $X=(a,0)$, es decir $X$ tiene coordenada $a$ en la recta $QR$.
- **Mediana:** $Z=(c/2,0)$, punto medio de $QR$.
- **Bisectriz:** con $QP=\sqrt{ac}$ y $PR=\sqrt{c(c-a)}$, el teorema de la bisectriz da
$$y=QY=\frac{c\cdot QP}{QP+PR}=\frac{c\sqrt a}{\sqrt a+\sqrt{c-a}}.$$

**Orden de los puntos.** Un cálculo directo muestra
$$y-a=\frac{\sqrt a\sqrt{c-a}\,\big(\sqrt{c-a}-\sqrt a\big)}{\sqrt a+\sqrt{c-a}},\qquad \frac c2-y=\frac{c\big(\sqrt{c-a}-\sqrt a\big)}{2(\sqrt a+\sqrt{c-a})},$$
que tienen el mismo signo: **$Y$ siempre queda entre $X$ y $Z$.** Por simetría (intercambiar $Q$ y $R$), puedo suponer $a<c/2$, con orden $X<Y<Z$.

**Traducción de los datos.** De $XY=5$ y $YZ=13$:
$$y=a+5,\qquad \frac c2=y+13 \;\Longrightarrow\; c=2a+36,\quad c-a=a+36.$$

**Ecuación en $a$.** Sustituyendo en la fórmula de la bisectriz:
$$(a+5)\big(\sqrt a+\sqrt{a+36}\big)=(2a+36)\sqrt a.$$
Con $s=\sqrt a$ y $u=\sqrt{a+36}$ (note que $u^2=s^2+36$), tras despejar:
$$u(s^2+5)=s(s^2+31).$$
Elevando al cuadrado y usando $u^2=s^2+36$, con $v=s^2=a$:
$$v(v+31)^2=(v+36)(v+5)^2\;\Longrightarrow\;16v^2+576v-900=0\;\Longrightarrow\;4v^2+144v-225=0,$$
con raíz positiva $v=\frac{-144+\sqrt{24336}}{8}=\frac{-144+156}{8}=\frac32$.

**Verificación.** Con $a=\frac32$: $c=2\cdot\frac32+36=39$, $b^2=a(c-a)=\frac32\cdot\frac{75}{2}=\frac{225}{4}$, así que $b=\frac{15}{2}$. Luego $QP=\frac{3\sqrt{26}}2$, $PR=\frac{15\sqrt{26}}2$, y
$$y=\frac{39\cdot 3}{18}=\frac{13}{2}.$$
Comprobamos: $XY=\frac{13}{2}-\frac32=5$ ✓ y $YZ=\frac{39}{2}-\frac{13}{2}=13$ ✓.

Por lo tanto,

$$\boxed{39}$$