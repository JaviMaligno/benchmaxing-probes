Voy a resolverlo paso a paso.

Tenemos que analizar

$$
(1+x+x^2)^{2019} = \sum_{k=0}^{4038} \binom{2019}{k}_3 x^k
$$

y queremos contar cuántos $k$ cumplen

$$
\binom{2019}{k}_3 \equiv 1 \pmod 3.
$$

Trabajo en el anillo $\mathbb{F}_3[x]$. Módulo $3$ tenemos

$$
1+x+x^2 \equiv (x-1)^2 \pmod 3,
$$

porque $x^2+x+1$ módulo $3$ y $x^2-2x+1 \equiv x^2+x+1$. Es decir,

$$
x^2+x+1 \equiv (x-1)^2 \pmod 3.
$$

Por lo tanto,

$$
(1+x+x^2)^{2019} \equiv (x-1)^{4038} \pmod 3.
$$

Recordemos que en característica $3$, todo polinomio binomial tiene la propiedad:

$$
(a+b)^3 \equiv a^3+b^3 \pmod 3.
$$

Escribimos $4038 = 3 \cdot 1346$. Aplicando repetidamente el teorema del binomio en característica $3$ (la expansión de Frobenius / teorema de Lucas):

Para un exponente $N$ cuya representación en base $3$ es

$$
N = n_0 + n_1 \cdot 3 + n_2 \cdot 3^2 + \cdots,
$$

se cumple que

$$
(A+B)^N = \prod_{i} (A^{3^i}+B^{3^i})^{n_i} \pmod 3.
$$

En nuestro caso:

$$
(x-1)^{4038} = (x-1)^{2 \cdot 2019} .
$$

Hallemos la representación en base $3$ de $4038$.

Calculamos:

- $4038 = 3 \cdot 1346$,
- $1346 = 3 \cdot 448 + 2$,
- $448 = 3 \cdot 149 + 1$,
- $149 = 3 \cdot 49 + 2$,
- $49 = 3 \cdot 16 + 1$,
- $16 = 3 \cdot 5 + 1$,
- $5 = 3 \cdot 1 + 2$,
- $1 = 0 \cdot 3 + 1$.

Leyendo los residuos de abajo hacia arriba:

$$
4038 = (12112110)_3.
$$

Es decir,

$$
4038 = 0 \cdot 3^0 + 1 \cdot 3^1 + 1 \cdot 3^2 + 2 \cdot 3^3 + 1 \cdot 3^4 + 2 \cdot 3^5 + 1 \cdot 3^6 + 1 \cdot 3^7.
$$

Comprobemos:

- $3+9=12$,
- $12 + 2\cdot 27 = 66$,
- $66 + 81 = 147$,
- $147 + 2\cdot 243 = 633$,
- $633 + 729 = 1362$,
- $1362 + 2187 = 3549$.

Falta algo: $4038 - 3549 = 489$. Reviso: parece que olvidé una cifra. Hagamos la división con más cuidado.

$4038 / 3$:

- $4038 = 3 \cdot 1346$, resto $0$.
- $1346 = 3 \cdot 448 + 2$, resto $2$.
- $448 = 3 \cdot 149 + 1$, resto $1$.
- $149 = 3 \cdot 49 + 2$, resto $2$.
- $49 = 3 \cdot 16 + 1$, resto $1$.
- $16 = 3 \cdot 5 + 1$, resto $1$.
- $5 = 3 \cdot 1 + 2$, resto $2$.
- $1 = 3 \cdot 0 + 1$, resto $1$.

Entonces, leyendo los restos en orden inverso:

$$
4038 = 1\cdot 3^8 + 2 \cdot 3^7 \cdots
$$

Espera, detengámonos en cuántas cifras hay. Los restos obtenidos en orden creciente de potencia son:

$r_0=0,\ r_1=2,\ r_2=1,\ r_3=2,\ r_4=1,\ r_5=1,\ r_6=2,\ r_7=1$.

Entonces

$$
4038 = 0 + 2\cdot 3 + 1\cdot 9 + 2\cdot 27 + 1\cdot 81 + 1\cdot 243 + 2\cdot 729 + 1\cdot 2187.
$$

