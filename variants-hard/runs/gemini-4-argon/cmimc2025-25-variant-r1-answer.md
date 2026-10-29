Para resolver el problema, fijemos sin pérdida de generalidad que la longitud del lado del triángulo equilátero $\triangle PQR$ es $PQ = QR = PR = 1$.

### 1. Determinación de los puntos de intersección de las elipses
Por definición, las tres elipses están dadas por:
$$\mathcal{E}_{PQ} = \left\{ A : AP + AQ = \frac{3}{2} \right\}, \quad \mathcal{E}_{QR} = \left\{ A : AQ + AR = \frac{3}{2} \right\}, \quad \mathcal{E}_{PR} = \left\{ A : AP + AR = \frac{3}{2} \right\}.$$

Consideremos los puntos de intersección de dos de estas elipses, por ejemplo $\mathcal{E}_{PQ}$ y $\mathcal{E}_{PR}$. Si $A \in \mathcal{E}_{PQ} \cap \mathcal{E}_{PR}$, entonces:
$$AP + AQ = \frac{3}{2} \quad \text{y} \quad AP + AR = \frac{3}{2} \implies AQ = AR.$$
Por lo tanto, cualquier punto de intersección entre $\mathcal{E}_{PQ}$ y $\mathcal{E}_{PR}$ debe pertenecer a la mediatriz del lado $QR$, la cual pasa por el vértice $P$ y por el punto medio $M$ de $QR$. Como $P$ es un foco de $\mathcal{E}_{PQ}$ (y por ende un punto interior a dicha elipse), la mediatriz de $QR$ intersecta a $\mathcal{E}_{PQ}$ en exactamente dos puntos, a los que llamaremos $U_P$ y $V_P$.

Sea $h = PM = \frac{\sqrt{3}}{2}$ la altura de $\triangle PQR$.
1. **Punto $U_P$ (en la semirrecta $MP$ más allá de $P$):**
   Sea $x = PU_P > 0$. Entonces $MU_P = \frac{\sqrt{3}}{2} + x$. Por el teorema de Pitágoras en $\triangle U_P M Q$:
   $$U_P Q = \sqrt{\left(\frac{\sqrt{3}}{2} + x\right)^2 + \left(\frac{1}{2}\right)^2} = \sqrt{x^2 + \sqrt{3}x + 1}.$$
   Sustituyendo en la ecuación de la elipse $U_P P + U_P Q = \frac{3}{2}$:
   $$x + \sqrt{x^2 + \sqrt{3}x + 1} = \frac{3}{2} \implies \sqrt{x^2 + \sqrt{3}x + 1} = \frac{3}{2} - x.$$
   Elevando al cuadrado ambos miembros:
   $$x^2 + \sqrt{3}x + 1 = \frac{9}{4} - 3x + x^2 \implies (3 + \sqrt{3})x = \frac{5}{4} \implies x = \frac{5}{4(3+\sqrt{3})} = \frac{15 - 5\sqrt{3}}{24}.$$

2. **Punto $V_P$ (en la semirrecta $PM$ más allá de $M$):**
   Sea $y = PV_P > 0$ a lo largo de la dirección de $P$ hacia $M$. Entonces $V_P Q = \sqrt{\left(y - \frac{\sqrt{3}}{2}\right)^2 + \frac{1}{4}} = \sqrt{y^2 - \sqrt{3}y + 1}$.
   De $V_P P + V_P Q = \frac{3}{2}$ obtenemos:
   $$\sqrt{y^2 - \sqrt{3}y + 1} = \frac{3}{2} - y \implies (3 - \sqrt{3})y = \frac{5}{4} \implies y = \frac{5}{4(3-\sqrt{3})} = \frac{15 + 5\sqrt{3}}{24}.$$
   Como $y = \frac{15 + 5\sqrt{3}}{24} > \frac{12\sqrt{3}}{24} = \frac{\sqrt{3}}{2} = PM$, el punto $V_P$ se encuentra en el exterior de $\triangle PQR$ del otro lado de $QR$ respecto a $P$.

