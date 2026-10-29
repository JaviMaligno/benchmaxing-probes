Como los frascos son indistinguibles y el orden de colocación no importa, contamos particiones de \(\{1,\dots,20\}\) en cinco bloques de tamaño \(4\).

Consideremos un frasco con cuatro etiquetas. Al ordenarlas, sus etiquetas forman tramos de números consecutivos. La condición dice que ninguna etiqueta puede estar sola en su tramo, porque entonces no tendría ninguna adyacente en el frasco. Por eso cada tramo tiene longitud al menos \(2\). Como el frasco tiene \(4\) etiquetas, sus tramos solo pueden ser:

\[
4 \quad \text{o} \quad 2+2.
\]

En ambos casos, el contenido del frasco se divide de manera única en dos pares de etiquetas consecutivas. Por ejemplo, cuatro consecutivas \(a,a+1,a+2,a+3\) se dividen en \((a,a+1)\) y \((a+2,a+3)\).

Así, en toda configuración válida, las \(20\) canicas quedan divididas en \(10\) pares consecutivos, con dos pares por frasco. Estos \(10\) pares forman un emparejamiento perfecto del camino

\[
1-2-3-\cdots-20.
\]

Pero ese camino tiene un único emparejamiento perfecto: el \(1\) solo puede emparejarse con el \(2\); después el \(3\) debe emparejarse con el \(4\); luego el \(5\) con el \(6\), y así sucesivamente. Por lo tanto los pares obligatorios son

\[
(1,2),(3,4),(5,6),\dots,(19,20).
\]

Recíprocamente, cualquier forma de agrupar estos \(10\) pares en cinco frascos, con dos pares por frasco, es válida, porque cada canica está con su compañero de par.

Entonces hay que contar las maneras de emparejar \(10\) objetos distintos:

\[
9\cdot 7\cdot 5\cdot 3\cdot 1=945.
\]

\[
\boxed{945}
\]