Sumamos:

- $6+9=15$,
- $15+54=69$,
- $69+81=150$,
- $150+243=393$,
- $393+1458=1851$,
- $1851+2187=4038$. Correcto.

Entonces la representación en base $3$ es

$$
4038 = (12112110)_3.
$$

Los dígitos, de mayor a menor potencia, son

$$
1,2,1,1,2,1,1,0.
$$

Aplicamos el teorema de Lucas en característica $3$ para el coeficiente de $x^k$ en $(x-1)^{4038}$.

Recordemos que

$$
(x-1)^N = \sum_k \binom{N}{k} x^k (-1)^{N-k}.
$$

En $\mathbb{F}_3$, el coeficiente de $x^k$ es $\binom{N}{k}(-1)^{N-k} \bmod 3$.

Por el teorema de Lucas:

$$
\binom{N}{k} \equiv \prod_i \binom{n_i}{k_i} \pmod 3,
$$

donde $n_i$ y $k_i$ son los dígitos en base $3$ de $N$ y $k$, respectivamente.

Definamos la función de Lucas que da el coeficiente igual a $0$ o distinto de $0$ (unitario). Queremos que el coeficiente de $x^k$ en $(x-1)^N$ sea congruente a $1$ módulo $3$.

Aquí $N=4038$ y $N \equiv 0 \pmod 3$, entonces $(-1)^{N-k}=(-1)^k$ con signo discutible; en $\mathbb{F}_3$, $-1 \equiv 2$.

Así, el coeficiente de $x^k$ módulo $3$ es

$$
\binom{4038}{k}(-1)^{4038-k}.
$$

Como $4038$ es par, $(-1)^{4038-k}=(-1)^k$. Entonces es

$$
\binom{4038}{k}(-1)^k .
$$

Ahora bien: por el teorema de Lucas, $\binom{4038}{k} \not\equiv 0 \pmod 3$ si y solo si cada dígito $k_i \le n_i$. Si se cumple esto, además

$$
\binom{4038}{k} \equiv \prod_i \binom{n_i}{k_i} \pmod 3.
$$

Los dígitos $n_i$ son:

$$
n_0 = 0,\quad n_1=2,\quad n_2=1,\quad n_3=2,\quad n_4=1,\quad n_5=1,\quad n_6=2,\quad n_7=1.
$$

Calculemos el producto de los binomios para cada elección de $k_i \le n_i$:

- Para $n_i=0$: $k_0=0$ únicamente, $\binom{0}{0}=1$.
- Para $n_i=1$: $k_i \in \{0,1\}$ y $\binom{1}{0}=1,\ \binom{1}{1}=1$. Ambos dan $1$.
- Para $n_i=2$: $k_i \in \{0,1,2\}$ y $\binom{2}{0}=1,\ \binom{2}{1}=2,\ \binom{2}{2}=1$.

Entonces cada dígito $1$ contribuye siempre un factor $1$; los dígitos $2$ contribuyen:

- $k_i=0$: factor $1$,
- $k_i=1$: factor $2$,
- $k_i=2$: factor $1$.

Por lo tanto, el producto total es $2^t$, donde $t$ es el número de posiciones con $n_i=2$ y $k_i=1$.

Los dígitos $2$ aparecen en las posiciones $i=1,3,6$. Son tres posiciones.

Así que $\binom{4038}{k} \equiv 2^t \pmod 3$.

Ahora multiplicamos por $(-1)^k$. Queremos que el resultado sea $1$ módulo $3$.

Es decir,

$$
2^t \cdot (-1)^k \equiv 1 \pmod 3.
$$

En $\mathbb{F}_3$, $2 \equiv -1$, de modo que $2^t = (-1)^t$. Por tanto:

$$
(-1)^{t+k} \equiv 1 \pmod 3.
$$

Esto quiere decir que $t+k$ debe ser par.

Recordemos que solo consideramos $k$ cuyos dígitos en base $3$ cumplen $k_i \le n_i$; de lo contrario, el coeficiente es $0$ y no contribuye.

