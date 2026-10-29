## Planteamiento

Sea $P$ el número de estudiantes de física. Entonces química $= 2P$, y cálculo $= 200$.

Estudiantes que toman al menos una materia: $390 - 20 = 370$.

## Inclusión-exclusión

$$|Cal \cup F \cup Q| = |Cal| + |F| + |Q| - |Cal\cap F| - |Cal \cap Q| - |F \cap Q| + |Cal\cap F\cap Q|$$

$$370 = 200 + P + 2P - 35 - 80 - 80 + 20$$

$$370 = 3P + 25$$

$$3P = 345 \quad \Rightarrow \quad P = 115$$

## Verificación

Con $P = 115$ y química $= 230$:

- Solo cálculo: $200 - 80 - 35 + 20 = 105$
- Solo física: $115 - 35 - 80 + 20 = 20$
- Solo química: $230 - 80 - 80 + 20 = 90$
- Cálculo y física únicamente: $35 - 20 = 15$
- Cálculo y química únicamente: $80 - 20 = 60$
- Física y química únicamente: $80 - 20 = 60$
- Las tres: $20$

Total: $105 + 20 + 90 + 15 + 60 + 60 + 20 = 370$ ✓, más los $20$ que no toman ninguna da $390$. ✓

\boxed{115}