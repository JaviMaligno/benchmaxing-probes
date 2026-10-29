## Resolución

**Planteamiento geométrico.** La primera ecuación, $|20+15i-z|=13$, describe una circunferencia de centro $C=(20,15)$ y radio $13$.

La segunda ecuación, $|z-(12+k)|=|z-(k+5i)|$, dice que $z$ equidista de los puntos $A=(k+12,\,0)$ y $B=(k,\,5)$; es decir, $z$ está en la **mediatriz** del segmento $AB$ (una recta, ya que $A\neq B$ siempre).

El sistema tiene exactamente una solución cuando la recta es **tangente** a la circunferencia.

**Ecuación de la mediatriz.** 
- Punto medio: $M=\left(k+6,\ \tfrac{5}{2}\right)$.
- Pendiente de $AB$: $\dfrac{0-5}{(k+12)-k}=-\dfrac{5}{12}$, así que la mediatriz tiene pendiente $\dfrac{12}{5}$.

La recta: $y-\tfrac{5}{2}=\tfrac{12}{5}(x-k-6)$, que en forma general es
$$12x-5y-12k-\tfrac{119}{2}=0.$$

**Condición de tangencia.** La distancia de $C=(20,15)$ a la recta debe ser $13$:
$$\frac{\left|12(20)-5(15)-12k-\tfrac{119}{2}\right|}{\sqrt{12^2+5^2}}=13
\;\Longrightarrow\; \frac{\left|\tfrac{211}{2}-12k\right|}{13}=13.$$

Entonces $\left|\tfrac{211}{2}-12k\right|=169$, lo que da
$$12k=\frac{211}{2}\pm 169 \;\Longrightarrow\; k=\frac{549}{24}\quad\text{o}\quad k=-\frac{127}{24}.$$

**Suma de los valores posibles:**
$$\frac{549}{24}-\frac{127}{24}=\frac{422}{24}=\frac{211}{12}.$$

Como $211$ es primo, $\gcd(211,12)=1$, así que $m=211$, $n=12$ y $m+n=223$.

$$\boxed{223}$$