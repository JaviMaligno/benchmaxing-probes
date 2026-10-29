## Solución

Busco la suma sobre todas las ternas $(a,b,c)$ de enteros positivos que satisfacen las desigualdades triangulares.

**Cambio de variables.** Defino $x = b+c-a$, $y = a+c-b$, $z = a+b-c$. Las desigualdades triangulares equivalen a $x, y, z > 0$. Invirtiendo:
$$a = \frac{y+z}{2}, \quad b = \frac{x+z}{2}, \quad c = \frac{x+y}{2}.$$
Para que $a,b,c$ sean enteros, $x, y, z$ deben tener **la misma paridad** (y cualquier terna así da una terna válida).

**Reescritura del término.**
$$\frac{2^a}{3^b 5^c} = 2^{(y+z)/2} \cdot 3^{-(x+z)/2} \cdot 5^{-(x+y)/2} = \left(\tfrac{1}{15}\right)^{x/2} \left(\tfrac{2}{5}\right)^{y/2} \left(\tfrac{2}{3}\right)^{z/2}.$$

Sea $p = \tfrac{1}{15}$, $q = \tfrac{2}{5}$, $r = \tfrac{2}{3}$.

**Caso 1: todos pares.** Con $x=2i, y=2j, z=2k$, $i,j,k \ge 1$:
$$\frac{p}{1-p}\cdot\frac{q}{1-q}\cdot\frac{r}{1-r} = \frac{1/15}{14/15}\cdot\frac{2/5}{3/5}\cdot\frac{2/3}{1/3} = \frac{1}{14}\cdot\frac{2}{3}\cdot 2 = \frac{2}{21}.$$

**Caso 2: todos impares.** Con $x=2i+1$, etc., $i,j,k \ge 0$:
$$\sqrt{pqr}\cdot\frac{1}{(1-p)(1-q)(1-r)} = \sqrt{\tfrac{4}{225}} \cdot \frac{1}{\tfrac{14}{15}\cdot\tfrac{3}{5}\cdot\tfrac{1}{3}} = \frac{2}{15}\cdot\frac{75}{14} = \frac{5}{7}.$$

**Total:**
$$\frac{2}{21} + \frac{5}{7} = \frac{2}{21} + \frac{15}{21} = \frac{17}{21}.$$

$$\boxed{\dfrac{17}{21}}$$