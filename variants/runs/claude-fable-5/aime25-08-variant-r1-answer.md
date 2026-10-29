Trabajemos el problema geométricamente.

**Primera ecuación:** $|20+15i-z|=13$ es una circunferencia con centro $(20,15)$ y radio $13$.

**Segunda ecuación:** $|z-(k+12)|=|z-(k+5i)|$ dice que $z$ equidista de los puntos $A=(k+12,\,0)$ y $B=(k,\,5)$, es decir, $z$ está en la mediatriz del segmento $AB$.

**Ecuación de la mediatriz:** con $z=x+yi$,
$$(x-(k+12))^2+y^2=(x-k)^2+(y-5)^2.$$
Expandiendo:
$$-2(k+12)x+(k+12)^2 = -2kx+k^2-10y+25,$$
$$-24x+24k+144=-10y+25,$$
$$24x-10y=24k+119.$$

**Condición de solución única:** la recta debe ser tangente a la circunferencia, así que la distancia del centro $(20,15)$ a la recta $24x-10y-(24k+119)=0$ debe valer $13$:
$$\frac{|24(20)-10(15)-24k-119|}{\sqrt{24^2+10^2}}=\frac{|480-150-24k-119|}{26}=\frac{|211-24k|}{26}=13.$$

Entonces $|211-24k|=338$, lo que da:
- $211-24k=338 \Rightarrow k=-\dfrac{127}{24}$,
- $211-24k=-338 \Rightarrow k=\dfrac{549}{24}$.

**Suma de los valores de $k$:**
$$\frac{549-127}{24}=\frac{422}{24}=\frac{211}{12}.$$

Como $\gcd(211,12)=1$, tenemos $m=211$, $n=12$, y $m+n=223$.

$$\boxed{223}$$