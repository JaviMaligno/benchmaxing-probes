Analizo el problema: hay 10 parábolas $y=(x-5i)^2$ con vértices en $x=0,5,\dots,45$.

**Intersecciones con $y=k$:** Para $k>0$, cada parábola aporta dos puntos: $x = 5i \pm \sqrt{k}$, es decir, 20 puntos en total antes de considerar coincidencias. (Con $k=0$ habría solo 10 puntos, y con $k<0$ ninguno, así que necesitamos $k>0$ con exactamente una coincidencia.)

**Cuándo coinciden dos puntos:** Una coincidencia ocurre cuando la rama derecha de la parábola $i$ toca el mismo punto que la rama izquierda de la parábola $j$ ($j>i$):
$$5i + \sqrt{k} = 5j - \sqrt{k} \implies \sqrt{k} = \frac{5(j-i)}{2}.$$

Dos ramas derechas (o dos izquierdas) nunca coinciden, pues $5i+\sqrt{k}=5j+\sqrt{k}$ forzaría $i=j$.

**Conteo:** Si $\sqrt{k} = \frac{5m}{2}$ con $m$ entero, coinciden los pares $(i, i+m)$ para $i = 0, \dots, 9-m$, es decir, $10-m$ coincidencias. El número de puntos distintos es
$$20 - (10-m) = 10 + m.$$

Para obtener 19 puntos necesitamos $m = 9$: solo coinciden la parábola con vértice en $0$ y la de vértice en $45$, en $x = 22.5$. Entonces
$$\sqrt{k} = \frac{45}{2} \implies k = \frac{2025}{4} = 506.25.$$

**Verificación:** con $k = 2025/4$, los puntos son $5i \pm 22.5$ para $i=0,\dots,9$; el único valor repetido es $22.5$ (de $0+22.5$ y $45-22.5$), dando $20-1 = 19$ puntos distintos. ✓

$$\boxed{k = \dfrac{2025}{4}}$$