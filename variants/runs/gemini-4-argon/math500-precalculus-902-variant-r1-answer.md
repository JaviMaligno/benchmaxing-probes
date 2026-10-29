Para encontrar la distancia desde el punto $Q$ hasta el sexto vértice del octaedro regular, podemos utilizar un sistema de coordenadas cartesianas.

### Paso 1: Coordenadas de los vértices del octaedro regular
Ubicamos el centro del octaedro regular en el origen $O(0,0,0)$ y alineamos los ejes coordenados con sus diagonales principales. Si la distancia desde el centro a cada vértice (el circunradio) es $R$, los seis vértices se agrupan en tres pares de vértices opuestos con coordenadas:
- $A_1(R, 0, 0)$ y $B_1(-R, 0, 0)$
- $A_2(0, R, 0)$ y $B_2(0, -R, 0)$
- $A_3(0, 0, R)$ y $B_3(0, 0, -R)$

### Paso 2: Relación entre las distancias a vértices opuestos
Sea $Q(x_0, y_0, z_0)$ el punto dado. Calculamos la suma de los cuadrados de las distancias desde $Q$ hasta el primer par de vértices opuestos $(A_1, B_1)$:
$$QA_1^2 + QB_1^2 = \left[(x_0 - R)^2 + y_0^2 + z_0^2\right] + \left[(x_0 + R)^2 + y_0^2 + z_0^2\right]$$
$$QA_1^2 + QB_1^2 = 2(x_0^2 + y_0^2 + z_0^2 + R^2)$$

Por simetría (o aplicando el teorema de la mediana en los triángulos $QA_iB_i$), esta suma depende únicamente de la distancia de $Q$ al centro del octaedro y del radio $R$. Por lo tanto, la suma de los cuadrados de las distancias a dos vértices opuestos es constante para los tres pares:
$$QA_1^2 + QB_1^2 = QA_2^2 + QB_2^2 = QA_3^2 + QB_3^2 = S$$

### Paso 3: Emparejamiento de las distancias dadas
Los cuadrados de las cinco distancias conocidas son:
- $4^2 = 16$
- $8^2 = 64$
- $10^2 = 100$
- $11^2 = 121$
- $13^2 = 169$

Cuatro de estos cinco valores deben corresponder a dos pares de vértices opuestos y, por ende, deben tener la misma suma $S$. Analizando las sumas por pares posibles entre $\{16, 64, 100, 121, 169\}$, observamos que la única suma que se repite es $185$:
$$16 + 169 = 185$$
$$64 + 121 = 185$$

Por lo tanto, la suma constante es $S = 185$.

### Paso 4: Cálculo de la distancia restante
El quinto valor ($10^2 = 100$) debe formar pareja con el cuadrado de la distancia $d$ al vértice restante:
$$10^2 + d^2 = 185$$
$$100 + d^2 = 185$$
$$d^2 = 85 \implies d = \sqrt{85}$$

\boxed{\sqrt{85}}