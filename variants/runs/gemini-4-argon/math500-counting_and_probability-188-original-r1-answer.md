Para determinar la probabilidad de que exista un triángulo con lados de longitud $1$, $x$ e $y$, podemos utilizar probabilidad geométrica.

1. **Espacio muestral:**
   Como $x$ e $y$ se eligen al azar de forma independiente en el intervalo $(0,3)$, el espacio muestral se puede representar como un cuadrado en el plano cartesiano $[0,3] \times [0,3]$. El área total de este cuadrado es:
   $$\text{Área total} = 3 \times 3 = 9$$

2. **Condiciones para formar un triángulo (Desigualdad triangular):**
   Tres segmentos de longitudes $1$, $x$ e $y$ pueden formar un triángulo si y solo si la suma de las longitudes de cualesquiera dos lados es mayor que la longitud del tercer lado:
   - $x + y > 1$
   - $x + 1 > y \implies y < x + 1$
   - $y + 1 > x \implies y > x - 1$

3. **Cálculo del área de la región favorable:**
   Es más sencillo calcular el área de las regiones dentro del cuadrado donde **no** se cumplen estas desigualdades y restarla del área total:
   - **Región 1 ($x + y \le 1$):** Forma un triángulo rectángulo con vértices en $(0,0)$, $(1,0)$ y $(0,1)$. Su base y altura miden $1$, por lo que su área es:
     $$A_1 = \frac{1 \times 1}{2} = \frac{1}{2}$$
   - **Región 2 ($y \ge x + 1$):** Forma un triángulo rectángulo en la esquina superior izquierda con vértices en $(0,1)$, $(0,3)$ y $(2,3)$. Sus catetos miden $2$, por lo que su área es:
     $$A_2 = \frac{2 \times 2}{2} = 2$$
   - **Región 3 ($y \le x - 1$):** Por simetría con la Región 2, forma un triángulo rectángulo en la esquina inferior derecha con vértices en $(1,0)$, $(3,0)$ y $(3,2)$. Sus catetos miden $2$, por lo que su área es:
     $$A_3 = \frac{2 \times 2}{2} = 2$$

   Estas tres regiones no se superponen (solo se tocan en los puntos $(1,0)$ y $(0,1)$). Por lo tanto, el área excluida es:
   $$\text{Área excluida} = A_1 + A_2 + A_3 = \frac{1}{2} + 2 + 2 = \frac{9}{2}$$

   El área de la región favorable donde sí existe el triángulo es:
   $$\text{Área favorable} = 9 - \frac{9}{2} = \frac{9}{2}$$

4. **Probabilidad:**
   Dividiendo el área favorable entre el área total del cuadrado obtenemos:
   $$P = \frac{9/2}{9} = \frac{1}{2}$$

\boxed{\frac{1}{2}}