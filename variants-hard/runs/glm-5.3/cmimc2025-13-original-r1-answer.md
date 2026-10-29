## Planteamiento

Cada ronda elimina a 3 personas (quedan 4 elegidos, el ganador se queda). Entonces el número de jugadores pasa por $34, 31, 28, \dots, 7, 4, 1$: hay exactamente **11 rondas**, y siempre hay al menos 4 jugadores disponibles.

«Batallar en la misma ronda» significa que Michael y James están **ambos entre los 4 elegidos** en alguna ronda. Observación clave: si ambos son elegidos, solo uno puede ganar, así que al menos uno se va — pueden enfrentarse a lo sumo una vez.

## Recurrencia

Sea $p_n$ la probabilidad de que Michael y James (ambos vivos, sin haberse enfrentado) batallen en el futuro, habiendo $n$ jugadores vivos. En una ronda con $n$ jugadores:

- **Ambos elegidos:** $\dfrac{\binom{n-2}{2}}{\binom{n}{4}} = \dfrac{12}{n(n-1)}$ → se enfrentan. ✓
- **Exactamente uno elegido:** $\dfrac{2\binom{n-2}{3}}{\binom{n}{4}} = \dfrac{8(n-4)}{n(n-1)}$; gana con prob. $\tfrac14$ (ambos vivos con $n-3$), pierde con $\tfrac34$ (nunca se enfrentan).
- **Ninguno elegido:** $\dfrac{\binom{n-2}{4}}{\binom{n}{4}} = \dfrac{(n-4)(n-5)}{n(n-1)}$ → ambos vivos con $n-3$.

Combinando los dos últimos casos (ambos sobreviven con prob. $\frac{(n-4)(n-3)}{n(n-1)}$):

$$p_n = \frac{12}{n(n-1)} + \frac{(n-4)(n-3)}{n(n-1)}\, p_{n-3}, \qquad p_4 = 1.$$

## Resolución: $p_n = \dfrac{4}{n}$

**Caso base:** $p_4 = 1 = \frac{4}{4}$ ✓ (con 4 jugadores, todos son elegidos).

**Paso inductivo:** sustituyendo $p_{n-3} = \frac{4}{n-3}$:

$$p_n = \frac{12}{n(n-1)} + \frac{(n-4)(n-3)}{n(n-1)}\cdot\frac{4}{n-3} = \frac{12 + 4(n-4)}{n(n-1)} = \frac{4(n-1)}{n(n-1)} = \frac{4}{n}. ✓$$

**Comprobación con $n=7$:** directo: $p_7 = \frac{2}{7}$ (elegidos juntos en la ronda 1) $+ \frac{2}{7}$ (ambos sobreviven hasta las últimas 4 posiciones, donde seguro coinciden) $= \frac{4}{7}$ ✓.

**Comprobación adicional (telescopio):** la probabilidad de que se enfrenten en la ronda $k$-ésima resulta ser exactamente $\frac{2}{187}$ en *cada* una de las 11 rondas (en la ronda 1 es $\frac{12}{34\cdot 33} = \frac{2}{187}$; los factores de supervivencia se cancelan con el factor $\frac{12}{n_k(n_k-1)}$ en las demás). Total: $11 \cdot \frac{2}{187} = \frac{22}{187} = \frac{2}{17}$ ✓.

## Conclusión

$$p_{34} = \frac{4}{34} = \frac{2}{17}$$

\boxed{\dfrac{2}{17}}