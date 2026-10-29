## Planteamiento

Sea $S=\omega^a+\omega^b+\omega^c+\omega^d$. Como $|\omega|=1$,

$$|S|^2 = 4 + 2\sum_{i<j}\cos\frac{2\pi (e_i-e_j)}{13} = 3 \quad\Longrightarrow\quad \sum_{i<j}\cos\frac{2\pi d_{ij}}{13} = -\tfrac12,$$

donde los $d_{ij}$ son las seis diferencias de exponentes módulo 13 (identificando $k$ con $13-k$, es decir, clases en $\{1,\dots,6\}$).

## Identificación de las soluciones

Con $c_k=\cos\frac{2\pi k}{13}$ se cumple la relación de traza $c_1+c_2+\cdots+c_6=-\tfrac12$. Si $n_k$ cuenta las parejas con diferencia de clase $k$, entonces $\sum n_k=6$ y $\sum (n_k-1)c_k=0$.

Los $c_1,\dots,c_6$ son los seis conjugados de Galois de $c_1$ sobre $\mathbb{Q}$ y forman una base de $\mathbb{Q}(c_1)$ (el núcleo del morfismo $\mathbb{Q}[G]\to\mathbb{Q}(c_1)$, $g\mapsto g(c_1)$, es nulo: ninguna de las cuatro componentes irreducibles lo anula). Por tanto son linealmente independientes y $n_k=1$ para todo $k$.

**Conclusión:** los residuos $\{a,b,c,d\}\bmod 13$ deben formar un *conjunto de diferencias perfecto* $(13,4,1)$: los $52$ trasladados de $\{0,1,3,9\}$, $\{0,2,5,6\}$, $\{0,4,10,12\}$, $\{0,7,8,11\}$.

## Uso de la paridad

Si $a\le 11$, los cuatro enteros impares son $\le 11$, así que coinciden con sus residuos y todas las diferencias son **pares**: $2,4,6,8,10$, cuyas clases son $2,4,6,5,3$. Nunca aparece la clase $1$, que es obligatoria. Luego $a\ge 13$.

## Caso $a=13$

Entonces $13\equiv 0$ y los otros tres son impares de $\{1,3,5,7,9,11\}$. Clases desde el $0$: $1\!\to\!1,\,3\!\to\!3,\,5\!\to\!5,\,7\!\to\!6,\,9\!\to\!4,\,11\!\to\!2$; clases de diferencias pares: $2\!\to\!2,\,4\!\to\!4,\,6\!\to\!6,\,8\!\to\!5,\,10\!\to\!3$. Revisando las $20$ ternas, solo sirven:

- $\{1,3,9\}$: clases $1,3,4$ y diferencias $2,8,6\to 2,5,6$ ✓
- $\{1,5,11\}$: clases $1,5,2$ y diferencias $4,10,6\to 4,3,6$ ✓

Dan $13931$ y $14151$. Verificación: $|1+\omega+\omega^3+\omega^9|^2=4+2(c_1+c_2+c_3+c_4+c_5+c_6)=4-1=3$ ✓.

Como $a\ge 13$ y cualquier $a\ge 15$ supera $14000$, el mínimo es con $(a,b,c,d)=(13,9,3,1)$.

$$\boxed{13931}$$