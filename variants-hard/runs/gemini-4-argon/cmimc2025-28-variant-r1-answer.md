Para hallar la longitud $OJ$, analizamos las propiedades geométricas y trigonométricas de la configuración.

### 1. Ángulos y longitudes en el triángulo $\triangle TPQ$
Como $\overline{PQ}$ es un diámetro de la circunferencia $\Gamma$ de centro $O$ y longitud $PQ = 20$, el radio de $\Gamma$ es $R_\Gamma = 10$ y los ángulos inscritos sobre el diámetro son rectos:
$$\angle PRQ = 90^\circ \quad \text{y} \quad \angle PSQ = 90^\circ.$$

Denotemos por $P = \angle TPQ$ y $Q = \angle TQP$ los ángulos en la base del triángulo $\triangle TPQ$.
- En el triángulo rectángulo $\triangle PQS$:
  $$\cos P = \frac{PS}{PQ} = \frac{8}{20} = \frac{2}{5}, \qquad \sin P = \sqrt{1 - \cos^2 P} = \frac{\sqrt{21}}{5}.$$
- En el triángulo rectángulo $\triangle PQR$:
  $$\cos Q = \frac{QR}{PQ} = \frac{12}{20} = \frac{3}{5}, \qquad \sin Q = \sqrt{1 - \cos^2 Q} = \frac{4}{5}.$$

Observemos que se cumple la relación clave:
$$\cos P + \cos Q = \frac{2}{5} + \frac{3}{5} = 1.$$

En el triángulo $\triangle TPQ$, el ángulo en $T$ es $T = \pi - (P+Q)$. Como $PQRS$ es un cuadrilátero cíclico, $\angle TRS = P$ y $\angle TSR = Q$.

---

### 2. Sistema de coordenadas centrado en $O$
Dado que $\triangle OQR$ y $\triangle OPS$ son isósceles con $OP = OQ = OR = OS = R_\Gamma$, los ángulos centrales son $\angle QOR = \pi - 2Q$ y $\angle POS = \pi - 2P$. Como $P, S, R, Q$ están ordenados a lo largo de la semicircunferencia, el ángulo central $\angle ROS$ es:
$$\angle ROS = \pi - (\pi - 2P) - (\pi - 2Q) = 2(P + Q) - \pi = 2\alpha,$$
donde $\alpha = P + Q - \frac{\pi}{2}$. Por tanto:
$$\cos \alpha = \sin(P+Q), \qquad \sin \alpha = -\cos(P+Q) = \sin P \sin Q - \cos P \cos Q.$$

Trabajando primero a escala unitaria ($R_\Gamma = 1$, multiplicando por $R_\Gamma = 10$ al final), situamos el origen en $O(0,0)$ y orientamos el eje $x$ positivo a lo largo de la bisectriz del ángulo $\angle ROS$. Entonces:
$$R = (\cos \alpha, -\sin \alpha), \qquad S = (\cos \alpha, \sin \alpha),$$
por lo que la recta $RS$ es la recta vertical $x = \cos \alpha$ y la longitud del segmento $RS$ es $2\sin \alpha$.

---

### 3. Coordenadas del $T$-excentro $J$
El punto $J$, centro de la $T$-excircunferencia de $\triangle TRS$, se encuentra del mismo lado de la recta $RS$ que $O$ ($x < \cos \alpha$), y es la intersección de las bisectrices exteriores de $\triangle TRS$ en $R$ y $S$. Como los ángulos interiores de $\triangle TRS$ en $R$ y $S$ son $P$ y $Q$, los ángulos de $\triangle JRS$ adyacentes a $RS$ son:
$$\angle JRS = \frac{\pi - P}{2}, \qquad \angle JSR = \frac{\pi - Q}{2}.$$

Si $h$ es la distancia horizontal de $J$ a la recta $RS$, la proyección vertical de $J$ sobre $RS$ divide al segmento $RS$ en dos partes de longitudes $h \cot(\angle JRS) = h \tan\frac{P}{2}$ y $h \cot(\angle JSR) = h \tan\frac{Q}{2}$. Así:
$$h \left(\tan\frac{P}{2} + \tan\frac{Q}{2}\right) = 2\sin \alpha \implies h = \frac{2\sin \alpha \cos\frac{P}{2}\cos\frac{Q}{2}}{\sin\left(\frac{P+Q}{2}\right)} = \frac{\sin \alpha \left[\cos\left(\frac{P+Q}{2}\right) + \cos\left(\frac{P-Q}{2}\right)\right]}{\sin\left(\frac{P+Q}{2}\right)}.$$

