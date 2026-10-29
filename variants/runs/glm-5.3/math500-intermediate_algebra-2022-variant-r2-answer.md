**Paso 1: Buscar una combinación nula de las sumas.**

Como $\sum b_i^2 / \sum b_i = 144/108 = 4/3$ y $\sum b_i^3 / \sum b_i^2 = 192/144 = 4/3$, sospechamos que todos los $b_i$ valen $4/3$. Para probarlo, expandimos:

$$\sum_{i=1}^n b_i\left(b_i - \tfrac{4}{3}\right)^2 = \sum b_i^3 - \tfrac{8}{3}\sum b_i^2 + \tfrac{16}{9}\sum b_i$$

**Paso 2: Sustituir los valores dados.**

$$= 192 - \tfrac{8}{3}(144) + \tfrac{16}{9}(108) = 192 - 384 + 192 = 0$$

**Paso 3: Concluir que todos los $b_i$ son iguales.**

Cada término $b_i(b_i - \tfrac{4}{3})^2$ es $\ge 0$ porque $b_i > 0$. Una suma de términos no negativos que vale $0$ obliga a que cada término sea $0$, así que $b_i = \tfrac{4}{3}$ para todo $i$.

**Paso 4: Determinar $n$ y verificar.**

De $\sum b_i = 108$:

$$n \cdot \tfrac{4}{3} = 108 \implies n = 81$$

Verificación: $81 \cdot \tfrac{16}{9} = 144$ ✓ y $81 \cdot \tfrac{64}{27} = 192$ ✓.

El único valor posible de $n$ es $81$, y la suma de todos los valores posibles es:

$$\boxed{81}$$