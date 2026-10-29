Sea $p$ la probabilidad de que salga la cara $F$, y sea $q$ la probabilidad de que salga la cara opuesta a $F$. Las otras cuatro caras tienen probabilidad $1/6$ cada una.

Como la suma de todas las probabilidades debe ser 1:

$$p+q+4\cdot \frac16=1 \implies p+q=\frac13=\frac{2}{6}.$$

Queremos que la suma de los dos números sea 7. Para un dado estándar, las parejas de caras opuestas suman 7, así que las parejas que suman 7 son exactamente las parejas de caras opuestas: $(F, \overline F)$, $(\overline F, F)$, y las otras dos parejas de caras opuestas.

La probabilidad de obtener 7 es:

$$\text{Prob}(F,\overline F)+\text{Prob}(\overline F,F)+2\cdot\left(\frac16\cdot\frac16+\frac16\cdot\frac16\right).$$

Calculamos:

- $\text{Prob}(F,\overline F)=p q$
- $\text{Prob}(\overline F,F)=q p = p q$
- Cada una de las otras dos parejas opuestas contribuye con $\frac16\cdot\frac16+\frac16\cdot\frac16=\frac{2}{36}=\frac1{18}$.

Por tanto:

$$\frac{71}{450}=2pq+2\cdot\frac1{18}=2pq+\frac19.$$

Restamos $\frac19$:

$$2pq=\frac{71}{450}-\frac19=\frac{71}{450}-\frac{50}{450}=\frac{21}{450}=\frac{7}{150}.$$

Entonces

$$pq=\frac{7}{300}.$$

Tenemos $p+q=\frac13$ y $pq=\frac{7}{300}$. Las raíces de la ecuación $x^2-\frac13x+\frac{7}{300}=0$ son $p$ y $q$. Multiplicamos por $300$:

$$300x^2-100x+7=0.$$

El discriminante es

$$\Delta=10000-8400=1600=40^2.$$

Entonces

$$x=\frac{100\pm 40}{600},$$

lo que da

$$x=\frac{140}{600}=\frac{7}{30}\quad\text{o}\quad x=\frac{60}{600}=\frac{1}{10}.$$

Como $p>1/6$ y $q<1/6$, tomamos

$$p=\frac{7}{30},\qquad q=\frac{1}{10}.$$

Así, $m=7$ y $n=30$, por lo que

$$m+n=37.$$

\boxed{37}