Paso a paso:

- Pat elige 6 cookies de 3 tipos (chocolate, avena, mantequilla de maní), donde las galletas del mismo tipo no se distinguen.
- Como hay al menos 6 de cada tipo, la única restricción es que la suma de las cantidades elegidas de cada tipo sea 6.
- Esto equivale a contar las soluciones enteras no negativas de:
$$c + o + p = 6$$
- Por "estrellas y barras", el número de soluciones es:
$$\binom{6 + 3 - 1}{3 - 1} = \binom{8}{2} = \frac{8 \cdot 7}{2} = 28$$

Verificación rápida: es el número de particiones de 6 en a lo más 3 partes: (6,0,0)→3, (5,1,0)→6, (4,2,0)→6, (4,1,1)→3, (3,3,0)→3, (3,2,1)→6, (2,2,2)→1; total 3+6+6+3+3+6+1 = 28. ✓

\boxed{28}