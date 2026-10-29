## Planteamiento

Tras $t$ segundos, cada posición contiene $b_i = \max(a_{i-t}, \ldots, a_{i+t})$. Con $t = 100$, cada $b_i$ es el máximo de una ventana de $201$ valores consecutivos.

Como los valores iniciales son distintos casi seguramente, un valor $a_j$ sobrevive (aparece entre los $b_i$) si y solo si $a_j$ es el máximo de **alguna** ventana de $201$ posiciones consecutivas que contenga a $j$.

## Condición de supervivencia

Sea $L$ el número de posiciones consecutivas a la izquierda de $j$ con valores menores que $a_j$, y $R$ lo análogo a la derecha. Una ventana $[j-l,\, j+r]$ con $l+r = 200$ tiene a $a_j$ como máximo si y solo si $l \le L$ y $r \le R$. Por tanto:

$$a_j \text{ sobrevive} \iff L + R \ge 200.$$

Como $2025 > 2\cdot 200 + 1$, no hay interferencia por la circularidad, y para valores i.i.d. uniformes:

$$P(L \ge l,\ R \ge r) = \frac{1}{l+r+1},$$

pues equivale a que $a_j$ sea el mayor de $l + r + 1$ valores.

## Cálculo de la probabilidad

$$P(L+R \ge 200) = \sum_{l=0}^{199} P(L = l,\ R \ge 200 - l) + P(L \ge 200).$$

Cada término de la suma vale
$$P(L \ge l, R \ge 200-l) - P(L \ge l+1, R \ge 200-l) = \frac{1}{201} - \frac{1}{202},$$

así que

$$P(L+R \ge 200) = 200\left(\frac{1}{201} - \frac{1}{202}\right) + \frac{1}{201} = \frac{200}{201 \cdot 202} + \frac{202}{201\cdot 202} = \frac{402}{201 \cdot 202} = \frac{1}{101}.$$

## Resultado

Por linealidad de la esperanza:

$$E[\#\text{valores distintos}] = 2025 \cdot \frac{1}{101} = \frac{2025}{101}.$$

$$\boxed{\dfrac{2025}{101}}$$