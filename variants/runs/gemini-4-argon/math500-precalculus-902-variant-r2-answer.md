Para hallar la distancia desde el punto $Q$ hasta el sexto vértice del octaedro regular, podemos utilizar las propiedades de simetría de esta figura geométrica.

### Paso 1: Relación entre las distancias a vértices opuestos
Un octaedro regular tiene 6 vértices que se agrupan en 3 pares de vértices opuestos: $(A_1, B_1)$, $(A_2, B_2)$ y $(A_3, B_3)$. Los tres segmentos que unen cada par de vértices opuestos son las diagonales del octaedro, las cuales tienen la misma longitud y se bisecan perpendicularmente en el centro $O$ del octaedro. 

Si $R$ es el radio de la esfera circunscrita al octaedro (la distancia desde el centro $O$ a cualquiera de los vértices), por el teorema de Apolonio (o ley del paralelogramo) aplicado a cualquier punto $Q$ del espacio y a cada par de vértices opuestos $(A_i, B_i)$, se cumple que:
$$QA_i^2 + QB_i^2 = 2QO^2 + 2R^2$$

Como el lado derecho de la ecuación depende únicamente de la posición de $Q$ respecto al centro $O$ y del tamaño del octaedro, la suma de los cuadrados de las distancias desde $Q$ a cualquier par de vértices opuestos es una constante $S$:
$$QA_1^2 + QB_1^2 = QA_2^2 + QB_2^2 = QA_3^2 + QB_3^2 = S$$

### Paso 2: Emparejamiento de las distancias conocidas
Las distancias dadas desde $Q$ a cinco de los vértices son $4, 8, 10, 11$ y $13$. Elevando estas distancias al cuadrado, obtenemos:
$$4^2 = 16$$
$$8^2 = 64$$
$$10^2 = 100$$
$$11^2 = 121$$
$$13^2 = 169$$

De estos cinco valores, cuatro corresponden a dos pares completos de vértices opuestos, por lo que deben existir dos pares de números que sumen exactamente lo mismo. Observando las sumas posibles de dos elementos del conjunto $\{16, 64, 100, 121, 169\}$, encontramos que la única coincidencia es:
$$16 + 169 = 185$$
$$64 + 121 = 185$$

Por lo tanto, la suma constante para cada par de vértices opuestos es $S = 185$.

### Paso 3: Cálculo de la distancia restante
El quinto valor cuadrado conocido es $100$ (correspondiente a la distancia $10$). Sea $x$ la distancia desde $Q$ hasta el sexto vértice (el opuesto al vértice a distancia $10$). Entonces se debe cumplir:
$$10^2 + x^2 = 185$$
$$100 + x^2 = 185$$
$$x^2 = 85 \implies x = \sqrt{85}$$

\boxed{\sqrt{85}}