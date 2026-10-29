Vamos a resolver el problema paso a paso.

## 1. La moneda de 25 centavos domina

Con monedas de $1, 10, 25$ centavos, cualquier colección óptima (mínima cantidad de monedas) usa a lo sumo $2$ monedas de $10$ centavos y a lo sumo $24$ monedas de $1$ centavo, porque:

- $3$ monedas de $10$ se reemplazan por $30$ centavos, que pueden hacerse con $1$ moneda de $25$ y $5$ de $1$: $6$ monedas → $6$ monedas, no mejora estrictamente, pero con $25 + 5$ también son $6$. Aún así, en el óptimo podemos suponer a lo sumo $2$ monedas de $10$.
- $5$ monedas de $10$ equivalen a $2$ de $25$, usando menos monedas ($5$ vs $2$).

De hecho, lo más útil es observar que el valor de las monedas de $25$ se puede elegir en una cantidad $q$, y el resto $r = N - 25q$ debe pagarse con monedas de $10$ y $1$.

## 2. El algoritmo voraz

Para $N = 25a + b$ con $0 \le b < 25$:
- Cantidad de monedas de $25$: $a$.
- Después, para el resto $b$:
  - monedas de $10$: $\lfloor b/10 \rfloor$
  - monedas de $1$: $b \bmod 10$

Total de monedas voraz:

\[
G(N) = a + \lfloor b/10 \rfloor + (b \bmod 10)
\]

## 3. El óptimo

El número óptimo de monedas es

\[
M(N) = \min_{\substack{q,d \\ 25q+10d \le N}} (q + d + (N - 25q - 10d))
\]

Pero notemos que para el resto $r = N - 25q$, con monedas de $10$ y $1$, el óptimo es

\[
f(r) = \min_{d} (d + (r - 10d)) = \min_d (r - 9d)
\]

con $r - 10d \ge 0$. Para maximizar $r-9d$ escogemos $d$ lo más grande posible, $d=\lfloor r/10\rfloor$, así

\[
f(r) = r - 9\lfloor r/10\rfloor = \lfloor r/10\rfloor + (r \bmod 10)
\]

Esto es exactamente lo mismo que haría el voraz para el resto. Por lo tanto, el óptimo global es

\[
M(N) = \min_{0\le q\le \lfloor N/25\rfloor} \left(q + f(N - 25q)\right)
\]

## 4. Condición de éxito del voraz

El voraz elige $q = a = \lfloor N/25\rfloor$. Entonces el voraz tiene éxito si:

\[
G(N) \le q + f(N - 25q) \quad \forall q
\]

es decir, el voraz iguala el óptimo.

Como $f$ es una función del resto módulo $25$, definamos para $b \in \{0,\dots,24\}$:

\[
f(b) = \lfloor b/10\rfloor + (b \bmod 10)
\]

El voraz con $a$ monedas de $25$ da $a + f(b)$. Otra elección $q = a - k$ (con $k \ge 1$) da:

\[
(a - k) + f(b + 25k)
\]

porque el resto crece en $25k$. El voraz fracasa si para algún $k\ge 1$:

\[
(a-k) + f(b+25k) < a + f(b)
\]

\[
f(b+25k) - k < f(b)
\]

Esto no depende de $a$, solo de $b$ y $k$.

Además, $q$ solo puede bajar hasta donde no se supere $N$. Para $k \le a$.

## 5. Análisis por restos $b$

