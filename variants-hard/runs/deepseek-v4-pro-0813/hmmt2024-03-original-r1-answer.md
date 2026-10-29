Voy a resolver el problema paso a paso.

Sea \(x\) un entero de dos cifras, es decir, \(10 \le x \le 99\).

Denotemos \(N = \overline{abc} = 100a + 10b + c\) y \(M = \overline{bca} = 100b + 10c + a\).

Queremos que, para todo \(N\) de tres cifras múltiplo de \(x\), también \(M\) sea múltiplo de \(x\).

## Paso 1: Relación entre \(M\) y \(N\)

\[
M = 100b + 10c + a
\]

Queremos expresar \(M\) en términos de \(N\). Observamos:

\[
10N = 1000a + 100b + 10c
\]

\[
M = 100b + 10c + a
\]

Restando:

\[
10N - M = 1000a + 100b + 10c - 100b - 10c - a = 999a
\]

Por lo tanto:

\[
M = 10N - 999a
\]

Como \(999 = 3^3 \cdot 37\), tenemos \(999 = 27 \cdot 37\).

Si \(N \equiv 0 \pmod{x}\) y queremos \(M \equiv 0 \pmod{x}\), entonces:

\[
M \equiv 10N - 999a \equiv -999a \pmod{x}
\]

Como \(10N \equiv 0 \pmod{x}\) cuando \(x \mid N\), la condición se reduce a:

\[
999a \equiv 0 \pmod{x} \quad \text{para todo } a \in \{1, \dots, 9\}
\]

## Paso 2: Condición según los dígitos posibles

La variable \(a\) (centena de \(N\)) puede tomar cualquier valor de \(1\) a \(9\). La condición requiere que \(999a \equiv 0 \pmod{x}\) para todos esos valores de \(a\).

En particular, tomando \(a=1\):

\[
999 \equiv 0 \pmod{x}
\]

Es decir, \(x \mid 999\).

Recíprocamente, si \(x \mid 999\), entonces \(x \mid 999a\) para todo \(a\), y la condición se cumple.

Por lo tanto:

\[
x \mid 999
\]

## Paso 3: Divisores de dos cifras de \(999\)

Factorizamos:

\[
999 = 3^3 \cdot 37
\]

Divisores de dos cifras:

- \(3^2 = 9\) (una cifra, se descarta)
- \(3^3 = 27\) ✓
- \(37\) ✓
- \(3 \cdot 37 = 111\) (tres cifras, se descarta)
- \(3^0 = 1, 3\) (una cifra)

Así que los divisores de dos cifras son:

\[
x = 27, \; 37
\]

## Paso 4: Verificación

Para \(x=27\): si \(N = \overline{abc}\) es múltiplo de \(27\), como \(999a \equiv 0 \pmod{27}\), entonces \(M = 10N - 999a \equiv 0 \pmod{27}\). ✓

Para \(x=37\): análogamente, \(999 = 27 \cdot 37\), así que \(999a \equiv 0 \pmod{37}\), y \(M \equiv 0 \pmod{37}\). ✓

## Paso 5: Suma

\[
27 + 37 = 64
\]

\[
\boxed{64}
\]