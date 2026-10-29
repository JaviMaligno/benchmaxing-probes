Para encontrar el área del triángulo $\triangle QXT$, primero determinamos las longitudes de los segmentos sobre la línea recta que contiene a los puntos $P, Q, R, S, T$ y $U$ en ese orden.

1. **Cálculo de la longitud del segmento $RS$:**
   Sabemos que la longitud total del segmento $PU$ es la suma de las partes:
   $$PU = PR + RS + SU$$
   Sustituyendo los valores dados ($PR = 24$, $SU = 29$ y $PU = 74$):
   $$74 = 24 + RS + 29 \implies RS = 74 - 53 = 21$$

2. **Cálculo de la base $QT$ del triángulo $\triangle QXT$:**
   Observamos que:
   $$QS + RT = (QR + RS) + (RS + ST) = QT + RS$$
   Sustituyendo $QS = 30$, $RT = 37$ y $RS = 21$:
   $$30 + 37 = QT + 21 \implies QT = 67 - 21 = 46$$

3. **Cálculo de la altura desde $X$ hasta la recta:**
   Consideremos el triángulo $\triangle RXS$, cuyos lados miden $RS = 21$, $RX = 17$ y $SX = 10$.
   Calculamos su semiperímetro $s$:
   $$s = \frac{21 + 17 + 10}{2} = 24$$
   Aplicando la fórmula de Herón para hallar el área de $\triangle RXS$:
   $$\text{Área}(\triangle RXS) = \sqrt{24(24 - 21)(24 - 17)(24 - 10)} = \sqrt{24 \cdot 3 \cdot 7 \cdot 14} = \sqrt{72 \cdot 98} = 84$$
   Sea $h$ la altura trazada desde $X$ hacia la recta que contiene a los puntos. Usando la fórmula del área de $\triangle RXS$:
   $$\frac{1}{2} \cdot RS \cdot h = 84 \implies \frac{1}{2} \cdot 21 \cdot h = 84 \implies h = 8$$

4. **Cálculo del área de $\triangle QXT$:**
   Como los puntos $Q, R, S, T$ son colineales, el triángulo $\triangle QXT$ comparte la misma altura $h = 8$ con respecto a la base $QT = 46$:
   $$\text{Área}(\triangle QXT) = \frac{1}{2} \cdot QT \cdot h = \frac{1}{2} \cdot 46 \cdot 8 = 184$$

\boxed{184}