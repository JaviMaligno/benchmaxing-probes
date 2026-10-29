## Planteamiento

Sea $S = \zeta^a + \zeta^b + \zeta^c + \zeta^d$ con $\zeta = e^{2\pi i/13}$. Entonces

$$|S|^2 = S\bar S = 4 + \sum_{i\neq j}\zeta^{e_i - e_j} = 3 \quad\Longrightarrow\quad \sum_{i\neq j}\zeta^{e_i-e_j} = -1.$$

Como $\sum_{k=1}^{12}\zeta^k = -1$ y las 12 diferencias ordenadas $e_i - e_j$ (con $i\neq j$) son exactamente 12 exponentes, la igualdad fuerza que esas 12 diferencias cubran **cada residuo no nulo módulo 13 exactamente una vez**. Es decir, $\{a,b,c,d\}$ debe ser, módulo 13, un **conjunto de diferencias perfecto** (el plano proyectivo de orden 3), como $\{0,1,3,9\}$.

## Minimización

Todos estos conjuntos son de la forma $m\cdot\{0,1,3,9\} + t \pmod{13}$ con $m$ invertible.

**Cota inferior para $a$:** si el rango es $r = \max - \min$, las diferencias caen en $\pm\{1,\dots,r\}$, que tiene $2r$ valores; necesitamos 12 diferencias distintas, así que $r \ge 6$. Con $d \ge 1$, resulta $a \ge 7$.

**Conjuntos con rango 6** (normalizados a mínimo 0): verificando los múltiplos y traslaciones, solo existen
- $\{0,1,4,6\}$: diferencias $\pm\{1,4,6,3,5,2\}$ ✓
- $\{0,2,5,6\}$: diferencias $\pm\{2,5,6,3,4,1\}$ ✓

Trasladando a enteros positivos mínimos ($+1$):
- $\{1,2,5,7\}$: da $1000(7)+100(5)+10(2)+1 = 7521$
- $\{1,3,6,7\}$: da $7631$

Con $a=7$ el mínimo se obtiene con $b=5$, $c=2$, $d=1$. Comprobación rápida: para $\{1,2,5,7\}$ las diferencias son $\pm 1, \pm 3, \pm 4, \pm 6, \pm 5, \pm 2$, que cubren todos los residuos no nulos módulo 13, de modo que $|S|^2 = 4 - 1 = 3$. ✓

$$\boxed{7521}$$