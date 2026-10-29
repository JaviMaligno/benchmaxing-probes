## Razonamiento

**Configuración.** Cada ronda elimina exactamente a 4 jugadores (de los 5 elegidos, cuatro se van y uno se queda). Partiendo de 45 jugadores hasta llegar a 1, el número de rondas es
$$\frac{45-1}{4} = 11.$$

**Observación clave: ninguna pareja baila junta dos veces.** Si Priya y Tomas están entre los 5 elegidos en una ronda, solo el ganador de esa ronda se queda; al menos uno de los dos no gana y se va para siempre. Por lo tanto, una vez que dos personas bailan juntas, nunca vuelven a coincidir en otra ronda.

**Conteo de parejas que bailan juntas.** En cada ronda, los 5 elegidos forman $\binom{5}{2} = 10$ parejas que bailan juntas. Como ninguna pareja puede repetirse entre rondas, el número total de parejas *distintas* que bailan juntas a lo largo de todo el juego es, con certeza,
$$10 \times 11 = 110.$$

**Simetría.** El proceso trata a todos los jugadores de manera idéntica (elección uniforme y probabilidad $1/5$ de ganar), así que las $\binom{45}{2} = 990$ parejas posibles tienen exactamente la misma probabilidad de bailar juntas. Sea $X_{ij}$ el indicador de que la pareja $\{i,j\}$ baila junta. Entonces
$$\sum_{i<j} X_{ij} = 110 \quad \text{(siempre)},$$
de modo que por simetría
$$\Pr(\text{Priya y Tomas bailan juntos}) = \mathbb{E}[X_{PT}] = \frac{110}{990} = \frac{1}{9}.$$

**Verificación por recursión.** Con $p_n$ la probabilidad de que bailen juntos quedando $n$ jugadores (ambos dentro), condicionando en la ronda: ambos elegidos con probabilidad $\frac{20}{n(n-1)}$, solo uno elegido (y ganando, prob. $\tfrac15$) o ninguno, se obtiene
$$p_n = \frac{20}{n(n-1)} + \frac{(n-4)(n-5)}{n(n-1)}\,p_{n-4}, \qquad p_5 = 1,$$
cuya solución es $p_n = \frac{5}{n}$. Con $n=45$: $p_{45} = \frac{5}{45} = \frac19$, lo que coincide. ✓

$$\boxed{\dfrac{1}{9}}$$