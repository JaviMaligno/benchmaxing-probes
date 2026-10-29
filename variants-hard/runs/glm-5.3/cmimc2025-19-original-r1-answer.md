## Planteamiento

Como cada subconjunto de $\{1,\dots,18\}$ es equiprobable, con $2^{18}=262144$ subconjuntos en total:

$$p(k)=\frac{A_k}{2^{18}},\qquad A_k=\sum_{j\equiv k\ (\mathrm{mód}\ 5)}\binom{18}{j}.$$

## Coeficientes y agrupación

Los coeficientes binomiales de $n=18$ son:
$$1,\ 18,\ 153,\ 816,\ 3060,\ 8568,\ 18564,\ 31824,\ 43758,\ 48620,\ 43758,\ 31824,\ 18564,\ 8568,\ 3060,\ 816,\ 153,\ 18,\ 1$$

Agrupando por $j \bmod 5$ (usando la simetría $\binom{18}{j}=\binom{18}{18-j}$, con $18\equiv 3$):

- $A_0 = \binom{18}{0}+\binom{18}{5}+\binom{18}{10}+\binom{18}{15}=1+8568+43758+816=53143$
- $A_1 = 18+18564+31824+153=50559$
- $A_2 = 153+31824+18564+18=50559$
- $A_3 = 816+43758+8568+1=53143$
- $A_4 = 3060+48620+3060=54740$

Verificación: $53143+50559+50559+53143+54740=262144=2^{18}$ ✓

## Desviaciones respecto de $2^{18}/5$

Como $\frac{2^{18}}{5}=52428.8$:

$$A_0-\tfrac{2^{18}}5=714.2,\quad A_1=-1869.8,\quad A_2=-1869.8,\quad A_3=714.2,\quad A_4=2311.2$$

(La suma de las desviaciones es $0$, como debe ser ✓)

## Suma pedida

$$\sum_{k=0}^{4}\left|p(k)-\frac15\right|=\frac{714.2+1869.8+1869.8+714.2+2311.2}{2^{18}}=\frac{7479.2}{262144}=\frac{37396}{1310720}=\frac{9349}{327680}$$

Comprobación adicional: con el filtro de raíces quintas las desviaciones son $\frac{L_{17}}{5},-\frac{L_{19}}{5},-\frac{L_{19}}{5},\frac{L_{17}}{5},\frac{2L_{18}}{5}$ con números de Lucas $L_{17}=3571$, $L_{18}=5778$, $L_{19}=9349$, lo que da $\frac{2(L_{17}+L_{18}+L_{19})}{5\cdot 2^{18}}=\frac{9349}{327680}$, igual al cálculo directo ✓

$$\boxed{\dfrac{9349}{327680}}$$