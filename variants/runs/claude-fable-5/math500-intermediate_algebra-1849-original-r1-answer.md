**Respuesta: 501.**

Razonamiento:

La ecuación $\log(kx)=2\log(x+2)$ exige $x+2>0$ (es decir, $x>-2$) y $kx>0$. Igualando argumentos: $kx=(x+2)^2$, o sea

$$x^2+(4-k)x+4=0.$$

El discriminante es $(4-k)^2-16=k(k-8)$.

**Caso $k<0$:** el discriminante $k(k-8)>0$, así que hay dos raíces reales. Su producto es $4>0$ y su suma es $k-4<0$, luego ambas son negativas (lo cual cumple $kx>0$). Evaluando el polinomio en $x=-2$: $f(-2)=4-2(4-k)+4=2k<0$, de modo que $x=-2$ queda entre las dos raíces: una raíz es menor que $-2$ (inválida) y la otra está en $(-2,0)$ (válida). Por tanto, cada $k\in\{-500,\dots,-1\}$ da exactamente una solución: **500 valores**.

**Caso $k=0$:** $\log(0)$ no está definido, sin soluciones.

**Caso $0<k<8$:** discriminante negativo, sin soluciones reales.

**Caso $k=8$:** raíz doble $x=\frac{k-4}{2}=2$, que cumple $x>-2$ y $kx=16>0$. Exactamente una solución: **1 valor**.

**Caso $k>8$:** dos raíces reales distintas con producto $4$ y suma $k-4>0$, ambas positivas y por tanto ambas válidas. Dos soluciones, no cuenta.

Total: $500+1=501$.

$$\boxed{501}$$