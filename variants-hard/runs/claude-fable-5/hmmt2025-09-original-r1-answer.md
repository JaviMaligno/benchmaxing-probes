## Planteamiento

Trabajamos módulo el primo $p = 2027$. Por interpolación de Lagrange:

$$f(x) = \sum_{\substack{n=1 \\ n \text{ cuadrado}}}^{2027} \prod_{m \neq n} \frac{x-m}{n-m}$$

**Coeficiente de $x^{2025}$ en cada término.** Cada producto es un polinomio de grado 2026, y su coeficiente de $x^{2025}$ es:

$$\frac{-\sum_{m \neq n} m}{\prod_{m \neq n} (n-m)}$$

**Denominador mod $p$:** cuando $m$ recorre $\{1,\dots,2027\}\setminus\{n\}$, los valores $n-m$ recorren exactamente todos los residuos no nulos módulo $p$. Por el teorema de Wilson:

$$\prod_{m \neq n}(n-m) \equiv (p-1)! \equiv -1 \pmod{p}$$

**Numerador mod $p$:** 

$$\sum_{m \neq n} m = \frac{2027 \cdot 2028}{2} - n \equiv -n \pmod{2027}$$

puesto que $\frac{2027\cdot 2028}{2} = 2027 \cdot 1014 \equiv 0$.

Por tanto, cada término cuadrado $n$ aporta al coeficiente de $x^{2025}$:

$$\frac{-(-n)}{-1} \equiv -n \pmod{2027}$$

**Suma sobre los cuadrados.** Los cuadrados perfectos en $\{1,\dots,2027\}$ son $k^2$ con $1 \le k \le 45$ (ya que $45^2 = 2025$). Entonces:

$$\frac{a}{b} \equiv -\sum_{k=1}^{45} k^2 = -\frac{45 \cdot 46 \cdot 91}{6} = -31395 \pmod{2027}$$

Como $31395 = 15 \cdot 2027 + 990$, tenemos $31395 \equiv 990$, así que:

$$\frac{a}{b} \equiv -990 \equiv 2027 - 990 = 1037 \pmod{2027}$$

Esto significa que $a \equiv 1037\, b \pmod{2027}$, es decir, $a - 1037\,b$ es divisible por $2027$.

$$\boxed{1037}$$