De este modo, las coordenadas $(x_J, y_J)$ de $J$ (para $R_\Gamma = 1$) son:
$$y_J = -\sin \alpha + h \tan\frac{P}{2} = \sin \alpha \frac{\tan\frac{P}{2} - \tan\frac{Q}{2}}{\tan\frac{P}{2} + \tan\frac{Q}{2}} = \sin \alpha \frac{\sin\left(\frac{P-Q}{2}\right)}{\sin\left(\frac{P+Q}{2}\right)},$$
$$x_J = \cos \alpha - h = \frac{\left[\cos \alpha \sin\left(\frac{P+Q}{2}\right) - \sin \alpha \cos\left(\frac{P+Q}{2}\right)\right] - \sin \alpha \cos\left(\frac{P-Q}{2}\right)}{\sin\left(\frac{P+Q}{2}\right)}.$$

Como $\frac{P+Q}{2} - \alpha = \frac{\pi}{2} - \frac{P+Q}{2}$, el corchete en el numerador de $x_J$ es $\sin\left(\frac{P+Q}{2} - \alpha\right) = \cos\left(\frac{P+Q}{2}\right)$, luego:
$$x_J = \frac{\cos\left(\frac{P+Q}{2}\right) - \sin \alpha \cos\left(\frac{P-Q}{2}\right)}{\sin\left(\frac{P+Q}{2}\right)}.$$

---

### 4. Cálculo de $OJ$
Elevando al cuadrado y sumando $x_J^2 + y_J^2$:
$$x_J^2 + y_J^2 = \frac{\cos^2\left(\frac{P+Q}{2}\right) - 2\sin \alpha \cos\left(\frac{P+Q}{2}\right)\cos\left(\frac{P-Q}{2}\right) + \sin^2 \alpha}{\sin^2\left(\frac{P+Q}{2}\right)}.$$

Usando que $2\cos\left(\frac{P+Q}{2}\right)\cos\left(\frac{P-Q}{2}\right) = \cos P + \cos Q = 1$ y que $\sin \alpha = -\cos(P+Q) = 1 - 2\cos^2\left(\frac{P+Q}{2}\right) = 2\sin^2\left(\frac{P+Q}{2}\right) - 1$:
$$x_J^2 + y_J^2 = \frac{\frac{1 - \sin \alpha}{2} - \sin \alpha + \sin^2 \alpha}{\frac{1 + \sin \alpha}{2}} = \frac{1 - \sin \alpha}{1 + \sin \alpha}(1 - 2\sin \alpha) = \cot^2\left(\frac{P+Q}{2}\right)(1 + 2\cos(P+Q)).$$

Además, como $\cos P + \cos Q = 1$:
1. $\cot\left(\frac{P+Q}{2}\right) = \frac{2\cos\left(\frac{P+Q}{2}\right)\cos\left(\frac{P-Q}{2}\right)}{2\sin\left(\frac{P+Q}{2}\right)\cos\left(\frac{P-Q}{2}\right)} = \frac{\cos P + \cos Q}{\sin P + \sin Q} = \frac{1}{\sin P + \sin Q}$.
2. $1 + 2\cos(P+Q) = (\cos P + \cos Q)^2 + 2\cos P \cos Q - 2\sin P \sin Q - (\cos^2 P + \cos^2 Q + 2\cos P \cos Q - 1) = (\sin P - \sin Q)^2$.

Por consiguiente:
$$\sqrt{x_J^2 + y_J^2} = \frac{|\sin P - \sin Q|}{\sin P + \sin Q}.$$

Finalmente, escalando por el radio $R_\Gamma = 10$ y sustituyendo $\sin P = \frac{\sqrt{21}}{5}$ y $\sin Q = \frac{4}{5}$:
$$OJ = 10 \cdot \frac{\frac{\sqrt{21}}{5} - \frac{4}{5}}{\frac{\sqrt{21}}{5} + \frac{4}{5}} = 10 \cdot \frac{\sqrt{21} - 4}{\sqrt{21} + 4} = 10 \cdot \frac{(\sqrt{21} - 4)^2}{21 - 16} = 2(37 - 8\sqrt{21}) = 74 - 16\sqrt{21}.$$

\boxed{74-16\sqrt{21}}