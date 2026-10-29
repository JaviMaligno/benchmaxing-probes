## Planteamiento

Total de miembros: 9 + 6 = 15. Elegimos 5 sin restricciones y restamos los casos inválidos.

**Total de comités de 5:**
$$\binom{15}{5} = 3003$$

**Casos sin diseñadores (solo ingenieros):**
$$\binom{9}{5} = 126$$

**Casos sin ingenieros (solo diseñadores):**
$$\binom{6}{5} = 6$$

Estos dos conjuntos son disjuntos (un grupo de 5 no puede ser simultáneamente solo ingenieros y solo diseñadores), así que se suman directamente:

$$3003 - 126 - 6 = 2871$$

\boxed{2871}