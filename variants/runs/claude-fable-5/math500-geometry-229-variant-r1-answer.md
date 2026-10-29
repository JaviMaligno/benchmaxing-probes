## Solución

**Planteamiento de las áreas.** Las rectas $y=px+r$ y $y=qx+r$ se cortan en $(0,r)$, y las rectas $y=px+s$ y $y=qx+s$ se cortan en $(0,s)$. Los otros dos vértices del primer paralelogramo se obtienen al igualar $px+r=qx+s$, es decir en $x=\pm\frac{s-r}{p-q}$.

Tomando como base el segmento vertical de $(0,r)$ a $(0,s)$, de longitud $|s-r|$, y como altura la distancia horizontal $\left|\frac{s-r}{p-q}\right|$, el área del primer paralelogramo es:

$$\frac{(s-r)^2}{|p-q|} = 8.$$

Para el segundo paralelogramo, las ordenadas al origen son $r$ y $-s$, así que por el mismo argumento:

$$\frac{(r+s)^2}{|p-q|} = 50.$$

**Resolver el sistema.** Dividiendo las dos ecuaciones:

$$\frac{(r+s)^2}{(s-r)^2} = \frac{50}{8} = \frac{25}{4} \quad\Longrightarrow\quad \frac{r+s}{s-r} = \frac{5}{2}.$$

(Se toma el signo positivo, pues ambas cantidades deben ser positivas.) Entonces $2(r+s)=5(s-r)$, lo que da $7r = 3s$. Como $r$ y $s$ son enteros positivos, $r = 3k$ y $s = 7k$ para algún entero $k \ge 1$.

Sustituyendo en la primera ecuación: $(s-r)^2 = (4k)^2 = 16k^2 = 8|p-q|$, de donde $|p-q| = 2k^2$.

**Minimizar.** Con $k=1$: $r=3$, $s=7$ y $|p-q|=2$. Los menores enteros positivos con diferencia 2 son $p=1$, $q=3$ (o viceversa), con suma $p+q=4$.

Verificación: $\frac{(7-3)^2}{2} = \frac{16}{2} = 8$ ✓ y $\frac{(7+3)^2}{2} = \frac{100}{2} = 50$ ✓.

Por lo tanto, el valor mínimo es $1+3+3+7 = 14$.

$$\boxed{14}$$