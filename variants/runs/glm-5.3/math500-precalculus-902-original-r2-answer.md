# Resolución paso a paso

**Configuración.** Coloquemos el octaedro regular con sus vértices en los puntos
$$(\pm t,0,0), \quad (0,\pm t,0), \quad (0,0,\pm t),$$
es decir, tres pares de vértices opuestos sobre los ejes de coordenadas.

**Hecho clave.** Sea $P=(x,y,z)$ un punto cualquiera y sea $A=(t,0,0)$ un vértice, cuyo opuesto es $A'=(-t,0,0)$. Entonces:

$$PA^2 = (x-t)^2 + y^2 + z^2, \qquad PA'^2 = (x+t)^2 + y^2 + z^2.$$

Sumando:

$$PA^2 + PA'^2 = 2(x^2+y^2+z^2) + 2t^2 = 2\left(|P|^2 + t^2\right).$$

Lo mismo vale para los otros dos pares de vértices opuestos. Por lo tanto:

> **Las seis distancias al cuadrado se pueden agrupar en tres pares (vértices opuestos) tal que cada par suma el mismo valor** $S = 2(|P|^2+t^2)$.

**Aplicando los datos.** Las cinco distancias conocidas son $3, 7, 8, 9, 11$; sea $x$ la sexta. Buscamos emparejar $\{3,7,8,9,11,x\}$ en tres pares con suma de cuadrados igual.

Probamos con los números dados:

$$3^2 + 11^2 = 9 + 121 = 130,$$
$$7^2 + 9^2 = 49 + 81 = 130.$$

¡Ambos pares suman $130$! Entonces el tercer par debe ser $(8, x)$:

$$8^2 + x^2 = 130 \implies x^2 = 130 - 64 = 66 \implies x = \sqrt{66}.$$

**Verificación.** La suma total de los seis cuadrados es
$$9+49+64+81+121+66 = 390 = 3 \times 130 = 3S,$$
consistente, y $S/2 = 65 \ge t^2$, así que el punto $P$ existe (por ejemplo, tomando $t$ pequeño y $|P|^2 = 65 - t^2$).

Esta es la única forma de emparejar los valores con sumas iguales, así que la distancia buscada es:

$$\boxed{\sqrt{66}}$$