Las posiciones con $n_i=2$ son tres, y en cada una podemos elegir $k_i \in \{0,1,2\}$. De esas elecciones:

- $k_i=0$ o $k_i=2$ aportan $0$ a $t$ y además son pares,
- $k_i=1$ aporta $1$ a $t$ y es impar.

Las posiciones con $n_i=1$ permiten $k_i=0$ o $k_i=1$. No afectan a $t$; solo afectan a la paridad de $k$. Ahí hay cuatro posiciones (los dígitos $1$ de $N$ en posiciones $2,4,5,7$).

La posición con $n_0=0$ solo permite $k_0=0$.

Entonces queremos que $t+k$ sea par, lo cual equivale a que la suma de dígitos de las posiciones donde elegimos $k_i=1$ (combinando todas las posiciones) tenga la misma paridad que $t$. Como $k \equiv \sum_i k_i \pmod 2$ (porque $3 \equiv 1 \pmod 2$), tenemos:

$$
k \equiv \sum_i k_i \pmod 2.
$$

Y $t$ es el número de posiciones de tipo $2$ con $k_i=1$. Así que $t+k \equiv 0 \pmod 2$ significa:

$$
t + \sum_i k_i \equiv 0 \pmod 2.
$$

Ahora notemos que $\sum_i k_i = t + s$, donde $s$ es el número de posiciones de tipo $1$ con $k_i=1$ (porque las posiciones de tipo $2$ pueden contribuir con $k_i=1$, y las demás con $k_i=1$). Además, las posiciones de tipo $2$ con $k_i=2$ contribuyen con $2$ a $k$, pero $2 \equiv 0 \pmod 2$. Por lo tanto la paridad de $k$ está determinada por $t+s$.

Entonces $t+k \equiv t + t + s = 2t + s \equiv s \pmod 2$. Por lo tanto, la condición es simplemente $s$ par.

Es decir: la cantidad de posiciones de tipo $1$ (dígitos $n_i=1$ de $N$) donde elegimos $k_i=1$ tiene que ser par.

Hay $4$ posiciones con $n_i=1$. Las elecciones de $k_i\in\{0,1\}$ en ellas dan un número de unos $s$ par. El número de subconjuntos de tamaño par de un conjunto de $4$ elementos es $2^{4-1}=8$.

En las posiciones con $n_i=2$ hay $3$ posiciones; cada una tiene $3$ opciones, luego $3^3=27$ combinaciones.

En la posición con $n_i=0$, hay una sola opción.

Por lo tanto, el número total de $k$ que cumplen la condición es

$$
27 \cdot 8 = 216.
$$

Veamos si hay que tener cuidado: ¿la paridad de $k$ como entero coincide con la paridad de la suma de dígitos en base $3$? Sí, porque $3^j$ es impar, de modo que

$$
k \equiv \sum_i k_i 3^i \equiv \sum_i k_i \pmod 2.
$$

Todo cuadra.

Por lo tanto, la respuesta es $216$.

Comprobemos con un argumento alternativo: en $\mathbb{F}_3[x]$,

$$
(x-1)^{4038} = (x^3-1)^{1346}
$$

porque $4038 = 3\cdot 1346$ y en característica $3$, $(x-1)^3=x^3-1$. Entonces

$$
(x^3-1)^{1346} = (x^3-1) \cdot (x^3-1)^{1345}.
$$

Mejor aún:

$$
(x^3-1)^{1346} = \sum_{r=0}^{1346} \binom{1346}{r} x^{3r} (-1)^{1346-r}.
$$

Solo aparecen potencias $x^k$ con $k$ múltiplo de $3$. ¡Un momento! Eso contradice mi análisis anterior, porque si solo hay potencias múltiplos de $3$, el número de soluciones debería ser un subconjunto más pequeño. Déjame revisar.

En característica $3$:

$$
(x-1)^{4038} = ((x-1)^3)^{1346} = (x^3-1)^{1346}.
$$

Es cierto. Entonces la expansión solo contiene términos con $x^{3r}$. Por lo tanto, el coeficiente de $x^k$ es $0$ módulo $3$ salvo cuando $k$ es múltiplo de $3$.

