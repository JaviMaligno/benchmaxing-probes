# Resolución paso a paso

**Datos:**
- Total de estudiantes: 360
- No toman ninguna de las tres materias: 15
- |Cálculo| = 180
- |Química| = 2 · |Física|
- |C ∩ Q| = 75, |F ∩ Q| = 75, |F ∩ C| = 30
- |C ∩ F ∩ Q| = 15

**Paso 1: Estudiantes que toman al menos una materia.**
$$360 - 15 = 345$$

**Paso 2: Aplicar inclusión-exclusión.**
$$|C \cup F \cup Q| = |C| + |F| + |Q| - |C \cap F| - |C \cap Q| - |F \cap Q| + |C \cap F \cap Q|$$

Llamemos $x = |F|$, entonces $|Q| = 2x$:

$$345 = 180 + x + 2x - 30 - 75 - 75 + 15$$

$$345 = 180 + 3x - 165$$

$$345 = 15 + 3x$$

$$330 = 3x \implies x = 110$$

**Paso 3: Verificación.**
- Química: $2(110) = 220$
- Solo F∩C: $30 - 15 = 15$; solo C∩Q: $75-15=60$; solo F∩Q: $75-15=60$
- Solo Cálculo: $180 - 60 - 15 - 15 = 90$
- Solo Física: $110 - 60 - 15 - 15 = 20$
- Solo Química: $220 - 60 - 60 - 15 = 85$
- Suma: $90 + 20 + 85 + 60 + 60 + 15 + 15 = 345$, y $345 + 15 = 360$ ✓

\boxed{110}