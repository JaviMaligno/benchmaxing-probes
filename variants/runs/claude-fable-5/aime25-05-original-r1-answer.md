## Solución

**Divisibilidad por 22 = divisible por 2 y por 11.**

**Condición de divisibilidad por 11:** si $S_{\text{imp}}$ y $S_{\text{par}}$ son las sumas de los dígitos en posiciones impares y pares, se necesita $S_{\text{imp}} - S_{\text{par}} \equiv 0 \pmod{11}$. Como $S_{\text{imp}} + S_{\text{par}} = 1+2+\cdots+8 = 36$, y cada grupo de 4 dígitos suma entre $10$ y $26$, la única opción es $S_{\text{imp}} = S_{\text{par}} = 18$.

**Subconjuntos de 4 dígitos que suman 18:** enumerándolos:
$$\{1,2,7,8\},\ \{1,3,6,8\},\ \{1,4,5,8\},\ \{2,3,5,8\},\ \{1,4,6,7\},\ \{2,3,6,7\},\ \{2,4,5,7\},\ \{3,4,5,6\}$$
Son **8 subconjuntos** (cada uno es complemento de otro de la lista, lo cual es consistente). Hay por tanto 8 maneras de elegir qué conjunto ocupa las posiciones pares (el complemento va a las impares).

**Observación clave:** cada uno de estos subconjuntos contiene exactamente **2 dígitos pares** (se verifica directamente en la lista; por ejemplo $\{3,4,5,6\}$ tiene 4 y 6).

**Condición de divisibilidad por 2:** el último dígito (posición 8, que es una posición par) debe ser par. Si $B$ es el conjunto de las posiciones pares:
- Elegir el dígito par para la posición 8: $2$ opciones.
- Ordenar los otros 3 dígitos de $B$: $3! = 6$.
- Ordenar los 4 dígitos de las posiciones impares: $4! = 24$.

Por cada elección de $B$: $2 \cdot 6 \cdot 24 = 288$ números.

**Total:**
$$N = 8 \cdot 288 = 2304$$

**Diferencia pedida:**
$$2304 - 2025 = 279$$

$$\boxed{279}$$