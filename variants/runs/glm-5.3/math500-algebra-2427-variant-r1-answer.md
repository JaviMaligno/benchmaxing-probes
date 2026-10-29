# Solución paso a paso

**Planteamiento del problema:**

La enfermera deposita $25{,}000 al final de cada año. Queremos que el total al final del tercer año (justo al hacer el tercer depósito) sea al menos $84{,}360.

**Valor de cada depósito al final del año 3** (con tasa compuesta anual $r$):

- **Depósito 1** (fin del año 1): capitaliza 2 años → $25000(1+r)^2$
- **Depósito 2** (fin del año 2): capitaliza 1 año → $25000(1+r)$
- **Depósito 3** (fin del año 3): no capitaliza → $25000$

**Ecuación:**

$$25000\left[(1+r)^2 + (1+r) + 1\right] \ge 84360$$

Dividiendo entre 25000:

$$(1+r)^2 + (1+r) + 1 \ge 3.3744$$

Haciendo $x = 1+r$:

$$x^2 + x - 2.3744 = 0$$

**Resolviendo con la fórmula cuadrática:**

$$x = \frac{-1 + \sqrt{1 + 4(2.3744)}}{2} = \frac{-1 + \sqrt{10.4976}}{2} = \frac{-1 + 3.24}{2} = \frac{2.24}{2} = 1.12$$

Por lo tanto, $r = 0.12$.

**Verificación:**

$$25000(1.12)^2 + 25000(1.12) + 25000 = 31360 + 28000 + 25000 = 84360 \checkmark$$

\boxed{12}