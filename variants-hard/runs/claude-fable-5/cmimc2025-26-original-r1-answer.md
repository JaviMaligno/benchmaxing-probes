Coloco $X$ en el origen con los ejes a lo largo de las tres cuerdas, y $O=(p,q,r)$ con $p^2+q^2+r^2 = OX^2 = \tfrac12$.

**Condiciones de la esfera.** Con $A=(\varepsilon_1,0,0)$, $C=(0,\varepsilon_2\sqrt2,0)$, $E=(0,0,2\varepsilon_3)$ (signos $\varepsilon_i=\pm1$), la condición $|OA|=|OC|=|OE|=R$ da, usando $p^2+q^2+r^2=\tfrac12$:

$$R^2 = \tfrac32 - 2\varepsilon_1 p = \tfrac52 - 2\sqrt2\,\varepsilon_2 q = \tfrac92 - 4\varepsilon_3 r.$$

Escribiendo $t=R^2$, esto determina los cuadrados sin importar los signos:

$$p^2=\frac{(t-\tfrac32)^2}{4},\qquad q^2=\frac{(t-\tfrac52)^2}{8},\qquad r^2=\frac{(t-\tfrac92)^2}{16}.$$

**Ecuación para $t$.** Sustituyendo en $p^2+q^2+r^2=\tfrac12$ y multiplicando por 16:

$$4\left(t-\tfrac32\right)^2+2\left(t-\tfrac52\right)^2+\left(t-\tfrac92\right)^2=8,$$

que se expande a $7t^2-31t+\tfrac{135}{4}=0$, es decir $28t^2-124t+135=0$.

El discriminante es $124^2-4\cdot28\cdot135=256>0$, con raíces $t=\tfrac{140}{56}=\tfrac52$ y $t=\tfrac{108}{56}=\tfrac{27}{14}$. Ambas cumplen $t>\tfrac12$ (es decir, $X$ queda dentro de la esfera) y producen valores reales de $p,q,r$ consistentes (por ejemplo, para $t=\tfrac{27}{14}$: $p^2+q^2+r^2=\tfrac{9+8+81}{196}=\tfrac12$ ✓), así que ambas configuraciones existen.

Suma de los valores posibles: $\tfrac52+\tfrac{27}{14}=\tfrac{62}{14}=\tfrac{31}{7}$.

$$\boxed{\dfrac{31}{7}}$$