# Solución

Buscamos el menor $C$ tal que $\|A\mathbf{w}\| \le C\|\mathbf{w}\|$ para todo $\mathbf{w}$, es decir, la norma de operador (norma espectral) de
$$A = \begin{pmatrix} 3 & 8 \\ 0 & -3 \end{pmatrix}.$$

**Paso 1: Reducir a un problema de valores propios.**

La norma espectral de $A$ es $\sqrt{\lambda_{\max}}$, donde $\lambda_{\max}$ es el mayor valor propio de $A^T A$. Calculamos:
$$A^T A = \begin{pmatrix} 3 & 0 \\ 8 & -3 \end{pmatrix}\begin{pmatrix} 3 & 8 \\ 0 & -3 \end{pmatrix} = \begin{pmatrix} 9 & 24 \\ 24 & 73 \end{pmatrix}.$$

**Paso 2: Valores propios de $A^T A$.**

- Traza: $9 + 73 = 82$
- Determinante: $9 \cdot 73 - 24^2 = 657 - 576 = 81$

Los valores propios satisfacen $\lambda^2 - 82\lambda + 81 = 0$, es decir $(\lambda - 1)(\lambda - 81) = 0$. Por tanto:
$$\lambda_{\max} = 81.$$

**Paso 3: Concluir.**

La norma espectral es $\sqrt{81} = 9$, que se alcanza (por ejemplo, con $\mathbf{w}$ el vector singular derecho correspondiente), así que $C$ no puede ser menor. Una verificación directa: para $\mathbf{w} = (4,3)/5$ (unitario),
$$A\mathbf{w} = \frac{1}{5}\begin{pmatrix} 36 \\ -9 \end{pmatrix}, \qquad \|A\mathbf{w}\| = \frac{\sqrt{1296+81}}{5} = \frac{45}{5} = 9.$$

$$\boxed{9}$$