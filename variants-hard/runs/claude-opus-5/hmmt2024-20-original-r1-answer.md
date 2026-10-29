Voy a verificar el razonamiento con un cálculo exhaustivo.

**Razonamiento**

Sea $M$ un peacock con $N=2M$ también peacock. Escribo $M=\overline{d_9d_8\cdots d_0}$.

*1) Acarreos.* Al duplicar, la posición $i$ produce acarreo si $2d_i+c_i\ge 10$, es decir si $d_i\ge 5$ (ya que $2\cdot4+1=9$ y $2\cdot5=10$): el acarreo saliente **no depende** del entrante. Hay exactamente cinco dígitos $\ge 5$, luego cinco acarreos. Como $N$ debe tener 10 cifras, no puede haber acarreo desde la posición 9: $d_9\in\{1,2,3,4\}$.

*2) Paridad.* El dígito de $N$ en la posición $i$ es $f(d_i)+c_i$ con $f(d)=2d\bmod 10\in\{0,2,4,6,8\}$ (sin desborde, pues $f+1\le 9$). Así el dígito de $N$ es **par** si no entra acarreo y **impar** si entra.

Sea $A$ el conjunto de posiciones sin acarreo entrante y $B$ con acarreo ($|A|=|B|=5$). Para que $N$ sea pandigital hacen falta $\{0,2,4,6,8\}$ entre las de $A$ y $\{1,3,5,7,9\}$ entre las de $B$; en ambos casos los $f(d_i)$ deben recorrer $\{0,2,4,6,8\}$. Como $f(k)=f(k+5)$, la condición es:

> para cada pareja $\{k,k+5\}$, $k=0,\dots,4$, uno de los dos dígitos ocupa posición de $A$ y el otro de $B$.

*3) Conteo.* Si $T$ es el conjunto de posiciones de los dígitos grandes ($9\notin T$, $T\subseteq\{0,\dots,8\}$, $|T|=5$), entonces $B=T+1$. Con $j=|T\cap(T+1)|$ = número de adyacencias de $T$, las colocaciones válidas son $\binom5j\,j!\,j!\,(5-j)!\,(5-j)! = 120\cdot j!\,(5-j)!$.

Si $T$ tiene $b$ bloques, $j=5-b$, y hay $\binom{4}{b-1}\binom5b$ tales $T$:

| $b$ | $j$ | #$T$ | $j!(5-j)!$ | producto |
|---|---|---|---|---|
|1|4|5|24|120|
|2|3|40|12|480|
|3|2|60|12|720|
|4|1|20|24|480|
|5|0|1|120|120|

Suma $=1920$, y el total es $120\cdot1920=230400$.

*4) Quitar $d_9=0$.* La posición 9 siempre lleva un dígito pequeño, y toda la construcción es simétrica bajo permutar las cinco parejas $\{k,k+5\}$; por tanto cada dígito pequeño ocupa la posición 9 en $1/5$ de los casos. Luego

$$230400\cdot\tfrac45=184320.$$