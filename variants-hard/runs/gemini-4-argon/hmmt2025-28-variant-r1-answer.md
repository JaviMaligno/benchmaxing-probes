Para calcular la longitud de $NS$, podemos utilizar geometría analítica o el teorema de Apolonio (fórmula de la mediana) mediante una construcción geométrica.

### Paso 1: Ubicación del centro y propiedades de la cuerda $PQ$
Sea $\omega$ la circunferencia de centro $O$ y radio $r = 7$ sobre la cual se encuentran los puntos $P, Q, R, S$ y $N$.

Como $PQRS$ es un trapecio isósceles inscrito en $\omega$ con $PQ \parallel RS$, los vértices aparecen en orden cíclico $P, Q, R, S$ alrededor de la circunferencia. El eje de simetría del trapecio es la mediatriz común de las bases $PQ$ y $RS$, la cual pasa por el centro $O$.

Sea $M$ el punto medio de $\overline{PQ}$. Como $PQ = 6$, tenemos que $PM = MQ = 3$ y $OM \perp PQ$. Por el teorema de Pitágoras en el triángulo rectángulo $\triangle OMP$:
$$OM^2 = OP^2 - PM^2 = 7^2 - 3^2 = 49 - 9 = 40$$

---

### Paso 2: Construcción de un paralelogramo auxiliar
El punto $T$ se encuentra en la recta $RS$ de modo que $S$ está entre $T$ y $R$, y $ST = 3$. Esto significa que el vector $\overrightarrow{ST}$ es paralelo al vector $\overrightarrow{QP}$ y tiene su mismo sentido y longitud ($\|\overrightarrow{ST}\| = 3 = \|\overrightarrow{MP}\|$).

Prolonguemos el segmento $MP$ más allá de $P$ hasta un punto $A$ en la recta $PQ$ tal que $PA = 3$ (con $P$ entre $M$ y $A$). Entonces:
1. El segmento $PA$ es paralelo al segmento $ST$ y tiene la misma longitud ($PA = ST = 3$) y el mismo sentido.
2. Por lo tanto, el cuadrilátero $PATS$ es un paralelogramo, cuyas diagonales son $\overline{PT}$ y $\overline{AS}$.

Como las diagonales de un paralelogramo se bisecan mutuamente y $N$ es el punto medio de $\overline{PT}$, se deduce que **$N$ también es el punto medio de $\overline{AS}$**.

---

### Paso 3: Cálculo de $OA$ y aplicación del teorema de Apolonio
En el triángulo rectángulo $\triangle OMA$, tenemos que $OM \perp MA$ y $MA = MP + PA = 3 + 3 = 6$. Aplicando el teorema de Pitágoras:
$$OA^2 = OM^2 + MA^2 = 40 + 6^2 = 40 + 36 = 76$$

Ahora consideremos el triángulo $\triangle OAS$. Como $N$ es el punto medio del lado $\overline{AS}$, el segmento $\overline{ON}$ es la mediana relativa a $\overline{AS}$ (y además $NS = NA$). Por el teorema de Apolonio (teorema de la mediana) en $\triangle OAS$:
$$OA^2 + OS^2 = 2\,ON^2 + 2\,NS^2$$

Dado que tanto $S$ como $N$ pertenecen a la circunferencia $\omega$ de centro $O$ y radio $7$, sabemos que $OS = 7$ y $ON = 7$. Sustituyendo estos valores en la ecuación:
$$76 + 7^2 = 2(7^2) + 2\,NS^2$$
$$76 + 49 = 98 + 2\,NS^2$$
$$2\,NS^2 = 76 - 49 = 27$$
$$NS^2 = \frac{27}{2}$$

Tomando la raíz cuadrada y racionalizando el denominador:
$$NS = \sqrt{\frac{27}{2}} = \frac{3\sqrt{3}}{\sqrt{2}} = \frac{3\sqrt{6}}{2}$$

\boxed{\frac{3\sqrt{6}}{2}}