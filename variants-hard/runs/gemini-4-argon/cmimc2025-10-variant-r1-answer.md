Para calcular el valor de la serie infinita, buscamos transformar el término general en una expresión telescópica.

**Paso 1: Analizar la relación de recurrencia**
Dada la sucesión definida por $b_0 = 2025$ y
$$b_{n+1} = b_n^3 + 7b_n^2 + 18b_n + 15,$$
observamos qué sucede al sumar $3$ a ambos lados de la ecuación:
$$b_{n+1} + 3 = b_n^3 + 7b_n^2 + 18b_n + 18.$$
Notamos que el polinomio del lado derecho se puede factorizar utilizando el denominador de la serie, $b_n^2 + 4b_n + 6$:
$$(b_n + 3)(b_n^2 + 4b_n + 6) = b_n^3 + 4b_n^2 + 6b_n + 3b_n^2 + 12b_n + 18 = b_n^3 + 7b_n^2 + 18b_n + 18.$$
Por lo tanto, tenemos la identidad:
$$b_{n+1} + 3 = (b_n + 3)(b_n^2 + 4b_n + 6).$$

**Paso 2: Reescribir el término general de la suma**
Multiplicamos el numerador y el denominador del término general por $(b_n + 3)$:
$$\frac{3^n (b_n + 1)}{b_n^2 + 4b_n + 6} = \frac{3^n (b_n + 1)(b_n + 3)}{(b_n + 3)(b_n^2 + 4b_n + 6)} = \frac{3^n (b_n^2 + 4b_n + 3)}{b_n + 3)(b_n^2 + 4b_n + 6)}.$$

Reescribimos el factor cuadrático del numerador como $(b_n^2 + 4b_n + 6) - 3$:
$$\frac{3^n \big((b_n^2 + 4b_n + 6) - 3\big)}{(b_n + 3)(b_n^2 + 4b_n + 6)} = \frac{3^n (b_n^2 + 4b_n + 6)}{(b_n + 3)(b_n^2 + 4b_n + 6)} - \frac{3^{n+1}}{(b_n + 3)(b_n^2 + 4b_n + 6)}.$$

Usando la identidad $b_{n+1} + 3 = (b_n + 3)(b_n^2 + 4b_n + 6)$ obtenida en el Paso 1, simplificamos:
$$\frac{3^n (b_n + 1)}{b_n^2 + 4b_n + 6} = \frac{3^n}{b_n + 3} - \frac{3^{n+1}}{b_{n+1} + 3}.$$

**Paso 3: Evaluar la suma telescópica**
Consideramos la suma parcial hasta un entero $N$:
$$S_N = \sum_{n=0}^{N} \left( \frac{3^n}{b_n + 3} - \frac{3^{n+1}}{b_{n+1} + 3} \right) = \frac{3^0}{b_0 + 3} - \frac{3^{N+1}}{b_{N+1} + 3}.$$

Dado que $b_0 = 2025 > 0$, la sucesión $b_n$ crece de manera superexponencial (en particular, $b_n^2 + 4b_n + 6 \ge 2025^2 \gg 3$ para todo $n \ge 0$), por lo que:
$$\lim_{N \to \infty} \frac{3^{N+1}}{b_{N+1} + 3} = 0.$$

Finalmente, sustituyendo $b_0 = 2025$:
$$\sum_{n=0}^{\infty} \frac{3^n (b_n + 1)}{b_n^2 + 4b_n + 6} = \frac{1}{2025 + 3} = \frac{1}{2028}.$$

\boxed{\frac{1}{2028}}