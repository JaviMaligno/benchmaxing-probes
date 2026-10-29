## Razonamiento

**Condición de divisibilidad por 11.** La suma total de los dígitos es $1+\dots+8=36$. Si $S_{\text{impar}}$ y $S_{\text{par}}$ son las sumas en posiciones impares y pares, entonces $S_{\text{impar}}+S_{\text{par}}=36$, así que su diferencia es par. Los múltiplos pares de 11 posibles son $0,\pm 22$, pero la diferencia máxima alcanzable es $26-10=16$. Luego la diferencia debe ser $0$:
$$S_{\text{impar}}=S_{\text{par}}=18.$$

**Particiones válidas.** Hay que contar los subconjuntos de 4 elementos de $\{1,\dots,8\}$ con suma 18:
$$\{1,2,7,8\},\{1,3,6,8\},\{1,4,5,8\},\{1,4,6,7\},\{2,3,5,8\},\{2,3,6,7\},\{2,4,5,7\},\{3,4,5,6\}$$
son 8 subconjuntos (4 pares complementarios).

**Condición de divisibilidad por 2.** El último dígito está en posición par, y debe ser par. Nota clave: cada uno de los 8 subconjuntos contiene exactamente **2 dígitos pares**.

**Conteo.** Elegimos uno de los 8 subconjuntos para las posiciones pares. Dentro de él, el dígito final puede ser uno de los 2 pares, y los otros 3 se ordenan de $3!$ formas. Las posiciones impares admiten $4!$ ordenaciones:
$$N = 8 \times (2 \cdot 3!) \times 4! = 8 \times 12 \times 24 = 2304.$$

**Diferencia.** $2304 - 2025 = 279$.

\boxed{279}