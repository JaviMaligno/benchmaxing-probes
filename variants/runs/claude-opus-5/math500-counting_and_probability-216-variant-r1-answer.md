## Planteamiento

**Total sin restricciones:** elegir 5 de 15 personas

$$\binom{15}{5} = 3003$$

**Casos a excluir:**

- Solo ingenieros (ningún diseñador): $\binom{9}{5} = 126$
- Solo diseñadores (ningún ingeniero): $\binom{6}{5} = 6$

Estos dos casos son disjuntos (un grupo de 5 no puede ser simultáneamente solo de ingenieros y solo de diseñadores), así que simplemente se suman: $126 + 6 = 132$.

**Resultado:**

$$3003 - 132 = 2871$$

\boxed{2871}