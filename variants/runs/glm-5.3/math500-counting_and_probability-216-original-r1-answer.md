## Solución paso a paso

**Paso 1: Total de subcomités de 5 miembros (sin restricciones).**

Hay 8 + 6 = 14 miembros en total, así que:

$$\binom{14}{5} = \frac{14!}{5! \cdot 9!} = 2002$$

**Paso 2: Restar los subcomités que violan la condición.**

La única forma de violar "al menos un miembro de cada partido" es que los 5 sean del mismo partido:

- **Todos Republicans:** $\binom{8}{5} = 56$
- **Todos Democrats:** $\binom{6}{5} = 6$

**Paso 3: Aplicar el principio de complemento.**

$$2002 - 56 - 6 = 1940$$

**Verificación (suma directa por casos):**

| Republicans | Democrats | Cálculo | Resultado |
|---|---|---|---|
| 1 | 4 | $\binom{8}{1}\binom{6}{4}$ | $8 \cdot 15 = 120$ |
| 2 | 3 | $\binom{8}{2}\binom{6}{3}$ | $28 \cdot 20 = 560$ |
| 3 | 2 | $\binom{8}{3}\binom{6}{2}$ | $56 \cdot 15 = 840$ |
| 4 | 1 | $\binom{8}{4}\binom{6}{1}$ | $70 \cdot 6 = 420$ |

Suma: $120 + 560 + 840 + 420 = 1940$ ✓

$$\boxed{1940}$$