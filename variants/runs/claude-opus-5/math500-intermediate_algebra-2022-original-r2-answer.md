## Razonamiento

Por la desigualdad de Cauchy–Schwarz aplicada a los vectores $(\sqrt{a_i})$ y $(a_i^{3/2})$:

$$\left(\sum a_i^2\right)^2 = \left(\sum \sqrt{a_i}\cdot a_i^{3/2}\right)^2 \le \left(\sum a_i\right)\left(\sum a_i^3\right)$$

Sustituyendo los datos:

$$144^2 = 20736, \qquad 96 \cdot 216 = 20736.$$

Se cumple la **igualdad**, lo que obliga a que los vectores sean proporcionales: $a_i^{3/2} = c\sqrt{a_i}$, es decir, $a_i = c$ para todo $i$ (todos los términos son iguales).

Entonces $nc = 96$ y $nc^2 = 144$, de donde $c = \tfrac{144}{96} = \tfrac{3}{2}$ y $n = \tfrac{96}{3/2} = 64$.

Verificación: $\sum a_i^3 = 64\left(\tfrac{3}{2}\right)^3 = 64 \cdot \tfrac{27}{8} = 216$. ✓

El único valor posible es $n = 64$.

\boxed{64}