## Solución

**Contar los rectángulos:** En una cuadrícula de 5×5 hay 6 líneas horizontales y 6 verticales. Un rectángulo se determina eligiendo 2 líneas verticales y 2 horizontales, es decir, un intervalo en el eje x y otro en el eje y, cada uno con $\binom{6}{2}=15$ opciones.

**Condición de no solapamiento:** Dos rectángulos no comparten interior, aristas ni vértices si y solo si sus proyecciones sobre el eje x son intervalos cerrados disjuntos, **o** sus proyecciones sobre el eje y lo son (basta con que estén separados en al menos una dirección, sin tocarse ni en un punto).

**Pares con proyecciones x disjuntas (ordenados):** Dos intervalos cerrados disjuntos en $\{0,\dots,5\}$ requieren 4 valores distintos $a<b<c<d$, con $[a,b]$ y $[c,d]$: hay $\binom{6}{4}=15$ pares no ordenados, o sea $30$ ordenados. Los intervalos en y son libres: $15 \times 15$. Total ordenado:
$$30 \cdot 15 \cdot 15 = 6750.$$

**Pares con proyecciones y disjuntas:** por simetría, también $6750$ ordenados.

**Intersección (disjuntos en ambas direcciones):** $30 \cdot 30 = 900$ ordenados.

**Inclusión-exclusión:**
$$6750 + 6750 - 900 = 12600 \text{ pares ordenados}.$$

Como el orden no importa, dividimos entre 2:
$$\frac{12600}{2} = 6300.$$

$$\boxed{6300}$$