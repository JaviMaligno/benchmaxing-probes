Para que exista un triángulo con lados $1$, $x$, $y$ deben cumplirse las desigualdades triangulares:

1. $1 + x > y$
2. $1 + y > x$
3. $x + y > 1$

Las dos primeras equivalen a $|x - y| < 1$.

**Espacio muestral:** el cuadrado $(0,3)\times(0,3)$, con área $9$.

**Región favorable:** $|x-y|<1$ y $x+y>1$.

- El área donde $|x-y|<1$ dentro del cuadrado es el área total menos los dos triángulos de las esquinas (cada uno con catetos de longitud $2$):
$$9 - 2\cdot\tfrac{1}{2}(2)^2 = 9 - 4 = 5.$$

- De esa región hay que quitar la parte donde $x+y\le 1$: el triángulo con vértices $(0,0)$, $(1,0)$, $(0,1)$, de área $\tfrac{1}{2}$. En ese triángulo siempre se cumple $|x-y|<1$, así que se resta completo:
$$5 - \tfrac{1}{2} = \tfrac{9}{2}.$$

**Probabilidad:**
$$\frac{9/2}{9} = \frac{1}{2}.$$

$$\boxed{\dfrac{1}{2}}$$