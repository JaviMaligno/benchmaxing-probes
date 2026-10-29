Analicemos el juego paso a paso:

**Planteamiento:** Sea $P$ la probabilidad de que Alice gane el juego.

**Turno de Alice:**
- Con probabilidad $\frac{1}{2}$ saca cara y gana inmediatamente.
- Con probabilidad $\frac{1}{2}$ saca cruz y el turno pasa a Bob.

**Turno de Bob:**
- Con probabilidad $\frac{1}{2}$ saca cruz y Bob gana (Alice pierde).
- Con probabilidad $\frac{1}{2}$ saca cara y el turno vuelve a Alice, donde la situación es idéntica al inicio del juego.

**Ecuación:** Alice gana si gana en su primer lanzamiento, o si ambos "fallan" y el juego se reinicia:

$$P = \frac{1}{2} + \frac{1}{2} \cdot \frac{1}{2} \cdot P$$

Resolviendo:

$$P = \frac{1}{2} + \frac{P}{4} \implies \frac{3P}{4} = \frac{1}{2} \implies P = \frac{2}{3}$$

**Verificación con serie geométrica:** Alice gana en la ronda $n$ (con $n = 0, 1, 2, \dots$) con probabilidad $\left(\frac{1}{4}\right)^n \cdot \frac{1}{2}$, así que:

$$P = \sum_{n=0}^{\infty} \frac{1}{2}\left(\frac{1}{4}\right)^n = \frac{1/2}{1 - 1/4} = \frac{2}{3}$$

$$\boxed{\dfrac{2}{3}}$$