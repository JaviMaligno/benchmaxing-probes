Numeremos los vértices \(0,1,\dots,23\). La longitud de una cuerda depende solo del salto mínimo \(t\in\{1,\dots,12\}\) entre sus extremos.

Para \(t<12\), los segmentos de salto \(t\) forman un grafo donde cada vértice se une con los vértices \(t\) posiciones antes y después. Sea  
\[
d=\operatorname{mcd}(24,t).
\]
Este grafo se descompone en \(d\) ciclos disjuntos, cada uno de longitud \(24/d\). En cada ciclo, un emparejamiento alternado queda forzado tras elegir una de las dos aristas que salen de un vértice; así, un ciclo par tiene exactamente \(2\) emparejamientos y un ciclo impar tiene \(0\).

Para \(t=12\), cada vértice solo puede unirse con su opuesto, lo que da exactamente \(1\) manera.

\[
\begin{array}{c|cccccccccccc}
t&1&2&3&4&5&6&7&8&9&10&11&12\\ \hline
\text{maneras}&2&4&8&16&2&64&2&0&8&4&2&1
\end{array}
\]

Entonces
\[
2+4+8+16+2+64+2+0+8+4+2+1=113.
\]

\[
\boxed{113}
\]