Para hallar el menor valor posible de $|a_{n-1}|$, podemos expresar el polinomio $f(x)$ en su forma factorizada a partir de sus $n$ raíces enteras distintas $r_1, r_2, \dots, r_n$:

$$f(x) = a_n(x - r_1)(x - r_2)\cdots(x - r_n)$$

Sabemos que $a_n = 2$, por lo que:
$$f(x) = 2(x - r_1)(x - r_2)\cdots(x - r_n)$$

Si definimos $s_i = -r_i$ para cada $i = 1, 2, \dots, n$, entonces $s_1, s_2, \dots, s_n$ también son números enteros distintos, y el polinomio se reescribe como:
$$f(x) = 2(x + s_1)(x + s_2)\cdots(x + s_n)$$

Al desarrollar este producto, utilizando las relaciones de Vieta tenemos que:
1. El término independiente es $a_0 = 2 s_1 s_2 \cdots s_n = 66$, lo que implica:
   $$s_1 s_2 \cdots s_n = 33$$
2. El coeficiente de $x^{n-1}$ es:
   $$a_{n-1} = 2(s_1 + s_2 + \cdots + s_n)$$

Por lo tanto, minimizar $|a_{n-1}|$ equivale a minimizar $2|s_1 + s_2 + \cdots + s_n|$, donde $s_1, s_2, \dots, s_n$ son enteros distintos cuyo producto es $33$.

La factorización en números primos de $33$ es $3 \times 11$. Para que la suma $|s_1 + s_2 + \cdots + s_n|$ sea lo más pequeña posible, nos conviene separar los factores $3$ y $11$ con signos opuestos para que se cancelen parcialmente:
- Si tomamos los factores con valor absoluto $3$ y $11$ con signos opuestos, su producto es $-33$ (es decir, $\{3, -11\}$ o $\{-3, 11\}$).
- Como el producto total debe ser $+33$, necesitamos multiplicar por $-1$ usando un subconjunto de $\{1, -1\}$ cuyo producto sea $-1$. Las opciones posibles para añadir al conjunto son únicamente $\{-1\}$ (que aporta $-1$ a la suma) o $\{1, -1\}$ (que aporta $0$ a la suma).

Analicemos las sumas de estas combinaciones:
- Con $\{-3, 11, -1\}$: el producto es $(-3)(11)(-1) = 33$ y la suma es $-3 + 11 - 1 = 7$.
- Con $\{-3, 11, 1, -1\}$: el producto es $(-3)(11)(1)(-1) = 33$ y la suma es $-3 + 11 + 1 - 1 = 8$.
- Con $\{3, -11, 1, -1\}$: el producto es $(3)(-11)(1)(-1) = 33$ y la suma es $3 - 11 + 1 - 1 = -8$.
- Con $\{3, -11, -1\}$: el producto es $(3)(-11)(-1) = 33$ y la suma es $3 - 11 - 1 = -9$.

El menor valor posible para $|s_1 + s_2 + \cdots + s_n|$ es $7$ (correspondiente a las raíces $r_1 = 3$, $r_2 = -11$ y $r_3 = 1$, que generan el polinomio $f(x) = 2(x-3)(x+11)(x-1) = 2x^3 + 14x^2 - 82x + 66$).

Así, el menor valor posible de $|a_{n-1}|$ es:
$$|a_{n-1}| = 2 \times 7 = 14$$

\boxed{14}