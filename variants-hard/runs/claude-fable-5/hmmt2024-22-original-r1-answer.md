Planteo el triángulo rectángulo en $A$ con $BC = a$, $AC = b$, $AB = c$, de modo que $b^2 + c^2 = a^2$ (supongamos $b > c$).

**Posiciones de los pies sobre $BC$ (medidas desde $B$):**
- Pie de la altura: $BD = \dfrac{c^2}{a}$.
- Pie de la bisectriz: divide $BC$ en razón $AB:AC = c:b$, así que $BE = \dfrac{ac}{b+c}$.
- Pie de la mediana: $BF = \dfrac{a}{2}$.

**Cálculo de los segmentos:**

$$DE = BE - BD = \frac{ac}{b+c} - \frac{c^2}{a} = \frac{c\left(a^2 - c(b+c)\right)}{a(b+c)} = \frac{c(b^2 - bc)}{a(b+c)} = \frac{bc(b-c)}{a(b+c)} = 3$$

$$EF = BF - BE = \frac{a}{2} - \frac{ac}{b+c} = \frac{a(b-c)}{2(b+c)} = 5$$

**Dos ecuaciones útiles:**

1. Cociente: $\dfrac{DE}{EF} = \dfrac{2bc}{a^2} = \dfrac{3}{5}$, es decir $2bc = \dfrac{3a^2}{5}$.

2. Suma: $DF = DE + EF = 8$, y $DF = \dfrac{a}{2} - \dfrac{c^2}{a} = \dfrac{b^2 - c^2}{2a}$, por lo que $(b-c)(b+c) = 16a$.

**Resolución:** usando $b^2 + c^2 = a^2$:

$$(b-c)^2 = a^2 - 2bc = a^2 - \tfrac{3a^2}{5} = \tfrac{2a^2}{5}, \qquad (b+c)^2 = a^2 + \tfrac{3a^2}{5} = \tfrac{8a^2}{5}$$

Entonces:

$$(b-c)(b+c) = \sqrt{\tfrac{2a^2}{5}\cdot\tfrac{8a^2}{5}} = \frac{4a^2}{5} = 16a \;\Rightarrow\; a = 20$$

**Verificación:** con $a = 20$ se obtiene $b = 6\sqrt{10}$, $c = 2\sqrt{10}$; entonces $b^2+c^2 = 360+40 = 400 = a^2$ ✓, $DE = \dfrac{120\cdot 4\sqrt{10}}{20\cdot 8\sqrt{10}} = 3$ ✓ y $EF = \dfrac{20\cdot 4\sqrt{10}}{2\cdot 8\sqrt{10}} = 5$ ✓.

$$\boxed{20}$$