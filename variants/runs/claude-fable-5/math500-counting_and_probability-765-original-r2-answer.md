Resolviendo paso a paso con inclusión-exclusión:

Sea $P$ el número de estudiantes que toman física. Entonces química tiene $2P$ estudiantes.

**Estudiantes que toman al menos una materia:** $360 - 15 = 345$.

**Inclusión-exclusión:**

$$|C \cup F \cup Q| = |C| + |F| + |Q| - |C \cap F| - |C \cap Q| - |F \cap Q| + |C \cap F \cap Q|$$

Sustituyendo:

$$345 = 180 + P + 2P - 30 - 75 - 75 + 15$$

$$345 = 3P + 15$$

$$3P = 330 \implies P = 110$$

**Verificación:** con $P = 110$ y $Q = 220$: $180 + 110 + 220 - 30 - 75 - 75 + 15 = 345$ ✓

$$\boxed{110}$$