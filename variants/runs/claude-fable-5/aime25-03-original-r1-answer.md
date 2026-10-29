Necesitamos repartir 9 jugadores entre chocolate (c), vainilla (v) y fresa (s) con c + v + s = 9 y c > v > s ≥ 1.

**Paso 1: encontrar las ternas válidas (c, v, s).**

- s = 1: entonces c + v = 8 con c > v > 1 → (6, 2, 1) y (5, 3, 1). (La opción (4, 4, 1) falla porque c > v no se cumple.)
- s = 2: entonces c + v = 7 con c > v > 2 → (4, 3, 2).
- s = 3: requeriría v ≥ 4 y c ≥ 5, sumando al menos 12 > 9. Imposible.

**Paso 2: contar las asignaciones para cada terna** (los jugadores son distinguibles, así que usamos coeficientes multinomiales):

- (6, 2, 1): 9!/(6!·2!·1!) = 252
- (5, 3, 1): 9!/(5!·3!·1!) = 504
- (4, 3, 2): 9!/(4!·3!·2!) = 1260

**Paso 3: sumar.**

N = 252 + 504 + 1260 = 2016, y 2016 mod 1000 = 16.

\boxed{16}