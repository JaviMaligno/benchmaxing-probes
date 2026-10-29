**Planteamiento geométrico.** La primera ecuación, $|25+20i-z|=5$, describe una circunferencia de centro $(25,20)$ y radio $5$. La segunda, $|z-(4+k)|=|z-(k+3i)|$, dice que $z$ equidista de los puntos $A=(4+k,\,0)$ y $B=(k,\,3)$, es decir, $z$ está en la mediatriz del segmento $AB$ (es una recta genuina porque $A\neq B$ siempre). Para que haya exactamente una solución, la recta debe ser **tangente** a la circunferencia.

**Ecuación de la recta.** Igualando distancias al cuadrado:
$$(x-(4+k))^2+y^2=(x-k)^2+(y-3)^2$$
$$-2(4+k)x+(4+k)^2 = -2kx+k^2-6y+9$$
$$-8x+16+8k=-6y+9 \;\Longrightarrow\; 8x-6y-(7+8k)=0.$$

**Condición de tangencia.** La distancia del centro $(25,20)$ a la recta debe ser $5$:
$$\frac{|8(25)-6(20)-(7+8k)|}{\sqrt{8^2+6^2}}=\frac{|200-120-7-8k|}{10}=\frac{|73-8k|}{10}=5.$$

Entonces $|73-8k|=50$, lo que da $8k=123$ o $8k=23$, es decir $k=\tfrac{123}{8}$ o $k=\tfrac{23}{8}$.

**Suma de valores.** 
$$\frac{123}{8}+\frac{23}{8}=\frac{146}{8}=\frac{73}{4},$$
con $m=73$, $n=4$ coprimos, así que $m+n=77$.

$$\boxed{77}$$