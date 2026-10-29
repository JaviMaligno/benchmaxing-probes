Para calcular el valor de la serie
$$
S = \sum_{n=1}^{\infty} \frac{\operatorname{sgn}\left(\sin \left(2^{n}\right)\right)}{2^{n}},
$$
analicemos el signo de $\sin(2^n)$ relacionándolo con la representación binaria de $\frac{1}{2\pi}$.

**Paso 1: Relación entre $\operatorname{sgn}(\sin(x))$ y la parte fraccionaria de $\frac{x}{2\pi}$**

Para cualquier número real $x$ que no sea múltiplo entero de $\pi$, el valor de $\sin(x)$ es positivo si $x \bmod 2\pi \in (0, \pi)$ y negativo si $x \bmod 2\pi \in (\pi, 2\pi)$. 

Definamos la parte fraccionaria de un número real $y$ como $\{y\} = y - \lfloor y \rfloor \in [0, 1)$. Entonces:
- $\sin(x) > 0 \iff \left\{\frac{x}{2\pi}\right\} \in \left(0, \frac{1}{2}\right)$,
- $\sin(x) < 0 \iff \left\{\frac{x}{2\pi}\right\} \in \left(\frac{1}{2}, 1\right)$.

Como $\pi$ es irracional, $2^n$ nunca es un múltiplo de $\pi$, por lo que $\sin(2^n) \neq 0$ para todo $n \geq 1$.

**Paso 2: Expansión binaria de $u = \frac{1}{2\pi}$**

Sea $u = \frac{1}{2\pi}$. Como $2\pi \approx 6.2832$, tenemos que $0 < u < \frac{1}{2}$. Escribamos la expansión en base $2$ de $u$:
$$
u = \sum_{k=1}^{\infty} \frac{b_k}{2^k}, \quad \text{donde } b_k \in \{0, 1\}.
$$
Dado que $u < \frac{1}{2}$, el primer dígito binario es $b_1 = 0$.

Al multiplicar $u$ por $2^n$, desplazamos el punto binario $n$ posiciones hacia la derecha, por lo que la parte fraccionaria de $2^n u$ viene dada por:
$$
\left\{2^n u\right\} = \left\{\frac{2^n}{2\pi}\right\} = \sum_{k=1}^{\infty} \frac{b_{n+k}}{2^k} = \frac{b_{n+1}}{2} + \frac{b_{n+2}}{4} + \cdots
$$
De aquí observamos que:
- Si $b_{n+1} = 0$, entonces $\left\{\frac{2^n}{2\pi}\right\} \in \left(0, \frac{1}{2}\right)$ y por tanto $\operatorname{sgn}(\sin(2^n)) = 1$.
- Si $b_{n+1} = 1$, entonces $\left\{\frac{2^n}{2\pi}\right\} \in \left(\frac{1}{2}, 1\right)$ y por tanto $\operatorname{sgn}(\sin(2^n)) = -1$.

Podemos expresar esto mediante la fórmula cerrada:
$$
\operatorname{sgn}(\sin(2^n)) = 1 - 2b_{n+1}.
$$

**Paso 3: Evaluación de la serie**

Sustituyendo esta expresión en la suma original, obtenemos:
$$
S = \sum_{n=1}^{\infty} \frac{1 - 2b_{n+1}}{2^n} = \sum_{n=1}^{\infty} \frac{1}{2^n} - 2 \sum_{n=1}^{\infty} \frac{b_{n+1}}{2^n}.
$$
Sabemos que $\sum_{n=1}^{\infty} \frac{1}{2^n} = 1$. Para la segunda suma, factorizamos potencias de $2$:
$$
2 \sum_{n=1}^{\infty} \frac{b_{n+1}}{2^n} = 4 \sum_{n=1}^{\infty} \frac{b_{n+1}}{2^{n+1}} = 4 \left( \sum_{k=1}^{\infty} \frac{b_k}{2^k} - \frac{b_1}{2} \right) = 4\left(u - \frac{b_1}{2}\right).
$$
Como $b_1 = 0$ y $u = \frac{1}{2\pi}$, resulta:
$$
S = 1 - 4\left(\frac{1}{2\pi} - 0\right) = 1 - \frac{2}{\pi}.
$$

\boxed{1 - \frac{2}{\pi}}