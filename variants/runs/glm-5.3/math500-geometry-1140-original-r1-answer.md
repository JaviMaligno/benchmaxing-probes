## Planteamiento

Coloco el triángol en coordenadas: $A = (0,0)$, $B = (17,0)$, y sea $C = (x, y)$ con $y > 0$.

**Paso 1: Encontrar la altura desde $C$.**

El área de $ABC$ por la fórmula de Herón, con $AB = 17$, $AC = 8$, $BC = 15$:

$$s = \frac{17+8+15}{2} = 20, \qquad [ABC] = \sqrt{20(20-17)(20-8)(20-15)} = \sqrt{20 \cdot 3 \cdot 12 \cdot 5} = \sqrt{3600} = 60.$$

Como $AB$ es la base, la altura desde $C$ es $h$:

$$\frac{1}{2} \cdot 17 \cdot h = 60 \quad \Longrightarrow \quad h = \frac{120}{17}.$$

**Paso 2: Encontrar $AD$.**

De las condiciones de distancia:

$$x^2 + y^2 = 64, \qquad (x-17)^2 + y^2 = 225.$$

Restando la primera de la segunda:

$$(x-17)^2 - x^2 = 161 \quad \Longrightarrow \quad -34x + 289 = 161 \quad \Longrightarrow \quad x = \frac{128}{34} = \frac{64}{17}.$$

Es decir, $AD = \dfrac{64}{17}$.

**Paso 3: Área de $ACD$.**

El triángolo $ACD$ es rectángulo en $D$, con cateto vertical $h = \frac{120}{17}$ (que es la altura desde $C$) y cateto horizontal $AD = \frac{64}{17}$:

$$[ACD] = \frac{1}{2} \cdot \frac{64}{17} \cdot \frac{120}{17} = \frac{3840}{289}.$$

**Verificación:** $\frac{64^2}{17^2} + \frac{120^2}{17^2} = \frac{4096+14400}{289} = \frac{18496}{289} = 64 = 8^2$ ✓ (consistente con $AC = 8$).

$$\boxed{\dfrac{3840}{289}}$$