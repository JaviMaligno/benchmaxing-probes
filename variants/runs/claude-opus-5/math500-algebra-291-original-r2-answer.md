## Planteamiento

Sea $P$ la probabilidad de que Alice gane, partiendo de un turno de Alice.

**Caso 1:** Alice saca cara (probabilidad $1/2$) → gana inmediatamente.

**Caso 2:** Alice saca cruz (probabilidad $1/2$) → pasa el turno a Bob.
- Bob saca cruz (probabilidad $1/2$) → Bob gana, Alice pierde.
- Bob saca cara (probabilidad $1/2$) → el turno vuelve a Alice, y la situación es **idéntica** a la inicial, así que la probabilidad vuelve a ser $P$.

## Ecuación

$$P = \frac{1}{2} + \frac{1}{2}\cdot\frac{1}{2}\cdot P = \frac{1}{2} + \frac{P}{4}$$

$$\frac{3}{4}P = \frac{1}{2} \quad\Longrightarrow\quad P = \frac{2}{3}$$

## Verificación por serie

Alice gana en su lanzamiento número $k$ si antes hubo $k-1$ rondas completas fallidas (cada ronda fallida requiere cruz de Alice y cara de Bob, probabilidad $1/4$) y luego cara:

$$P = \sum_{k=1}^{\infty} \left(\frac{1}{4}\right)^{k-1}\cdot\frac{1}{2} = \frac{1/2}{1 - 1/4} = \frac{1/2}{3/4} = \frac{2}{3}$$

Coincide. La ventaja de empezar es considerable: Alice gana dos de cada tres partidas.

$$\boxed{\dfrac{2}{3}}$$