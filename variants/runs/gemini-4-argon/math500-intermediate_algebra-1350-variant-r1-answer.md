Para encontrar el menor valor posible de $|c_{n-1}|$, podemos expresar el polinomio $g(x)$ en función de sus raíces. 

Dado que $g(x)$ es un polinomio de grado $n$ con coeficiente principal $c_n = 2$ y todas sus raíces $r_1, r_2, \dots, r_n$ son enteros distintos, podemos factorizar $g(x)$ como:
$$g(x) = 2(x - r_1)(x - r_2)\cdots(x - r_n)$$

Expandiendo este producto o utilizando las fórmulas de Vieta, relacionamos los coeficientes $c_0$ y $c_{n-1}$ con las raíces:
1. Para el término constante $c_0$:
   $$c_0 = 2(-r_1)(-r_2)\cdots(-r_n) = 78$$
   Dividiendo entre $2$, obtenemos:
   $$(-r_1)(-r_2)\cdots(-r_n) = 39$$

2. Para el coeficiente $c_{n-1}$:
   $$c_{n-1} = 2\big((-r_1) + (-r_2) + \cdots + (-r_n)\big)$$

Definamos $s_i = -r_i$ para cada $i = 1, 2, \dots, n$. Como las raíces $r_i$ son enteros distintos, los números $s_i$ también son enteros distintos. Las condiciones anteriores se simplifican a:
- $s_1 s_2 \cdots s_n = 39$
- $|c_{n-1}| = 2|s_1 + s_2 + \cdots + s_n|$

Para minimizar $|c_{n-1}|$, debemos minimizar el valor absoluto de la suma $|s_1 + s_2 + \cdots + s_n|$, donde $\{s_1, s_2, \dots, s_n\}$ es un conjunto de enteros distintos cuyo producto es $39$.

La factorización en primos de $39$ es $3 \times 13$, por lo que los únicos divisores enteros de $39$ son $\pm 1, \pm 3, \pm 13$ y $\pm 39$.
Para que la suma esté lo más cerca posible de $0$, conviene elegir divisores de magnitud pequeña ($3$ y $13$ en lugar de $39$) y con signos opuestos:
- Si tomamos $13$ y $-3$, su producto es $-39$.
- Para que el producto total sea $+39$ usando enteros distintos adicionales, debemos multiplicar por $-1$ (o por $-1$ y $1$).

Evaluemos las sumas posibles en estos casos:
- Con el conjunto $\{13, -3, -1\}$, el producto es $13 \times (-3) \times (-1) = 39$ y la suma es $13 - 3 - 1 = 9$.
- Con el conjunto $\{13, -3, -1, 1\}$, el producto es $39$ y la suma es $13 - 3 - 1 + 1 = 10$.
- Con el conjunto $\{-13, 3, -1\}$, el producto es $39$ y la suma es $-13 + 3 - 1 = -11$.

El valor mínimo posible para $|s_1 + s_2 + \cdots + s_n|$ es $9$ (que corresponde a las raíces $r_1 = -13, r_2 = 3, r_3 = 1$, dando el polinomio $g(x) = 2x^3 + 18x^2 - 98x + 78$).

Por lo tanto, el menor valor posible de $|c_{n-1}|$ es:
$$|c_{n-1}| = 2 \times 9 = 18$$

\boxed{18}