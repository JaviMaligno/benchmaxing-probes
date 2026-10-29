Para encontrar la distancia desde el punto $P$ hasta el sexto vértice del octaedro regular, podemos situar el octaedro en un sistema de coordenadas cartesianas tridimensional centrado en el origen.

Sean los seis vértices del octaedro regular:
- $A = (a, 0, 0)$ y $B = (-a, 0, 0)$
- $C = (0, a, 0)$ y $D = (0, -a, 0)$
- $E = (0, 0, a)$ y $F = (0, 0, -a)$

donde $A$ y $B$, $C$ y $D$, y $E$ y $F$ son los tres pares de vértices opuestos.

Sea $P = (x, y, z)$ un punto arbitrario en el espacio. Calculamos la suma de los cuadrados de las distancias desde $P$ a un par de vértices opuestos, por ejemplo $A$ y $B$:
$$PA^2 + PB^2 = \left((x - a)^2 + y^2 + z^2\right) + \left((x + a)^2 + y^2 + z^2\right) = 2(x^2 + y^2 + z^2 + a^2)$$

Por simetría, obtenemos exactamente el mismo resultado para los otros dos pares de vértices opuestos:
$$PA^2 + PB^2 = PC^2 + PD^2 = PE^2 + PF^2$$

Esto significa que la suma de los cuadrados de las distancias desde $P$ a dos vértices opuestos cualesquiera es constante.

Las cinco distancias conocidas son $3, 7, 8, 9$ y $11$. Elevando cada una al cuadrado, obtenemos:
- $3^2 = 9$
- $7^2 = 49$
- $8^2 = 64$
- $9^2 = 81$
- $11^2 = 121$

Debemos agrupar cuatro de estos valores en dos pares que tengan la misma suma. Observando los números, notamos que:
$$9 + 121 = 130$$
$$49 + 81 = 130$$

Por lo tanto, la suma constante de los cuadrados de las distancias a vértices opuestos es $130$. Sea $d$ la distancia al sexto vértice, la cual debe formar pareja con la distancia restante ($8$, cuyo cuadrado es $64$):
$$64 + d^2 = 130$$
$$d^2 = 66$$
$$d = \sqrt{66}$$

\boxed{\sqrt{66}}