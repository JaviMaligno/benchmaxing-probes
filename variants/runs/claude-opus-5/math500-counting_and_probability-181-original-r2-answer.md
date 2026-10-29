## Razonamiento

En una malla de 3 filas por n columnas, los cuadrados posibles son de tres tamaños:

**1. Cuadrados de lado 1:** hay 2 franjas horizontales de altura 1 y (n−1) posiciones horizontales → 2(n−1).

**2. Cuadrados de lado 2:** solo hay una franja vertical de altura 2 (la malla tiene 3 filas) y (n−2) posiciones → (n−2).

**3. Cuadrados inclinados de lado √2:** cada uno se inscribe en un bloque de 2×2 uniendo los puntos medios de sus lados; hay exactamente un bloque de 2×2 verticalmente y (n−2) horizontalmente → (n−2).

Total:
$$2(n-1) + (n-2) + (n-2) = 4n - 6$$

Igualando a 70:
$$4n - 6 = 70 \implies 4n = 76 \implies n = 19$$

\boxed{19}