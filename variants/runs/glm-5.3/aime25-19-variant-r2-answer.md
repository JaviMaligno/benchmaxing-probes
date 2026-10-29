**Desarrollo paso a paso**

Cada término se simplifica usando identidades de logaritmos:

$$\log_k(7^{k^2-1}) = (k^2-1)\frac{\ln 7}{\ln k}, \qquad \log_{k+1}(7^{k^2-4}) = (k^2-4)\frac{\ln 7}{\ln(k+1)}$$

Por lo tanto cada factor del producto es:

$$\frac{\log_k(7^{k^2-1})}{\log_{k+1}(7^{k^2-4})} = \frac{k^2-1}{k^2-4}\cdot\frac{\ln(k+1)}{\ln k}$$

**Producto de logaritmos (telescópico):**

$$\prod_{k=3}^{80}\frac{\ln(k+1)}{\ln k} = \frac{\ln 4\cdot\ln 5\cdots \ln 81}{\ln 3\cdot\ln 4\cdots \ln 80} = \frac{\ln 81}{\ln 3} = \log_3 81 = 4$$

**Producto de razones (telescópico por pares):**

$$\frac{k^2-1}{k^2-4} = \frac{(k-1)(k+1)}{(k-2)(k+2)}$$

Se separa en dos productos:

$$\prod_{k=3}^{80}\frac{k-1}{k-2} = \frac{2\cdot 3\cdots 79}{1\cdot 2\cdots 78} = 79$$

$$\prod_{k=3}^{80}\frac{k+1}{k+2} = \frac{4\cdot 5\cdots 81}{5\cdot 6\cdots 82} = \frac{4}{82} = \frac{2}{21}$$

**Resultado total:**

$$4\cdot 79\cdot\frac{2}{21} = \frac{632}{21}$$

Como $632 = 2^3\cdot 79$ y $21 = 3\cdot 7$, la fracción es irreducible: $m=632$, $n=21$.

$$\boxed{653}$$