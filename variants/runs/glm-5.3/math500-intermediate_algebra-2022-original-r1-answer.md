Razono paso a paso.

**Paso 1: Acotar $n$ con Cauchy–Schwarz.**
Aplicando Cauchy–Schwarz a los vectores $(a_i)$ y $(1,\dots,1)$:
$$(\sum a_i)^2 \le n \sum a_i^2 \implies 96^2 \le n\cdot 144 \implies n \ge \frac{9216}{144}=64.$$

**Paso 2: Verificar la igualdad.**
Aplicando Cauchy–Schwarz a los vectores $(\sqrt{a_i})$ y $(a_i^{3/2})$:
$$\Big(\sum a_i^2\Big)^2 \le \Big(\sum a_i\Big)\Big(\sum a_i^3\Big).$$
Comprobando con los datos: $144^2 = 20736$ y $96\cdot 216 = 20736$. Hay **igualdad**, y la condición de igualdad en Cauchy–Schwarz obliga a que todos los $a_i$ sean iguales: $a_1=\dots=a_n=a$.

**Paso 3: Resolver para $a$ y $n$.**
De $\sum a_i = 96$ y $\sum a_i^2 = 144$: $na=96$ y $na^2=144$, así que
$$a=\frac{144}{96}=\frac32,\qquad n=\frac{96}{3/2}=64.$$
Verificación con la tercera condición: $64\cdot\left(\frac32\right)^3 = 64\cdot\frac{27}{8}=216$. ✓ (Y coincide con el paso 1: $64\cdot 144=9216=96^2$.)

**Paso 4: Conclusión.**
El único valor posible de $n$ es $64$, así que la suma de todos los valores posibles es $64$.

$$\boxed{64}$$