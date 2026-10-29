Analicemos el proceso paso a paso.

**Estructura del juego:** Cada ronda, 5 personas bailan y 4 se eliminan, así que el número de jugadores baja de 4 en 4: 45 → 41 → 37 → ... → 5 → 1. El número total de rondas es (45 − 1)/4 = **11 rondas**.

**Conteo de parejas que bailan juntas:** En cada ronda bailan 5 personas, lo que genera C(5,2) = 10 parejas que comparten pista esa ronda. Un detalle clave: si dos personas bailan juntas en una ronda, a lo sumo una sobrevive (el ganador se queda, los otros cuatro se van), así que **ninguna pareja puede bailar junta dos veces**. Por lo tanto, en todo el juego hay exactamente 11 × 10 = **110 parejas distintas** que bailan en la misma ronda, y esto es determinista (siempre son 110, sin importar cómo salgan los sorteos).

**Simetría:** Todos los jugadores son intercambiables (las selecciones son uniformes y todos ganan con igual probabilidad), de modo que cada una de las C(45,2) = 990 parejas posibles tiene la misma probabilidad de ser una de esas 110 parejas. Como el número esperado de parejas que bailan juntas es exactamente 110, la probabilidad para una pareja concreta como Priya y Tomas es:

$$P = \frac{110}{990} = \frac{1}{9}$$

$$\boxed{\dfrac{1}{9}}$$