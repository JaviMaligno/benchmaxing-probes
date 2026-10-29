Para encontrar el valor óptimo de $x$ que Arquímedes debe elegir, analizamos el juego de atrás hacia adelante (inducción hacia atrás), comenzando con la elección de Brahmagupta.

**Paso 1: Maximizar $z$ con respecto a $y$ (turno de Brahmagupta)**

Primero, expandimos la función $z(x,y)$ y agrupamos los términos según las potencias de $y$, tratando a $x$ como una constante:
\[z(x,y) = (2x - y)^2 - 2y^2 - 3y\]
\[z(x,y) = 4x^2 - 4xy + y^2 - 2y^2 - 3y\]
\[z(x,y) = -y^2 - (4x + 3)y + 4x^2\]

Para un valor fijo de $x$, esta expresión es una parábola en función de $y$ que se abre hacia abajo (ya que el coeficiente de $y^2$ es $-1 < 0$). Brahmagupta busca maximizar $z$, por lo que elegirá el valor de $y$ correspondiente al vértice de esta parábola:
\[y = -\frac{-(4x + 3)}{2(-1)} = -\frac{4x + 3}{2}\]

**Paso 2: Minimizar el resultado con respecto a $x$ (turno de Arquímedes)**

Sustituimos la elección óptima de $y$ de Brahmagupta en la función $z$ para obtener el valor máximo $M(x)$ en función de $x$:
\[M(x) = -\left(-\frac{4x + 3}{2}\right)^2 - (4x + 3)\left(-\frac{4x + 3}{2}\right) + 4x^2\]
\[M(x) = -\frac{(4x + 3)^2}{4} + \frac{(4x + 3)^2}{2} + 4x^2\]
\[M(x) = \frac{(4x + 3)^2}{4} + 4x^2\]

Desarrollamos el numerador:
\[M(x) = \frac{16x^2 + 24x + 9}{4} + 4x^2\]
\[M(x) = 4x^2 + 6x + \frac{9}{4} + 4x^2\]
\[M(x) = 8x^2 + 6x + \frac{9}{4}\]

Esta nueva función $M(x)$ es una parábola en términos de $x$ que se abre hacia arriba (el coeficiente de $x^2$ es $8 > 0$). Como Arquímedes desea minimizar $z$, debe elegir el valor de $x$ en el vértice de $M(x)$:
\[x = -\frac{6}{2(8)} = -\frac{6}{16} = -\frac{3}{8}\]

\boxed{-\frac{3}{8}}