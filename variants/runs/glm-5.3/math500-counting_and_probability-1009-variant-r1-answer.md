**Razonamiento paso a paso:**

Sea $(b, n, z)$ la cantidad de muffins de arándano (blueberry), plátano (banana) y salvado (bran) que elige Maya.

Como los muffins del mismo tipo son indistinguibles, cada surtido distinto corresponde exactamente a una solución entera no negativa de:

$$b + n + z = 7,\qquad b,n,z \ge 0$$

(La condición de que hay al menos 7 de cada tipo garantiza que cualquier solución no negativa es factible.)

Contamos las soluciones con la técnica de **estrellas y barras**: las 7 elecciones son "estrellas", y colocamos $3-1 = 2$ barras para separarlas en los 3 tipos. El número de arreglos es:

$$\binom{7 + 3 - 1}{3 - 1} = \binom{9}{2} = \frac{9 \cdot 8}{2} = 36$$

**Verificación por conteo directo:** para $b = 0, 1, \dots, 7$, el número de formas de repartir lo restante entre $n$ y $z$ es $8 - b$. Sumando: $8+7+6+5+4+3+2+1 = 36$. ✓

\boxed{36}