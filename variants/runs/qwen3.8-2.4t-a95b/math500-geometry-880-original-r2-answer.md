

Tomemos las dos paredes laterales de \(10\times 8\) como paredes opuestas, separadas por \(12\) pies. Las paredes trasera y delantera son de \(12\times 8\), y el techo es de \(12\times 10\). El suelo no está permitido.

Usemos coordenadas en el techo desplegado: \(x\) de \(0\) a \(12\) entre las paredes laterales, \(y\) de \(0\) a \(10\) desde la pared trasera hasta la delantera.

- El gecko está en la pared lateral inicial, a \(1\) pie del techo y \(1\) pie de la pared trasera. Al desplegar esa pared a la izquierda del techo, queda en  
  \[
  (-1,1).
  \]

- La mosca está en la pared lateral opuesta, a \(1\) pie del suelo y \(1\) pie de la pared delantera. Consideremos el recorrido que pasa por el techo, luego la pared delantera, luego la pared opuesta. La pared delantera se despliega arriba del techo; como la mosca está a \(1\) pie del suelo, está a \(7\) pies del techo, así que su coordenada vertical desplegada es \(10+7=17\). Además, está a \(1\) pie de la pared delantera, así que al desplegar la pared opuesta queda en
  \[
  (12+1,17)=(13,17).
  \]

La distancia recta en este despliegue es
\[
\sqrt{(13-(-1))^2+(17-1)^2}
=\sqrt{14^2+16^2}
=\sqrt{196+256}
=\sqrt{452}
=2\sqrt{113}.
\]

La recta cruza las aristas dentro de las caras: cruza \(x=0\) en \(y=15/7\), \(y=10\) en \(x=55/8\), y \(x=12\) en \(y=111/7\), todo dentro de los límites, así que el camino es válido.

Las otras secuencias simples posibles de caras dan distancias mayores:

\[
\begin{array}{c|c}
\text{Recorrido} & \text{Longitud} \\
\hline
\text{techo solamente} & 4\sqrt{29} \\
\text{pared trasera o delantera solamente} & 2\sqrt{130} \\
\text{techo + trasera} & 2\sqrt{137} \\
\text{trasera + techo} & 10\sqrt5 \\
\text{delantera + techo} & 2\sqrt{197}
\end{array}
\]

Por tanto, la longitud mínima es

\[
\boxed{2\sqrt{113}}
\]