Por simetría, las tres elipses determinan en total $6$ puntos de intersección: $U_P, U_Q, U_R$ (situados más allá de los vértices $P, Q, R$ desde el centro $O$ del triángulo) y $V_P, V_Q, V_R$ (situados más allá de los puntos medios de los lados $QR, PR, PQ$).

---

### 2. Identificación del triángulo $\triangle XYZ$ y cálculo de su lado mayor
Sea $O$ el baricentro (y circuncentro) de $\triangle PQR$. La distancia de $O$ a cada vértice de $\triangle PQR$ es $OP = \frac{\sqrt{3}}{3}$.
- La distancia de $O$ a $U_P, U_Q, U_R$ es:
  $$OU_P = OP + x = \frac{\sqrt{3}}{3} + \frac{15 - 5\sqrt{3}}{24} = \frac{15 + 3\sqrt{3}}{24} = \frac{5 + \sqrt{3}}{8}.$$
- La distancia de $O$ a $V_P, V_Q, V_R$ (en sentido opuesto a $P, Q, R$) es:
  $$OV_P = y - OP = \frac{15 + 5\sqrt{3}}{24} - \frac{\sqrt{3}}{3} = \frac{15 - 3\sqrt{3}}{24} = \frac{5 - \sqrt{3}}{8}.$$

Analicemos qué segmentos entre estos $6$ puntos no intersectan las aristas de $\triangle PQR$:
- La distancia del centro $O$ a cualquiera de las rectas que contienen los lados de $\triangle PQR$ es el inradio $r = \frac{\sqrt{3}}{6}$.
- Para el triángulo equilátero $\triangle U_P U_Q U_R$, la distancia de $O$ a sus lados (por ejemplo $U_Q U_R$, que es paralelo a $QR$ del lado opuesto a $P$) es $\frac{1}{2} OU_P = \frac{5 + \sqrt{3}}{16} > \frac{\sqrt{3}}{6}$, por lo que los tres segmentos $U_P U_Q$, $U_Q U_R$ y $U_R U_P$ son completamente exteriores a $\triangle PQR$.
- Asimismo, dado que $OV_P = \frac{5 - \sqrt{3}}{8} > \frac{\sqrt{3}}{6}$, el punto $V_P$ está separado de $\triangle PQR$ por la recta $QR$, de modo que los segmentos $V_P U_Q$ y $V_P U_R$ tampoco intersectan a $\triangle PQR$ (y análogamente para $V_Q$ y $V_R$). En cambio, cualquier segmento del tipo $V_P V_Q$ o $U_P V_P$ atraviesa los lados de $\triangle PQR$.

Por consiguiente, $\triangle XYZ$ puede ser $\triangle U_P U_Q U_R$ o bien uno de los tres triángulos congruentes $\triangle U_Q U_R V_P$, $\triangle U_P U_R V_Q$, $\triangle U_P U_Q V_R$. En estos tres últimos, $V_P$ se encuentra muy próximo al punto medio de $U_Q U_R$ (pues $OV_P = \frac{10-2\sqrt{3}}{16} \approx \frac{5+\sqrt{3}}{16} = \frac{1}{2}OU_P$), por lo que su lado mayor también es $U_Q U_R$.

Como $\triangle U_P U_Q U_R$ es homotético a $\triangle PQR$ respecto a $O$, la longitud del lado mayor de $\triangle XYZ$ es:
$$U_P U_Q = \sqrt{3} \cdot OU_P = \sqrt{3} \left(\frac{5 + \sqrt{3}}{8}\right) = \frac{3 + 5\sqrt{3}}{8}.$$

Dado que el lado de $\triangle PQR$ es $1$, la razón buscada es:

\boxed{\frac{3+5\sqrt{3}}{8}}