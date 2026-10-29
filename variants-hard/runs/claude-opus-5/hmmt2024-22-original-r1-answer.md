## Planteamiento

Con $\angle BAC = 90°$, sean $b=AC$, $c=AB$, $a=BC$, y midamos distancias desde $B$:

- **Altura**: $BD = \dfrac{c^2}{a}$
- **Bisectriz**: $BE = \dfrac{ac}{b+c}$ (pues $BE/EC = c/b$)
- **Mediana**: $BF = \dfrac{a}{2}$

## Cálculo de los segmentos

$$DE = \left|\frac{ac}{b+c}-\frac{c^2}{a}\right| = \frac{c\,|b^2+c^2-cb-c^2|}{a(b+c)} = \frac{bc\,|b-c|}{a(b+c)}$$

$$EF = \left|\frac{a}{2}-\frac{ac}{b+c}\right| = \frac{a\,|b-c|}{2(b+c)}$$

## Razón $DE/EF$

$$\frac{DE}{EF} = \frac{bc|b-c|}{a(b+c)}\cdot\frac{2(b+c)}{a|b-c|} = \frac{2bc}{a^2} = \frac{3}{5}$$

Por lo tanto $2bc = \tfrac{3}{5}a^2$, y con $b^2+c^2 = a^2$ (Pitágoras):

$$(b-c)^2 = a^2 - \tfrac{3}{5}a^2 = \tfrac{2}{5}a^2, \qquad (b+c)^2 = a^2 + \tfrac{3}{5}a^2 = \tfrac{8}{5}a^2$$

$$\frac{|b-c|}{b+c} = \sqrt{\frac{2/5}{8/5}} = \frac{1}{2}$$

## Conclusión

$$EF = \frac{a}{2}\cdot\frac{|b-c|}{b+c} = \frac{a}{2}\cdot\frac{1}{2} = \frac{a}{4} = 5 \implies a = 20$$

(Verificación: $DF = DE+EF = 8$ es consistente, ya que $DF/EF = (b+c)^2/a^2 = 8/5$.)

\boxed{20}