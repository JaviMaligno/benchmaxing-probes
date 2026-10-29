**Planteamiento.** Los lados $2$, $a$, $b$ forman un triángulo si y solo si se cumplen las tres desigualdades triangulares:

1. $a + b > 2$
2. $2 + a > b \iff b - a < 2$
3. $2 + b > a \iff a - b < 2$

Las condiciones 2 y 3 juntas equivalen a $|a - b| < 2$.

**Geometría en el cuadrado $(0,4)^2$.** El espacio muestral es un cuadrado de área $16$. Calculo el área de las regiones donde **falla** alguna condición:

- **Falla $a+b>2$:** la región $a+b \le 2$ es un triángulo con vértices $(0,0)$, $(2,0)$, $(0,2)$, de área $\frac{1}{2}\cdot 2\cdot 2 = 2$.
- **Falla $a - b < 2$:** la región $a - b \ge 2$ es un triángulo con vértices $(2,0)$, $(4,0)$, $(4,2)$, de área $2$.
- **Falla $b - a < 2$:** por simetría, otro triángulo de área $2$.

Estas tres regiones son disjuntas (por ejemplo, $a-b\ge 2$ exige $a\ge 2$, incompatible con $a+b\le 2$ para $b>0$). Área total desfavorable: $2+2+2 = 6$.

**Probabilidad.** Área favorable $= 16 - 6 = 10$, así que

$$P = \frac{10}{16} = \frac{5}{8}$$

$$\boxed{\dfrac{5}{8}}$$