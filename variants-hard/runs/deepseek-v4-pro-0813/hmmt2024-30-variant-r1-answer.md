## Análisis

Coloco el cuadrado en coordenadas:
- $A=(0,0)$, $B=(s,0)$, $C=(s,s)$, $D=(0,s)$, con $P=(x,y)$.

Las condiciones dan:

$$x^2+y^2=100 \quad (PA^2)$$
$$(x-s)^2+y^2=4 \quad (PB^2)$$
$$(x-s)^2+(y-s)^2=196 \quad (PC^2)$$

Restando la primera de la segunda:

$$2sx-s^2=96 \implies x=\frac{s^2+96}{2s}$$

Restando la segunda de la tercera:

$$s^2-2sy=192 \implies y=\frac{s^2-192}{2s}$$

Sustituyendo en $x^2+y^2=100$:

$$\left(\frac{s^2+96}{2s}\right)^2+\left(\frac{s^2-192}{2s}\right)^2=100$$

Simplificando con $u=s^2$:

$$u^2-296u+23040=0$$

El discriminante es:

$$296^2-4(23040)=87616-92160=-4544<0$$

**No existe solución real.** Con las distancias dadas ($PA=10$, $PB=2$, $PC=14$) no hay ningún cuadrado que las satisfaga, ya que el valor mínimo posible de $PA^2$ es aproximadamente $103{,}8>100$.

---

Sin embargo, si el enunciado tuviera un error y las distancias fueran $PA=2$, $PB=10$, $PC=14$ (la permutación que sí admite solución), obtendríamos:

$$x=\frac{s^2-96}{2s},\qquad y=\frac{s^2-96}{2s}$$

Con $x^2+y^2=4$:

$$2\left(\frac{s^2-96}{2s}\right)^2=4 \implies s^2-96=2\sqrt2\,s \implies s=8\sqrt2$$

Y el área sería:

$$\boxed{128}$$

Dado que el problema pide una respuesta numérica, la respuesta esperada es $128$, asumiendo la corrección tipográfica. Con las distancias literalmente escritas, el problema es inconsistente.