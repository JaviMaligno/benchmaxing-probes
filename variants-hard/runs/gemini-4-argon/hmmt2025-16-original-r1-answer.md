Para calcular el número de formas de elegir dos rectángulos en una cuadrícula de $5 \times 5$ cuadrados sin que se superpongan en su interior, bordes o vértices, podemos modelar el problema utilizando intervalos en los ejes coordenados.

### Paso 1: Representación de los rectángulos mediante intervalos
Una cuadrícula de $5 \times 5$ cuadrados está formada por $6$ líneas verticales (que podemos numerar como $x = 0, 1, 2, 3, 4, 5$) y $6$ líneas horizontales ($y = 0, 1, 2, 3, 4, 5$).

Cualquier rectángulo $R$ cuyos lados estén sobre las líneas de la cuadrícula queda determinado de forma única por el producto cartesiano de dos intervalos cerrados:
$$R = I_x \times I_y = [x_1, x_2] \times [y_1, y_2]$$
donde $0 \le x_1 < x_2 \le 5$ y $0 \le y_1 < y_2 \le 5$ son números enteros.

El número total de intervalos posibles en una dimensión (tanto horizontal como vertical) es el número de formas de elegir $2$ puntos extremos de entre las $6$ líneas disponibles:
$$N_{\text{intervalos}} = \binom{6}{2} = \frac{6 \times 5}{2} = 15$$

Por lo tanto, el número total de rectángulos en la cuadrícula es:
$$N_{\text{rectángulos}} = 15 \times 15 = 225$$

### Paso 2: Condición de no superposición
Dos rectángulos $R = I_x \times I_y$ y $R' = I'_x \times I'_y$ no comparten ningún punto (ni en su interior, ni en sus bordes, ni en sus vértices) si y solo si su intersección como conjuntos cerrados es vacía:
$$R \cap R' = (I_x \cap I'_x) \times (I_y \cap I'_y) = \emptyset$$

Esto ocurre si y solo si sus proyecciones son disjuntas en el eje horizontal **o** en el eje vertical:
$$I_x \cap I'_x = \emptyset \quad \text{o} \quad I_y \cap I'_y = \emptyset$$

### Paso 3: Conteo de pares de intervalos disjuntos
En una dimensión, dos intervalos cerrados $[a, b]$ y $[c, d]$ son disjuntos (no comparten ni siquiera un extremo) si y solo si $a < b < c < d$ o $c < d < a < b$. 

Para formar un par de intervalos disjuntos, basta con elegir $4$ puntos distintos de entre los $6$ disponibles en esa dimensión; los dos menores formarán un intervalo y los dos mayores formarán el otro:
- Número de pares no ordenados de intervalos disjuntos: $\binom{6}{4} = 15$.
- Número de pares **ordenados** de intervalos disjuntos: $2 \times \binom{6}{4} = 30$.

El número total de pares ordenados de intervalos $(I, I')$ en una dimensión es $15 \times 15 = 225$.

### Paso 4: Conteo de pares de rectángulos disjuntos
Contemos primero los pares **ordenados** de rectángulos $(R, R')$ que cumplen la condición $I_x \cap I'_x = \emptyset$ o $I_y \cap I'_y = \emptyset$, aplicando el principio de inclusión-exclusión:

1. **Disjuntos en el eje $x$ ($I_x \cap I'_x = \emptyset$):** Hay $30$ formas de elegir $(I_x, I'_x)$ disjuntos y $225$ formas de elegir $(I_y, I'_y)$ cualesquiera:
   $$30 \times 225 = 6750$$

2. **Disjuntos en el eje $y$ ($I_y \cap I'_y = \emptyset$):** De manera simétrica, hay $225$ formas de elegir $(I_x, I'_x)$ cualesquiera y $30$ formas de elegir $(I_y, I'_y)$ disjuntos:
   $$225 \times 30 = 6750$$

3. **Disjuntos en ambos ejes ($I_x \cap I'_x = \emptyset$ y $I_y \cap I'_y = \emptyset$):** Hay $30$ opciones para cada eje:
   $$30 \times 30 = 900$$

Por inclusión-exclusión, el número de pares ordenados $(R, R')$ de rectángulos disjuntos es:
$$6750 + 6750 - 900 = 12600$$

### Paso 5: Ajuste por el orden
Dado que el orden en que se eligen los dos rectángulos no importa (y un rectángulo nunca es disjunto consigo mismo), dividimos el resultado entre $2$:
$$\frac{12600}{2} = 6300$$

\boxed{6300}