# Resolución paso a paso

**Paso 1: Identificar los datos.**
- Total de estudiantes: 390, y 20 no toman ninguna de las tres materias → toman al menos una: 390 − 20 = **370**
- |C| = 200 (cálculo)
- |C ∩ Q| = 80 (cálculo ∩ química)
- |F ∩ Q| = 80 (física ∩ química)
- |C ∩ F| = 35 (cálculo ∩ física)
- |C ∩ F ∩ Q| = 20
- |Q| = 2|F|

**Paso 2: Aplicar inclusión-exclusión.**

$$|C \cup F \cup Q| = |C| + |F| + |Q| - |C \cap F| - |C \cap Q| - |F \cap Q| + |C \cap F \cap Q|$$

$$370 = 200 + F + 2F - 35 - 80 - 80 + 20$$

$$370 = 200 + 3F - 175 \implies 370 = 25 + 3F$$

$$3F = 345 \implies F = 115$$

**Paso 3: Verificar.** Con F = 115 y Q = 230:
- Solo C: 200 − 60 − 15 − 20 = 105
- Solo F: 115 − 15 − 60 − 20 = 20
- Solo Q: 230 − 60 − 60 − 20 = 90
- Solo C∩F: 15; Solo C∩Q: 60; Solo F∩Q: 60; las tres: 20

Total: 105 + 20 + 90 + 15 + 60 + 60 + 20 = 370 ✓ (todas las regiones son no negativas)

\boxed{115}