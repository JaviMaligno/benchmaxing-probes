Voy a resolver esto con inclusión-exclusión.

**Paso 1:** Estudiantes que toman al menos una materia: 360 − 15 = 345.

**Paso 2:** Sea $P$ el número de estudiantes que toman física. Entonces química tiene $2P$ estudiantes y cálculo tiene 180.

**Paso 3:** Aplico el principio de inclusión-exclusión:

$$|C \cup F \cup Q| = |C| + |F| + |Q| - |C \cap F| - |C \cap Q| - |F \cap Q| + |C \cap F \cap Q|$$

$$345 = 180 + P + 2P - 30 - 75 - 75 + 15$$

**Paso 4:** Simplifico:

$$345 = 3P + 180 - 180 + 15 = 3P + 15$$

$$3P = 330 \implies P = 110$$

**Verificación:** con $P = 110$, química tiene 220. Entonces: $180 + 110 + 220 - 30 - 75 - 75 + 15 = 345$. ✓ Y $345 + 15 = 360$. ✓

$$\boxed{110}$$