Para que exista un triángulo con lados $2$, $a$ y $b$, deben cumplirse las desigualdades triangulares:

1. $a + b > 2$
2. $2 + a > b$, es decir, $b - a < 2$
3. $2 + b > a$, es decir, $a - b < 2$

Las condiciones 2 y 3 juntas equivalen a $|a - b| < 2$.

**Cálculo geométrico:** el espacio muestral es el cuadrado $(0,4) \times (0,4)$, con área $16$. Calculo el área de las regiones donde **falla** alguna condición:

- **Falla $a + b > 2$:** la región $a + b \le 2$ es un triángulo con catetos de longitud $2$, de área $\frac{1}{2} \cdot 2 \cdot 2 = 2$.
- **Falla $a - b < 2$:** la región $a - b \ge 2$ es el triángulo con vértices $(2,0)$, $(4,0)$, $(4,2)$, de área $2$.
- **Falla $b - a < 2$:** por simetría, otro triángulo de área $2$.

Estas tres regiones no se solapan entre sí (por ejemplo, $a+b \le 2$ exige $a \le 2$, mientras que $a - b \ge 2$ exige $a \ge 2$, y la intersección tiene área cero; las dos franjas de las esquinas opuestas tampoco se tocan).

Área desfavorable total: $2 + 2 + 2 = 6$.

Área favorable: $16 - 6 = 10$.

Probabilidad: $\dfrac{10}{16} = \dfrac{5}{8}$.

$$\boxed{\dfrac{5}{8}}$$