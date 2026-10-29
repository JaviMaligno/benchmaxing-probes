# Solución paso a paso

## Planteamiento

El trabajador deposita \$20,000 al final de cada año. Con interés compuesto anual $r$, el valor de cada depósito al final del tercer año es:

- **Depósito 1** (fin del año 1): acumula intereses durante 2 años → $20000(1+r)^2$
- **Depósito 2** (fin del año 2): acumula intereses durante 1 año → $20000(1+r)$
- **Depósito 3** (fin del año 3): no acumula intereses → $20000$

## Ecuación

$$20000\left[(1+r)^2 + (1+r) + 1\right] \geq 66200$$

Dividiendo entre 200:

$$(1+r)^2 + (1+r) + 1 \geq 3.31$$

Con $x = 1+r$:

$$x^2 + x - 2.31 \geq 0$$

## Resolución

$$x = \frac{-1 + \sqrt{1 + 4(2.31)}}{2} = \frac{-1 + \sqrt{10.24}}{2} = \frac{-1 + 3.2}{2} = 1.1$$

Por lo tanto, $1 + r = 1.1$, es decir, $r = 0.10 = 10\%$.

## Verificación

$$20000(1.1)^2 + 20000(1.1) + 20000 = 24200 + 22000 + 20000 = 66200 \checkmark$$

La tasa mínima requerida es:

\boxed{10}