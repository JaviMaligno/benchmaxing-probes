Voy a resolver el problema paso a paso.

Queremos los enteros positivos \(n\) con \(60 \le n \le 120\) tales que \(2n+3\) **no** divide a \(2^{n!} - 1\).

---

## Paso 1: Condición de divisibilidad

\(2n+3 \mid 2^{n!} - 1\) significa que
\[
2^{n!} \equiv 1 \pmod{2n+3}.
\]

Sea \(m = 2n+3\). Notemos que \(m\) es impar (pues \(2n+3\) es impar), así que 2 es invertible módulo \(m\).

Entonces la condición es equivalente a que el orden de 2 módulo \(m\) divida a \(n!\).

---

## Paso 2: Reformular el problema

Queremos los \(n\) donde esto **no** ocurre. Dividimos el análisis según la factorización de \(m = 2n+3\).

Sea \(\ell\) un primo que divide a \(m\), con \(\ell^a \| m\) (potencia exacta). Entonces:

- Para \(\ell = 2\): no aplica, \(m\) es impar.
- Para \(\ell\) impar: el orden de 2 módulo \(\ell^a\) es un divisor de \(\varphi(\ell^a) = \ell^{a-1}(\ell-1)\).

La condición \(2^{n!} \equiv 1 \pmod{\ell^a}\) para todos los \(\ell^a \| m\) ocurre si y solo si el orden de 2 módulo \(\ell^a\) divide a \(n!\) para cada primo \(\ell\).

---

## Paso 3: ¿Cuándo podría fallar?

El orden de 2 módulo \(\ell^a\) divide a \(\ell^{a-1}(\ell-1)\). Para que este orden divida a \(n!\), basta que \(\ell\) sea suficientemente pequeño comparado con \(n\), o que \(\ell-1\) tenga factores que aparezcan en \(n!\).

En concreto, si \(\ell \le n\), entonces todos los factores del orden (que dividen a \(\ell^{a-1}(\ell-1)\)) aparecen en \(n!\), así que la congruencia se cumple automáticamente. Es decir, **solo pueden fallar los casos donde hay un primo \(\ell \mid m\) con \(\ell > n\)**.

---

## Paso 4: Los posibles "primos malos" \(\ell > n\)

Como \(m = 2n+3\) y \(n \le 120\), tenemos \(m \le 243\).

Si \(\ell \mid m\) y \(\ell > n\), entonces \(\ell > n \ge 60\). Como \(m \le 243\), el primo \(\ell\) puede ser mayor que \(n\) pero menor o igual que \(243\).

Además, \(m = 2n+3\), así que \(\ell\) debe cumplir \(\ell \le 2n+3\).

Si \(\ell \mid (2n+3)\), escribamos \(2n+3 = k\ell\) con \(k \ge 1\) entero impar.

---

## Paso 5: Análisis de casos

**Caso principal:** El mayor primo \(\ell\) que divide a \(m\) es \(> n\).

Esto implica \(2n+3\) tiene un factor primo \(\ell > n\). Como \(2n+3 < 3n\) para \(n > 3\), el factor \(\ell\) debe ser el primo grande y el cofactor debe ser pequeño.

Escribamos \(2n+3 = \ell \cdot q\) con \(\ell > n\) primo y \(q\) impar.

Como \(\ell > n\):
\[
q = \frac{2n+3}{\ell} < \frac{2n+3}{n} = 2 + \frac{3}{n} < 3
\]
para \(n > 3\). Como \(q\) es entero impar, \(q = 1\).

Entonces \(2n+3 = \ell\) debe ser primo y \(\ell > n\).

---

## Paso 6: Verificar cuándo el orden de 2 no divide a \(n!\)

Si \(m = 2n+3 = \ell\) es primo con \(\ell > n\), el orden de 2 módulo \(\ell\) divide a \(\ell - 1 = 2n+2 = 2(n+1)\).

Para que el orden divida a \(n!\), necesitamos que todos los factores primos del orden estén en \(n!\).

