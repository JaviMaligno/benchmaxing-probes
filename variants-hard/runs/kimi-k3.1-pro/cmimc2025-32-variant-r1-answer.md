Fijemos \(a\neq 4,6\). Solo necesitamos seguir las posiciones de \(a\) y de \(6\): el procedimiento termina cuando cualquiera de los dos llega a la raíz. Llamemos **centro** de una rama al hijo de la raíz y **hoja** a cualquiera de sus dos hijos.

### 1. Si \(a\) está en la rama izquierda

Los dos números se mueven en ramas independientes. Definamos:

- \(A\): ambos están en el centro de su rama.
- \(B\): \(a\) está en el centro y \(6\) en una hoja.
- \(C\): \(a\) está en una hoja y \(6\) en el centro.
- \(D\): ambos están en hojas.

Usaremos las mismas letras para las probabilidades de que \(a\) llegue a la raíz antes que \(6\). Contando las seis aristas, incluidos los movimientos que no cambian el estado, obtenemos:
\[
\begin{aligned}
6A&=1+2B+2C,\\
4B&=1+A+2D,\\
4C&=A+2D,\\
2D&=B+C.
\end{aligned}
\]
Por ejemplo, desde \(A\), una arista hace ganar a \(a\), otra hace ganar a \(6\), dos mueven a \(a\) a una hoja y dos mueven a \(6\) a una hoja.

Resolviendo:
\[
A=\frac12,\qquad B=\frac58,\qquad C=\frac38,\qquad D=\frac12.
\]
Como \(2\) empieza en el centro, mientras que \(1\) y \(3\) empiezan en hojas,
\[
q(2)=\frac12,\qquad q(1)=q(3)=\frac38.
\]

### 2. Si \(a\) es \(5\) o \(7\)

Ahora \(a\) y \(6\) comparten la rama derecha. Sean:

- \(X\): estado inicial, con \(6\) en el centro y \(a\) en una hoja.
- \(Y\): \(a\) en el centro y \(6\) en una hoja.
- \(Z\): ambos en hojas.

Las ecuaciones son
\[
3X=Y+Z,\qquad 3Y=1+X+Z,\qquad 2Z=X+Y.
\]
Su solución da
\[
X=\frac38,\qquad Y=\frac58,\qquad Z=\frac12.
\]
Por tanto,
\[
q(5)=q(7)=\frac38.
\]

Finalmente,
\[
q(1)+q(2)+q(3)+q(5)+q(7)
=2\cdot\frac38+\frac12+2\cdot\frac38
=\boxed{2}.
\]