## Resolución

**Paso 1: Descomponer f.** Observamos que
$$f(x) = x^4 - 4x^2 + 2 = (x^2-2)^2 - 2 = g(g(x)), \quad \text{donde } g(x) = x^2 - 2.$$
Por tanto $f^k = g^{2k}$ (iteración $2k$ veces de $g$).

**Paso 2: Forma cerrada de la iteración.** El argumento es $\frac{n^2+1}{n} = n + \frac{1}{n}$. La función $g$ tiene la propiedad clave: si $x = t + \frac{1}{t}$, entonces $g(x) = t^2 + \frac{1}{t^2}$. Iterando:
$$g^m\!\left(n + \tfrac{1}{n}\right) = n^{2^m} + n^{-2^m} \;\Longrightarrow\; f^k\!\left(n + \tfrac{1}{n}\right) = n^{4^k} + \frac{1}{n^{4^k}}.$$

**Paso 3: Condición de cercanía.** Para $n \ge 2$, el valor $f^k(\cdot) = N + \varepsilon$ donde $N = n^{4^k} \in \mathbb{N}$ y $\varepsilon = 1/n^{4^k}$. Como $c^{144}$ es entero, la distancia mínima a un entero se logra solo si $c^{144} = n^{4^k}$ exactamente, y entonces la diferencia es $\varepsilon = 1/n^{4^k} < \frac{1}{100}$, lo cual se cumple en cuanto $n^{4^k} > 100$.

(Para $n = 1$: el valor es $2$, punto fijo de $f$, y $|2 - c^{144}| \ge 1$ para todo $c$; falla.)

**Paso 4: ¿Cuándo es $n^{4^k}$ una potencia 144-ésima?** Sea $n = \prod p_i^{e_i}$. Necesitamos $144 \mid e_i \cdot 4^k$ para todo $i$, con $144 = 2^4 \cdot 3^2$. El factor $4^k = 2^{2k}$ aporta toda la parte de potencia de 2 (basta $k \ge 2$), pero **no aporta ningún factor 3**. Por tanto es necesario y suficiente que $9 \mid e_i$ para todo $i$, es decir, que $n$ sea una potencia novena perfecta.

**Paso 5: Mínimo.** La menor potencia novena mayor que 1 es $n = 2^9 = 512$. Verificación: con $k = 2$,
$$f^2\!\left(\tfrac{512^2+1}{512}\right) = 512^{16} + 512^{-16} = 2^{144} + 2^{-144},$$
y tomando $c = 2$: $\left|2^{144} + 2^{-144} - 2^{144}\right| = 2^{-144} < \frac{1}{100}$. ✓

$$\boxed{512}$$