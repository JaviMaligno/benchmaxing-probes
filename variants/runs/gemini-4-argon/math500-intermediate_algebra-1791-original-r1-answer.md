Para determinar qué valor de $x$ debe elegir Arquímedes, primero debemos analizar cómo jugará Brahmagupta de manera óptima para un valor fijo de $x$.

1. **Expandir la función $z(x,y)$ en términos de $y$:**
   \[
   z(x,y) = (2x - y)^2 - 2y^2 - 3y
   \]
   \[
   z(x,y) = 4x^2 - 4xy + y^2 - 2y^2 - 3y
   \]
   \[
   z(x,y) = -y^2 - (4x + 3)y + 4x^2
   \]

2. **Maximizar $z$ respecto a $y$ (turno de Brahmagupta):**
   Para un valor dado de $x$, la función $z(x,y)$ es una parábola en términos de $y$ que se abre hacia abajo (ya que el coeficiente de $y^2$ es $-1 < 0$). Brahmagupta maximizará $z$ eligiendo el vértice de esta parábola:
   \[
   y = -\frac{-(4x + 3)}{2(-1)} = -\frac{4x + 3}{2}
   \]

3. **Sustituir el valor óptimo de $y$ en $z$:**
   Completando el cuadrado para $y$, o sustituyendo $y = -\frac{4x + 3}{2}$ en la ecuación, el valor máximo que alcanza $z$ en función de $x$ es:
   \[
   z_{\text{máx}}(x) = -\left(-\frac{4x + 3}{2}\right)^2 - (4x + 3)\left(-\frac{4x + 3}{2}\right) + 4x^2
   \]
   \[
   z_{\text{máx}}(x) = \frac{(4x + 3)^2}{4} + 4x^2
   \]
   \[
   z_{\text{máx}}(x) = \frac{16x^2 + 24x + 9}{4} + 4x^2 = 4x^2 + 6x + \frac{9}{4} + 4x^2
   \]
   \[
   z_{\text{máx}}(x) = 8x^2 + 6x + \frac{9}{4}
   \]

4. **Minimizar $z_{\text{máx}}(x)$ respecto a $x$ (turno de Arquímedes):**
   Arquímedes desea minimizar esta expresión cuadrática en $x$, la cual tiene un coeficiente principal positivo ($8 > 0$). El mínimo se alcanza en el vértice de la parábola:
   \[
   x = -\frac{6}{2(8)} = -\frac{6}{16} = -\frac{3}{8}
   \]

\boxed{-\frac{3}{8}}