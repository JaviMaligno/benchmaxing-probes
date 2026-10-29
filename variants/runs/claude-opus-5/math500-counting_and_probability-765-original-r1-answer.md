## Planteamiento

Sean:
- $|Cal| = 180$
- $|F| = x$ (física)
- $|Q| = 2x$ (química)

Datos de intersecciones:
- $|Cal \cap Q| = 75$
- $|F \cap Q| = 75$
- $|Cal \cap F| = 30$
- $|Cal \cap F \cap Q| = 15$

## Estudiantes que toman al menos una materia

$$360 - 15 = 345$$

## Principio de inclusión-exclusión

$$|Cal \cup F \cup Q| = |Cal| + |F| + |Q| - |Cal\cap F| - |Cal\cap Q| - |F\cap Q| + |Cal\cap F\cap Q|$$

$$345 = 180 + x + 2x - 30 - 75 - 75 + 15$$

## Resolución

$$345 = 3x + (180 - 30 - 75 - 75 + 15)$$
$$345 = 3x + 15$$
$$3x = 330$$
$$x = 110$$

**Verificación:** física $= 110$, química $= 220$. Entonces $180 + 110 + 220 - 30 - 75 - 75 + 15 = 345$ ✓

\boxed{110}