Para calcular la suma
\[S = \frac{1}{1 + z} + \frac{1}{1 + z^2} + \frac{1}{1 + z^3} + \dots + \frac{1}{1 + z^{2027}},\]
observamos primero que como $z^{2027} = 1$ y $2027$ es impar, ningún término tiene denominador cero (pues si $z^k = -1$, tendríamos $1 = (z^{2027})^k = (z^k)^{2027} = (-1)^{2027} = -1$, lo cual es una contradicción).

1. **Evaluamos el último término ($k = 2027$):**
   Dado que $z^{2027} = 1$, el último término de la suma es:
   \[\frac{1}{1 + z^{2027}} = \frac{1}{1 + 1} = \frac{1}{2}.\]

2. **Agrupamos los primeros $2026$ términos en parejas:**
   Para cualquier $k \in \{1, 2, \dots, 2026\}$, podemos usar que $z^{2027 - k} = z^{2027} z^{-k} = z^{-k}$. Al sumar el término correspondiente a $k$ con el correspondiente a $2027 - k$, obtenemos:
   \[\frac{1}{1 + z^k} + \frac{1}{1 + z^{2027 - k}} = \frac{1}{1 + z^k} + \frac{1}{1 + z^{-k}} = \frac{1}{1 + z^k} + \frac{z^k}{z^k + 1} = \frac{1 + z^k}{1 + z^k} = 1.\]

3. **Sumamos todas las parejas y el término final:**
   Los términos desde $k = 1$ hasta $k = 2026$ forman exactamente $\frac{2026}{2} = 1013$ parejas ($k=1$ con $k=2026$, $k=2$ con $k=2025$, ..., hasta $k=1013$ con $k=1014$), y cada pareja suma $1$.

   Por lo tanto, la suma total es:
   \[S = 1013 \cdot 1 + \frac{1}{2} = \frac{2027}{2}.\]

\boxed{\frac{2027}{2}}