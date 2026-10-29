## Planteamiento

Queremos saber para qué $n$ el polinomio $f(x) = x^4 + 16x^2 + n$ se factoriza módulo **todo** primo $p$ en factores de grado menor que 4.

**Caso $p = 2$:** módulo 2, $f \equiv x^4 + n \equiv (x^2 + n)^2 \pmod 2$ (el cuadrado es el Frobenius), así que siempre se factoriza. Solo importan los primos impares.

## Factorización módulo un primo impar

Sobre $\overline{\mathbb{F}_p}$, las raíces de $f$ son $\pm u, \pm v$, donde $u^2, v^2$ son las raíces de $y^2 + 16y + n$, es decir $u^2, v^2 = \frac{-16 \pm \sqrt{256-4n}}{2}$. Nótese que $u^2 v^2 = n$ y $u^2 + v^2 = -16$.

Si $f$ es reducible mod $p$, tiene un factor cuadrático (un factor lineal daría $u \in \mathbb{F}_p$, luego $u^2 \in \mathbb{F}_p$). Las posibles parejas de raíces son:

- $(x-u)(x+u) = x^2 - u^2$: requiere $u^2 \in \mathbb{F}_p$, es decir que $256 - 4n$ sea residuo cuadrático (RC) mod $p$.
- $(x-u)(x\mp v)$: el término constante es $\mp uv$ con $(uv)^2 = n$, así que requiere que $n$ sea RC mod $p$.

Recíprocamente:

- Si $256 - 4n$ es RC, entonces $u^2, v^2 \in \mathbb{F}_p$ y $f = (x^2 - u^2)(x^2 - v^2)$ funciona.
- Si $n \equiv \gamma^2$ es RC, intentamos $f = (x^2 + \beta x + \gamma)(x^2 - \beta x + \gamma)$, que exige $\beta^2 = 2\gamma - 16$. Para las dos elecciones $\pm\gamma$, el producto es $(2\gamma - 16)(-2\gamma - 16) = 256 - 4n$. Si $256-4n$ no es RC, exactamente una de las dos opciones es RC y la factorización existe; si sí es RC, ya estamos en el caso anterior.

**Conclusión local:** $f$ es reducible mod $p$ $\iff$ $n$ o $256 - 4n$ es un cuadrado mod $p$.

## Condición global

$f$ es splitty $\iff$ para todo primo impar $p$, $n$ o $256-4n$ es RC mod $p$.

- Si $n$ es un cuadrado perfecto o $256 - 4n$ es un cuadrado perfecto, la condición se cumple para todo $p$. ✓
- Si ninguno lo es: si $n(256-4n)$ **no** es cuadrado perfecto, $\sqrt{n}$ y $\sqrt{256-4n}$ generan cuerpos cuadráticos distintos y (por reciprocidad cuadrática / Chebotarev) existe un primo $p$ donde ambos son no residuos. Si $n(256-4n)$ **sí** es cuadrado perfecto, entonces $n$ y $256-4n$ son residuos o no residuos simultáneamente; eligiendo $p$ donde $n$ es no residuo, ambos fallan. En cualquier caso, $f$ no es splitty. ✗

Por tanto: $f$ es splitty $\iff$ $n$ es cuadrado perfecto o $256 - 4n = 4(64-n)$ es cuadrado perfecto, es decir, $64 - n$ es cuadrado perfecto.

## Cuenta para $1 \le n \le 100$

**Cuadrados perfectos:** $1+4+9+16+25+36+49+64+81+100 = 385$.

**$64 - n = k^2$ con $n \ge 1$:** $n \in \{63, 60, 55, 48, 39, 28, 15, 64\}$ (para $k = 1,\dots,7$ y $k=0$), con suma $63+60+55+48+39+28+15+64 = 372$.

**Intersección:** solo $n = 64$ (es $8^2$ y da $64-64 = 0^2$).

$$385 + 372 - 64 = 693$$

$$\boxed{693}$$