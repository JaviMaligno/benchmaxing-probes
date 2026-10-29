Representemos cada configuración como una cadena de 17 posiciones, con 1 (asiento ocupado) y 0 (asiento vacío), exactamente con nueve unos.

La condición «ningún invitado queda junto a otros dos invitados» significa que no puede haber tres unos consecutivos (no se permite el bloque `111`).

Hay 8 ceros, que crean 9 huecos (antes, entre y después de los ceros). En cada hueco pueden ir 0, 1 o 2 unos, sin superar 2. Por tanto, contamos los repartos de 9 unos en 9 huecos con capacidad máxima 2:

\[
[x^9](1+x+x^2)^9.
\]

Si usamos \(a\) huecos con dos unos, \(b\) con un uno y \(c\) vacíos, entonces
\[
2a+b=9,\qquad a+b+c=9,
\]
de donde \(b=9-2a\) y \(c=a\). El número de configuraciones para cada \(a\) es
\[
\frac{9!}{a!\,(9-2a)!\,a!}.
\]

Sumando para \(a=0,1,2,3,4\):

\[
\frac{9!}{0!9!0!}+\frac{9!}{1!7!1!}+\frac{9!}{2!5!2!}+\frac{9!}{3!3!3!}+\frac{9!}{4!1!4!}
=1+72+756+1680+630=3139.
\]

Así, \(N=3139\), y al dividir entre \(1000\) el residuo es \(139\).

\[
\boxed{139}
\]