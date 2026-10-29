Para hallar la razón entre el lado mayor de $\triangle GHI$ y el de $\triangle ABC$, fijemos sin pérdida de generalidad la longitud del lado del triángulo equilátero $\triangle ABC$ igual a $1$.

### 1. Determinación de los puntos de intersección de las elipses
Por definición, la elipse $E_{AB}$ tiene focos en $A$ y $B$ y pasa por $C$. Como $CA + CB = 1 + 1 = 2$, $E_{AB}$ es el lugar geométrico de los puntos $P$ del plano tales que:
$$PA + PB = 2$$
De manera análoga, $E_{BC}$ y $E_{AC}$ están definidas por $PB + PC = 2$ y $PA + PC = 2$, respectivamente.

Si un punto $P$ pertenece a la intersección de dos elipses, por ejemplo $E_{AB} \cap E_{AC}$, debe cumplir simultáneamente:
$$PA + PB = 2 \quad \text{y} \quad PA + PC = 2 \implies PB = PC$$
Por lo tanto, cualquier punto de intersección de $E_{AB}$ y $E_{AC}$ se encuentra sobre la mediatriz del segmento $BC$ (que es el eje de simetría de $\triangle ABC$ que pasa por $A$ y por el punto medio $M_A$ de $BC$). Como una recta corta a una elipse en a lo sumo dos puntos, existen exactamente dos puntos en $E_{AB} \cap E_{AC}$.

Situemos el origen de coordenadas en $M_A = (0,0)$, con la recta $BC$ sobre el eje de abscisas ($B = (-1/2, 0)$, $C = (1/2, 0)$) y el vértice $A$ en $(0, \frac{\sqrt{3}}{2})$. El baricentro de $\triangle ABC$ es $O = (0, \frac{\sqrt{3}}{6})$.

Para un punto $P = (0, y)$ sobre la mediatriz de $BC$, tenemos $PB = \sqrt{y^2 + \frac{1}{4}}$ y $PA = \left|y - \frac{\sqrt{3}}{2}\right|$. La ecuación $PA + PB = 2$ se escribe como:
$$\left|y - \frac{\sqrt{3}}{2}\right| + \sqrt{y^2 + \frac{1}{4}} = 2$$

Analizamos los dos casos posibles:

- **Caso 1: $y \ge \frac{\sqrt{3}}{2}$ (punto $P_A^+$, situado más allá del vértice $A$).**
  $$\sqrt{y^2 + \frac{1}{4}} = 2 + \frac{\sqrt{3}}{2} - y$$
  Elevando al cuadrado ambos miembros:
  $$y^2 + \frac{1}{4} = \left(2 + \frac{\sqrt{3}}{2}\right)^2 - (4 + \sqrt{3})y + y^2$$
  $$(4 + \sqrt{3})y = \frac{19}{4} + 2\sqrt{3} - \frac{1}{4} = \frac{9 + 4\sqrt{3}}{2}$$
  Racionalizando el denominador:
  $$y_1 = \frac{(9 + 4\sqrt{3})(4 - \sqrt{3})}{2(16 - 3)} = \frac{24 + 7\sqrt{3}}{26}$$
  La distancia de este punto $P_A^+$ al baricentro $O$ es:
  $$r_1 = y_1 - \frac{\sqrt{3}}{6} = \frac{24 + 7\sqrt{3}}{26} - \frac{\sqrt{3}}{6} = \frac{72 + 8\sqrt{3}}{78} = \frac{36 + 4\sqrt{3}}{39} \approx 1.1007$$

- **Caso 2: $y < \frac{\sqrt{3}}{2}$ (punto $P_A^-$, situado más allá del lado $BC$).**
  $$\sqrt{y^2 + \frac{1}{4}} = 2 - \frac{\sqrt{3}}{2} + y$$
  Elevando al cuadrado ambos miembros de forma análoga:
  $$(4 - \sqrt{3})y = \frac{1}{4} - \left(2 - \frac{\sqrt{3}}{2}\right)^2 = \frac{-9 + 4\sqrt{3}}{2} \implies y_2 = \frac{-24 + 7\sqrt{3}}{26} < 0$$
  La distancia de $P_A^-$ al baricentro $O$ (en sentido opuesto a $A$) es:
  $$r_2 = \frac{\sqrt{3}}{6} - y_2 = \frac{36 - 4\sqrt{3}}{39} \approx 0.7454$$

