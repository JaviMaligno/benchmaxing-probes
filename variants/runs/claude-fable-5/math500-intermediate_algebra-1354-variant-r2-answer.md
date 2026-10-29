Analicemos la suma usando que $z^{2027} = 1$ y $z \neq 1$.

**Paso 1: El último término.** Como $z^{2027} = 1$, el término final es
$$\frac{1}{1 + z^{2027}} = \frac{1}{1+1} = \frac{1}{2}.$$

**Paso 2: Emparejar los términos restantes.** Como 2027 es primo y $z \neq 1$, el orden de $z$ es exactamente 2027, así que $z^k \neq -1$ para todo $k$ (ningún denominador se anula). Para $k = 1, \dots, 2026$, emparejamos el término $k$ con el término $2027 - k$. Usando $z^{2027-k} = z^{-k}$:

$$\frac{1}{1 + z^k} + \frac{1}{1 + z^{-k}} = \frac{1}{1 + z^k} + \frac{z^k}{z^k + 1} = \frac{1 + z^k}{1 + z^k} = 1.$$

**Paso 3: Contar los pares.** Los índices $1, \dots, 2026$ forman $\frac{2026}{2} = 1013$ pares (los pares $(k, 2027-k)$ son disjuntos porque $k \neq 2027 - k$, al ser 2027 impar), y cada par aporta 1.

**Total:**
$$1013 + \frac{1}{2} = \frac{2027}{2}.$$

$$\boxed{\dfrac{2027}{2}}$$