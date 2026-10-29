## Solución

**Planteamiento con razones.** Sobre $\overline{PQ}$: $PD=3$, $DE=9$, $EQ=6$, así que $PQ=18$, $PE=12$. Sobre $\overline{PR}$: $PF=5$, $FG=15$, $GR=10$, así que $PR=30$, $PG=20$.

**Área del triángulo.** Si $S=[\triangle PQR]$, entonces
$$[\triangle PEG]=\frac{PE}{PQ}\cdot\frac{PG}{PR}\,S=\frac{12}{18}\cdot\frac{20}{30}S=\frac{4}{9}S,\qquad [\triangle PDF]=\frac{3}{18}\cdot\frac{5}{30}S=\frac{S}{36}.$$
Por lo tanto $[DEGF]=\frac{4}{9}S-\frac{1}{36}S=\frac{15}{36}S=\frac{5}{12}S=300$, de donde $S=720$.

**Verificación con coordenadas.** Tomo $P=(0,0)$, $Q=(18,0)$, $R=(0,80)$ (área $=\frac12\cdot18\cdot80=720$). Entonces $D=(3,0)$, $E=(12,0)$, $F=(0,\tfrac{40}{3})$, $G=(0,\tfrac{160}{3})$; la fórmula del polígono confirma $[DEGF]=300$. ✓

Las reflexiones son $M=2F-D=(-3,\tfrac{80}{3})$ y $N=2E-G=(24,-\tfrac{160}{3})$.

Aplicando la fórmula del área (shoelace) al heptágono $P,F,N,Q,R,E,M$:
$$\tfrac12\left|0-320+960+1440-960+320+0\right|=\tfrac12\cdot1440=720.$$

Esto tiene sentido geométricamente: las reflexiones hacen que $[\triangle M F P]=[\triangle D F P]$ y $[\triangle N E Q]=[\triangle G E Q]$ (misma base reflejada), de modo que las piezas añadidas fuera del triángulo compensan exactamente las quitadas, y el heptágono tiene la misma área que $\triangle PQR$.

$$\boxed{720}$$