## Planteamiento

Coloco el centro $O$ en el origen y tomo circunradio $1$. Los vértices son
$$P=(0,1),\quad Q=\left(-\tfrac{\sqrt3}{2},-\tfrac12\right),\quad R=\left(\tfrac{\sqrt3}{2},-\tfrac12\right).$$

**Condición "más cerca de $O$ que de $P$":** es el semiplano delimitado por la mediatriz del segmento $OP$. Como $|OP|=1$, esa mediatriz es la recta $y=\tfrac12$, y la condición es $y\le \tfrac12$.

Por simetría, las otras dos condiciones son los semiplanos acotados por las mediatrices de $OQ$ y $OR$, rectas también a distancia $\tfrac12$ de $O$ y perpendiculares a las direcciones de $Q$ y $R$.

## Identificación de la región

La intersección de esos tres semiplanos es un triángulo equilátero con inradio $\tfrac12$ centrado en $O$, cuyas direcciones normales apuntan hacia $P,Q,R$: es exactamente el triángulo $PQR$ rotado $180^\circ$ respecto de $O$ (nótese que el inradio de $PQR$ también es $\tfrac12$, pues inradio $=$ circunradio$/2$).

Por tanto la región buscada es
$$PQR \cap (-PQR),$$
que es el hexágono regular clásico que se forma al superponer un triángulo equilátero con su simétrico central.

## Cálculo del área

Si el lado de $PQR$ es $s$, las rectas del triángulo rotado cortan cada lado en sus puntos de trisección, de modo que el hexágono es regular de lado $s/3$:
$$[\text{hexágono}]=\frac{3\sqrt3}{2}\left(\frac{s}{3}\right)^2=\frac{\sqrt3\,s^2}{6},\qquad [PQR]=\frac{\sqrt3\,s^2}{4}.$$

La probabilidad es el cociente:
$$\frac{\sqrt3 s^2/6}{\sqrt3 s^2/4}=\frac{4}{6}=\frac{2}{3}.$$

$\boxed{\dfrac{2}{3}}$