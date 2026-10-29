## Planteamiento

Un rectángulo queda determinado por un intervalo horizontal $[a,b]$ y uno vertical $[c,d]$ con $0\le a<b\le 6$. Hay $\binom{7}{2}=21$ intervalos posibles en cada dirección.

Dos rectángulos con lados paralelos a los ejes **se intersecan** (como conjuntos cerrados, incluyendo bordes y vértices) si y solo si sus intervalos en $x$ se cortan **y** sus intervalos en $y$ se cortan.

Por tanto son totalmente disjuntos (sin interior, bordes ni vértices comunes) si y solo si:
- sus intervalos en $x$ son disjuntos, **o**
- sus intervalos en $y$ son disjuntos.

## Conteo por inclusión–exclusión

**Pares de intervalos estrictamente separados:** necesito $a<b<a'<b'$, es decir elegir 4 de las 7 rectas:
$$\binom{7}{4}=35.$$

**$A$ = pares separados horizontalmente:** elijo el par de intervalos en $x$ con orden izquierda–derecha (35 formas; el orden identifica cuál rectángulo es cuál, así que el par no ordenado se cuenta una sola vez) y luego cada rectángulo recibe cualquier intervalo vertical:
$$A = 35 \cdot 21 \cdot 21 = 35\cdot 441 = 15435.$$

**$B$ = pares separados verticalmente:** por simetría, $B = 15435$.

**$C$ = separados en ambas direcciones:** 35 formas para el par de intervalos en $x$ (izquierda–derecha), 35 para el par en $y$, y 2 maneras de asignar (el de la izquierda puede ir abajo o arriba):
$$C = 35\cdot 35\cdot 2 = 2450.$$

## Resultado

$$A + B - C = 15435 + 15435 - 2450 = 28420.$$

\boxed{28420}