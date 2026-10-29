Para determinar la probabilidad de que exista un triángulo con lados de longitud $1$, $x$ e $y$, donde $x$ e $y$ se eligen al azar en el intervalo $(0,3)$, podemos utilizar probabilidad geométrica.

**Paso 1: Definir el espacio muestral**
Como $x \in (0,3)$ e $y \in (0,3)$, el espacio muestral corresponde a un cuadrado en el plano cartesiano con vértices en $(0,0)$, $(3,0)$, $(3,3)$ y $(0,3)$. El área total de este cuadrado es:
$$\text{Área total} = 3 \times 3 = 9$$

**Paso 2: Aplicar la desigualdad triangular**
Para que tres segmentos de longitudes $1$, $x$ e $y$ formen un triángulo, deben cumplir las tres desigualdades triangulares:
1. $x + y > 1$
2. $x + 1 > y \implies y < x + 1$
3. $y + 1 > x \implies y > x - 1$

**Paso 3: Calcular el área de la región favorable**
Es más sencillo calcular el área de las regiones dentro del cuadrado donde **no** se cumplen estas desigualdades (las cuales son mutuamente excluyentes para $x, y > 0$) y restarlas del área total:

1. **Región donde $x + y \le 1$:** Forma un triángulo rectángulo con vértices en $(0,0)$, $(1,0)$ y $(0,1)$.
   $$\text{Área}_1 = \frac{1 \times 1}{2} = \frac{1}{2}$$

2. **Región donde $y \ge x + 1$:** Forma un triángulo rectángulo con vértices en $(0,1)$, $(0,3)$ y $(2,3)$. Sus catetos miden $2$ unidades cada uno.
   $$\text{Área}_2 = \frac{2 \times 2}{2} = 2$$

3. **Región donde $y \le x - 1$:** Forma un triángulo rectángulo con vértices en $(1,0)$, $(3,0)$ y $(3,2)$. Sus catetos también miden $2$ unidades cada uno.
   $$\text{Área}_3 = \frac{2 \times 2}{2} = 2$$

Sumando las áreas no favorables:
$$\text{Área no favorable} = \frac{1}{2} + 2 + 2 = \frac{9}{2}$$

Por lo tanto, el área de la región favorable donde el triángulo existe es:
$$\text{Área favorable} = 9 - \frac{9}{2} = \frac{9}{2}$$

**Paso 4: Calcular la probabilidad**
Dividiendo el área favorable entre el área total del cuadrado:
$$P = \frac{\frac{9}{2}}{9} = \frac{1}{2}$$

\boxed{\frac{1}{2}}