Por simetría rotacional de $120^\circ$ alrededor de $O$, los seis puntos de intersección entre pares de elipses son $P_A^+, P_B^+, P_C^+$ (a distancia $r_1$ de $O$ en las direcciones de los vértices $A, B, C$) y $P_A^-, P_B^-, P_C^-$ (a distancia $r_2$ de $O$ en las direcciones de los puntos medios $M_A, M_B, M_C$).

---

### 2. Identificación del triángulo $\triangle GHI$ y su lado mayor
Observemos las ordenadas de los puntos $P_B^+, P_A^-, P_C^+$ respecto a la recta $BC$ ($y = 0$):
- Para $P_A^-$, tenemos $y(P_A^-) = y_2 < 0$.
- Para $P_B^+$ y $P_C^+$ (cuyas semirrectas desde $O$ forman un ángulo de $30^\circ$ por debajo de la horizontal), su ordenada es:
  $$y(P_B^+) = y(P_C^+) = \frac{\sqrt{3}}{6} - r_1 \sin 30^\circ = \frac{\sqrt{3}}{6} - \frac{36 + 4\sqrt{3}}{78} = \frac{9\sqrt{3} - 36}{78} < 0$$

Como $P_B^+, P_A^-, P_C^+$ tienen todos ordenada estrictamente negativa ($y < 0$), mientras que $\triangle ABC$ está contenido en el semiplano $y \ge 0$:
1. El segmento $P_B^+ P_C^+$ y los segmentos $P_B^+ P_A^-$ y $P_A^- P_C^+$ están contenidos íntegramente en el semiplano abierto $y < 0$, por lo que no cortan a $\triangle ABC$ (y lo mismo ocurre por simetría en los otros dos lados de $\triangle ABC$).
2. En cambio, los segmentos del tipo $P_B^- P_C^-$ tienen ordenada $y = \frac{\sqrt{3}}{6} + \frac{r_2}{2} = \frac{18 + 11\sqrt{3}}{39} \approx 0.6614 \in \left(0, \frac{\sqrt{3}}{2}\right)$, por lo que atraviesan los lados $AB$ y $AC$ de $\triangle ABC$. Asimismo, las diagonales que pasan por $O$ (como $P_A^+ P_A^-$) cortan a $\triangle ABC$.

En consecuencia, los únicos triángulos $\triangle GHI$ cuyas aristas no intersecan las de $\triangle ABC$ son:
- Los tres triángulos isósceles congruentes a $\triangle P_B^+ P_A^- P_C^+$ situados cada uno en el semiplano exterior a un lado de $\triangle ABC$. En $\triangle P_B^+ P_A^- P_C^+$, los dos lados iguales miden $\sqrt{r_1^2 + r_2^2 - r_1 r_2} < r_1$, mientras que la base mide $|P_B^+ P_C^+| = \sqrt{3}\,r_1$.
- El triángulo equilátero $\triangle P_A^+ P_B^+ P_C^+$, cuyos tres lados miden igualmente $|P_B^+ P_C^+| = \sqrt{3}\,r_1$.

En cualquiera de los casos, el lado mayor de $\triangle GHI$ tiene longitud:
$$|P_B^+ P_C^+| = \sqrt{3}\,r_1 = \sqrt{3} \left(\frac{36 + 4\sqrt{3}}{39}\right) = \frac{36\sqrt{3} + 12}{39} = \frac{4 + 12\sqrt{3}}{13}$$

Como el lado de $\triangle ABC$ es $1$, la razón buscada es:

\boxed{\frac{4 + 12\sqrt{3}}{13}}