Para encontrar el área de $\triangle QXT$, primero determinamos las longitudes de los segmentos sobre la recta que contiene a los puntos $P, Q, R, S, T$ y $U$.

Sean las longitudes de los segmentos adyacentes:
- $a = PQ$
- $b = QR$
- $c = RS$
- $d = ST$
- $e = TU$

A partir de los datos del problema, tenemos el siguiente sistema de ecuaciones:
1. $PR = a + b = 24$
2. $QS = b + c = 30$
3. $RT = c + d = 37$
4. $SU = d + e = 29$
5. $PU = a + b + c + d + e = 74$

Sustituyendo (1) y (4) en (5), podemos hallar la longitud de $RS = c$:
$$24 + c + 29 = 74 \implies c = 74 - 53 = 21$$

Con el valor de $c = 21$, hallamos la longitud de la base $QT = b + c + d$ del triángulo $\triangle QXT$:
$$QT = (b + c) + (c + d) - c = QS + RT - RS = 30 + 37 - 21 = 46$$

Ahora consideramos el triángulo $\triangle RSX$, cuyos lados miden $RS = 21$, $RX = 17$ y $SX = 10$. Calculamos su semiperímetro $s$:
$$s = \frac{21 + 17 + 10}{2} = 24$$

Por la fórmula de Herón, el área de $\triangle RSX$ es:
$$\text{Área}(\triangle RSX) = \sqrt{24(24 - 21)(24 - 17)(24 - 10)} = \sqrt{24 \cdot 3 \cdot 7 \cdot 14} = \sqrt{72 \cdot 98} = 84$$

Sea $h$ la altura trazada desde $X$ hacia la recta. Como esta altura es común para $\triangle RSX$ y $\triangle QXT$:
$$\text{Área}(\triangle RSX) = \frac{1}{2} \cdot RS \cdot h \implies 84 = \frac{1}{2} \cdot 21 \cdot h \implies h = 8$$

Finalmente, calculamos el área de $\triangle QXT$:
$$\text{Área}(\triangle QXT) = \frac{1}{2} \cdot QT \cdot h = \frac{1}{2} \cdot 46 \cdot 8 = 184$$

\boxed{184}