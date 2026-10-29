## Solución

**Paso 1: Formulación de la dinámica.** La actualización simultánea $a_i \gets \max(a_{i-1},a_i,a_{i+1})$ tras $t$ segundos produce
$$a_i^{(t)} = \max\{a_{i-t},\ldots,a_{i+t}\}$$
(índices módulo $2025$). Con $n=2025$ impar y $t=100$, cada ventana tiene $2t+1 = 201$ elementos, y no cubre todo el círculo.

**Paso 2: Los valores que sobreviven son máximos locales iniciales.** Como las $a_i$ son i.i.d. continuas, casi seguramente no hay empates en la configuración inicial. Todo valor que no sea un máximo local estricto (es decir, si $a_i < \max(a_{i-1},a_i,a_{i+1})$) desaparece ya en el primer paso: su vecino mayor lo domina en la ventana de radio $t \geq 1$. Por tanto, el conjunto de valores distintos tras $t$ pasos está contenido en el conjunto de máximos locales estrictos de la configuración inicial.

**Paso 3: Criterio exacto de supervivencia.** Sea $M$ una posición de máximo local estricto. Tras $t$ pasos, el valor en $M$ se propaga a las posiciones $M-t,\ldots,M+t$. Este máximo local sobrevive como *valor único* (no fusionado con otro) si y solo si es estrictamente mayor que los $201$ valores a su izquierda y los $201$ valores a su derecha — es decir, es el máximo estricto de su bloque de $201$ posiciones. Como los valores son continuos, no hay empates en la configuración inicial.

**Paso 4: Independencia de los supervivientes.** Sea $X$ el número de valores distintos tras $t=100$ pasos. Los bloques locales son internamente independientes entre sí. Cada uno de los $n$ valores es un máximo estricto de su vecindario con probabilidad $p = \int_0^1 P(\text{máximo estricto})$. Como la posición es uniforme, $p = 1/201$ (probabilidad de que un elemento dado sea el máximo de un conjunto de $201$ elementos i.i.d. continuos).

Como los bloques son de tamaño impar $201 < n$, el número de valores distintos sobrevivientes es casi seguramente igual al número de máximos locales estrictos de la configuración inicial que son máximos estrictos en su vecindad. Cada máximo local sobrevive con probabilidad $1/201$ condicionada a que sea un máximo local. El número de máximos locales es casi seguramente un número aleatorio, pero podemos usar simetría de intercambio:

$$
\mathbb{E}[X] = n \cdot P(\text{$a_1$ sobrevive})
$$

donde $a_1$ sobrevive si es un máximo estricto en un círculo de $201$ posiciones alrededor de él, pero dado que la configuración es uniforme y las posiciones son i.i.d., $P(\text{$a_1$ sobrevive}) = 1 \cdot \frac{1}{201}$ (probabilidad de ser el máximo de su vecindad de tamaño $201$).

$$
\mathbb{E}[X] = 2025 \cdot \frac{1}{201} = \frac{2025}{201} = \frac{2025}{201}
$$

Como $2025 = 201 \cdot 10 + 15$, tenemos $2025/201 \approx 10.07$.

Verificamos: $201 \cdot 10 = 2010$, $2025 - 2010 = 15$, así que $2025/201 = 10 + 15/201 = 10 + 5/67$.

$$
\boxed{\frac{2025}{201}}$$