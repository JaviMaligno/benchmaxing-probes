## Planteamiento

Coloco coordenadas: la habitación mide 12 (largo, eje x), 10 (ancho, eje y), 8 (alto, eje z).

- **Gecko**: en la pared lateral x = 0, a 1 pie del techo y 1 pie de la pared trasera → posición (y = 1, z = 7).
- **Mosca**: en la pared lateral x = 12, a 1 pie del suelo y 1 pie de la pared frontal → posición (y = 9, z = 1).

El camino más corto sobre superficies se encuentra "desplegando" las paredes en un plano y midiendo la recta. Hay que probar varios despliegues (el suelo está prohibido).

## Despliegues candidatos

**1. Pared lateral → pared trasera → pared lateral**
Horizontal: 1 + 12 + 9 = 22; vertical: |7 − 1| = 6.
Longitud: √(22² + 6²) = √520 = 2√130 ≈ 22.80.

**2. Pared lateral → techo → pared lateral**
Distancia "a lo largo": 1 + 12 + 7 = 20; transversal: |9 − 1| = 8.
Longitud: √(20² + 8²) = √464 = 4√29 ≈ 21.54.

**3. Pared lateral → techo → pared frontal → pared lateral**
Despliego el techo como el rectángulo x ∈ [0,12], y ∈ [0,10]; la pared inicial hacia abajo en x, la pared frontal hacia arriba en y, y la pared final girada sobre su arista vertical común con la frontal:

- Gecko: está a 1 pie del techo → se despliega en (−1, 1).
- Mosca: a 1 pie de la frontal y a 7 pies del techo → se despliega en (12 + 1, 10 + 7) = (13, 17).

Longitud: √((13−(−1))² + (17−1)²) = √(14² + 16²) = √(196 + 256) = √452 = **2√113 ≈ 21.26**.

Verifico que la recta cruza efectivamente las cuatro superficies en orden: entra al techo en (0, 2.14), sale hacia la pared frontal en (6.875, 10) y pasa a la pared final en (12, 15.86) — todo dentro de los rangos válidos. ✓

**4. Otras combinaciones** (pared trasera + techo, pared frontal directa, etc.) dan 10√5 ≈ 22.36 o 2√130, todas peores.

## Conclusión

El camino más corto cruza la pared inicial, el techo, la pared frontal y la pared final, con longitud

$$\boxed{2\sqrt{113}}$$