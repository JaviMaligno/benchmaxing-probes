## Reformulación

Cada celda unitaria tiene tantos lados en $P$ como vecinas del lado opuesto. Si una celda es interior y tiene $d$ vecinas interiores, aporta $4-d$ lados; igual para las exteriores con el grafo exterior. Entonces, con $n_d$ = celdas interiores de grado $d$ y $m_d$ = celdas exteriores de grado $d$:

$$a_3=n_1+m_1,\qquad a_2=n_2+m_2,\qquad a_1=n_3+m_3.$$

Llamo **lengüeta** a una celda interior de grado 1 y **muesca** a una exterior de grado 1 (las que cuentan en $a_3$); las de grado 2 o 3 son las "malas" (cuentan en $a_1+a_2$).

## Cota inferior: cada lengüeta/muesca exige una celda mala

Sea una muesca $N=(0,0)$ (exterior) con única vecina exterior $(0,1)$; sus vecinas $(\pm1,0),(0,-1)$ son interiores. En el vértice común a $(0,0),(1,0),(0,-1),(1,-1)$ ya hay dos celdas interiores en diagonal; si $(1,-1)$ fuese exterior, $P$ pasaría dos veces por ese vértice (autointersección). Luego $(1,-1)$ y, análogamente, $(-1,-1)$ son interiores, así que la **base** $(0,-1)$ tiene grado $\ge 2$ (y $\le 3$ por ser vecina de $N$): es mala.

El argumento dual (mismo chequeo de vértices) da: la celda exterior opuesta a la vecina interior de una lengüeta tiene grado exterior $\ge2$: es mala.

Una celda mala interior tiene a lo sumo 2 vecinas exteriores, luego es base de $\le2$ muescas; igual para las malas exteriores con las lengüetas. Como las malas interiores sólo sirven a muescas y las exteriores sólo a lengüetas:

$$a_1+a_2\;\ge\;\frac{m_1}{2}+\frac{n_1}{2}=\frac{a_3}{2}.$$

La igualdad es imposible: de $3n_1+2n_2+n_3=L=3m_1+2m_2+m_3$ (contar los $L$ lados desde dentro y desde fuera) y de $C-R=4$ (esquinas convexas menos cóncavas), el caso de igualdad forzaría a la vez $n_1=m_1$ y $n_1=m_1+6$. Por tanto $a_1+a_2>\tfrac12 a_3$ **siempre**.

## El valor $1/2$ se alcanza en el límite

Patrón periódico (luego se trunca, uniendo las filas con una columna a la izquierda; las correcciones son $O(N+K)$ frente a área $\sim NK$):

- $y\equiv0\ (4)$: todo interior;
- $y\equiv1,3\ (4)$: interior en $x$ impar (lengüetas), exterior en $x$ par (muescas);
- $y\equiv2\ (4)$: todo exterior.

Grados: $(x,0)$ con $x$ par → grado 2 (mala, sirve a dos muescas); $(x,0)$ con $x$ impar → grado 4 (libre); $(x,2)$ con $x$ impar → grado exterior 2 (mala, sirve a dos lengüetas); $(x,2)$ con $x$ par → grado 4 (libre). Por periodo de $2\times4$: $a_3=4$ y $a_1+a_2=2$, es decir cociente $\to\tfrac12$.

Así $\inf\frac{a_1+a_2}{a_3}=\frac12$ sin alcanzarse, y el mayor $k$ válido es:

$$\boxed{\dfrac{1}{2}}$$