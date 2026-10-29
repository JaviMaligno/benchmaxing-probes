**Solución.**

La clave está en factorizar la recurrencia. Observemos que:

$$a_{n+1} + 2 = a_n^3 + 5a_n^2 + 10a_n + 8 = (a_n+2)(a_n^2+3a_n+4),$$

ya que $a_n = -2$ anula el polinomio cúbico.

Ahora busquemos escribir el término general como diferencia telescópica. Calculemos:

$$\frac{1}{a_n+2} - \frac{2}{a_{n+1}+2} = \frac{1}{a_n+2} - \frac{2}{(a_n+2)(a_n^2+3a_n+4)} = \frac{a_n^2+3a_n+4-2}{(a_n+2)(a_n^2+3a_n+4)}.$$

Como $a_n^2+3a_n+2 = (a_n+1)(a_n+2)$, esto se simplifica a:

$$\frac{(a_n+1)(a_n+2)}{(a_n+2)(a_n^2+3a_n+4)} = \frac{a_n+1}{a_n^2+3a_n+4}.$$

Por lo tanto, multiplicando por $2^n$:

$$\frac{2^n(a_n+1)}{a_n^2+3a_n+4} = \frac{2^n}{a_n+2} - \frac{2^{n+1}}{a_{n+1}+2},$$

que es exactamente una suma telescópica. Sumando desde $n=0$ hasta $N$:

$$\sum_{n=0}^{N} \frac{2^n(a_n+1)}{a_n^2+3a_n+4} = \frac{1}{a_0+2} - \frac{2^{N+1}}{a_{N+1}+2}.$$

Como $a_{n+1} \approx a_n^3$, la sucesión $a_n$ crece de forma triplemente exponencial (como $2024^{3^n}$), mientras que $2^{N+1}$ solo crece exponencialmente, así que $\dfrac{2^{N+1}}{a_{N+1}+2} \to 0$.

Entonces la suma vale $\dfrac{1}{a_0+2} = \dfrac{1}{2026}$.

$$\boxed{\dfrac{1}{2026}}$$