Para encontrar el menor valor posible de $|a_{n-1}|$, podemos expresar el polinomio $f(x)$ en términos de sus $n$ raíces enteras y distintas, que llamaremos $r_1, r_2, \ldots, r_n$. 

Dado que el coeficiente principal es $a_n = 2$, podemos factorizar $f(x)$ como:
$$f(x) = 2(x - r_1)(x - r_2)\cdots(x - r_n)$$

Si definimos $s_i = -r_i$ para cada $i \in \{1, 2, \ldots, n\}$, entonces $s_1, s_2, \ldots, s_n$ también son números enteros distintos, y el polinomio se reescribe como:
$$f(x) = 2(x + s_1)(x + s_2)\cdots(x + s_n)$$

Por las fórmulas de Vieta (o expandiendo el producto):
1. El término independiente es $a_0 = 2 s_1 s_2 \cdots s_n$. Como $a_0 = 66$, tenemos:
   $$s_1 s_2 \cdots s_n = 33$$
2. El coeficiente de $x^{n-1}$ es:
   $$a_{n-1} = 2(s_1 + s_2 + \cdots + s_n)$$

Para minimizar $|a_{n-1}| = 2|s_1 + s_2 + \cdots + s_n|$, debemos encontrar un conjunto de enteros distintos $\{s_1, s_2, \ldots, s_n\}$ cuyo producto sea $33$ y cuya suma tenga el menor valor absoluto posible.

La factorización en primos de $33$ es $3 \times 11$, por lo que los únicos divisores enteros de $33$ son $\pm 1, \pm 3, \pm 11, \pm 33$. Para minimizar el valor absoluto de la suma, debemos usar los factores con módulo $3$ y $11$ con signos opuestos (en lugar de $\pm 33$).

Como $( -3 ) \times 11 = -33$ (o $3 \times (-11) = -33$), necesitamos incluir el factor $-1$ para que el producto total sea $+33$ positivo. Opcionalmente también podemos incluir el factor $1$. Analicemos las combinaciones posibles:

- $\{11, -3, -1\}$: el producto es $11 \times (-3) \times (-1) = 33$, y la suma es $11 - 3 - 1 = 7$.
- $\{11, -3, -1, 1\}$: el producto es $33$, y la suma es $11 - 3 - 1 + 1 = 8$.
- $\{-11, 3, -1\}$: el producto es $(-11) \times 3 \times (-1) = 33$, y la suma es $-11 + 3 - 1 = -9$ (valor absoluto $9$).
- $\{-11, 3, -1, 1\}$: el producto es $33$, y la suma es $-11 + 3 - 1 + 1 = -8$ (valor absoluto $8$).
- Si ambos factores mayores que $1$ tienen el mismo signo (como $\{-11, -3, 1\}$), el menor valor absoluto de la suma es $|-11 - 3 + 1| = 13$.

El menor valor posible para $|s_1 + s_2 + \cdots + s_n|$ es $7$, que se alcanza con el polinomio de grado $3$ cuyas raíces son $-11, 3, 1$:
$$f(x) = 2(x + 11)(x - 3)(x - 1) = 2x^3 + 14x^2 - 82x + 66$$

Por lo tanto, el menor valor posible de $|a_{n-1}|$ es $2 \times 7 = 14$.

\boxed{14}