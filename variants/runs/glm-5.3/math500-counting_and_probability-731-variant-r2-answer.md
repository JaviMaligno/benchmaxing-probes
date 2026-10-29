## Planteamiento

Como el triángulo es equilátero, todos sus centros coinciden en $O$. Tomemos el circunradio $=1$ y $O$ en el origen:

$$P=(0,1),\quad Q=\left(-\tfrac{\sqrt3}{2},-\tfrac12\right),\quad R=\left(\tfrac{\sqrt3}{2},-\tfrac12\right),$$

con $\text{área}(PQR)=\tfrac{3\sqrt3}{4}$.

## Traducir la condición a mediatrices

Un punto $X=(x,y)$ está más cerca de $O$ que de $P$ si y solo si

$$x^2+y^2< x^2+(y-1)^2 \iff y<\tfrac12,$$

es decir, $X$ debe quedar del lado de $O$ en la mediatriz de $OP$, que es la recta $y=\tfrac12$ **paralela al lado $QR$**. De forma análoga:

- más cerca de $O$ que de $Q$: $\sqrt3\,x+y>-1$ (mediatriz de $OQ$, paralela a $PR$),
- más cerca de $O$ que de $R$: $\sqrt3\,x-y<1$ (mediatriz de $OR$, paralela a $PQ$).

## Los tres casquetes excluidos

El complemento dentro del triángulo es la unión de tres "casquetes", uno por vértice. Por ejemplo, el casquete en $P$ es $\{y>\tfrac12\}\cap PQR$: como la mediatriz de $OP$ es paralela a $QR$, es un triángulo **semejante** a $PQR$.

Alturas (con circunradio $\rho=1$, inradio $\rho/2$):
- altura del casquete: $\rho-\tfrac{\rho}{2}=\tfrac{\rho}{2}=\tfrac12$,
- altura total del triángulo: $\rho+\tfrac{\rho}{2}=\tfrac{3\rho}{2}=\tfrac32$.

Razón lineal $=\tfrac12/\tfrac32=\tfrac13$, así que cada casquete tiene área $\tfrac19$ del triángulo. (Equivalentemente: los casquetes cortan cada lado en sus **puntos de trisección**.)

**No se solapan:** un punto del casquete en $P$ cumple $y>\tfrac12$, luego $|x|<\tfrac{1}{2\sqrt3}$; pero si además cumpliera $\sqrt3 x+y<-1$, entonces $x<-\tfrac{1+y}{\sqrt3}<-\tfrac{\sqrt3}{2}$, contradicción. Por simetría, los tres casquetes son disjuntos dos a dos.

## Cálculo

$$\Pr(\text{excluido})=\frac{3\cdot\frac19\,\text{área}}{\text{área}}=\frac13,$$

de modo que la región favorable (un hexágono regular de lado $s/3$) ocupa

$$1-\frac13=\frac23.$$

*(Verificación: el hexágono tiene vértices $\left(\pm\tfrac{1}{2\sqrt3},\pm\tfrac12\right),\left(\pm\tfrac{1}{\sqrt3},0\right)$; por el formula del shoelace su área es $\tfrac{\sqrt3}{2} = \tfrac23\cdot\tfrac{3\sqrt3}{4}$, que coincide.)*

$$\boxed{\dfrac{2}{3}}$$