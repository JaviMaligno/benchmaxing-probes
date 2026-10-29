Queremos la norma de operador de $A = \begin{pmatrix} 3 & 8 \\ 0 & -3 \end{pmatrix}$, que es la raíz cuadrada del mayor autovalor de $A^\top A$.

**Paso 1: calcular $A^\top A$.**

$$A^\top A = \begin{pmatrix} 3 & 0 \\ 8 & -3 \end{pmatrix}\begin{pmatrix} 3 & 8 \\ 0 & -3 \end{pmatrix} = \begin{pmatrix} 9 & 24 \\ 24 & 73 \end{pmatrix}.$$

**Paso 2: hallar los autovalores.** El polinomio característico es

$$\lambda^2 - (9+73)\lambda + (9\cdot 73 - 24^2) = \lambda^2 - 82\lambda + (657 - 576) = \lambda^2 - 82\lambda + 81.$$

Entonces

$$\lambda = \frac{82 \pm \sqrt{82^2 - 4\cdot 81}}{2} = \frac{82 \pm \sqrt{6724 - 324}}{2} = \frac{82 \pm 80}{2},$$

es decir, $\lambda = 81$ o $\lambda = 1$.

**Paso 3: concluir.** El mayor autovalor de $A^\top A$ es $81$, así que la menor constante válida es $C = \sqrt{81} = 9$. En efecto, $\|A\mathbf{w}\|^2 = \mathbf{w}^\top A^\top A\, \mathbf{w} \le 81\|\mathbf{w}\|^2$ para todo $\mathbf{w}$, con igualdad para el autovector correspondiente a $\lambda = 81$, por lo que ninguna constante menor funciona.

$$\boxed{9}$$