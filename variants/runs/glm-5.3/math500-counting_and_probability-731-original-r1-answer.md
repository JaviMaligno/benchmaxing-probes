## Planteamiento

Coloco el centro en el origen: $O=(0,0)$, con vértices $(\pm a,\pm b)$, de modo que $AB/AD = a/b = k$ y el rectángulo tiene área $4ab$.

**Condición "más cerca de $O$ que del vértice $V$":** es el semiplano delimitado por la mediatriz de $OV$. Para $V=(a,b)$, los puntos equidistantes cumplen
$$x^2+y^2=(x-a)^2+(y-b)^2 \iff ax+by=\tfrac{a^2+b^2}{2}.$$

La región buscada es la intersección de los 4 semiplanos (uno por vértice) dentro del rectángulo. Como el conjunto de vértices es simétrico respecto a ambos ejes, la región también lo es.

## Análisis en el primer cuadrante

Basta calcular en el primer cuadrante y multiplicar por 4. Allí, con $x,y\ge 0$, la restricción más fuerte es la del vértice $(a,b)$:
$$ax+by\le \tfrac{a^2+b^2}{2},$$
pues las otras tres se deducen de ella (por ejemplo, $ax-by\le ax+by$).

**Simetría:** puedo suponer $a\ge b$ (el caso $b\ge a$ es análogo intercambiando ejes).

La recta $ax+by=\frac{a^2+b^2}{2}$ corta:
- el borde superior $y=b$ en $x_0=\dfrac{a^2-b^2}{2a}$,
- el borde inferior $y=0$ en $x^*=\dfrac{a^2+b^2}{2a}$ (nótese que $x^*\le a$ pues $b\le a$).

## Cálculo del área

La porción en el primer cuadrante es un rectángulo de base $x_0$ y altura $b$, más un triángulo de base $x^*-x_0$ y altura $b$:
$$\text{Área}_{Q1}=b\,x_0+\frac{b}{2}(x^*-x_0)=\frac{b}{2}\,(x_0+x^*)=\frac{b}{2}\cdot\frac{(a^2-b^2)+(a^2+b^2)}{2a}=\frac{b}{2}\cdot\frac{2a^2}{2a}=\frac{ab}{2}.$$

El área total de la región es $4\cdot\frac{ab}{2}=2ab$.

## Verificación

Para el cuadrado ($a=b$), la región es el rombo $|x|+|y|\le a$, con área $2a^2$ frente a $4a^2$: razón $\tfrac12$. ✓ Para $k$ muy grande, la condición tiende a $x\le a/2$: aproximadamente la mitad del rectángulo. ✓

## Probabilidad

$$P=\frac{2ab}{4ab}=\frac12,$$

y la cancelación es exacta: **el resultado no depende de $k$**.

$$\boxed{\dfrac{1}{2}}$$