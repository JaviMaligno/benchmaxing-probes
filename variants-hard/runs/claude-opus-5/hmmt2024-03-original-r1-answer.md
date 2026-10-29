## Planteamiento

Sea $N = \underline{a}\,\underline{b}\,\underline{c} = 100a + 10b + c$ y $M = \underline{b}\,\underline{c}\,\underline{a} = 100b + 10c + a$.

**Relación clave:**
$$10N = 1000a + 100b + 10c = (100b + 10c + a) + 999a = M + 999a$$

Es decir, $M = 10N - 999a$.

## Condición sobre $x$

Si $x \mid N$, entonces $x \mid 10N$, de modo que
$$x \mid M \iff x \mid 999a.$$

Por lo tanto, $x$ cumple la propiedad si y solo si $x \mid 999a$ para todo dígito de centenas $a$ que aparezca en algún múltiplo de $x$ de tres cifras.

## ¿Qué valores de $a$ aparecen?

Como $x$ tiene dos cifras, $x \le 99 < 100$, así que todo intervalo de 100 enteros consecutivos contiene un múltiplo de $x$. En particular, cada bloque $[100a, 100a+99]$ con $a = 1,\dots,9$ contiene un múltiplo de $x$. Luego **todos** los dígitos $a = 1, 2, \dots, 9$ se realizan.

Escribiendo $g = \gcd(x, 999)$ y $k = x/g$, la condición $x \mid 999a$ equivale a $k \mid a$. Al exigirlo para todo $a \in \{1,\dots,9\}$ (en particular $a=1$), se obtiene $k = 1$, es decir:
$$x \mid 999.$$

## Divisores de dos cifras de $999$

$$999 = 3^3 \cdot 37$$

Sus divisores son $1, 3, 9, 27, 37, 111, 333, 999$. Los de dos cifras: $\boxed{27}$ y $37$.

**Verificación ($x=27$):** $N=135 \Rightarrow M=351 = 27\cdot 13$. ✓
**Verificación ($x=37$):** $N=148 \Rightarrow M=481 = 37\cdot 13$. ✓
(Y en general $M = 10N - 999a$ es múltiplo de $x$ porque $x$ divide a ambos términos.)

## Suma

$$27 + 37 = 64$$

\boxed{64}