## Planteamiento

Sea $N = \underline{p}\,\underline{q}\,\underline{r}\,\underline{s} = 1000p + 100q + 10r + s$ y sea $N' = 1000q + 100r + 10s + p$.

Entonces:
$$N' = 10(N - 1000p) + p = 10N - 9999p$$

## Condición

Si $m \mid N$, entonces $m \mid N'$ si y solo si $m \mid 9999p$.

Es decir, la propiedad pedida equivale a:
$$\text{para todo múltiplo de cuatro cifras } N \text{ de } m,\quad m \mid 9999p$$

Sea $d = \gcd(m, 9999)$ y $k = m/d$. Como $\gcd(m/d,\ 9999/d) = 1$, se tiene
$$m \mid 9999p \iff k \mid p.$$

## Análisis

**Caso $k = 1$** (o sea $m \mid 9999$): la condición se cumple siempre, sin importar $p$.

**Caso $k > 1$**: haría falta que $k \mid p$ para todos los dígitos iniciales $p$ que aparecen. Pero como $m \le 99 < 1000$, cada bloque $[1000p,\ 1000p + 999]$ con $p = 1,\dots,9$ (de longitud 1000) contiene al menos un múltiplo de $m$. Por tanto **todos** los valores $p = 1,2,\dots,9$ se realizan, y necesitaríamos $k \mid p$ para todo $p$ de 1 a 9, lo que fuerza $k = 1$. Contradicción.

Luego la propiedad se cumple exactamente cuando $m \mid 9999$.

## Divisores

$$9999 = 3^2 \cdot 11 \cdot 101$$

Divisores: $1, 3, 9, 11, 33, 99, 101, 303, 909, 1111, 3333, 9999$.

Los de dos cifras son: $11,\ 33,\ 99$.

## Suma

$$11 + 33 + 99 = 143$$

\boxed{143}