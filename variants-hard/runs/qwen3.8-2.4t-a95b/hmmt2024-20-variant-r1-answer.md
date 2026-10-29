

Sea \(M\) un “lantern” tal que \(N=2M\) también es un lantern. Escribimos la multiplicación por 2 dígito a dígito, desde las unidades hacia la izquierda.

Sea \(c_i\) el acarreo después del dígito \(i\)-ésimo, con \(c_0=0\) y \(c_9=0\). Como multiplicamos por 2, cada acarreo es 0 o 1.

Para un dígito \(a\) con acarreo entrante \(c\), el dígito resultante es
\[
b \equiv 2a+c \pmod{10}.
\]

Analicemos los posibles dígitos:

- Si el acarreo entrante es \(0\):
  - \(1,2,3,4\) producen \(2,4,6,8\) y acarreo saliente \(0\).
  - \(6,7,8,9\) producen \(2,4,6,8\) y acarreo saliente \(1\).
  - \(5\) produciría \(0\), no permitido.

- Si el acarreo entrante es \(1\):
  - \(1,2,3,4\) producen \(3,5,7,9\) y acarreo saliente \(0\).
  - \(5,6,7,8,9\) producen \(1,3,5,7,9\) y acarreo saliente \(1\).

Los dígitos de salida deben ser exactamente \(1,2,\dots,9\). El dígito \(1\) solo puede provenir del \(5\) con acarreo entrante \(1\), así que el \(5\) debe tener acarreo entrante \(1\).

Además, para cada pareja
\[
\{1,6\},\{2,7\},\{3,8\},\{4,9\},
\]
los dos elementos producen el mismo dígito par si tienen acarreo entrante \(0\), y el mismo dígito impar si tienen acarreo entrante \(1\). Por tanto, en cada pareja exactamente uno debe tener acarreo entrante \(0\) y el otro acarreo entrante \(1\).

Sea \(a\) el número de parejas donde el dígito menor tiene acarreo entrante \(0\). Entonces las transiciones de acarreo posibles tienen estos conteos:

\[
\begin{aligned}
00 &: a,\\
01 &: 4-a,\\
10 &: 4-a,\\
11 &: a+1.
\end{aligned}
\]

Sea \(r=4-a\) el número de transiciones \(0\to 1\). Como empezamos y terminamos en acarreo \(0\), también hay \(r\) transiciones \(1\to 0\). El caso \(a=4\) daría \(r=0\), pero habría 5 transiciones \(11\), imposible. Así que \(a=0,1,2,3\).

Para un \(r>0\), el camino de acarreos tiene \(r\) bloques de unos y \(r+1\) bloques de ceros. Repartimos las \(a\) transiciones \(00\) entre los \(r+1\) bloques de ceros, y las \(a+1\) transiciones \(11\) entre los \(r\) bloques de unos. El número de caminos de acarreo es

\[
P(a)=\binom{a+r}{r}\binom{a+r}{r-1},
\qquad r=4-a.
\]

Esto da:

\[
\begin{array}{c|c|c}
a & r & P(a)\\
\hline
0 & 4 & 4\\
1 & 3 & 24\\
2 & 2 & 24\\
3 & 1 & 4
\end{array}
\]

Para un camino de acarreos fijo con valor \(a\):

- Elegimos cuáles \(a\) parejas tienen el dígito menor con acarreo entrante \(0\): \(\binom{4}{a}\) formas.
- Asignamos los dígitos a las posiciones de cada tipo de transición:
\[
a!(4-a)!(4-a)!(a+1)!
\]
formas.

Por tanto, el total para cada \(a\) es

\[
P(a)\binom{4}{a}a!(4-a)!(4-a)!(a+1)!.
\]

Calculamos:

\[
\begin{array}{c|c|c|c}
a & P(a) & \text{asignaciones de dígitos} & \text{total}\\
\hline
0 & 4 & 576 & 2304\\
1 & 24 & 288 & 6912\\
2 & 24 & 288 & 6912\\
3 & 4 & 576 & 2304
\end{array}
\]

Sumando:

\[
2304+6912+6912+2304=18432.
\]

Cada construcción produce un único \(M\), y la aplicación \(M\mapsto 2M\) es biyectiva entre los lanterns que sirven como mitad y los lanterns que son exactamente el doble de otro lantern. Por lo tanto, el número pedido es

\[
\boxed{18432}
\]