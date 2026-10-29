Para determinar la probabilidad de que exista un triángulo con lados de longitudes $2$, $a$ y $b$, primero definimos el espacio muestral y las condiciones necesarias.

1. **Espacio muestral:**
   Los números $a$ y $b$ se eligen de forma independiente y uniforme en el intervalo $(0,4)$. Esto se puede representar geométricamente como un cuadrado en el plano cartesiano $(a,b)$ con vértices en $(0,0)$, $(4,0)$, $(4,4)$ y $(0,4)$. El área total de este cuadrado es:
   $$\text{Área total} = 4 \times 4 = 16$$

2. **Desigualdad triangular:**
   Para que tres segmentos de longitudes $2$, $a$ y $b$ formen un triángulo, deben cumplir las tres desigualdades triangulares:
   - $a + b > 2$
   - $a + 2 > b \implies b < a + 2$
   - $b + 2 > a \implies a < b + 2 \quad (\text{o } b > a - 2)$

3. **Cálculo del área de la región favorable:**
   Es más sencillo calcular el área de las regiones dentro del cuadrado donde **no** se cumplen estas condiciones (las cuales son mutuamente excluyentes salvo en puntos de la frontera):
   - Para $a + b \le 2$: forma un triángulo rectángulo en la esquina inferior izquierda con vértices en $(0,0)$, $(2,0)$ y $(0,2)$. Su área es $\frac{2 \times 2}{2} = 2$.
   - Para $b \ge a + 2$: forma un triángulo rectángulo en la esquina superior izquierda con vértices en $(0,2)$, $(0,4)$ y $(2,4)$. Su área es $\frac{2 \times 2}{2} = 2$.
   - Para $b \le a - 2$: forma un triángulo rectángulo en la esquina inferior derecha con vértices en $(2,0)$, $(4,0)$ y $(4,2)$. Su área es $\frac{2 \times 2}{2} = 2$.

   El área total no favorable es la suma de las áreas de estos tres triángulos:
   $$\text{Área no favorable} = 2 + 2 + 2 = 6$$

   Por lo tanto, el área de la región donde sí se puede formar un triángulo es:
   $$\text{Área favorable} = 16 - 6 = 10$$

4. **Probabilidad:**
   Dividiendo el área favorable entre el área total del cuadrado obtenemos la probabilidad buscada:
   $$P = \frac{10}{16} = \frac{5}{8}$$

\boxed{\frac{5}{8}}