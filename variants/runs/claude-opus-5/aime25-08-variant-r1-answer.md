## Planteamiento

**Primera ecuación:** $|20+15i-z|=13$ es la circunferencia de centro $C=(20,15)$ y radio $13$.

**Segunda ecuación:** $|z-(k+12)|=|z-(k+5i)|$ es la mediatriz del segmento que une $A=(k+12,\,0)$ y $B=(k,\,5)$ (nunca coinciden, así que siempre es una recta).

## Ecuación de la recta

Con $z=x+iy$:
$$(x-k-12)^2+y^2=(x-k)^2+(y-5)^2$$

Desarrollando y cancelando $x^2,y^2,k^2$:
$$-24x+24k+144=-10y+25$$
$$-24x+10y+24k+119=0$$

## Condición de solución única

Una recta y una circunferencia tienen exactamente un punto común si y solo si son tangentes, es decir, si la distancia del centro a la recta es igual al radio:

$$\frac{|-24(20)+10(15)+24k+119|}{\sqrt{24^2+10^2}}=13$$

$$\frac{|24k-211|}{26}=13 \quad\Longrightarrow\quad |24k-211|=338$$

Esto da dos valores:
$$24k=211\pm338 \quad\Longrightarrow\quad k_1=\frac{549}{24},\qquad k_2=-\frac{127}{24}$$

## Suma

$$k_1+k_2=\frac{2\cdot 211}{24}=\frac{211}{12}$$

Como $\gcd(211,12)=1$ (211 es primo), se tiene $m=211$, $n=12$, luego $m+n=223$.

\boxed{223}