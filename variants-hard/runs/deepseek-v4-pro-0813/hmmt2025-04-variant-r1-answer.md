Vamos a razonar paso a paso.

Queremos calcular

\[
S=\sum_{k=-1200}^{1200}\left\lfloor\frac{3150}{k+0{,}5}\right\rfloor
\]

donde \(k\) recorre los enteros desde \(-1200\) hasta \(1200\).

## 1. Qué ocurre en los extremos y el salto

Para \(k=1200\),

\[
\frac{3150}{1200{,}5}<3,\quad
\left\lfloor\frac{3150}{1200{,}5}\right\rfloor=2.
\]

De hecho \(3150/1200{,}5 \approx 2{,}624\).

Para \(k=-1200\),

\[
\frac{3150}{-1200{,}5}\approx -2{,}624,
\]

y como es un número negativo no entero,

\[
\left\lfloor -2{,}624\right\rfloor=-3.
\]

Los valores intermedios van pasando por todos los enteros.

## 2. Separar denominadores positivos y negativos

Los términos con denominador positivo son \(k+0{,}5>0\), es decir \(k\ge 0\), o sea \(k=0,1,\dots,1200\). Hay \(1201\) términos.

Los términos con denominador negativo son \(k+0{,}5<0\), es decir \(k\le -1\), o sea \(k=-1,-2,\dots,-1200\). Hay \(1200\) términos.

## 3. Términos con denominador negativo

Para \(k=-m\), con \(m=1,\dots,1200\), tenemos

\[
\frac{3150}{-m+0{,}5}
=
\frac{-3150}{m-0{,}5}
=
-\frac{3150}{m-0{,}5}.
\]

Como \(3150/(m-0{,}5)\) no es entero, se cumple

\[
\left\lfloor -\frac{3150}{m-0{,}5}\right\rfloor
=
-\left\lceil \frac{3150}{m-0{,}5}\right\rceil.
\]

Además, como la cantidad no es entera,

\[
\left\lceil \frac{3150}{m-0{,}5}\right\rceil
=
\left\lfloor \frac{3150}{m-0{,}5}\right\rfloor+1.
\]

Por lo tanto

\[
\left\lfloor \frac{3150}{-m+0{,}5}\right\rfloor
=
-\left(\left\lfloor \frac{3150}{m-0{,}5}\right\rfloor+1\right).
\]

Así, la parte negativa de la suma es

\[
\sum_{m=1}^{1200}\left\lfloor\frac{3150}{-m+0{,}5}\right\rfloor
=
-\sum_{m=1}^{1200}\left\lfloor\frac{3150}{m-0{,}5}\right\rfloor
-1200.
\]

## 4. Agrupar con la parte positiva

La suma total es

\[
S
=
\sum_{k=0}^{1200}\left\lfloor\frac{3150}{k+0{,}5}\right\rfloor
+
\sum_{m=1}^{1200}\left\lfloor\frac{3150}{-m+0{,}5}\right\rfloor.
\]

Sustituyendo:

\[
S
=
\sum_{k=0}^{1200}\left\lfloor\frac{3150}{k+0{,}5}\right\rfloor
-
\sum_{m=1}^{1200}\left\lfloor\frac{3150}{m-0{,}5}\right\rfloor
-1200.
\]

Ahora hacemos un cambio de índice en la segunda suma: \(n=m-1\), de modo que \(n=0,\dots,1199\) y \(m-0{,}5=n+0{,}5\). Además \(n+1=m\), así que

\[
\left\lfloor\frac{3150}{m-0{,}5}\right\rfloor
=
\left\lfloor\frac{3150}{n+0{,}5}\right\rfloor.
\]

Por lo tanto

\[
S
=
\sum_{k=0}^{1200}\left\lfloor\frac{3150}{k+0{,}5}\right\rfloor
-
\sum_{n=0}^{1199}\left\lfloor\frac{3150}{n+0{,}5}\right\rfloor
-1200.
\]

Las dos sumas se cancelan casi completamente, quedando solo el término \(k=1200\) de la primera:

\[
S
=
\left\lfloor\frac{3150}{1200{,}5}\right\rfloor
-1200.
\]

## 5. Cálculo final

\[
3150=2\cdot 1200{,}5+3150-2401=749.
\]

Más exactamente,

\[
\frac{6300}{2401}\quad\text{con }2401=2\cdot 1200{,}5.
\]

Tenemos

\[
3150 = 2\cdot 1200{,}5 + 749,
\]

luego

\[
\frac{3150}{1200{,}5}
=
2+\frac{749}{1200{,}5}
=
2+\frac{749}{1200{,}5}.
\]

Como \(0<\frac{749}{1200{,}5}<1\),

\[
\left\lfloor\frac{3150}{1200{,}5}\right\rfloor=2.
\]

Por tanto

\[
S=2-1200=-1198.
\]

\[
\boxed{-1198}
\]