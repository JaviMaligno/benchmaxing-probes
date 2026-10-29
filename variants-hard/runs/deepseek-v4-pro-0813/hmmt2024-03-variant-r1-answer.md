Voy a razonar el problema paso a paso.

Sea $m$ un entero positivo de dos cifras. La propiedad dice: para todo número de cuatro cifras $N = \overline{pqrs} = 1000p + 100q + 10r + s$ que sea múltiplo de $m$, el número $N' = \overline{qrsp} = 1000q + 100r + 10s + p$ también es múltiplo de $m$.

Analicemos la relación entre $N$ y $N'$:

$$N' = 1000q + 100r + 10s + p$$

$$N = 1000p + 100q + 10r + s$$

Multipliquemos $N$ por $10$:

$$10N = 10000p + 1000q + 100r + 10s$$

Ahora restemos $N'$ de $10N$:

$$10N - N' = 10000p + 1000q + 100r + 10s - (1000q + 100r + 10s + p) = 9999p$$

Por lo tanto:

$$N' = 10N - 9999p$$

Dado que $9999 = 9 \cdot 1111 = 9 \cdot 11 \cdot 101 = 3^2 \cdot 11 \cdot 101$, tenemos:

$$9999 = 9 \cdot 11 \cdot 101$$

Si $N$ es múltiplo de $m$, queremos que $N'$ sea múltiplo de $m$ para **todo** $N$ múltiplo de $m$. Entonces:

$$N' \equiv -9999p \pmod{m}$$

Para que $N'$ sea múltiplo de $m$ para todo $N$ de cuatro cifras múltiplo de $m$, necesitamos que $m \mid 9999p$ para todo dígito $p$ que aparezca como primer dígito de un múltiplo de cuatro cifras de $m$.

Consideremos qué valores de $p$ pueden aparecer. Para cada $m$ de dos cifras, ¿existe un múltiplo de $m$ de cuatro cifras con primer dígito $p$ arbitrario?

Para que la propiedad valga con total generalidad, lo más natural es exigir que $m \mid 9999$, porque así $m \mid 9999p$ para todo $p$. De hecho, si $m \mid 9999$, entonces:

$$N' \equiv 10N - 9999p \equiv 0 - 0 = 0 \pmod{m}$$

siempre que $N \equiv 0 \pmod{m}$. Así que la condición suficiente es que $m \mid 9999$.

¿Es también necesaria? Verifiquemos. Para cada $m$ de dos cifras, existe al menos un múltiplo de $m$ de cuatro cifras con primer dígito $p$ para cada $p \in \{1, 2, \dots, 9\}$. En particular, para $p$ coprimo con $m$ (o más precisamente, tomando $p=1$), necesitamos $m \mid 9999 \cdot 1 = 9999$.

De hecho, para $m$ de dos cifras, siempre existe un múltiplo de $m$ de cuatro cifras que empieza con $1$: por ejemplo, $1000 \le km < 2000$ para algún $k$ entero. Como $m \le 99$, el intervalo de longitud $1000$ dentro de $[1000, 2000)$ contiene a un múltiplo de $m$ para todo $m \le 99$ (más precisamente, la distancia entre múltiplos consecutivos de $m$ es $m \le 99 < 1000$). Entonces existe $k$ con $1000 \le km < 2000$, es decir un múltiplo de $m$ de cuatro cifras con $p=1$.

Para ese $N$ con $p=1$, tenemos $N' \equiv -9999 \pmod{m}$. Como $N'$ debe ser múltiplo de $m$, tenemos $9999 \equiv 0 \pmod{m}$, es decir $m \mid 9999$.

Por lo tanto la condición es exactamente $m \mid 9999$, con $10 \le m \le 99$.

Los divisores de $9999 = 3^2 \cdot 11 \cdot 101$ son:

$$1, 3, 9, 11, 33, 99, 101, 303, 909, 1111, 3333, 9999$$

De dos cifras: $11, 33, 99$.

La suma es:

$$11 + 33 + 99 = 143$$

\boxed{143}