Resolvamos el problema paso a paso.

Sea el trapecio $PQRS$ con $\overline{PS}\parallel\overline{QR}$, lo que significa que las bases son $PS$ y $QR$.

**Dato 1:** $\overline{PR}\perp\overline{RS}$, es decir, el ángulo en $R$ del triángulo $PRS$ es recto.

**Dato 2:** $\overline{PR}$ biseca $\angle QPS$, es decir, $\angle QPR = \angle RPS$.

Llamemos $\theta = \angle RPS$. Entonces $\angle QPR = \theta$, y por lo tanto $\angle QPS = 2\theta$.

Como $PS \parallel QR$, el ángulo $\angle QPS$ y el ángulo $\angle PQR$ son ángulos internos en el mismo lado de la transversal $PQ$, así que son suplementarios:

$$\angle PQR = 180^\circ - 2\theta.$$

En el triángulo $PQR$, los ángulos son:
- $\angle QPR = \theta$
- $\angle PQR = 180^\circ - 2\theta$
- Entonces $\angle PRQ = 180^\circ - \theta - (180^\circ - 2\theta) = \theta$.

Luego, $\angle QPR = \angle PRQ = \theta$, lo que significa que el triángulo $PQR$ es isósceles con $PQ = QR$.

---

Ahora trabajemos con el triángulo rectángulo $PRS$, con ángulo recto en $R$. Tenemos $\angle RPS = \theta$ y $\angle PRS = 90^\circ$, de modo que $\angle PSR = 90^\circ - \theta$.

Como $PS \parallel QR$, el ángulo $\angle PSR$ y el ángulo $\angle SRQ$ son ángulos internos en el mismo lado, por lo que son suplementarios:

$$\angle SRQ = 180^\circ - (90^\circ - \theta) = 90^\circ + \theta.$$

En el cuadrilátero, consideremos también el ángulo en $S$ y el ángulo en $R$.

Podemos calcular las áreas. Sea:
- $x = PR$ (la altura común / cateto),
- $y = RS$ (el otro cateto del triángulo rectángulo).

Entonces
$$[PRS] = \frac{1}{2}xy.$$

Como $PS \parallel QR$, la distancia (altura) entre las bases es la misma.

En el triángulo rectángulo $PRS$:
$$\tan\theta = \frac{RS}{PR} = \frac{y}{x}.$$

Consideremos ahora el trapecio completo. La base mayor es $PS$ y la base menor es $QR$.

En el triángulo rectángulo $PRS$, por Pitágoras:
$$PS = \sqrt{x^2 + y^2}.$$

Del triángulo isósceles $PQR$, tenemos $PQ = QR$. Usando ley de cosenos con $\angle QPR = \theta$ y lados $PQ = QR$:

$$PR^2 = PQ^2 + QR^2 - 2 \cdot PQ \cdot QR \cdot \cos(180^\circ - 2\theta)$$
$$PR^2 = QR^2 + QR^2 + 2QR^2\cos(2\theta) = 2QR^2(1 + \cos 2\theta) = 4QR^2\cos^2\theta.$$

Entonces
$$PR = 2QR\cos\theta,$$
es decir,
$$x = 2QR\cos\theta \implies QR = \frac{x}{2\cos\theta}.$$

La altura del trapecio es $RS = y$, y sus bases son $PS = \sqrt{x^2+y^2}$ y $QR = \dfrac{x}{2\cos\theta}$.

El área del trapecio es:

$$[PQRS] = \frac{1}{2}(PS + QR) \cdot RS = 45.$$

Sustituimos:
$$\frac{1}{2}\left(\sqrt{x^2+y^2} + \frac{x}{2\cos\theta}\right) y = 45.$$

Tenemos $y = x\tan\theta$ y $\sqrt{x^2+y^2} = x\sqrt{1+\tan^2\theta} = \dfrac{x}{\cos\theta}$.

