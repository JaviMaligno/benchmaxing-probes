## Razonamiento

**Paso 1: Caracterizar el proceso.**

Sea $S=\{j: c_j=c_{j-1}\}$ el conjunto de posiciones donde hay un double. El escaneo greedy toma el menor $j_1\in S$ (ahí se remueve), y como el nuevo bloque empieza en $j_1+1$, el siguiente disparo debe cumplir $j\ge j_1+2$. Así, $N$ es el tamaño de la selección greedy de $S$ con separación mínima $2$.

**Paso 2: Descomponer por rachas.**

En una racha maximal de enteros consecutivos de $S$ de longitud $L$, el greedy elige $\lceil L/2\rceil$ elementos, y las rachas no interfieren entre sí. Una racha de longitud $L$ en $S$ corresponde a un bloque maximal de $L+1$ cartas iguales consecutivas. Por tanto, si las rachas maximales de valores iguales en el mazo tienen longitudes $\ell$:

$$N=\sum_{\text{rachas}}\left\lceil \tfrac{\ell-1}{2}\right\rceil=\sum_{\text{rachas}}\left\lfloor \tfrac{\ell}{2}\right\rfloor$$

(para $\ell=1,2,3,4$ da $0,1,1,2$).

**Paso 3: Convertir en suma por posiciones.**

$\lfloor \ell/2\rfloor$ cuenta las posiciones de offset par dentro de la racha. Si $r(i)$ es la longitud de la racha de iguales que **termina** en $i$, entonces $N=\#\{i: r(i)\text{ par}\}$, así que

$$E[N]=\sum_{i=1}^{12}\big(P(r(i)=2)+P(r(i)=4)\big)$$

**Paso 4: Probabilidades.**

Para posiciones fijas consecutivas (mazo barajado uniformemente, 3 valores × 4 palos):
- 2 iguales: $\frac{3\cdot4\cdot3}{12\cdot11}=\frac{3}{11}$
- 3 iguales: $\frac{3\cdot4\cdot3\cdot2}{12\cdot11\cdot10}=\frac{3}{55}$
- 4 iguales: $\frac{3\cdot 4!}{12\cdot11\cdot10\cdot9}=\frac{1}{165}$

Entonces $P(r(i)=2)=\frac{3}{11}-\frac{3}{55}=\frac{12}{55}$ para $i\ge3$, y $P(r(2)=2)=\frac{3}{11}$; además $P(r(i)=4)=\frac{1}{165}$ para $i\ge4$ (no hay 5 iguales).

**Paso 5: Sumar.**

$$E[N]=\underbrace{\frac{3}{11}}_{i=2}+\underbrace{10\cdot\frac{12}{55}}_{i=3..12}+\underbrace{9\cdot\frac{1}{165}}_{i=4..12}=\frac{45+360+9}{165}=\frac{414}{165}=\frac{138}{55}$$

Verificación del método en un caso pequeño ($\{A,A,B,B\}$): la fórmula da $1$, y el conteo directo sobre las 6 palabras da $(2+0+1+1+0+2)/6=1$. ✓

$$\boxed{\dfrac{138}{55}}$$