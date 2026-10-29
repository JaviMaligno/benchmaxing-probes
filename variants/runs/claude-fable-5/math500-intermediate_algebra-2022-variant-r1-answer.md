Por la desigualdad de Cauchy-Schwarz aplicada a los vectores $(\sqrt{b_i})$ y $(\sqrt{b_i^3})$:

$$\left(\sum b_i^2\right)^2 \le \left(\sum b_i\right)\left(\sum b_i^3\right)$$

Comprobamos con los datos: $144^2 = 20736$ y $108 \cdot 192 = 20736$. Se cumple la **igualdad**, lo que fuerza que $\sqrt{b_i^3}/\sqrt{b_i} = b_i$ sea constante, es decir, todos los $b_i$ son iguales a un valor $c > 0$.

Entonces:
- $nc = 108$
- $nc^2 = 144 \Rightarrow c = \dfrac{144}{108} = \dfrac{4}{3}$
- $n = \dfrac{108}{4/3} = 81$

Verificación con los cubos: $nc^3 = 81 \cdot \dfrac{64}{27} = 192$ ✓.

El único valor posible es $n = 81$, así que la suma de todos los valores posibles es:

$$\boxed{81}$$