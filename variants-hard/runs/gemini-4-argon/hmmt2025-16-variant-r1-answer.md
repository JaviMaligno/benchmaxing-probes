Para determinar de cuántas maneras se pueden elegir dos rectángulos en una cuadrícula de $6 \times 6$ sin que compartan puntos interiores, puntos en sus bordes ni vértices, podemos representar cada rectángulo mediante sus proyecciones sobre los ejes de coordenadas.

### 1. Representación mediante intervalos
Una cuadrícula de $6 \times 6$ cuadrados unitarios está formada por $7$ líneas verticales y $7$ líneas horizontales, cuyas coordenadas podemos numerar con el conjunto $\{0, 1, 2, 3, 4, 5, 6\}$.

Cualquier rectángulo $R$ cuyos lados estén sobre las líneas de la cuadrícula queda determinado de forma única como el producto cartesiano de dos intervalos cerrados:
$$R = I \times J = [x_1, x_2] \times [y_1, y_2]$$
donde $0 \le x_1 < x_2 \le 6$ y $0 \le y_1 < y_2 \le 6$.

El número total de intervalos posibles en una dimensión (tanto horizontal como vertical) equivale a elegir $2$ líneas de las $7$ disponibles:
$$\binom{7}{2} = \frac{7 \times 6}{2} = 21$$

Por lo tanto, el número de pares ordenados de intervalos $(I_1, I_2)$ en una sola dimensión es:
$$21 \times 21 = 441$$

### 2. Condición para que dos rectángulos sean disjuntos
Dos rectángulos $R_1 = I_1 \times J_1$ y $R_2 = I_2 \times J_2$ no comparten ningún punto (ni interior, ni de borde, ni vértice) si y solo si su intersección es vacía:
$$R_1 \cap R_2 = (I_1 \cap I_2) \times (J_1 \cap J_2) = \emptyset$$

Esto ocurre si y solo si sus proyecciones horizontales son disjuntas ($I_1 \cap I_2 = \emptyset$) **o** sus proyecciones verticales son disjuntas ($J_1 \cap J_2 = \emptyset$).

Para que dos intervalos cerrados $I_1$ e $I_2$ sean disjuntos, sus cuatro extremos deben ser puntos distintos en $\{0, 1, 2, 3, 4, 5, 6\}$ tales que un intervalo quede completamente a la izquierda del otro (es decir, $a < b < c < d$). El número de pares ordenados $(I_1, I_2)$ de intervalos disjuntos es:
$$2 \times \binom{7}{4} = 2 \times 35 = 70$$
(donde el factor $2$ se debe a que cualquiera de los dos intervalos puede ir primero).

### 3. Conteo mediante el Principio de Inclusión-Exclusión
Consideremos primero pares **ordenados** de rectángulos $(R_1, R_2)$:
- Sea $A$ el conjunto de pares donde $I_1 \cap I_2 = \emptyset$. Hay $70$ formas de elegir $(I_1, I_2)$ y $441$ formas de elegir $(J_1, J_2)$ sin restricción:
  $$|A| = 70 \times 441 = 30\,870$$
- Sea $B$ el conjunto de pares donde $J_1 \cap J_2 = \emptyset$. Por simetría, hay $441$ formas para $(I_1, I_2)$ y $70$ formas para $(J_1, J_2)$:
  $$|B| = 441 \times 70 = 30\,870$$
- La intersección $A \cap B$ corresponde a los pares donde tanto los intervalos horizontales como los verticales son disjuntos:
  $$|A \cap B| = 70 \times 70 = 4\,900$$

Por el principio de inclusión-exclusión, el número de pares ordenados de rectángulos disjuntos es:
$$|A \cup B| = |A| + |B| - |A \cap B| = 30\,870 + 30\,870 - 4\,900 = 56\,840$$

### 4. Pares no ordenados
Dado que el orden en que se eligen los dos rectángulos no importa (y dos rectángulos disjuntos nunca pueden ser iguales), dividimos el resultado entre $2$:
$$\frac{56\,840}{2} = 28\,420$$

\boxed{28420}