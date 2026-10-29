# Resolución paso a paso

## Paso 1: Establecer las distancias desde $B_1$

Sea $r_i = B_1B_i$ para $i = 2, 3, \ldots, 11$, y sea $\theta_i = \angle B_iB_1B_{i+1}$.

Dado que $\cos\theta_i = \frac{4}{5}$, tenemos $\sin\theta_i = \frac{3}{5}$.

## Paso 2: Usar la condición de área

El área del triángulo $B_iB_1B_{i+1}$ es:
$$\frac{1}{2}r_i \cdot r_{i+1} \cdot \sin\theta_i = 1 \implies \frac{1}{2}r_i r_{i+1} \cdot \frac{3}{5} = 1 \implies r_i r_{i+1} = \frac{10}{3}$$

Esto vale para todo $i = 2, \ldots, 10$. De la cadena de ecuaciones:
$$r_2 r_3 = r_3 r_4 = r_4 r_5 = \cdots = r_{10} r_{11} = \frac{10}{3}$$

Se deduce que $r_2 = r_4 = r_6 = r_8 = r_{10} = a$ y $r_3 = r_5 = r_7 = r_9 = r_{11} = b$, con $ab = \frac{10}{3}$.

## Paso 3: Calcular las longitudes de los lados interiores

Por la ley de cosenos en cada triángulo $B_iB_1B_{i+1}$:
$$B_iB_{i+1}^2 = r_i^2 + r_{i+1}^2 - 2r_ir_{i+1}\cos\theta_i = r_i^2 + r_{i+1}^2 - 2\cdot\frac{10}{3}\cdot\frac{4}{5} = r_i^2 + r_{i+1}^2 - \frac{16}{3}$$

Tanto si $(r_i, r_{i+1}) = (a,b)$ como $(b,a)$, el resultado es $a^2 + b^2 - \frac{16}{3}$. Por tanto, **los 9 lados** $B_2B_3, B_3B_4, \ldots, B_{10}B_{11}$ tienen la misma longitud $s$, donde:
$$s^2 = a^2 + b^2 - \frac{16}{3}$$

## Paso 4: Aplicar la condición del perímetro

$$B_1B_2 + B_2B_3 + \cdots + B_{10}B_{11} + B_{11}B_1 = a + 9s + b = 20$$
$$s = \frac{20 - (a+b)}{9}$$

## Paso 5: Resolver para $u = a + b$

Sea $u = a + b$. Como $ab = \frac{10}{3}$:
$$a^2 + b^2 = u^2 - 2ab = u^2 - \frac{20}{3}$$
$$s^2 = u^2 - \frac{20}{3} - \frac{16}{3} = u^2 - 12$$

Igualando con $s^2 = \frac{(20-u)^2}{81}$:

$$\frac{(20-u)^2}{81} = u^2 - 12$$
$$(20-u)^2 = 81u^2 - 972$$
$$400 - 40u + u^2 = 81u^2 - 972$$
$$80u^2 + 40u - 1372 = 0$$
$$20u^2 + 10u - 343 = 0$$

Aplicando la fórmula cuadrática:
$$u = \frac{-10 + \sqrt{100 + 4(20)(343)}}{40} = \frac{-10 + \sqrt{27540}}{40}$$

Factorizando: $27540 = 324 \times 85$, así que $\sqrt{27540} = 18\sqrt{85}$.

$$u = \frac{-10 + 18\sqrt{85}}{40} = \frac{9\sqrt{85} - 5}{20}$$

## Paso 6: Identificar $m, n, p, q$

$$B_1B_2 + B_1B_{11} = \frac{9\sqrt{85} - 5}{20}$$

- $m = 9$, $n = 85 = 5 \times 17$ (libre de cuadrados ✓)
- $p = 5$, $q = 20$
- Ningún primo divide a la vez $9$, $5$ y $20$ ✓

$$m + n + p + q = 9 + 85 + 5 + 20 = \boxed{119}$$