Eso es consistente con el teorema de Lucas: el dígito $n_0=0$ exige $k_0=0$; o sea, $k$ debe ser múltiplo de $3$.

Entonces, como $k_0=0$, el rango de $k$ con $0\le k\le 4038$ y $k_0=0$ son $k=0,3,6,\dots,4038$: hay $1347$ valores posibles.

Ahora, para estos $k$, el coeficiente está dado por

$$
(x^3-1)^{1346} = \sum_{r=0}^{1346} \binom{1346}{r} x^{3r}(-1)^{1346-r}.
$$

Como $1346$ es par, $(-1)^{1346-r}=(-1)^r$. Por tanto el coeficiente de $x^{3r}$ es $\binom{1346}{r}(-1)^r \pmod 3$.

Queremos que sea $1$ módulo $3$.

Entonces necesitamos $\binom{1346}{r}(-1)^r \equiv 1$.

Hallemos la base $3$ de $1346$:

- $1346 = 3\cdot 448 + 2$, resto $2$,
- $448 = 3\cdot 149 + 1$, resto $1$,
- $149 = 3\cdot 49 + 2$, resto $2$,
- $49 = 3\cdot 16 + 1$, resto $1$,
- $16 = 3\cdot 5 + 1$, resto $1$,
- $5 = 3\cdot 1 + 2$, resto $2$,
- $1 = 3\cdot 0 + 1$, resto $1$.

Entonces

$$
1346 = (1211210)_3
$$

(o sea, los dígitos de $4038$ sin el último $0$: $n_7,\dots,n_1 = 1,2,1,1,2,1$).

Aplicamos el mismo razonamiento: los dígitos de $1346$ en base $3$ son

- posición $0$: $0$,
- posición $1$: $2$,
- posición $2$: $1$,
- posición $3$: $2$,
- posición $4$: $1$,
- posición $5$: $1$,
- posición $6$: $2$,
- (posición $7$: $1$ en $1346$ no; reviso).

Reviso la cantidad de cifras: hice divisiones hasta que el cociente fue $0$, obteniendo 8 restos en total para $4038$. Para $1346$:

- $1346 \div 3 = 448$, resto $2$ (cifra de $3^0$),
- $448 \div 3 = 149$, resto $1$ (cifra de $3^1$),
- $149 \div 3 = 49$, resto $2$ (cifra de $3^2$),
- $49 \div 3 = 16$, resto $1$ (cifra de $3^3$),
- $16 \div 3 = 5$, resto $1$ (cifra de $3^4$),
- $5 \div 3 = 1$, resto $2$ (cifra de $3^5$),
- $1 \div 3 = 0$, resto $1$ (cifra de $3^6$).

Así que $1346$ tiene $7$ cifras:

$$
1346 = 1\cdot 729 + 2\cdot 243 + 1\cdot 81 + 1\cdot 27 + 2\cdot 9 + 1\cdot 3 + 0 \cdot 1.
$$

Sumemos: $729+486=1215$, $+81=1296$, $+27=1323$, $+18=1341$, $+3=1344$, $+0=1344$. Faltan $2$. Hmm, no da.

Reviso $1346$ módulo $9$: $1346 = 9 \cdot 149 + 5$, resto $5$. Con mi expansión: $1+2\cdot 3 + 1\cdot 9 \equiv 1+6+0=7 \pmod 9$. No coincide. Algo está mal.

Recalculemos las divisiones de $1346$:

$1346 = 3 \cdot 448 + 2$, así que $r_0=2$, cociente $448$.

$448 = 3 \cdot 149 + 1$, $r_1=1$, cociente $149$.

$149 = 3 \cdot 49 + 2$, $r_2=2$, cociente $49$.

$49 = 3 \cdot 16 + 1$, $r_3=1$, cociente $16$.

$16 = 3 \cdot 5 + 1$, $r_4=1$, cociente $5$.

$5 = 3 \cdot 1 + 2$, $r_5=2$, cociente $1$.

$1 = 3 \cdot 0 + 1$, $r_6=1$, cociente $0$.

Entonces los restos en orden creciente son $2,1,2,1,1,2,1$.

Por lo tanto

