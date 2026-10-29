Para resolver el problema paso a paso, establecemos un sistema de coordenadas cartesianas:

1. **Ubicación de los círculos y puntos principales:**
   - Sea $P(0,0)$ el origen de coordenadas, centro del círculo $\omega_1$ de radio $r_1 = 4$. La ecuación de $\omega_1$ es $x^2 + y^2 = 16$.
   - Situamos el punto de tangencia en $Q(-4, 0)$ y hacemos que el diámetro $\overline{QR}$ de $\omega_2$ coincida con el eje $x$.
   - Como $\omega_1$ es internamente tangente a $\omega_2$ (de radio $r_2 = 20$) en $Q(-4,0)$, el centro de $\omega_2$ se encuentra en $(-4 + 20, 0) = (16, 0)$ y el otro extremo del diámetro es $R(-4 + 40, 0) = (36, 0)$.
   - La ecuación de $\omega_2$ es $(x - 16)^2 + y^2 = 20^2 = 400$.
   - Dado que $\overline{QR} \perp \overline{PS}$ y $P$ es el origen $(0,0)$, el segmento $\overline{PS}$ está sobre el eje $y$ ($x = 0$). Sustituyendo $x = 0$ en la ecuación de $\omega_2$:
     $$(-16)^2 + y^2 = 400 \implies 256 + y^2 = 400 \implies y^2 = 144$$
     Sin pérdida de generalidad, tomamos $S(0, 12)$.

2. **Coordenadas del rectángulo $KLMN$:**
   - Como $KLMN$ está inscrito en $\omega_1$, su centro es $P(0,0)$ y sus lados son paralelos a los ejes coordenados ya que $\overline{KL} \perp \overline{QR}$.
   - Sean $x = \pm a$ y $y = \pm b$ las rectas que contienen los lados del rectángulo, con $a, b > 0$ tales que $a^2 + b^2 = 4^2 = 16$.
   - Como $R(36, 0)$ está más cerca de $\overline{MN}$ que de $\overline{KL}$, el lado $\overline{MN}$ está en $x = a$ y $\overline{KL}$ está en $x = -a$.
   - Como $S(0, 12)$ está más cerca de $\overline{LM}$ que de $\overline{KN}$, el lado $\overline{LM}$ está en $y = b$ y $\overline{KN}$ está en $y = -b$.
   - Así, los vértices son $K(-a, -b)$, $L(-a, b)$, $M(a, b)$ y $N(a, -b)$.

3. **Igualdad de áreas de $\triangle SML$ y $\triangle RNM$:**
   - Para $\triangle SML$, la base es $ML = 2a$ (sobre la recta $y = b$) y la altura desde $S(0,12)$ es $12 - b$:
     $$\text{Área}(\triangle SML) = \frac{1}{2}(2a)(12 - b) = a(12 - b)$$
   - Para $\triangle RNM$, la base es $NM = 2b$ (sobre la recta $x = a$) y la altura desde $R(36,0)$ es $36 - a$:
     $$\text{Área}(\triangle RNM) = \frac{1}{2}(2b)(36 - a) = b(36 - a)$$
   - Igualando ambas áreas:
     $$a(12 - b) = b(36 - a) \implies 12a - ab = 36b - ab \implies 12a = 36b \implies a = 3b$$

4. **Cálculo del área de $KLMN$:**
   - Sustituyendo $a = 3b$ en $a^2 + b^2 = 16$:
     $$(3b)^2 + b^2 = 16 \implies 10b^2 = 16 \implies b^2 = \frac{8}{5}$$
   - El área del rectángulo $KLMN$ es:
     $$\text{Área}(KLMN) = (2a)(2b) = 4ab = 4(3b)b = 12b^2 = 12 \cdot \frac{8}{5} = \frac{96}{5}$$

Como $m = 96$ y $n = 5$ son enteros positivos coprimos, tenemos $m + n = 96 + 5 = 101$.

\boxed{101}