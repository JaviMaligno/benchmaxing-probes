Para que exista un triángulo con lados 1, $x$, $y$ deben cumplirse las tres desigualdades triangulares:

1. $x + y > 1$
2. $1 + x > y$, es decir, $y - x < 1$
3. $1 + y > x$, es decir, $x - y < 1$

Las condiciones 2 y 3 juntas equivalen a $|x - y| < 1$.

**Cálculo del área favorable** en el cuadrado $(0,3)\times(0,3)$, de área total $9$:

- La región $|x-y|<1$ es la banda entre las rectas $y = x-1$ e $y = x+1$. Fuera de ella quedan dos triángulos rectángulos con catetos de longitud $2$, cada uno de área $\frac{1}{2}\cdot 2\cdot 2 = 2$. El área de la banda es $9 - 2\cdot 2 = 5$.

- De esa banda hay que quitar la parte donde $x+y \le 1$. El triángulo $\{x+y<1,\ x>0,\ y>0\}$ tiene área $\frac{1}{2}$ y está completamente contenido en la banda (en él, $|x-y|<1$ siempre). Área favorable: $5 - \frac{1}{2} = \frac{9}{2}$.

**Probabilidad:**

$$P = \frac{9/2}{9} = \frac{1}{2}$$

$$\boxed{\dfrac{1}{2}}$$