Sea $N = \underline{abcd} = 1000a + m$, donde $m = \underline{bcd}$.

La condición es $\sqrt{1000a + m} = a\sqrt{m}$. Elevando al cuadrado:

$$1000a + m = a^2 m \implies 1000a = (a^2 - 1)m \implies m = \frac{1000a}{(a-1)(a+1)}$$

Probando $a = 1, \dots, 9$, se necesita que $(a-1)(a+1)$ divida a $1000a$ y que $m$ sea de tres dígitos (o menos, pero debe dar un número de cuatro cifras válido):

- $a=2$: $m = 2000/3$, no entero.
- $a=3$: $m = 3000/8 = 375$. ✓
- $a=4$: $m = 4000/15$, no entero.
- $a=5$: $m = 5000/24$, no entero.
- $a=6,7,8,9$: tampoco dan enteros ($6000/35$, $7000/48$, $8000/63$, $9000/80$).

Verificación: $\sqrt{3375} = \sqrt{9 \cdot 375} = 3\sqrt{375}$. ✓

$$\boxed{3375}$$