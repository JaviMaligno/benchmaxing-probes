## Planteamiento

**Paso 1: Una identidad clave para $g$.**

Si $x = t + t^{-1}$ con $t \neq 0$, entonces expandiendo:
$$(t+t^{-1})^3 - 3(t+t^{-1}) = \big(t^3 + 3t + 3t^{-1} + t^{-3}\big) - \big(3t + 3t^{-1}\big) = t^3 + t^{-3}.$$

Es decir, $g(t+t^{-1}) = t^3 + t^{-3}$, y por inducción:
$$g^{k}\big(t+t^{-1}\big) = t^{3^{k}} + t^{-3^{k}} \quad \text{para todo } k \ge 0.$$

**Paso 2: Aplicarla al argumento del problema.**

Como $\dfrac{n^{2}+1}{n} = n + \dfrac{1}{n}$, tomando $t = n$ obtenemos:
$$g^{k}\!\left(\frac{n^{2}+1}{n}\right) = n^{3^{k}} + n^{-3^{k}}.$$

**Paso 3: Reducir la desigualdad a una igualdad exacta.**

Supongamos $n \ge 2$ y $k \ge 1$. Tanto $n^{3^{k}}$ como $c^{72}$ son enteros; si fuesen distintos, su diferencia sería de módulo $\ge 1$ en valor absoluto, y como $0 < n^{-3^{k}} \le 2^{-3} = \tfrac18$, resultaría
$$\big|n^{3^{k}} + n^{-3^{k}} - c^{72}\big| \ge 1 - \tfrac18 = \tfrac78 > \tfrac{1}{100}.$$

Por tanto **es necesario** que $n^{3^{k}} = c^{72}$, y en ese caso la condición es simplemente
$$n^{-3^{k}} < \frac{1}{100}, \quad \text{es decir} \quad n^{3^{k}} > 100,$$
lo cual se cumple de sobra para cualquier candidato razonable.

(Para $n = 1$: $g^{k}(2) = 2$ para todo $k$, y $|2 - c^{72}| \ge 1$ siempre; no funciona.)

**Paso 4: ¿Qué $n$ cumplen $n^{3^{k}} = c^{72}$?**

Escribamos $n = \prod p_i^{a_i}$. La igualdad $n^{3^{k}} = c^{72}$ exige que cada exponente satisfaga $72 \mid 3^{k} a_i$ (y es además suficiente, con $c = \prod p_i^{3^k a_i/72}$):

- **$k = 1$:** se necesita $24 \mid a_i$, así que $n \ge 2^{24}$.
- **$k \ge 2$:** como $9 \mid 3^{k}$, la condición $72 \mid 3^{k}a_i$ equivale a $8 \mid a_i$; es decir, $n$ debe ser una **octava potencia**, y el mínimo es $n = 2^{8} = 256$.

(Si se admitiera $k = 0$, haría falta $n = c^{72} > 100$, todavía mayor.)

**Paso 5: Verificar $n = 256$ y la minimalidad.**

Con $n = 256 = 2^{8}$, $k = 2$, $c = 2$:
$$g^{2}\!\left(256 + \tfrac{1}{256}\right) = 256^{9} + 256^{-9} = 2^{72} + 2^{-72},$$
$$\big|2^{72} + 2^{-72} - 2^{72}\big| = 2^{-72} \approx 2{,}1\times 10^{-22} < \frac{1}{100}. \checkmark$$

Todo $n \ge 2$ que funciona debe ser una octava potencia (o una $24$-ésima potencia si $k=1$), luego ningún $n < 256$ sirve.

$$\boxed{256}$$