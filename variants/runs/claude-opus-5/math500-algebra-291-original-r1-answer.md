## Planteamiento

Sea $P$ la probabilidad de que Alice gane, estando a punto de lanzar ella.

**Caso 1:** Alice saca cara (probabilidad $1/2$) → gana inmediatamente.

**Caso 2:** Alice saca cruz (probabilidad $1/2$) → pasa el turno a Bob:
- Bob saca cruz (probabilidad $1/2$) → Bob gana, Alice pierde.
- Bob saca cara (probabilidad $1/2$) → vuelve el turno a Alice, y la situación es idéntica a la inicial, así que la probabilidad de que Alice gane desde ahí vuelve a ser $P$.

## Ecuación

$$P = \frac{1}{2} + \frac{1}{2}\cdot\frac{1}{2}\cdot P = \frac{1}{2} + \frac{P}{4}$$

$$P - \frac{P}{4} = \frac{1}{2} \quad\Longrightarrow\quad \frac{3P}{4} = \frac{1}{2} \quad\Longrightarrow\quad P = \frac{2}{3}$$

## Verificación por serie

Alice gana en su lanzamiento número $k$ si antes hubo $k-1$ rondas completas fallidas (cada una con probabilidad $1/4$) y luego ella saca cara:

$$P = \sum_{k=1}^{\infty} \left(\frac{1}{4}\right)^{k-1}\cdot\frac{1}{2} = \frac{1/2}{1 - 1/4} = \frac{2}{3}$$

Coincide. La ventaja de Alice proviene únicamente de lanzar primero.

$$\boxed{\dfrac{2}{3}}$$