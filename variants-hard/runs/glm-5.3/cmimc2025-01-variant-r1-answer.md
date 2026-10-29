# Resolución paso a paso

**Velocidad inicial de Sam:** un tercio de la velocidad de Rosa = (1/3)(3) = **1 mph**.

**Tiempos de llegada de los otros corredores (1 milla):**
- Priya (12 mph): $\frac{1}{12}$ horas
- Quinn (6 mph): $\frac{1}{6}$ horas
- Rosa (3 mph): $\frac{1}{3}$ horas

**Velocidad de Sam por tramos** (se duplica cada vez que alguien termina):

| Tramo | Velocidad | Duración | Distancia recorrida |
|---|---|---|---|
| $0 \le t < \frac{1}{12}$ | 1 mph | $\frac{1}{12}$ h | $\frac{1}{12}$ mi |
| $\frac{1}{12} \le t < \frac{1}{6}$ | 2 mph | $\frac{1}{12}$ h | $\frac{1}{6}$ mi |
| $\frac{1}{6} \le t < \frac{1}{3}$ | 4 mph | $\frac{1}{6}$ h | $\frac{2}{3}$ mi |

**Distancia acumulada cuando Rosa termina** ($t = \frac{1}{3}$):
$$\frac{1}{12} + \frac{1}{6} + \frac{2}{3} = \frac{1}{12} + \frac{2}{12} + \frac{8}{12} = \frac{11}{12} \text{ millas}$$

A Sam le falta $\frac{1}{12}$ de milla. Tras el tercer doblez, su velocidad es $1 \to 2 \to 4 \to 8$ mph, así que corre a **8 mph**:
$$t_{\text{extra}} = \frac{1/12}{8} = \frac{1}{96} \text{ horas}$$

**Tiempo total:**
$$\frac{1}{3} + \frac{1}{96} = \frac{32}{96} + \frac{1}{96} = \frac{33}{96} = \frac{11}{32} \text{ horas}$$

$\boxed{\dfrac{11}{32}}$