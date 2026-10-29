# Planteamiento

Sea $n=23$ y fijemos $k$. Escribimos $j=g(k)$, que es uniforme en $\{1,\dots,n\}$.

**Caso $j=k$** (probabilidad $1/n$): entonces $g(g(k))=g(k)=k$, y el término vale $0$.

**Caso $j\neq k$** (probabilidad $(n-1)/n$): el valor $g(j)$ es independiente de $g(k)$ y uniforme en $\{1,\dots,n\}$, así que $g(g(k))$ es uniforme.

Por tanto
$$E\bigl[(g(g(k))-k)^2\bigr]=\frac{n-1}{n}\cdot\frac1n\sum_{m=1}^n (m-k)^2 .$$

# Suma doble

$$\sum_{k=1}^n\sum_{m=1}^n (m-k)^2 = 2n\sum_{m=1}^n m^2 - 2\Bigl(\sum_{m=1}^n m\Bigr)^2 = \frac{n^2(n+1)(2n+1)}{3}-\frac{n^2(n+1)^2}{2}=\frac{n^2(n+1)(n-1)}{6}.$$

Entonces
$$E\left[\sum_{k=1}^n (g(g(k))-k)^2\right]=\frac{n-1}{n^2}\cdot\frac{n^2(n+1)(n-1)}{6}=\frac{(n-1)^2(n+1)}{6}.$$

# Evaluación

Con $n=23$: $\dfrac{22^2\cdot 24}{6}=484\cdot 4=1936$.

\boxed{1936}