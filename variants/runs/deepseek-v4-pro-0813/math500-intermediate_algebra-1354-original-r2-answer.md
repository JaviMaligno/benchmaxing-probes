Necesitamos evaluar  

\[
S = \sum_{k=1}^{1997} \frac{1}{1+\omega^k}
\]

donde \(\omega \neq 1\) es una raíz 1997-ésima de la unidad, es decir, \(\omega^{1997}=1\).

## Paso 1. Relacionar \(\omega^k\) con su conjugado

Como \(\omega^{1997}=1\), el inverso de \(\omega^k\) es \(\omega^{1997-k}\), ya que

\[
\omega^k \cdot \omega^{1997-k} = \omega^{1997} = 1.
\]

Además, \(|\omega|=1\), por lo que el conjugado de \(\omega^k\) es su inverso:

\[
\overline{\omega^k} = \omega^{-k} = \omega^{1997-k}.
\]

## Paso 2. Emparejar términos

Para \(k\) entre \(1\) y \(1996\), agrupamos el término \(k\) con el término \(1997-k\). Notemos que no hay solapamiento porque el conjunto \(\{1,2,\dots,1996\}\) se agrupa en pares y el índice central \(k\) no pertenece al rango.

Veamos la suma de un par:

\[
\frac{1}{1+\omega^k} + \frac{1}{1+\omega^{1997-k}}
\]

Escribimos

\[
\omega^{1997-k} = \omega^{-k},
\]

entonces

\[
\frac{1}{1+\omega^k} + \frac{1}{1+\omega^{-k}}
= \frac{1+\omega^{-k} + 1+\omega^k}{(1+\omega^k)(1+\omega^{-k})}.
\]

Multiplicamos el denominador:

\[
(1+\omega^k)(1+\omega^{-k})
= 1 + \omega^{-k} + \omega^k + \omega^k\omega^{-k}
= 1 + \omega^{-k} + \omega^k + 1
= 2 + \omega^k + \omega^{-k}.
\]

El numerador es

\[
2 + \omega^k + \omega^{-k}.
\]

Por lo tanto, la suma del par es

\[
\frac{2+\omega^k+\omega^{-k}}{2+\omega^k+\omega^{-k}} = 1.
\]

## Paso 3. Contar pares y tratar el término restante

Los índices \(k=1,\dots,1996\) forman \(1996/2 = 998\) pares, cada uno de los cuales suma \(1\). Así suman

\[
998.
\]

Queda el término correspondiente a \(k=1997\):

\[
\omega^{1997} = 1,
\]

entonces

\[
\frac{1}{1+\omega^{1997}} = \frac{1}{1+1} = \frac12.
\]

## Paso 4. Suma total

\[
S = 998 + \frac12 = \frac{1996}{2}+\frac12 = \frac{1997}{2}.
\]

Por lo tanto,

\[
\boxed{\frac{1997}{2}}
\]