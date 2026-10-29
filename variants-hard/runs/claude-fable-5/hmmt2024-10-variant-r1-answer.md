## Planteamiento

Queremos los $n \le 100$ tales que $f(x) = x^4 + 20x^2 + n$ se factoriza módulo **todo** primo $p$ en factores de grado menor que 4.

**Hecho clave (Chebotarev/Dedekind):** si $f$ es irreducible sobre $\mathbb{Q}$, entonces $f$ es irreducible módulo algún primo si y solo si su grupo de Galois contiene un 4-ciclo. Para los primos que dividen al discriminante, $f \bmod p$ tiene raíz repetida, luego $\gcd(f, f')$ da un factor propio, así que esos primos nunca obstruyen.

Para un bicuadrático irreducible $x^4 + ax^2 + b$, el grupo de Galois es:
- $V_4$ (sin 4-ciclos) si $b$ es un cuadrado,
- $C_4$ o $D_4$ (con 4-ciclos) en caso contrario.

Por tanto, $f$ es *breakable* si y solo si **es reducible sobre $\mathbb{Z}$** o **$n$ es un cuadrado perfecto**.

## Caso reducible sobre $\mathbb{Z}$

No hay raíces racionales (pues $n > 0$), así que la única opción es producto de dos cuadráticas mónicas $(x^2+ax+b)(x^2+cx+d)$. Del coeficiente de $x^3$: $c = -a$; del coeficiente de $x$: $a(d-b) = 0$. Dos subcasos:

- **$a = 0$:** $b + d = 20$, $bd = n$, es decir $n = b(20-b)$. Para $b = 1, \dots, 10$ se obtiene $n \in \{19, 36, 51, 64, 75, 84, 91, 96, 99, 100\}$.
- **$d = b$:** $2b - a^2 = 20$, $n = b^2$, que ya cae dentro del caso "$n$ cuadrado".

## Caso $n$ cuadrado

$n \in \{1, 4, 9, 16, 25, 36, 49, 64, 81, 100\}$. Aquí el grupo de Galois es $V_4$ (o $f$ es reducible), y en ambos casos $f$ se factoriza módulo todo primo. (Verificación en primos malos: módulo 2, $f \equiv x^4$ o $(x+1)^4$; en general los primos del discriminante dan factores repetidos.)

## Suma

- Suma de cuadrados: $1+4+\cdots+100 = 385$.
- Suma de $b(20-b)$: $19+36+51+64+75+84+91+96+99+100 = 715$.
- Intersección: $\{36, 64, 100\}$, suma $200$.

Total: $385 + 715 - 200 = 900$.

$$\boxed{900}$$