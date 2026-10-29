Para encontrar el área del heptágono $PFNQREM$, primero analizamos las longitudes de los segmentos sobre los lados $\overline{PQ}$ y $\overline{PR}$ del triángulo $\triangle PQR$:

1. **Longitudes y proporciones en los lados:**
   * En el lado $\overline{PQ}$:
     $$PD = 3, \quad PE = PD + DE = 3 + 9 = 12, \quad PQ = PE + EQ = 12 + 6 = 18$$
   * En el lado $\overline{PR}$:
     $$PF = 5, \quad PG = PF + FG = 5 + 15 = 20, \quad PR = PG + GR = 20 + 10 = 30$$

   Observamos que las razones desde el vértice $P$ son iguales en ambos lados:
   $$\frac{PD}{PQ} = \frac{3}{18} = \frac{1}{6}, \quad \frac{PF}{PR} = \frac{5}{30} = \frac{1}{6}$$
   $$\frac{PE}{PQ} = \frac{12}{18} = \frac{2}{3}, \quad \frac{PG}{PR} = \frac{20}{30} = \frac{2}{3}$$
   Por lo tanto, $\overline{DF} \parallel \overline{EG} \parallel \overline{QR}$, y los triángulos $\triangle PDF$, $\triangle PEG$ y $\triangle PQR$ son semejantes entre sí con razones de semejanza $1 : 4 : 6$.

2. **Área de $\triangle PQR$:**
   Como las áreas de triángulos semejantes son proporcionales al cuadrado de sus razones de semejanza, si llamamos $K = [\triangle PDF]$, tenemos:
   $$[\triangle PEG] = 4^2 K = 16K, \quad [\triangle PQR] = 6^2 K = 36K$$
   El área del cuadrilátero $DEGF$ es:
   $$[DEGF] = [\triangle PEG] - [\triangle PDF] = 16K - K = 15K$$
   Dado que $[DEGF] = 300$, obtenemos $K = \frac{300}{15} = 20$. Por consiguiente:
   $$[\triangle PQR] = 36 \times 20 = 720$$

3. **Coordenadas afines y fórmula de Gauss (Shoelace):**
   Como las razones de áreas se conservan bajo transformaciones afines, podemos elegir un sistema de coordenadas con origen en $P(0,0)$ tomando como vectores base $\vec{u} = \overrightarrow{PD}$ y $\vec{v} = \overrightarrow{PF}$. En este sistema, cada triángulo de base $1$ y altura $1$ tiene área $K = 20$ (es decir, una unidad cuadrada de área equivale a $2K = 40$).

   Las coordenadas de los puntos sobre los ejes son:
   * $P = (0, 0)$
   * $D = (1, 0)$, $E = (4, 0)$, $Q = (6, 0)$
   * $F = (0, 1)$, $G = (0, 4)$, $R = (0, 6)$

   Calculamos las coordenadas de las reflexiones $M$ y $N$:
   * $M$ es la reflexión de $D(1,0)$ respecto a $F(0,1)$:
     $$M = 2F - D = 2(0,1) - (1,0) = (-1, 2)$$
   * $N$ es la reflexión de $G(0,4)$ respecto a $E(4,0)$:
     $$N = 2E - G = 2(4,0) - (0,4) = (8, -4)$$

4. **Área del heptágono $PFNQREM$:**
   Aplicamos la fórmula de Gauss (o descomposición en triángulos con vértice en el origen $P$) recorriendo los vértices en orden $P(0,0) \to F(0,1) \to N(8,-4) \to Q(6,0) \to R(0,6) \to E(4,0) \to M(-1,2) \to P(0,0)$:
   $$\begin{aligned}
   2 \cdot \text{Área}_{\text{coord}}(PFNQREM) &= (0\cdot 1 - 0\cdot 0) + (0\cdot(-4) - 1\cdot 8) + (8\cdot 0 - (-4)\cdot 6) \\
   &\quad + (6\cdot 6 - 0\cdot 0) + (0\cdot 0 - 6\cdot 4) + (4\cdot 2 - 0\cdot(-1)) + (-1\cdot 0 - 2\cdot 0) \\
   &= 0 - 8 + 24 + 36 - 24 + 8 + 0 \\
   &= 36
   \end{aligned}$$
   Así, en unidades de coordenadas, el área del heptágono es $\frac{36}{2} = 18$, que coincide exactamente con el área en coordenadas de $\triangle PQR$ ($\frac{1}{2} \times 6 \times 6 = 18$).

   Multiplicando por el factor de escala de área ($40$ por unidad cuadrada):
   $$[PFNQREM] = 18 \times 40 = 720$$

\boxed{720}