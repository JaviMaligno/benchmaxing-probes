## Planteamiento

Las feathers se vuelven naranjas el día en que el total alcanza por primera vez $\ge 8$. En ese mismo día no se enferma si y solo si el total es **exactamente 8** (si fuera 9, se enferma ese mismo día).

Como los pasos son de $1$ o $2$, el único modo de "saltarse" el 8 es estar en 7 y comer 2 peces. Por tanto necesitamos $p_8=P(\text{el total pasa exactamente por } 8)$.

## Recurrencia

Sea $p_n$ la probabilidad de que la suma acumulada tome el valor $n$. Se llega a $n$ desde $n-1$ (comiendo 1, prob. $2/3$) o desde $n-2$ (comiendo 2, prob. $1/3$):

$$p_n=\tfrac23 p_{n-1}+\tfrac13 p_{n-2},\qquad p_0=1,\; p_1=\tfrac23$$

$$p_2=\tfrac79,\quad p_3=\tfrac{20}{27},\quad p_4=\tfrac{61}{81},\quad p_5=\tfrac{182}{243},\quad p_6=\tfrac{547}{729},\quad p_7=\tfrac{1640}{2187}$$

En forma cerrada: $p_n=\dfrac{3^{n+1}+(-1)^n}{4\cdot 3^{n}}$.

## Resultado

$$p_8=1-\tfrac13 p_7=1-\frac{1640}{6561}=\frac{4921}{6561}$$

que coincide con la fórmula: $\dfrac{3^9+1}{4\cdot 3^8}=\dfrac{19684}{26244}=\dfrac{4921}{6561}$.

$$\boxed{\dfrac{4921}{6561}}$$