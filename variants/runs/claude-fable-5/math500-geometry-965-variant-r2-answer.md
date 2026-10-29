Analicemos el problema paso a paso.

**Configuración.** Sea $\angle RPS = \theta$. Como $\overline{PR}$ biseca $\angle QPS$, también $\angle QPR = \theta$. Como $\overline{PS}\parallel\overline{QR}$, los ángulos alternos dan $\angle PRQ = \angle RPS = \theta$. Entonces el triángulo $PQR$ es isósceles con $QP = QR$.

**Coordenadas.** Pongamos $P=(0,0)$, $S=(a,0)$ con $PS=a$. Como $\angle PRS = 90^\circ$ en el triángulo rectángulo $PRS$, se tiene $PR = a\cos\theta$, y por lo tanto
$$R = (a\cos^2\theta,\; a\cos\theta\sin\theta).$$
La altura del trapezoide es $h = a\cos\theta\sin\theta = \tfrac{a}{2}\sin 2\theta$.

El vértice $Q$ cumple $\angle QPS = 2\theta$ y $PQ = QR = b$, así que $Q = (b\cos 2\theta,\; b\sin 2\theta)$. Como $Q$ y $R$ están a la misma altura:
$$b\sin 2\theta = \tfrac{a}{2}\sin 2\theta \;\Longrightarrow\; b = \tfrac{a}{2}.$$
(Se verifica que $QR = R_x - Q_x = \tfrac{a}{2}(1+\cos 2\theta) - \tfrac{a}{2}\cos 2\theta = \tfrac{a}{2}$, consistente.)

**Áreas.** El área del trapezoide es
$$[PQRS] = \frac{1}{2}(PS + QR)\,h = \frac{1}{2}\left(a + \frac{a}{2}\right)h = \frac{3}{4}\,a h = 45 \;\Longrightarrow\; ah = 60.$$

El triángulo $PRS$ tiene base $PS = a$ y altura $h$ (la ordenada de $R$):
$$[\triangle PRS] = \frac{1}{2}\,a h = \frac{60}{2} = 30.$$

$$\boxed{30}$$