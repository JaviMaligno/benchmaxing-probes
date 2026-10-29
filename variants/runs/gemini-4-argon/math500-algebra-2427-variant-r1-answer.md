Para encontrar la tasa de interés compuesto mínima anual, representemos la tasa de interés como $r$ (en forma decimal).

1. **Al final del primer año:** Se realiza el primer depósito de $\$25{,}000$.
   $$\text{Saldo}_1 = 25{,}000$$

2. **Al final del segundo año:** El primer depósito habrá generado intereses durante un año y se suma el segundo depósito de $\$25{,}000$.
   $$\text{Saldo}_2 = 25{,}000(1 + r) + 25{,}000$$

3. **Al final del tercer año:** El primer depósito habrá acumulado intereses durante dos años, el segundo depósito durante un año, y se realiza el tercer depósito de $\$25{,}000$.
   $$\text{Saldo}_3 = 25{,}000(1 + r)^2 + 25{,}000(1 + r) + 25{,}000$$

Se requiere que este monto total sea al menos $\$84{,}360$:
$$25{,}000(1 + r)^2 + 25{,}000(1 + r) + 25{,}000 \ge 84{,}360$$

Dividiendo ambos lados de la desigualdad entre $25{,}000$:
$$(1 + r)^2 + (1 + r) + 1 \ge \frac{84{,}360}{25{,}000}$$
$$(1 + r)^2 + (1 + r) + 1 \ge 3.3744$$

Sea $x = 1 + r$. Reordenando los términos para formar una ecuación cuadrática:
$$x^2 + x - 2.3744 \ge 0$$

Aplicando la fórmula general para ecuaciones de segundo grado:
$$x = \frac{-1 \pm \sqrt{1^2 - 4(1)(-2.3744)}}{2}$$
$$x = \frac{-1 \pm \sqrt{1 + 9.4976}}{2}$$
$$x = \frac{-1 \pm \sqrt{10.4976}}{2}$$

Como $3.24^2 = 10.4976$, tenemos que $\sqrt{10.4976} = 3.24$. Tomando la raíz positiva (ya que $1 + r > 0$):
$$x = \frac{-1 + 3.24}{2} = \frac{2.24}{2} = 1.12$$

Dado que $x = 1 + r$, obtenemos:
$$1 + r = 1.12 \implies r = 0.12$$

Expresado como porcentaje, $r = 12\%$.

\boxed{12}