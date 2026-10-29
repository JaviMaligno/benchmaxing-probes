## Resolución

**Configuración de coordenadas.** Coloco $P$ en el origen. Como $\omega_1$ (radio 4) es tangente internamente a $\omega_2$ (radio 20) en $Q$, el centro $O$ de $\omega_2$ cumple $OP = 20 - 4 = 16$. Tomo $Q = (4, 0)$, de modo que $O = (-16, 0)$.

**Puntos R y S.** Como $\overline{QR}$ es diámetro de $\omega_2$: $R = 2O - Q = (-36, 0)$. Como $\overline{PS} \perp \overline{QR}$, $S$ está en la recta vertical $x = 0$ sobre $\omega_2$: $(0+16)^2 + y^2 = 400 \Rightarrow y = \pm 12$. Tomo $S = (0, 12)$.

**El rectángulo.** Con $\overline{KL} \perp \overline{QR}$, los lados $KL$ y $MN$ son verticales. Sea el rectángulo con vértices en $(\pm a, \pm b)$, con $a^2 + b^2 = 16$ (inscrito en $\omega_1$). Las condiciones de cercanía ($R$ más cerca de $\overline{MN}$, $S$ más cerca de $\overline{LM}$) dan:
$$K = (a, -b),\quad L = (a, b),\quad M = (-a, b),\quad N = (-a, -b)$$
así $MN$ es el lado izquierdo (cerca de $R$) y $LM$ el lado superior (cerca de $S$).

**Igualdad de áreas.**
- $\triangle SML$: base $ML = 2a$ (horizontal), altura $12 - b$. Área $= a(12 - b)$.
- $\triangle RNM$: base $NM = 2b$ (vertical), altura $36 - a$. Área $= b(36 - a)$.

Igualando:
$$a(12 - b) = b(36 - a) \;\Rightarrow\; 12a - ab = 36b - ab \;\Rightarrow\; 12a = 36b \;\Rightarrow\; a = 3b$$

**Área del rectángulo.** Sustituyendo en $a^2 + b^2 = 16$: $10b^2 = 16 \Rightarrow b^2 = \tfrac{8}{5}$.

$$\text{Área} = (2a)(2b) = 4ab = 12b^2 = \frac{96}{5}$$

Con $m = 96$ y $n = 5$ coprimos, $m + n = 101$.

$$\boxed{101}$$