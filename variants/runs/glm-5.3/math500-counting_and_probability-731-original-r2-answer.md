## Planteamiento

Pongo el rectángulo con centro $O$ en el origen: sean $AB = 2a$ y $AD = 2b$, de modo que $k = a/b$. Los vértices son
$$A=(-a,b),\quad B=(a,b),\quad C=(a,-b),\quad D=(-a,-b).$$

## Condición «más cerca de $O$ que de un vértice»

Para un punto $P=(x,y)$, comparar distancias al cuadrado con $O$ y con $B=(a,b)$:
$$x^2+y^2 < (x-a)^2+(y-b)^2 \iff 2(ax+by) < a^2+b^2.$$

Repitiendo esto con los cuatro vértices (cambiando los signos de $a$ y $b$), la región buscada es
$$R=\{\,2a|x| + 2b|y| < a^2+b^2\,\},$$
un rombo con diagonales sobre los ejes, de vértices $\left(\pm\tfrac{a^2+b^2}{2a},0\right)$ y $\left(0,\pm\tfrac{a^2+b^2}{2b}\right)$. Como el punto se elige dentro del rectángulo, hay que intersecar este rombo con el rectángulo $|x|\le a,\ |y|\le b$.

## Área de la intersección

Supongo $k\ge 1$ (es decir $a\ge b$); el caso $k\le 1$ es idéntico intercambiando los papeles de $a$ y $b$.

Comparo el rombo con el rectángulo:
- Horizontalmente: $\tfrac{a^2+b^2}{2a}\le a \iff b\le a$ ✓ (el rombo no sobresale a los lados),
- Verticalmente: $\tfrac{a^2+b^2}{2b}\ge b \iff a\ge b$ ✓ (el rombo sobresale arriba y abajo).

Así que dentro de la franja $|y|\le b$, la sección horizontal del rombo queda completa dentro del rectángulo: para cada $y$ con $|y|\le b$,
$$|x| \le \frac{a^2+b^2-2b|y|}{2a},$$
cociente que está entre $0$ y $a$ en todo el rango (en $|y|=b$ vale $\tfrac{a^2-b^2}{2a}\ge 0$).

Integro el ancho de las secciones:
$$\text{Área} = \int_{-b}^{b}\frac{a^2+b^2-2b|y|}{a}\,dy = \frac{2}{a}\int_0^b (a^2+b^2-2by)\,dy = \frac{2}{a}\Big[(a^2+b^2)b - b^3\Big] = \frac{2}{a}\cdot a^2 b = 2ab.$$

## Probabilidad

El rectángulo mide $2a \times 2b = 4ab$, así que
$$P = \frac{2ab}{4ab} = \frac12.$$

El resultado no depende de $k$: el aspecto solo decide por qué lado sobresale el rombo, pero el área recortada siempre es exactamente la mitad del rectángulo.

$$\boxed{\dfrac{1}{2}}$$