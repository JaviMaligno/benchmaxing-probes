## Resolución

**Paso 1: Convertir a ecuación polinómica.** Multiplico ambos lados por $P(x) = (x^2-1)(x^2-2)(x^2-3)(x^2-4)$:

$$\sum_{k=1}^{4} k \prod_{j \neq k} (x^2 - j) = (2022x - 4)\,P(x)$$

**Paso 2: Analizar los grados.** El lado izquierdo es una suma de polinomios de grado 6 (cada producto tiene tres factores cuadráticos), así que tiene grado a lo sumo 6. El lado derecho tiene grado 9, pues $P(x)$ tiene grado 8.

Expandiendo $P(x) = x^8 - 10x^6 + 35x^4 - 50x^2 + 24$, el lado derecho es:

$$(2022x - 4)(x^8 - 10x^6 + \cdots) = 2022x^9 - 4x^8 - 20220x^7 + \cdots$$

**Paso 3: Formar el polinomio y aplicar Vieta.** Pasando todo a un lado:

$$2022x^9 - 4x^8 - 20220x^7 + (\text{términos de grado} \le 6 \text{ ajustados}) = 0$$

Como el lado izquierdo original solo tiene grado 6, los coeficientes de $x^9$ y $x^8$ no se ven afectados: son $2022$ y $-4$ respectivamente.

Por las fórmulas de Vieta, la suma de las 9 raíces complejas es:

$$-\frac{-4}{2022} = \frac{4}{2022} = \frac{2}{1011}$$

**Paso 4: Verificar que no hay raíces extrañas.** Los puntos problemáticos serían $x^2 \in \{1,2,3,4\}$. Pero si $x^2 = k$, el lado izquierdo de la ecuación polinómica vale $k\prod_{j\neq k}(x^2 - j) \neq 0$, mientras que el derecho vale $0$. Por tanto, ninguna raíz del polinomio anula los denominadores originales: las 9 raíces son válidas.

$$\boxed{\dfrac{2}{1011}}$$