Para encontrar el menor valor posible de $|c_{n-1}|$, podemos expresar el polinomio $g(x)$ en términos de sus raíces.

Dado que el polinomio $g(x)$ tiene grado $n$, coeficiente principal $c_n = 2$ y todas sus raíces son enteros distintos $r_1, r_2, \dots, r_n$, podemos factorizar $g(x)$ como:
$$g(x) = 2(x - r_1)(x - r_2)\cdots(x - r_n)$$

Al evaluar en $x = 0$, obtenemos el término constante $c_0$:
$$c_0 = g(0) = 2(-r_1)(-r_2)\cdots(-r_n) = 78$$

Si definimos $s_i = -r_i$ para cada $i = 1, 2, \dots, n$, entonces $s_1, s_2, \dots, s_n$ también son enteros distintos y cumplen que:
$$2 s_1 s_2 \cdots s_n = 78 \implies s_1 s_2 \cdots s_n = 39$$

Por las fórmulas de Vieta (o expandiendo el producto), el coeficiente $c_{n-1}$ de $x^{n-1}$ está dado por:
$$c_{n-1} = -2(r_1 + r_2 + \cdots + r_n) = 2(s_1 + s_2 + \cdots + s_n)$$

Por lo tanto, minimizar $|c_{n-1}|$ equivale a minimizar $|s_1 + s_2 + \cdots + s_n|$, donde $s_1, s_2, \dots, s_n$ son divisores enteros distintos de $39$ cuyo producto es $39$.

La factorización en primos de $39$ es $3 \times 13$, por lo que sus divisores enteros son $\{\pm 1, \pm 3, \pm 13, \pm 39\}$. Para que la suma en valor absoluto sea lo más pequeña posible, debemos elegir los factores de mayor magnitud ($3$ y $13$) con signos opuestos, y ajustar el signo del producto utilizando $-1$ (y opcionalmente $1$):

1. Si elegimos $13$ y $-3$, su producto es $-39$. Para obtener un producto igual a $39$, debemos incluir el factor $-1$:
   - Conjunto $\{13, -3, -1\}$: el producto es $13 \times (-3) \times (-1) = 39$ y la suma es $13 - 3 - 1 = 9$.
   - Si además incluimos el $1$, obtenemos el conjunto $\{13, -3, -1, 1\}$: el producto sigue siendo $39$ y la suma es $13 - 3 - 1 + 1 = 10$.

2. Si elegimos $-13$ y $3$, su producto es $-39$. De nuevo, debemos incluir $-1$:
   - Conjunto $\{-13, 3, -1\}$: el producto es $39$ y la suma es $-13 + 3 - 1 = -11$ (valor absoluto $11$).
   - Conjunto $\{-13, 3, -1, 1\}$: el producto es $39$ y la suma es $-13 + 3 - 1 + 1 = -10$ (valor absoluto $10$).

El menor valor posible para $|s_1 + s_2 + \cdots + s_n|$ es $9$ (que corresponde a las raíces $r_1 = -13, r_2 = 3, r_3 = 1$). 

Por consiguiente, el menor valor posible de $|c_{n-1}|$ es:
$$|c_{n-1}| = 2 \times 9 = 18$$

\boxed{18}