Como $f(b+25)=f(b)+f(25)=f(b)+3$, porque $f(25)=3$ ($25 = 10+10+1+1+1+1$ en $6$? No, veamos: $f(25)=\lfloor 25/10\rfloor + (25\bmod 10) = 2+5=7$. Hmm, cuidado.

Calculemos $f(b+25)$ directamente. Por ejemplo $b+25$ con monedas de $10$ y $1$:

Para $r = b+25$, usando $d=\lfloor (b+25)/10\rfloor$:

\[
f(b+25) = \left\lfloor \frac{b+25}{10}\right\rfloor + ((b+25)\bmod 10)
\]

No es simplemente $f(b)+f(25)$ porque $25$ no es múltiplo de $10$.

Así que analicemos todos los $b$:

| $b$ | $f(b)$ | $f(b+25)$ | $f(b+50)$ | $f(b+75)$ |
|---|---|---|---|---|
| 0 | 0 | 7 | 14 | 21 |
| 1 | 1 | 8 | 15 | 22 |
| 2 | 2 | 9 | 16 | 23 |
| 3 | 3 | 10 | 17 | 24 |
| 4 | 4 | 11 | 18 | 25 |
| 5 | 5 | 12 | 19 | 26 |
| 6 | 6 | 13 | 20 | 27 |
| 7 | 7 | 14 | 21 | 28 |
| 8 | 8 | 15 | 22 | 29 |
| 9 | 9 | 16 | 23 | 30 |
| 10 | 1 | 8 | 15 | 22 |
| 11 | 2 | 9 | 16 | 23 |
| 12 | 3 | 10 | 17 | 24 |
| 13 | 4 | 11 | 18 | 25 |
| 14 | 5 | 12 | 19 | 26 |
| 15 | 6 | 13 | 20 | 27 |
| 16 | 7 | 14 | 21 | 28 |
| 17 | 8 | 15 | 22 | 29 |
| 18 | 9 | 16 | 23 | 30 |
| 19 | 10 | 17 | 24 | 31 |
| 20 | 2 | 9 | 16 | 23 |
| 21 | 3 | 10 | 17 | 24 |
| 22 | 4 | 11 | 18 | 25 |
| 23 | 5 | 12 | 19 | 26 |
| 24 | 6 | 13 | 20 | 27 |

## 6. Condición de éxito

Para cada $b$, el voraz falla si existe $k \ge 1$ con

\[
f(b+25k) - k < f(b)
\]

Comprobemos $k=1,2,3,4$ (más allá, la tabla sugiere que la diferencia crece).

Para cada $b$, busquemos el mínimo de $f(b+25k)-k$:

- $b=0$: $k=1$: $7-1=6 > 0$. $k=2$: $14-2=12$, etc. No falla.
- $b=1$: $k=1$: $8-1=7>1$. No falla.
- $b=2$: $k=1$: $9-1=8>2$.
- $b=3$: $k=1$: $10-1=9>3$.
- $b=4$: $k=1$: $11-1=10>4$.
- $b=5$: $k=1$: $12-1=11>5$.
- $b=6$: $k=1$: $13-1=12>6$.
- $b=7$: $k=1$: $14-1=13>7$.
- $b=8$: $k=1$: $15-1=14>8$.
- $b=9$: $k=1$: $16-1=15>9$.
- $b=10$: $f(10)=1$. $k=1$: $f(35)=8$, $8-1=7>1$. Sí.
- $b=11$: $f(11)=2$, $k=1$: $f(36)=9$, $9-1=8>2$.
- $b=12$: $f(12)=3$, $f(37)=10$, $10-1=9>3$.
- $b=13$: $f(13)=4$, $f(38)=11$, $11-1=10>4$.
- $b=14$: $f(14)=5$, $f(39)=12$, $12-1=11>5$.
- $b=15$: $f(15)=6$, $f(40)=13$, $13-1=12>6$.
- $b=16$: $f(16)=7$, $f(41)=14$, $14-1=13>7$.
- $b=17$: $f(17)=8$, $f(42)=15$, $15-1=14>8$.
- $b=18$: $f(18)=9$, $f(43)=16$, $16-1=15>9$.
- $b=19$: $f(19)=10$, $f(44)=17$, $17-1=16>10$.
- $b=20$: $f(20)=2$, $k=1$: $f(45)=9$, $9-1=8>2$.
- $b=21$: $f(21)=3$, $f(46)=10$, $10-1=9>3$.
- $b=22$: $f(22)=4$, $f(47)=11$, $11-1=10>4$.
- $b=23$: $f(23)=5$, $f(48)=12$, $12-1=11>5$.
- $b=24$: $f(24)=6$, $f(49)=13$, $13-1=12>6$.

Parece que para $k=1$ nunca hay mejora. ¿Qué pasa con valores más grandes? La tendencia es que $f(b+25k) \approx 7k$, así que $f(b+25k)-k \approx 6k$, siempre crece. Entonces no hay ninguna mejora posible.

## 7. Conclusión sorprendente

¿Eso implicaría que el voraz siempre acierta? Eso contradice el ejemplo de $N=42$ dado en el enunciado.

Revisemos $N=42$: $42 = 25+17$, así que $a=1$, $b=17$.

Voraz: moneda de $25$, luego $17$ con una de $10$ y $7$ de $1$: $1+1+7=9$ monedas.

Óptimo: $42 = 4\cdot 10 + 2$, son $6$ monedas.

Pero en mi análisis, el óptimo con $q=0$ sería $q=0$, $f(42) = \lfloor 42/10\rfloor + (42\bmod 10) = 4+2=6$. Eso es $0 + f(42) = 6$.

Entonces la condición con $k=1$ (es decir $q = a-1 = 0$) es:

\[
f(b+25) - 1 < f(b)
\]

Para $b=17$:

\[
f(42) - 1 = 6 - 1 = 5 < f(17) = 8
\]

¡Sí! $5 < 8$. Entonces sí falla. ¿Por qué en mi tabla me dio $15 - 1 = 14 > 8$? ¡Error mío al calcular $f(42)$!

Revisemos. $42 = 4\cdot 10 + 2$, así que monedas: $4$ de $10$ y $2$ de $1$: $6$ monedas. Entonces $f(42)=6$, no $15$.

El error está en la tabla. Para $b=17$, $b+25=42$. Calculemos bien:

- $f(42) = \lfloor 42/10\rfloor + (42 \bmod 10) = 4 + 2 = 6$.

En mi tabla puse $15$ para $f(b+25)$ con $b=17$. Eso fue incorrecto; parece que usé $f(r)=r-9\lfloor r/10\rfloor$ mal, o simplemente cometí un error aritmético.

Rehagamos la tabla con cuidado.

$f(r) = \lfloor r/10\rfloor + (r\bmod 10)$.

| $r$ | $f(r)$ |
|---|---|
| 0 | 0 |
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |
| 4 | 4 |
| 5 | 5 |
| 6 | 6 |
| 7 | 7 |
| 8 | 8 |
| 9 | 9 |
| 10 | 1 |
| 11 | 2 |
| 12 | 3 |
| 13 | 4 |
| 14 | 5 |
| 15 | 6 |
| 16 | 7 |
| 17 | 8 |
| 18 | 9 |
| 19 | 10 |
| 20 | 2 |
| 21 | 3 |
| 22 | 4 |
| 23 | 5 |
| 24 | 6 |
| 25 | 7 |
| 26 | 8 |
| 27 | 9 |
| 28 | 10 |
| 29 | 11 |
| 30 | 3 |
| 31 | 4 |
| 32 | 5 |
| 33 | 6 |
| 34 | 7 |
| 35 | 8 |
| 36 | 9 |
| 37 | 10 |
| 38 | 11 |
| 39 | 12 |
| 40 | 4 |
| 41 | 5 |
| 42 | 6 |
| 43 | 7 |
| 44 | 8 |
| 45 | 9 |
| 46 | 10 |
| 47 | 11 |
| 48 | 12 |
| 49 | 13 |

Ahora sí. Entonces para $b=17$:

\[
f(b)=f(17)=8
\]

\[
f(b+25)=f(42)=6
\]

Condición con $k=1$:

\[
6 - 1 = 5 < 8
\]

Así que el voraz falla. Correcto.

## 8. Análisis correcto

El voraz tiene éxito si para todo $k \ge 1$ (con $k\le a$):

\[
f(b+25k) - k \ge f(b)
\]

Es decir, quitar $k$ monedas de $25$ no reduce el total.

Veamos cuándo falla. Como $f$ es periódica en cierta forma, analicemos.

Notemos que $f(r) = \lfloor r/10\rfloor + (r\bmod 10)$. Para $r = b + 25k$:

Escribamos $b = 10m + n$ con $0\le n \le 9$ y $m\in\{0,1,2\}$ (pues $b<25$).

Entonces:

\[
b + 25k = 10m + n + 25k = 10(m + \lfloor (n+25k)/10\rfloor) + ((n+25k)\bmod 10)
\]

pero es más simple trabajar directamente.

También observemos que $25k = 2\cdot 10k + 5k$. Así,

\[
b+25k = 10m+n + 20k + 5k = 10(m+2k) + n + 5k
\]

Entonces:

\[
\left\lfloor \frac{b+25k}{10}\right\rfloor = m + 2k + \left\lfloor \frac{n+5k}{10}\right\rfloor
\]

y

\[
(b+25k)\bmod 10 = (n+5k)\bmod 10
\]

Por lo tanto:

\[
f(b+25k) = m + 2k + \left\lfloor \frac{n+5k}{10}\right\rfloor + (n+5k)\bmod 10
\]

Y $f(b) = m + n$ (porque $\lfloor b/10\rfloor = m$ y $b\bmod 10 = n$).

Entonces:

\[
f(b+25k) - f(b) = 2k + \left\lfloor \frac{n+5k}{10}\right\rfloor + ((n+5k)\bmod 10) - n
\]

Ahora, notemos la identidad

\[
x = \lfloor x/10\rfloor \cdot 10 + (x\bmod 10)
\]

así que $\lfloor x/10\rfloor + (x\bmod 10) = x - 9\lfloor x/10\rfloor$.

Sea $x = n+5k$. Entonces:

\[
\left\lfloor \frac{n+5k}{10}\right\rfloor + ((n+5k)\bmod 10) = n + 5k - 9\left\lfloor \frac{n+5k}{10}\right\rfloor
\]

Sustituyendo:

\[
f(b+25k) - f(b) = 2k + n + 5k - 9\lfloor (n+5k)/10\rfloor - n
\]

\[
= 7k - 9\left\lfloor \frac{n+5k}{10}\right\rfloor
\]

La condición de fracaso es:

\[
f(b+25k) - k < f(b)
\]

\[
f(b+25k) - f(b) < k
\]

\[
7k - 9\left\lfloor \frac{n+5k}{10}\right\rfloor < k
\]

\[
6k < 9\left\lfloor \frac{n+5k}{10}\right\rfloor
\]

\[
\frac{2k}{3} < \left\lfloor \frac{n+5k}{10}\right\rfloor
\]

Equivalentemente, el voraz falla para $b=10m+n$ si existe $k\ge 1$ (con $k\le a$) tal que:

\[
\left\lfloor \frac{n+5k}{10}\right\rfloor > \frac{2k}{3}
\]

Analicemos. Notemos que $n+5k$ está entre $5k$ y $5k+9$. Entonces

\[
\frac{n+5k}{10} = \frac{5k+n}{10}
\]

\[
\left\lfloor \frac{5k+n}{10}\right\rfloor \in \left\{ \left\lfloor \frac{5k}{10}\right\rfloor, \left\lfloor \frac{5k}{10}\right\rfloor + \text{quizá } 1\right\}
\]

porque $n\le 9 < 10$, el valor puede aumentar a lo sumo en $1$ (si $5k \bmod 10 + n \ge 10$).

Entonces:

\[
\left\lfloor \frac{5k+n}{10}\right\rfloor = \left\lfloor \frac{5k}{10}\right\rfloor + \mathbf{1}_{\{5k \bmod 10 + n \ge 10\}}
\]

Y $\lfloor 5k/10\rfloor = \lfloor k/2\rfloor$ (pues $5k/10 = k/2$).

Así:

\[
\left\lfloor \frac{n+5k}{10}\right\rfloor = \left\lfloor \frac{k}{2}\right\rfloor + c
\]

donde $c\in\{0,1\}$ y $c=1$ si y solo si $(5k \bmod 10) + n \ge 10$.

Ahora,

- Si $k$ es par, $5k \bmod 10 = 0$, así $c=1$ si y solo si $n\ge 10$, lo que es falso. Por tanto $c=0$ siempre para $k$ par.
- Si $k$ es impar, $5k \bmod 10 = 5$, así $c=1$ si y solo si $n \ge 5$.

Entonces:

\[
\left\lfloor \frac{n+5k}{10}\right\rfloor =
\begin{cases}
k/2, & k \text{ par}\\
(k-1)/2 + (n\ge 5 ? 1 : 0), & k \text{ impar}
\end{cases}
\]

La condición de fracaso $\left\lfloor \frac{n+5k}{10}\right\rfloor > 2k/3$:

**Para $k$ par:**

\[
k/2 > 2k/3 \iff 3k > 4k \iff 0 > k
\]

imposible para $k>0$. Así que el voraz nunca falla con $k$ par.

**Para $k$ impar:**

- Si $n < 5$:

\[
\frac{k-1}{2} > \frac{2k}{3}
\]

\[
3(k-1) > 4k \Rightarrow 3k - 3 > 4k \Rightarrow -3 > k
\]

imposible.

- Si $n \ge 5$:

\[
\frac{k-1}{2} + 1 > \frac{2k}{3}
\]

\[
\frac{k+1}{2} > \frac{2k}{3}
\]

\[
3(k+1) > 4k \Rightarrow 3k + 3 > 4k \Rightarrow 3 > k
\]

Entonces $k = 1$ es la única posibilidad (impar) y requiere $n\ge 5$.

Por lo tanto, el voraz falla exactamente cuando existe $k=1$ con $n\ge 5$, es decir, cuando $a \ge 1$ (para que $k=1\le a$) y $b \bmod 10 \ge 5$.

Es decir, el voraz falla si y solo si:

\[
a \ge 1 \quad \text{y} \quad b \bmod 10 \ge 5
\]

donde $b = N \bmod 25$ y $a = \lfloor N/25\rfloor$.

## 9. Contar éxitos

El voraz acierta cuando:
- $a = 0$ (es decir $N < 25$), o
- $b \bmod 10 < 5$ (es decir $b$ tiene dígito de unidades $0,1,2,3,4$).

Contemos para $N = 1$ a $1000$.

**Caso $a=0$:** $N=1$ a $24$, son $24$ valores, todos son éxitos.

**Caso $a \ge 1$:** necesitamos $b \bmod 10 < 5$.

Los valores de $b \in \{0,\dots,24\}$ con $b \bmod 10 < 5$ son:

$0,1,2,3,4,10,11,12,13,14,20,21,22,23,24$: son $15$ valores.

Para cada $a$, el rango de $N$ es $25a \le N \le 25a+24$, es decir $b$ varía en $\{0,\dots,24\}$, con $15$ éxitos. Además, $a$ va de $1$ a cuánto.

Para $N\le 1000$:

$1000 / 25 = 40$ exactamente. Así que $a$ va de $1$ a $39$ incluye bloques completos de $25$ valores: $N=25$ hasta $N=999 = 25\cdot 39 + 24$. El último bloque, $a=40$, solo contiene $N=1000$ (pues $25\cdot 40 = 1000$), con $b=0$, que sí es éxito.

Por lo tanto:
- $a=0$: $24$ éxitos.
- $a=1$ a $39$: $39$ bloques, cada uno con $15$ éxitos: $39 \cdot 15 = 585$.
- $a=40$: $b=0$, $1$ éxito.

Total éxitos:

\[
24 + 585 + 1 = 610
\]

## 10. Verificación rápida con el ejemplo

$N=42$: $a=1$, $b=17$, $b\bmod 10 = 7 \ge 5$, así que el voraz falla. Correcto.

$N=25$: $a=1$, $b=0$, $0<5$, éxito. El voraz da $1$ moneda y el óptimo también es $1$. Correcto.

$N=1000$: $a=40$, $b=0$, éxito. El voraz usa $40$ monedas de $25$, claramente óptimo.

Por lo tanto, la respuesta es:

\[
\boxed{610}
\]