$$
1346 = 2 + 1\cdot 3 + 2\cdot 9 + 1\cdot 27 + 1\cdot 81 + 2\cdot 243 + 1\cdot 729.
$$

Sumo: $2+3=5$, $+18=23$, $+27=50$, $+81=131$, $+486=617$, $+729=1346$. Correcto.

Entonces los dígitos en orden de mayor a menor son:

Posiciones: $n_6=1, n_5=2, n_4=1, n_3=1, n_2=2, n_1=1, n_0=2$.

Es decir, hay cuatro dígitos $1$ y tres dígitos $2$, y un dígito $0$ ... no, en $1346$ no hay dígito $0$ porque el de posición $0$ es $2$. 

Ahora, para el coeficiente $\binom{1346}{r}$, por el teorema de Lucas:

$$
\binom{1346}{r} \equiv \prod \binom{n_i}{r_i}.
$$

Necesitamos $\binom{1346}{r}(-1)^r \equiv 1$.

Primero, $\binom{1346}{r}$ es distinto de $0$ módulo $3$ si y solo si $r_i \le n_i$ para todo $i$.

Los dígitos $n_i$ de $1346$ son:

- $n_0=2$, $n_1=1$, $n_2=2$, $n_3=1$, $n_4=1$, $n_5=2$, $n_6=1$.

Hay tres dígitos $2$ y cuatro dígitos $1$.

Para cada dígito $1$: $r_i \in \{0,1\}$, factor $1$ en ambos casos.

Para cada dígito $2$: $r_i \in \{0,1,2\}$, factor $1,2,1$ respectivamente.

Entonces $\binom{1346}{r} \equiv 2^u$, donde $u$ es el número de posiciones con $n_i=2$ y $r_i=1$.

Queremos

$$
2^u \cdot (-1)^r \equiv 1 \pmod 3.
$$

Como $2 \equiv -1$, $2^u \equiv (-1)^u$. Así que la condición es

$$
(-1)^{u+r} \equiv 1,
$$

es decir, $u+r$ par.

Pero $r \equiv \sum_i r_i \pmod 2$. Además $r_i=1$ en las posiciones de tipo $2$ contribuyen a $u$ y a la suma; los $r_i=2$ contribuyen $0$ a la paridad de la suma (porque $2\equiv 0 \bmod 2$). Las posiciones de tipo $1$ con $r_i=1$ contribuyen a la suma y sea $v$ su número.

Entonces $r \equiv u+v \pmod 2$. Luego

$$
u+r \equiv u+u+v \equiv v \pmod 2.
$$

Así que la condición es que $v$ sea par, donde $v$ es el número de posiciones de tipo $1$ (dígitos $n_i=1$) con $r_i=1$.

Hay $4$ posiciones de tipo $1$. El número de elecciones con $v$ par es $2^{4-1}=8$.

Hay $3$ posiciones de tipo $2$, cada una con $3$ opciones: $3^3=27$.

Entonces el número de $r$ con $0\le r \le 1346$ y $\binom{1346}{r}(-1)^r \equiv 1$ es

$$
27 \cdot 8 = 216.
$$

Esto confirma el resultado anterior, pero ahora es claro que $k=3r$ recorre exactamente los valores con $k_0=0$, y hay $216$ valores de $r$ válidos. Como la correspondencia $k=3r$ es inyectiva, hay exactamente $216$ valores de $k$.

Espera, hay una sutileza: $r$ puede ser $0,1,\dots,1346$, y $k=3r$ recorre $0,3,\dots,4038$. Precisamente los múltiplos de $3$ en el rango pedido. Como los coeficientes de $x^k$ para $k$ no múltiplo de $3$ son $0$ módulo $3$, y $0 \not\equiv 1$, esos no sirven. Por lo tanto la respuesta final es $216$.

No obstante, verifica el caso $k=0$ (o sea $r=0$): $\binom{2019}{0}_3 = 1$, y $1 \equiv 1 \pmod 3$. Con nuestro conteo, $r=0$: todos los $r_i=0$, luego $u=0$, $v=0$ par, así que se cuenta. Correcto.

Así que la respuesta es:

\[
\boxed{216}
\]