## Planteamiento

Con 45 jugadores, cada ronda elimina a 4 (entran 5, queda 1), así que el juego dura exactamente $(45-1)/4 = 11$ rondas.

**Recursión.** Sea $p(n)$ la probabilidad de que Priya y Tomás lleguen a bailar juntos, dado que ambos siguen en el círculo con $n$ jugadores. Al elegir 5 al azar:

- ambos elegidos: $\dfrac{20}{n(n-1)}$ → se encuentran;
- exactamente uno elegido: $\dfrac{10(n-5)}{n(n-1)}$ → solo sirve si ese gana (prob. $1/5$), y entonces quedan $n-4$;
- ninguno elegido: $\dfrac{(n-5)(n-6)}{n(n-1)}$ → quedan $n-4$.

Entonces
$$p(n)=\frac{20}{n(n-1)}+\frac{2(n-5)+(n-5)(n-6)}{n(n-1)}\,p(n-4)=\frac{20}{n(n-1)}+\frac{(n-4)(n-5)}{n(n-1)}\,p(n-4).$$

Definiendo $S(n)=n(n-1)p(n)$, la recursión se simplifica a
$$S(n)=20+S(n-4),\qquad S(5)=5\cdot 4\cdot 1=20.$$

Como $45 = 5 + 4\cdot 10$, resulta $S(45)=20+10\cdot 20=220$, y por tanto
$$p(45)=\frac{220}{45\cdot 44}=\frac{220}{1980}=\frac19 .$$

**Verificación por simetría.** En las 11 rondas se forman $11\cdot\binom52 = 110$ parejas que coinciden. Por simetría, las $\binom{45}{2}=990$ parejas posibles son equiprobables, así que la probabilidad para una pareja fija es $110/990 = 1/9$. ✓

\boxed{\dfrac{1}{9}}