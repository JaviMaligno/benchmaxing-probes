## Razonamiento

Se trata de contar las soluciones enteras no negativas de

$$c + o + p = 6$$

donde $c$, $o$ y $p$ son las cantidades de galletas de chocolate chip, avena y mantequilla de maní. Como hay al menos seis de cada tipo, no existe restricción superior que limite las soluciones.

Aplicando combinaciones con repetición (el método de "estrellas y barras"), con $n = 6$ objetos y $k = 3$ tipos:

$$\binom{n + k - 1}{k - 1} = \binom{6 + 3 - 1}{3 - 1} = \binom{8}{2} = \frac{8 \cdot 7}{2} = 28$$

**Verificación** por conteo directo según el número de galletas de chocolate chip $c$: para cada valor de $c$ quedan $6 - c$ galletas por repartir entre dos tipos, lo que da $7 - c$ opciones:

$$7 + 6 + 5 + 4 + 3 + 2 + 1 = 28$$

\boxed{28}