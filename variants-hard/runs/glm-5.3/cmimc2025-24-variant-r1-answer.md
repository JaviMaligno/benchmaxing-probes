## Planteamiento

Coloco el hexágono regular (lado $1$) con centro en el origen y vértices consecutivos en ángulos de $60^\circ$:

$$P=(1,0),\ Q=\left(\tfrac12,\tfrac{\sqrt3}{2}\right),\ R=\left(-\tfrac12,\tfrac{\sqrt3}{2}\right),\ S=(-1,0),\ T=\left(-\tfrac12,-\tfrac{\sqrt3}{2}\right),\ U=\left(\tfrac12,-\tfrac{\sqrt3}{2}\right).$$

**Punto $X$:** está en $\overline{RS}$ con $RX=\tfrac13$, así que

$$X = R + \tfrac13(S-R) = \left(-\tfrac12,\tfrac{\sqrt3}{2}\right) + \tfrac13\left(-\tfrac12,-\tfrac{\sqrt3}{2}\right) = \left(-\tfrac23,\tfrac{\sqrt3}{3}\right).$$

**Punto $Y$:** un punto de $\overline{ST}$ tiene la forma $Y=(-1+\tfrac t2,\,-\tfrac{t\sqrt3}{2})$ con $t=SY$. En el cuadrilátero $PXYU$, el lado $UP$ es lado del hexágono, y $XY\parallel UP$ solo ocurre en el caso degenerado $t=0$; luego la condición de trapecio es $PX\parallel YU$. Impongo el producto cruzado nulo entre $\vec{PX}=(-\tfrac53,\tfrac{\sqrt3}{3})$ y $\vec{YU}=(\tfrac{3-t}{2},-\tfrac{\sqrt3(1-t)}{2})$:

$$\tfrac{5(1-t)}{6} = \tfrac{3-t}{6}\ \Longrightarrow\ 5-5t = 3-t \ \Longrightarrow\ t=\tfrac12,$$

de donde $Y=(-\tfrac34,-\tfrac{\sqrt3}{4})$, punto interior de $\overline{ST}$.

**Altura desde $Y$ a $\overline{PX}$:** con $d = X-P=(-\tfrac53,\tfrac{\sqrt3}{3})$ y $v=Y-P=(-\tfrac74,-\tfrac{\sqrt3}{4})$,

$$|d| = \sqrt{\tfrac{25}{9}+\tfrac13} = \tfrac{2\sqrt7}{3},\qquad |d\times v| = \left|-\tfrac53\cdot\left(-\tfrac{\sqrt3}{4}\right)-\tfrac{\sqrt3}{3}\cdot\left(-\tfrac74\right)\right| = \tfrac{12\sqrt3}{12}=\sqrt3.$$

La distancia de $Y$ a la recta $PX$ es

$$h = \frac{|d\times v|}{|d|} = \frac{\sqrt3}{2\sqrt7/3} = \frac{3\sqrt3}{2\sqrt7} = \frac{3\sqrt{21}}{14}.$$

**Verificación:** el pie de la altura es $Z=P+\tfrac67 d$, y como $s=\tfrac{(Y-P)\cdot d}{|d|^2}=\tfrac{8/3}{28/9}=\tfrac67\in(0,1)$, el pie cae dentro del segmento, así que la altura al segmento es bien esta distancia. Numéricamente $\tfrac{3\sqrt{21}}{14}\approx 0.982$, y comprobando con la ecuación de la recta $\sqrt3\,x+5y-\sqrt3=0$: la distancia de $Y$ es $\tfrac{3\sqrt3}{\sqrt{28}}=\tfrac{3\sqrt3}{2\sqrt7}$, que coincide. ✓

$$\boxed{\dfrac{3\sqrt{21}}{14}}$$