

Sea \(\zeta=\omega=e^{2\pi i/13}\). Consideremos los exponentes módulo \(13\).

Para los cuatro exponentes, sean \(n_r\) sus multiplicidades como residuos módulo \(13\), con \(\sum_r n_r=4\). Entonces

\[
\left|\sum_r n_r\zeta^r\right|^2
=\sum_{s,t} n_s n_t \zeta^{s-t}
=\sum_{u=0}^{12} C_u \zeta^u,
\]

donde \(C_u\) es el número de pares ordenados cuya diferencia es \(u\) módulo \(13\). Además,

\[
\sum_{u=0}^{12} C_u = 4^2=16.
\]

Como el módulo al cuadrado es \(3\),

\[
\sum_{u=0}^{12} C_u\zeta^u=3.
\]

La única relación racional entre \(1,\zeta,\dots,\zeta^{12}\) proviene de

\[
1+\zeta+\cdots+\zeta^{12}=0,
\]

así que los coeficientes de \(\sum C_u\zeta^u-3=0\) deben ser todos iguales. Por tanto, para alguna constante \(q\),

\[
C_1=\cdots=C_{12}=q,\qquad C_0-3=q.
\]

Usando \(\sum C_u=16\),

\[
(q+3)+12q=16 \implies 13q=13 \implies q=1.
\]

Luego \(C_0=4\) y cada diferencia no nula módulo \(13\) aparece exactamente una vez. En particular, los cuatro residuos módulo \(13\) son distintos y forman un conjunto de diferencias \((13,4,1)\).

Si \(a\le 11\), entonces \(a,b,c,d\) son impares menores que \(13\), así que sus residuos están en

\[
\{1,3,5,7,9,11\}.
\]

La diferencia entre dos de estos residuos es un número par entre \(-10\) y \(10\), por lo que nunca puede ser congruente con \(1\) módulo \(13\). Pero necesitamos que aparezca la diferencia \(1\). Contradicción. Por tanto,

\[
a\ge 13.
\]

Probemos \(a=13\). Entonces el residuo de \(a\) es \(0\). El conjunto

\[
\{0,1,3,9\}
\]

es un conjunto de diferencias módulo \(13\): sus diferencias ordenadas son exactamente \(1,2,\dots,12\). Así,

\[
\left|\omega^{13}+\omega^9+\omega^3+\omega^1\right|=\sqrt{3}.
\]

Esto corresponde a

\[
(a,b,c,d)=(13,9,3,1).
\]

Falta ver que no hay una opción menor con \(a=13\). Los otros tres exponentes deben ser impares menores que \(13\). La diferencia \(1\) debe aparecer; como entre impares menores que \(13\) no hay diferencias congruentes con \(1\) módulo \(13\), debe estar el exponente \(1\).

Si \(b\le 7\), los tres impares serían uno de

\[
\{1,3,5\},\quad \{1,3,7\},\quad \{1,5,7\}.
\]

Pero:

- \(\{0,1,3,5\}\) repite la diferencia \(2\): \(3-1=2\) y \(5-3=2\).
- \(\{0,1,3,7\}\) repite la diferencia \(6\): \(0-7\equiv 6\) y \(7-1=6\).
- \(\{0,1,5,7\}\) repite la diferencia \(6\): \(0-7\equiv 6\) y \(7-1=6\).

Por tanto \(b\ge 9\). Con \(b=9\), la menor opción posible es \(c=3,d=1\), y ya vimos que funciona.

Así, el mínimo se alcanza en

\[
(a,b,c,d)=(13,9,3,1).
\]

El valor pedido es

\[
1000a+100b+10c+d
=1000(13)+100(9)+10(3)+1
=13931.
\]

\[
\boxed{13931}
\]