Entonces:
$$PS = \frac{x}{\cos\theta}, \qquad QR = \frac{x}{2\cos\theta}.$$

Así,
$$\frac{1}{2}\left(\frac{x}{\cos\theta} + \frac{x}{2\cos\theta}\right) x\tan\theta = 45.$$

$$\frac{1}{2} \cdot \frac{3x}{2\cos\theta} \cdot x\tan\theta = 45$$

$$\frac{3x^2\tan\theta}{4\cos\theta} = 45.$$

Como $\tan\theta = \dfrac{\sin\theta}{\cos\theta}$:
$$\frac{3x^2\sin\theta}{4\cos^2\theta} = 45.$$

Ahora, el área del triángulo $[PRS]$ es:
$$[PRS] = \frac{1}{2}xy = \frac{1}{2}x\cdot x\tan\theta = \frac{x^2\tan\theta}{2}.$$

Sustituimos $x^2\tan\theta$ de la ecuación anterior. De 
$$\frac{3x^2\tan\theta}{4\cos\theta} = 45,$$
obtenemos
$$x^2\tan\theta = \frac{45 \cdot 4\cos\theta}{3} = 60\cos\theta.$$

Entonces
$$[PRS] = \frac{60\cos\theta}{2} = 30\cos\theta.$$

Necesitamos determinar $\cos\theta$.

---

**Determinando $\theta$:** Del triángulo rectángulo $PRS$ y de que $PS \parallel QR$, el ángulo en $Q$ interior es $90^\circ+\theta$ (calculado arriba), pero en un trapecio los ángulos adyacentes a un mismo lado son suplementarios, lo que ya usamos. Necesitamos otra relación geométrica.

En realidad, los ángulos en $R$ del trapecio: el ángulo interior en $R$ es $\angle QRS = \angle QRP + \angle PRS$.

Del triángulo $PQR$, $\angle QRP = \theta$ (ya calculado), y $\angle PRS = 90^\circ$. Por lo tanto,

$$\angle QRS = \theta + 90^\circ.$$

El ángulo en $S$ es $\angle PSR = 90^\circ - \theta$.

En un trapecio con $PS \parallel QR$, los ángulos sobre el lado $RS$ son suplementarios:
$$\angle QRS + \angle PSR = (\theta + 90^\circ) + (90^\circ - \theta) = 180^\circ.$$

Esto se cumple automáticamente, no nos da $\theta$.

Necesitamos relacionar las alturas. Como $PS \parallel QR$, la proyección horizontal de $RS$ sobre la dirección de las bases más la longitud de $QR$ debe dar $PS$.

La proyección de $RS$ (que vale $y$) sobre la dirección horizontal (paralela a las bases) es $y\cos(90^\circ -\theta) = y\sin\theta = x\tan\theta\sin\theta = \dfrac{x\sin^2\theta}{\cos\theta}$.

Entonces:
$$PS = QR + RS \cdot \sin\theta$$
(en valor absoluto; aquí la configuración da que $PS$ es la base mayor).

$$\frac{x}{\cos\theta} = \frac{x}{2\cos\theta} + x\tan\theta\sin\theta.$$

Dividimos entre $x$:
$$\frac{1}{\cos\theta} = \frac{1}{2\cos\theta} + \frac{\sin^2\theta}{\cos\theta}.$$

Multiplicando por $\cos\theta$:
$$1 = \frac{1}{2} + \sin^2\theta$$
$$\sin^2\theta = \frac{1}{2}.$$

Por lo tanto $\sin\theta = \dfrac{1}{\sqrt{2}}$, es decir, $\theta = 45^\circ$, y $\cos\theta = \dfrac{1}{\sqrt{2}}$.

Finalmente:
$$[PRS] = 30\cos\theta = 30 \cdot \frac{\sqrt{2}}{2} = 15\sqrt{2}.$$

$$\boxed{15\sqrt{2}}$$