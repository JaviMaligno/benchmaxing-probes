## Solución

**Paso 1: Coordenadas del octaedro.**
Coloquemos el octaedro regular con centro en el origen y vértices en
$$(\pm a, 0,0), \quad (0,\pm a, 0), \quad (0,0,\pm a),$$
y sea $P = (x,y,z)$.

**Paso 2: Propiedad clave de los vértices opuestos.**
Para un par de vértices opuestos, por ejemplo $(a,0,0)$ y $(-a,0,0)$:
$$PA^2 + PB^2 = \big[(x-a)^2+y^2+z^2\big] + \big[(x+a)^2+y^2+z^2\big] = 2(x^2+y^2+z^2+a^2).$$

El mismo cálculo vale para los otros dos pares de vértices opuestos. Por lo tanto:

> **La suma de los cuadrados de las distancias a cada par de vértices opuestos es la misma constante** $S = 2(x^2+y^2+z^2+a^2)$.

**Paso 3: Formar los pares.**
Los cuadrados de las cinco distancias conocidas son:
$$3^2,\ 7^2,\ 8^2,\ 9^2,\ 11^2 \;=\; 9,\ 49,\ 64,\ 81,\ 121.$$

Las seis distancias (las cinco dadas más la desconocida $d$) deben repartirse en **tres pares con la misma suma de cuadrados**. Buscamos dos pares disjuntos entre los números dados que tengan igual suma:

$$9 + 121 = 130, \qquad 49 + 81 = 130.$$

(Es la única forma de lograrlo: por ejemplo, $9+49=58$, $9+64=73$, $64+81=145$, etc., no tienen ninguna otra coincidencia.)

**Paso 4: Hallar la distancia restante.**
Las distancias $3$ y $11$ van a un par de vértices opuestos, y $7$ y $9$ a otro. Entonces la distancia $8$ y la desconocida $d$ ocupan el tercer par de vértices opuestos, así que:
$$8^2 + d^2 = 130 \quad\Longrightarrow\quad d^2 = 130 - 64 = 66,$$
$$d = \sqrt{66}.$$

$\boxed{\sqrt{66}}$