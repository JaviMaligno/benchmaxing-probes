Para resolver el problema paso a paso, podemos establecer un sistema de coordenadas cartesianas centrado en el punto $P$.

### Paso 1: Configurar el sistema de coordenadas
1. Situamos el centro $P$ del círculo $\omega_1$ en el origen $(0,0)$. Dado que $\omega_1$ tiene radio $r_1 = 4$, su ecuación es:
   $$x^2 + y^2 = 16$$
2. Como $\omega_1$ es internamente tangente a $\omega_2$ en el punto $Q$ y $\overline{QR}$ es un diámetro de $\omega_2$, los puntos $Q$, $P$, el centro de $\omega_2$ y $R$ son colineales. Ubicamos la recta $QR$ sobre el eje $x$, de modo que $Q = (-4, 0)$.
3. El círculo $\omega_2$ tiene radio $r_2 = 20$ y es tangente en $Q(-4, 0)$ conteniendo a $\omega_1$ en su interior. Por lo tanto, el centro de $\omega_2$ está en $(-4 + 20, 0) = (16, 0)$ y el otro extremo del diámetro es $R = (-4 + 40, 0) = (36, 0)$.
4. Se nos dice que $S$ está en $\omega_2$ y que $\overline{QR} \perp \overline{PS}$. Como $\overline{QR}$ está sobre el eje $x$ y $P$ es el origen, la recta $PS$ coincide con el eje $y$ ($x = 0$). Sin pérdida de generalidad, tomamos la coordenada $y$ de $S$ positiva. Por el teorema de las cuerdas (o sustituyendo $x=0$ en la ecuación de $\omega_2$, $(x-16)^2 + y^2 = 20^2$):
   $$PS^2 = QP \cdot PR = 4 \cdot 36 = 144 \implies PS = 12$$
   Por lo tanto, $S = (0, 12)$.

### Paso 2: Coordenadas del rectángulo $KLMN$
El rectángulo $KLMN$ está inscrito en $\omega_1$, por lo que su centro también es $P(0,0)$ y sus vértices son de la forma $(\pm a, \pm b)$ con $a, b > 0$ tales que:
$$a^2 + b^2 = 4^2 = 16$$

Determinamos la posición de los lados a partir de las condiciones del problema:
- $\overline{KL} \perp \overline{QR}$: Como $\overline{QR}$ es horizontal, los lados $\overline{KL}$ y $\overline{MN}$ son verticales, mientras que $\overline{LM}$ y $\overline{KN}$ son horizontales.
- $R(36, 0)$ está más cerca de $\overline{MN}$ que de $\overline{KL}$: El lado $\overline{MN}$ está en la recta $x = a$ y $\overline{KL}$ está en $x = -a$.
- $S(0, 12)$ está más cerca de $\overline{LM}$ que de $\overline{KN}$: El lado $\overline{LM}$ está en la recta $y = b$ y $\overline{KN}$ está en $y = -b$.

Así, las coordenadas de los vértices son:
$$K = (-a, -b), \quad L = (-a, b), \quad M = (a, b), \quad N = (a, -b)$$

### Paso 3: Igualdad de áreas de los triángulos
Calculamos las áreas de $\triangle SML$ y $\triangle RNM$:
- Para $\triangle SML$: La base es el segmento horizontal $ML$ de longitud $2a$ sobre la recta $y = b$, y la altura desde $S(0, 12)$ hasta dicha recta es $12 - b$. Su área es:
  $$[\triangle SML] = \frac{1}{2} \cdot 2a \cdot (12 - b) = a(12 - b)$$
- Para $\triangle RNM$: La base es el segmento vertical $NM$ de longitud $2b$ sobre la recta $x = a$, y la altura desde $R(36, 0)$ hasta dicha recta es $36 - a$. Su área es:
  $$[\triangle RNM] = \frac{1}{2} \cdot 2b \cdot (36 - a) = b(36 - a)$$

Igualando ambas áreas según el enunciado:
$$a(12 - b) = b(36 - a)$$
$$12a - ab = 36b - ab$$
$$12a = 36b \implies a = 3b$$

### Paso 4: Área del rectángulo $KLMN$
Sustituimos $a = 3b$ en la relación $a^2 + b^2 = 16$:
$$(3b)^2 + b^2 = 16 \implies 10b^2 = 16 \implies b^2 = \frac{8}{5}$$

El área del rectángulo $KLMN$ de lados $2a$ y $2b$ es:
$$\text{Área}(KLMN) = (2a)(2b) = 4ab = 4(3b)b = 12b^2 = 12 \cdot \frac{8}{5} = \frac{96}{5}$$

Como $m = 96$ y $n = 5$ son enteros positivos coprimos, tenemos que $m + n = 96 + 5 = 101$.

\boxed{101}