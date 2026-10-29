Razonamiento paso a paso:

**Paso 1: Analizar el primer turno de Alice.**
- Con probabilidad 1/2, Alice saca cara y gana inmediatamente.
- Con probabilidad 1/2, saca cruz y pasa al turno de Bob.

**Paso 2: Analizar el turno de Bob.**
- Con probabilidad 1/2, Bob saca cruz y gana inmediatamente.
- Con probabilidad 1/2, saca cara y el turno vuelve a Alice, quedando el juego en el estado inicial.

**Paso 3: Plantear la ecuación recursiva.**
Sea $P$ la probabilidad de que Alice gane. Después de un ciclo completo (Alice falla y Bob falla), que ocurre con probabilidad $\frac{1}{2}\cdot\frac{1}{2} = \frac{1}{4}$, el juego vuelve a su estado inicial. Por lo tanto:

$$P = \frac{1}{2} + \frac{1}{4}P$$

**Paso 4: Resolver la ecuación.**
$$P - \frac{1}{4}P = \frac{1}{2} \quad\Rightarrow\quad \frac{3}{4}P = \frac{1}{2} \quad\Rightarrow\quad P = \frac{1}{2}\cdot\frac{4}{3} = \frac{2}{3}$$

**Verificación por suma de serie:** Alice gana en la ronda $k$ si sobrevive $k-1$ ciclos completos (probabilidad $(1/4)^{k-1}$) y luego saca cara:
$$\sum_{k=1}^{\infty}\left(\frac{1}{4}\right)^{k-1}\cdot\frac{1}{2} = \frac{1/2}{1-1/4} = \frac{2}{3}\checkmark$$

También se confirma con la probabilidad de Bob: $P(\text{Bob}) = \frac{1}{4}\cdot\frac{1}{1/4+1/2}\cdot\ldots$ o más directamente, $P(\text{Bob}) = \frac{1}{4} + \frac{1}{4}P(\text{Bob}) \Rightarrow \frac{1}{3}$, y en efecto $\frac{2}{3}+\frac{1}{3}=1$.

\boxed{\dfrac{2}{3}}