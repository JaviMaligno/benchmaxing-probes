Para evaluar la serie infinita
$$S = \sum_{n=1}^{\infty} \frac{\operatorname{sgn}\left(\sin\left(3\cdot 2^{n}\right)\right)}{2^{n}},$$
definamos $y = \frac{3}{\pi}$. Como $3 < \pi < 4$, tenemos que $0 < y < 1$. Además, dado que $\pi$ es irracional, $y$ también es irracional, por lo que posee una representación binaria única que no termina ni tiene una cola infinita de unos:
$$y = \sum_{k=1}^{\infty} \frac{b_k}{2^k}, \quad \text{donde } b_k \in \{0, 1\}.$$

Observemos que podemos reescribir el argumento del seno como $3 \cdot 2^n = \pi y 2^n$. Al multiplicar la expansión binaria de $y$ por $2^n$, obtenemos:
$$y 2^n = \sum_{k=1}^{n} b_k 2^{n-k} + \sum_{k=n+1}^{\infty} \frac{b_k}{2^{k-n}} = I_n + F_n,$$
donde:
- $I_n = \sum_{k=1}^{n} b_k 2^{n-k}$ es la parte entera de $y 2^n$.
- $F_n = \sum_{m=1}^{\infty} \frac{b_{n+m}}{2^m}$ es la parte fraccionaria de $y 2^n$.

Dado que $y$ es irracional, la parte fraccionaria cumple estrictamente que $0 < F_n < 1$ para todo $n \ge 1$, lo que implica que $\sin(\pi F_n) > 0$.

Por otro lado, todos los términos en la suma de $I_n$ con $k < n$ son múltiplos pares de $b_k$ (ya que $2^{n-k}$ es par para $n - k \ge 1$). Por lo tanto, la paridad de $I_n$ está determinada únicamente por el último dígito $b_n$:
$$I_n \equiv b_n \pmod{2}.$$

Usando las propiedades trigonométricas del seno, tenemos:
$$\sin(3 \cdot 2^n) = \sin(\pi I_n + \pi F_n) = (-1)^{I_n} \sin(\pi F_n) = (-1)^{b_n} \sin(\pi F_n).$$

Como $\sin(\pi F_n) > 0$, el signo de $\sin(3 \cdot 2^n)$ depende exclusivamente de $(-1)^{b_n}$:
$$\operatorname{sgn}\left(\sin\left(3\cdot 2^{n}\right)\right) = (-1)^{b_n} = 1 - 2b_n.$$

Sustituyendo esta expresión en la serie original, obtenemos:
$$S = \sum_{n=1}^{\infty} \frac{1 - 2b_n}{2^n} = \sum_{n=1}^{\infty} \frac{1}{2^n} - 2\sum_{n=1}^{\infty} \frac{b_n}{2^n}.$$

Sabemos que $\sum_{n=1}^{\infty} \frac{1}{2^n} = 1$ y que $\sum_{n=1}^{\infty} \frac{b_n}{2^n} = y = \frac{3}{\pi}$. Por consiguiente:
$$S = 1 - 2y = 1 - \frac{6}{\pi}.$$

\boxed{1 - \frac{6}{\pi}}