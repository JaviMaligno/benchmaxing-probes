Para encontrar la probabilidad de que Alice gane el juego, podemos analizar los posibles resultados en cada ronda asumiendo una moneda justa (donde la probabilidad de obtener cara es $\frac{1}{2}$ y la de obtener cruz es $\frac{1}{2}$):

1. **Primer turno (turno de Alice):**
   - Alice lanza la moneda. Obtiene cara y gana inmediatamente con probabilidad $\frac{1}{2}$.
   - Obtiene cruz con probabilidad $\frac{1}{2}$, en cuyo caso el turno pasa a Bob.

2. **Segundo turno (turno de Bob):**
   - Si el juego llega al turno de Bob (lo cual ocurre con probabilidad $\frac{1}{2}$), Bob lanza la moneda.
   - Bob obtiene cruz y gana con probabilidad $\frac{1}{2}$ (probabilidad total de $\frac{1}{2} \times \frac{1}{2} = \frac{1}{4}$).
   - Bob obtiene cara con probabilidad $\frac{1}{2}$, devolviendo el turno a Alice. La probabilidad de que ambos fallen en la primera ronda y el juego vuelva exactamente al estado inicial es $\frac{1}{2} \times \frac{1}{2} = \frac{1}{4}$.

3. **Planteamiento de la ecuación:**
   Sea $P$ la probabilidad de que Alice gane el juego. Dado que el juego se reinicia con probabilidad $\frac{1}{4}$, tenemos:
   $$P = \frac{1}{2} + \frac{1}{4}P$$

4. **Resolución:**
   Restando $\frac{1}{4}P$ en ambos lados de la ecuación:
   $$\frac{3}{4}P = \frac{1}{2}$$
   Multiplicando ambos lados por $\frac{4}{3}$:
   $$P = \frac{1}{2} \times \frac{4}{3} = \frac{2}{3}$$

\boxed{\frac{2}{3}}