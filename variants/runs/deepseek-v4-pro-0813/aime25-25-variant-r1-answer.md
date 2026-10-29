Representemos cada configuración como una cadena binaria de longitud 17, con un `1` si el asiento está ocupado y `0` si está vacío. Necesitamos exactamente 9 unos, y la condición “ningún invitado está junto a otros dos” equivale a que no aparezca el bloque `111`.

Sea \(f(n,k)\) el número de cadenas de longitud \(n\) con \(k\) unos y sin `111`. Clasificando según el inicio de la cadena:

\[
f(n,k)=f(n-1,k)+f(n-2,k-1)+f(n-3,k-2).
\]

Con los casos base \(f(n,0)=1\) y \(f(0,0)=1\), se obtiene:

\[
f(17,9)=f(16,9)+f(15,8)+f(14,7).
\]

Calculando:

\[
f(14,7)=1016,\quad f(15,8)=1107,\quad f(16,9)=1016.
\]

Por lo tanto:

\[
f(17,9)=1016+1107+1016=3139.
\]

El resto al dividir por \(1000\) es

\[
\boxed{139}
\]