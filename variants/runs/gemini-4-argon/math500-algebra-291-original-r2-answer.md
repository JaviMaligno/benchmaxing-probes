Para encontrar la probabilidad de que Alice gane el juego, podemos analizar los posibles resultados turno por turno (asumiendo una moneda justa con probabilidad $\frac{1}{2}$ para cara y $\frac{1}{2}$ para cruz):

1. **Primer turno (turno de Alice):**
   - Alice lanza la moneda y obtiene cara con probabilidad $\frac{1}{2}$, ganando el juego inmediatamente.
   - Con probabilidad $\frac{1}{2}$, obtiene cruz y el turno pasa a Bob.

2. **Segundo turno (turno de Bob):**
   - Si el juego llega al turno de Bob, Bob lanza la moneda y obtiene cruz con probabilidad $\frac{1}{2}$, ganando el juego.
   - Con probabilidad $\frac{1}{2}$, obtiene cara y el turno regresa a Alice.

3. **Ecuación de recurrencia:**
   - Sea $P$ la probabilidad de que Alice gane el juego.
   - Si tanto Alice como Bob fallan en sus primeros intentos (lo cual ocurre con probabilidad $\frac{1}{2} \times \frac{1}{2} = \frac{1}{4}$), el juego vuelve exactamente a su estado inicial, donde la probabilidad de que Alice gane vuelve a ser $P$.
   - Por lo tanto, podemos plantear la siguiente ecuación:
     $$P = \frac{1}{2} + \frac{1}{4}P$$

4. **Resolución:**
   - Restamos $\frac{1}{4}P$ en ambos lados:
     $$\frac{3}{4}P = \frac{1}{2}$$
   - Despejamos $P$:
     $$P = \frac{1/2}{3/4} = \frac{2}{3}$$

\boxed{\frac{2}{3}}