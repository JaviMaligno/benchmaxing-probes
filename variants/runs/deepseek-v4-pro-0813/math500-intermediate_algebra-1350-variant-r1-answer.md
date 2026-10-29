Sea $g(x)=2(x-r_1)(x-r_2)\cdots(x-r_n)$ donde los $r_i$ son enteros distintos.

Como $g(0)=78$, tenemos

$$2(-r_1)(-r_2)\cdots(-r_n)=78 \implies (-1)^n\, r_1r_2\cdots r_n = 39.$$

Por tanto, $r_1r_2\cdots r_n=\pm 39$. Dado que $39=3\cdot 13$, los productos posibles son $39$, $-39$, $1$, $-1$ (según el número de raíces).

El coeficiente $c_{n-1}$ cumple

$$c_{n-1}=-2(r_1+r_2+\cdots+r_n).$$

Queremos minimizar $|c_{n-1}|$, es decir, minimizar $|r_1+\cdots+r_n|$.

Analicemos las posibilidades de las raíces como enteros distintos cuyo producto es $\pm 39$ o $\pm 1$.

- Para $n=2$: producto $\pm 39$. Los pares son $(1,39)$, $(-1,-39)$, $(1,-39)$, $(-1,39)$, $(3,13)$, $(-3,-13)$, $(3,-13)$, $(-3,13)$. La suma mínima en valor absoluto es $10$ (del par $(3,13)$ con suma $16$, o $(3,-13)$ con suma $-10$). Así $|c_1|=20$.

- Para $n=3$: necesitamos tres enteros distintos con producto $\pm39$ o $\pm1$. Producto $\pm39$: los únicos divisores son $1,3,13$, pero si usamos $3$ y $13$ ya son dos factores distintos de $\pm1$, no queda un tercer factor distinto. Si usamos $1$ y $39$, tampoco. Por tanto no hay tres enteros distintos cuyo producto sea $\pm39$. Producto $\pm1$ con tres enteros distintos: $1,-1$ y falta un tercer factor cuyo producto global sea $1$, imposible con un tercer entero distinto. No hay configuración.

- Para $n=4$: necesitamos cuatro enteros distintos con producto $\pm39$ o $\pm1$. Producto $\pm39$ solo puede tener dos factores no triviales, y los otros dos serían $\pm1$, pero no pueden ser ambos $1$ (distintos) ni $1$ y $-1$ sin anular el valor absoluto $39$ si los otros son $3$ y $13$... de hecho $1,-1,3,13$ tiene producto $-39$, que sí es válido. La suma es $1+(-1)+3+13=16$, lo que da $|c_3|=32$. Otra opción $1,-1,3,-13$ da suma $-10$, y $|c_3|=20$.

Espera: con $n=4$, el conjunto $\{1,-1,3,13\}$ da producto $1\cdot(-1)\cdot3\cdot13=-39$, válido, y suma $16$. El conjunto $\{1,-1,3,-13\}$ da producto $39$, válido, y suma $-10$, por lo que $|c_3|=20$.

- Para $n=5$: cinco enteros distintos. El producto debe ser $\pm39$ o $\pm1$. Como $\pm39$ tiene a lo sumo dos factores no triviales, los demás deben ser $\pm1$, pero solo hay dos valores $\pm1$ disponibles y ya los usamos. Para producto $\pm1$: necesitamos $1,-1$ y tres factores más cuyo producto sea $\pm1$, imposible con enteros distintos de módulo mayor que $1$. No hay configuración.

Así, el mínimo de $|c_{n-1}|$ es $20$.

Comprobemos si con $n=4$ podemos lograr una suma menor que $10$ en valor absoluto. Los factores son $\{\pm1,\pm3,\pm13\}$ en algún signo, con cuatro elementos. Como $\pm1$ no puede aparecer dos veces (distintos), necesariamente usamos $1$ y $-1$ y dos de $\{3,13\}$. Las sumas posibles son $1+(-1)+3+13=16$, $1+(-1)+3-13=-10$, $1+(-1)-3+13=10$, $1+(-1)-3-13=-16$. El mínimo es $10$. Eso da $|c_{n-1}|=2\cdot 10=20$.

Por tanto, el menor valor posible es $20$.

\boxed{20}