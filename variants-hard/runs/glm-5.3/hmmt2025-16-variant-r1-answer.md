## Planteamiento

Pongo coordenadas de modo que las líneas de la cuadrícula sean $x = 0,\dots,6$ e $y = 0,\dots,6$. Un rectángulo con lados sobre las líneas de la cuadrícula es de la forma $[a,b]\times[c,d]$ con $0\le a<b\le 6$ y $0\le c<d\le 6$, es decir, un par de intervalos (uno en $x$, otro en $y$). En cada eje hay $\binom{7}{2}=21$ intervalos, así que hay $21^2 = 441$ rectángulos en total.

**Paso 1: Criterio de disjunction.**
Dos rectángulos cerrados $R_1=[a_1,b_1]\times[c_1,d_1]$ y $R_2=[a_2,b_2]\times[c_2,d_2]$ no comparten **ningún** punto (interior, borde o vértice) si y solo si sus proyecciones en $x$ son disjuntas **o** sus proyecciones en $y$ son disjuntas:
$$b_1<a_2 \;\text{ó}\; b_2<a_1 \quad\text{o bien}\quad d_1<c_2 \;\text{ó}\; d_2<c_1.$$
Las desigualdades son estrictas: si $b_1=a_2$, los rectángulos se tocarían en el borde (o en un vértice).

**Paso 2: Pares de intervalos estrictamente disjuntos.**
Cuento los pares ordenados de intervalos disjuntos. Si $I_1=[a_1,b_1]$ queda a la izquierda de $I_2=[a_2,b_2]$, necesito
$$0\le a_1 < b_1 < a_2 < b_2 \le 6,$$
que equivale a elegir $4$ valores distintos entre los $7$ de $\{0,\dots,6\}$ y asignarlos en orden creciente: $\binom{7}{4}=35$. Contando también el orden inverso:
$$D = 2\cdot 35 = 70 \quad\text{pares ordenados de intervalos disjuntos.}$$

**Paso 3: Inclusión–exclusión sobre pares ordenados de rectángulos.**
- Proyecciones en $x$ disjuntas (las de $y$ son libres): $70\cdot 21\cdot 21 = 30870$.
- Proyecciones en $y$ disjuntas: por simetría, $30870$.
- Ambas a la vez: $70\cdot 70 = 4900$.

Pares ordenados de rectángulos disjuntos:
$$30870 + 30870 - 4900 = 56840.$$

**Paso 4: Rectángulos no ordenados.**
Dos rectángulos disjuntos no pueden ser idénticos, de modo que cada par no ordenado $\{R_1,R_2\}$ corresponde a exactamente $2$ pares ordenados:
$$\frac{56840}{2}=28420.$$

**Verificación (complemento).** Pares no ordenados totales: $\binom{441}{2}=97020$. Pares que comparten algún punto: pares ordenados de intervalos que se tocan o cruzan $=441-70=371$ por eje, luego $\bigl(371^2-441\bigr)/2 = 68600$ pares no ordenados distintos que se intersecan. Restando: $97020-68600=28420$. ✓

$$\boxed{28420}$$