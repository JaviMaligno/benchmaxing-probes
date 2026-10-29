**Planteamiento.** Las plumas se vuelven naranjas el primer día en que el total es ≥ 8. Ese día Coral no enferma si y solo si el total es exactamente 8 (y no 9). Como cada día come 1 o 2 peces, el total alcanza exactamente 8 si y solo si la suma acumulada "pisa" el valor 8 en algún momento (en vez de saltar de 7 a 9).

**Recurrencia.** Sea $p_n$ la probabilidad de que la suma acumulada visite exactamente el valor $n$. Condicionando en el último paso (de $n-1$ con un pez, o de $n-2$ con dos peces):

$$p_n = \tfrac{2}{3}p_{n-1} + \tfrac{1}{3}p_{n-2}, \qquad p_0 = 1,\; p_1 = \tfrac{2}{3}.$$

**Cálculo.** La ecuación característica $x^2 = \tfrac{2}{3}x + \tfrac{1}{3}$ tiene raíces $1$ y $-\tfrac{1}{3}$, así que

$$p_n = \tfrac{3}{4} + \tfrac{1}{4}\left(-\tfrac{1}{3}\right)^n.$$

(Se verifica: $p_0 = 1$, $p_1 = \tfrac{3}{4} - \tfrac{1}{12} = \tfrac{2}{3}$.)

Para $n = 8$:

$$p_8 = \frac{3}{4} + \frac{1}{4}\cdot\frac{1}{3^8} = \frac{3\cdot 6561 + 1}{4\cdot 6561} = \frac{19684}{26244} = \frac{4921}{6561}.$$

También se puede comprobar iterando la recurrencia: $p_2=\tfrac{7}{9}$, $p_3=\tfrac{20}{27}$, $p_4=\tfrac{61}{81}$, $p_5=\tfrac{182}{243}$, $p_6=\tfrac{547}{729}$, $p_7=\tfrac{1640}{2187}$, $p_8=\tfrac{4921}{6561}$.

$$\boxed{\dfrac{4921}{6561}}$$