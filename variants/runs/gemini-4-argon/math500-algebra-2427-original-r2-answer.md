Para encontrar la tasa de interés compuesto mínima necesaria, planteamos el saldo de la cuenta al final de cada uno de los tres años.

Sea $r$ la tasa de interés anual (en forma decimal) y sea $x = 1 + r$ el factor de capitalización anual:

1. **Al final del primer año:** Se realiza el primer depósito de $\$20{,}000$. Este depósito acumulará intereses durante $2$ años (el segundo y el tercer año), por lo que al final del tercer año su valor será:
   $$20{,}000(1 + r)^2$$

2. **Al final del segundo año:** Se realiza el segundo depósito de $\$20{,}000$. Este monto acumulará intereses durante $1$ año (el tercer año), alcanzando un valor de:
   $$20{,}000(1 + r)$$

3. **Al final del tercer año:** Se realiza el tercer depósito de $\$20{,}000$, el cual no acumula intereses adicionales en ese momento:
   $$20{,}000$$

La suma total al final del tercer año debe ser de al menos $\$66{,}200$:
$$20{,}000(1 + r)^2 + 20{,}000(1 + r) + 20{,}000 \ge 66{,}200$$

Dividiendo ambos lados de la desigualdad entre $20{,}000$:
$$(1 + r)^2 + (1 + r) + 1 \ge \frac{66{,}200}{20{,}000}$$
$$(1 + r)^2 + (1 + r) + 1 \ge 3.31$$

Sustituyendo $x = 1 + r$ y pasando todos los términos a un lado para encontrar el valor mínimo:
$$x^2 + x - 2.31 = 0$$

Aplicando la fórmula general para ecuaciones de segundo grado:
$$x = \frac{-1 \pm \sqrt{1^2 - 4(1)(-2.31)}}{2} = \frac{-1 \pm \sqrt{1 + 9.24}}{2} = \frac{-1 \pm \sqrt{10.24}}{2}$$

Como $\sqrt{10.24} = 3.2$ y $x$ debe ser positivo:
$$x = \frac{-1 + 3.2}{2} = \frac{2.2}{2} = 1.1$$

Recordando que $x = 1 + r$:
$$1 + r = 1.1 \implies r = 0.1$$

Expresado como porcentaje, $r = 10\%$.

\boxed{10}