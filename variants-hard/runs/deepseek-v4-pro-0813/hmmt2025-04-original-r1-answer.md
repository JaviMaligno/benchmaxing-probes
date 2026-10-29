Voy a razonar paso a paso.

Sea $N=\sum_{j=-1000}^{1000}\left\lfloor\frac{2025}{j+0.5}\right\rfloor$.

Defino $x=j+0.5$. Entonces $j$ recorre los enteros de $-1000$ a $1000$, así que $x$ toma los valores:

$$
x=-999.5,\;-998.5,\;\ldots,\;1000.5,
$$

es decir, todos los semienteros desde $-999.5$ hasta $1000.5$, con paso $1$.

Por lo tanto,

$$
N=\sum_{j=-1000}^{1000}\left\lfloor\frac{2025}{j+0.5}\right\rfloor
=\sum_{x=-999.5}^{1000.5}\left\lfloor\frac{2025}{x}\right\rfloor,
$$

donde $x$ recorre los $2001$ valores semienteros consecutivos.

Observamos que $\left\lfloor\frac{2025}{x}\right\rfloor$ es una función impar en $x$ en el sentido:

$$
\left\lfloor\frac{2025}{-x}\right\rfloor
=\left\lfloor-\frac{2025}{x}\right\rfloor
=-\left\lceil\frac{2025}{x}\right\rceil.
$$

La expresión no es exactamente $-\lfloor 2025/x\rfloor$ salvo que $2025/x$ sea entero. Por eso conviene separar en pares $x$ y $-x$ junto con el término central $x=0.5$.

Los valores simétricos de los semienteros son:

- Positivos: $0.5,1.5,2.5,\ldots,1000.5$.
- Negativos: $-0.5,-1.5,-2.5,\ldots,-999.5$.

Falta un término positivo más ($1000.5$) porque $j$ va de $-1000$ a $1000$, lo que da $x=-999.5$ hasta $1000.5$. Así que hay $1000$ pares simétricos $(\pm 0.5,\pm 1.5,\ldots,\pm 999.5)$ y el término solitario $x=1000.5$.

Analicemos un par $x=a$ y $x=-a$, con $a>0$ semientero.

Queremos:

$$
\left\lfloor\frac{2025}{a}\right\rfloor+\left\lfloor\frac{2025}{-a}\right\rfloor
=\left\lfloor\frac{2025}{a}\right\rfloor+\left\lfloor-\frac{2025}{a}\right\rfloor.
$$

Sea $q=\frac{2025}{a}$. Entonces:

$$
\lfloor q\rfloor+\lfloor -q\rfloor
=
\begin{cases}
0, & q\in\mathbb Z,\\
-1, & q\notin\mathbb Z.
\end{cases}
$$

Así que cada par simétrico contribuye $-1$, salvo si $2025/a$ es entero, en cuyo caso contribuye $0$.

Determinemos cuándo $2025/a$ es entero para $a$ semientero positivo con $a\le 999.5$.

$2025=45^2=3^4\cdot 5^2$. Si $a=n+\frac12$, con $n\in\{0,1,\ldots,999\}$, entonces:

$$
\frac{2025}{a}=\frac{2\cdot 2025}{2n+1}=\frac{4050}{2n+1}.
$$

Como $2n+1$ es impar, $4050/(2n+1)$ es entero exactamente cuando $2n+1$ divide a $4050$.

$$
4050=2\cdot 2025=2\cdot 3^4\cdot 5^2.
$$

Los divisores impares de $4050$ son los divisores de $2025=3^4\cdot 5^2$, que son:

$$
(4+1)(2+1)=15.
$$

Estos divisores impares son:

$$
1,3,5,9,15,25,27,45,75,81,125,135,225,375,405,675,2025.
$$

Pero $2n+1$ debe ser un entero impar entre $1$ y $1999$ (porque $n\le 999$). Todos los divisores impares de $4050$ cumplen esto, salvo $2025$, que excede $1999$. Así que los valores posibles de $2n+1$ son los otros $14$ divisores impares.

Por tanto, hay $14$ valores de $a$ semientero positivo con $a\le 999.5$ para los cuales $2025/a$ es entero. Para esos $14$ pares simétricos, la contribución es $0$; para los restantes $1000-14=986$ pares, la contribución es $-1$.

Además, el término solitario es $x=1000.5$:

$$
\left\lfloor\frac{2025}{1000.5}\right\rfloor
=\left\lfloor\frac{4050}{2001}\right\rfloor
=\lfloor 2.023\ldots\rfloor
=2.
$$

Sumando todo:

$$
N=986\cdot(-1)+14\cdot 0+2=-986+2=-984.
$$

Por lo tanto, la respuesta es:

$$
\boxed{-984}
$$