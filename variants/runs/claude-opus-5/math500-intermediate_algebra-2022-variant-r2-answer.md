## Razonamiento

**Paso 1: Aplicar Cauchy–Schwarz sobre las sucesiones $(b_i^{1/2})$ y $(b_i^{3/2})$.**

$$\left(\sum_{i=1}^n b_i^{1/2}\cdot b_i^{3/2}\right)^2 \le \left(\sum_{i=1}^n b_i\right)\left(\sum_{i=1}^n b_i^3\right)$$

El lado izquierdo es $\left(\sum b_i^2\right)^2 = 144^2 = 20736$, y el lado derecho vale $108 \cdot 192 = 20736$.

**Paso 2: Se da la igualdad.**

Como hay igualdad en Cauchy–Schwarz, los vectores son proporcionales: existe $c$ con $b_i^{3/2} = c\, b_i^{1/2}$ para todo $i$, y al ser $b_i > 0$ esto da $b_i = c$ para todo $i$. Es decir, todos los términos son iguales.

**Paso 3: Determinar $n$.**

De $nc = 108$ y $nc^2 = 144$ se obtiene $c = \frac{144}{108} = \frac{4}{3}$, y por tanto
$$n = \frac{108}{4/3} = 81.$$

**Verificación:** $\sum b_i = 81\cdot\frac43 = 108$; $\sum b_i^2 = 81\cdot\frac{16}{9} = 144$; $\sum b_i^3 = 81\cdot\frac{64}{27} = 192$. ✓

El único valor posible es $n = 81$, así que la suma de todos los valores posibles es $81$.

\boxed{81}