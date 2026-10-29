La constante buscada es la norma operador de la matriz, es decir, su mayor valor singular.

**Paso 1.** Sea $A = \begin{pmatrix} 3 & 8 \\ 0 & -3 \end{pmatrix}$. El menor $C$ que satisface $\|A\mathbf{w}\| \le C\|\mathbf{w}\|$ para todo $\mathbf{w}$ es $\sqrt{\lambda_{\max}(A^TA)}$.

**Paso 2.** Calculamos
$$A^TA = \begin{pmatrix} 3 & 0 \\ 8 & -3 \end{pmatrix}\begin{pmatrix} 3 & 8 \\ 0 & -3 \end{pmatrix} = \begin{pmatrix} 9 & 24 \\ 24 & 73 \end{pmatrix}.$$

**Paso 3.** El polinomio característico es
$$\lambda^2 - 82\lambda + (9\cdot 73 - 24^2) = \lambda^2 - 82\lambda + (657 - 576) = \lambda^2 - 82\lambda + 81.$$

**Paso 4.** Las raíces son
$$\lambda = \frac{82 \pm \sqrt{6724 - 324}}{2} = \frac{82 \pm \sqrt{6400}}{2} = \frac{82 \pm 80}{2},$$
es decir $\lambda = 81$ y $\lambda = 1$.

**Paso 5.** Por lo tanto $C = \sqrt{81} = 9$, y este valor se alcanza con el vector propio correspondiente, así que es el mínimo posible.

$$\boxed{9}$$