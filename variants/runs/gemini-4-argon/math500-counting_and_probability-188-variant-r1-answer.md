Para que exista un triángulo con lados de longitudes $2$, $a$ y $b$, estos valores deben satisfacer las desigualdades triangulares:

1. $a + b > 2$
2. $a + 2 > b \implies b < a + 2$
3. $b + 2 > a \implies b > a - 2$

Como $a$ y $b$ se eligen de forma independiente y uniforme en el intervalo $(0, 4)$, el espacio muestral se puede representar como un cuadrado en el plano cartesiano $(a, b)$ con vértices en $(0,0)$, $(4,0)$, $(4,4)$ y $(0,4)$. El área total de este cuadrado es:
$$\text{Área total} = 4 \times 4 = 16$$

Es más sencillo calcular el área de las regiones donde **no** se cumplen las desigualdades (el complemento) dentro del cuadrado:

1. **Cuando $a + b \le 2$:** Esta región forma un triángulo rectángulo en la esquina inferior izquierda con vértices en $(0,0)$, $(2,0)$ y $(0,2)$. Su área es:
   $$\text{Área}_1 = \frac{2 \times 2}{2} = 2$$

2. **Cuando $b \ge a + 2$:** Esta región forma un triángulo rectángulo en la esquina superior izquierda con vértices en $(0,2)$, $(0,4)$ y $(2,4)$. Su área es:
   $$\text{Área}_2 = \frac{2 \times 2}{2} = 2$$

3. **Cuando $b \le a - 2$:** Esta región forma un triángulo rectángulo en la esquina inferior derecha con vértices en $(2,0)$, $(4,0)$ y $(4,2)$. Su área es:
   $$\text{Área}_3 = \frac{2 \times 2}{2} = 2$$

Estas tres regiones no se superponen (solo se tocan en puntos de la frontera). Por lo tanto, el área favorable donde sí se puede formar un triángulo es el área del cuadrado menos las tres áreas excluidas:
$$\text{Área favorable} = 16 - (2 + 2 + 2) = 10$$

La probabilidad buscada es el cociente entre el área favorable y el área total:
$$P = \frac{10}{16} = \frac{5}{8}$$

\boxed{\frac{5}{8}}