El orden de 2 módulo \(\ell\) es un divisor de \(2(n+1)\). Si el orden tiene un factor primo \(p\) tal que \(p > n\), entonces el orden no dividirá a \(n!\) (porque \(n!\) no contiene primos mayores que \(n\)).

Los divisores de \(2(n+1)\) con factores primos \(> n\): los únicos primos posibles mayores que \(n\) que dividen a \(2(n+1)\) son los primos \(p\) con \(p \le 2n+2\). En particular, si \(n+1\) tiene un factor primo \(p > n\), esto fuerza \(p = n+1\) (porque \(p \le n+1\) y \(p > n\)). Entonces \(n+1\) debe ser primo.

---

## Paso 7: Subcaso \(n+1\) primo

Si \(n+1 = p\) es primo, entonces \(\ell = 2n+3 = 2p+1\).

El orden de 2 módulo \(\ell = 2p+1\) divide a \(\ell - 1 = 2p\).

Los divisores de \(2p\) son \(1, 2, p, 2p\). El orden podría ser \(p\) o \(2p\), que contienen el factor primo \(p > n\) (pues \(p = n+1 > n\)). En ese caso el orden no dividiría a \(n!\).

Sin embargo, podría ocurrir que el orden de 2 módulo \(\ell\) sea 1 o 2, que sí dividen a \(n!\). El orden es 1 si \(\ell \mid 1\), imposible. El orden es 2 si \(2^2 \equiv 1 \pmod{\ell}\), es decir \(\ell \mid 3\), así \(\ell = 3\), que es imposible aquí.

Por lo tanto, si \(n+1\) es primo, el orden de 2 módulo \(2n+3 = 2p+1\) es \(p\) o \(2p\), que no dividen a \(n!\).

**Pero falta verificar que \(2n+3 = 2p+1\) sea efectivamente primo.** No todos los \(n+1\) primos dan \(2n+3\) primo.

---

## Paso 8: Enumerar los casos

Necesitamos \(n \in [60,120]\) con \(2n+3\) primo y \(n+1\) primo.

Como \(n+1\) primo, \(n\) es par (pues si \(n+1 > 2\) es primo, \(n+1\) es impar, luego \(n\) es par).

Los primos \(p = n+1\) en el rango:

Para \(n \in [60,120]\), \(p = n+1 \in [61,121]\). Primos en ese rango: 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113.

Check \(2p+1\) primo:

- \(p=61\): \(2p+1 = 123 = 3 \cdot 41\), no primo.
- \(p=67\): \(135 = 3^3 \cdot 5\), no.
- \(p=71\): \(143 = 11 \cdot 13\), no.
- \(p=73\): \(147 = 3 \cdot 49\), no.
- \(p=79\): \(159 = 3 \cdot 53\), no.
- \(p=83\): \(167\), primo. ✓
- \(p=89\): \(179\), primo. ✓
- \(p=97\): \(195 = 3\cdot 5\cdot 13\), no.
- \(p=101\): \(203 = 7 \cdot 29\), no.
- \(p=103\): \(207 = 9 \cdot 23\), no.
- \(p=107\): \(215 = 5 \cdot 43\), no.
- \(p=109\): \(219 = 3 \cdot 73\), no.
- \(p=113\): \(227\), primo. ✓

Así que \(p \in \{83, 89, 113\}\), lo que da \(n = p-1 \in \{82, 88, 112\}\).

Estos son los \(n\) donde \(2n+3 \nmid 2^{n!}-1\).

---

## Paso 9: Verificación adicional

¿Hay casos con \(m\) compuesto donde aún así falle la divisibilidad?

Si \(m = 2n+3\) tiene todos sus divisores primos \(\le n\), el orden de 2 módulo cada potencia prima divide a un número cuyos factores primos son \(\le n\), así que divide a \(n!\), y la congruencia se cumple.

La única forma de fallar es tener un primo \(\ell \mid m\) con \(\ell > n\). Como mostramos, eso fuerza \(m = \ell\) primo y además, para que el orden no divida a \(n!\), necesitamos \(n+1\) primo. Los únicos casos son \(n = 82, 88, 112\).

---

## Paso 10: Suma final

\[
82 + 88 + 112 = 282
\]

\[
\boxed{282}
\]