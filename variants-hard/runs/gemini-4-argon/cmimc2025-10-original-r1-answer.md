Para determinar el valor de la serie infinita, primero analizamos la relación de recurrencia dada:

$$a_{n+1} = a_{n}^{3} + 5 a_{n}^{2} + 10 a_{n} + 6$$

Si sumamos $2$ a ambos lados de la ecuación, podemos factorizar el polinomio resultante:

$$a_{n+1} + 2 = a_{n}^{3} + 5 a_{n}^{2} + 10 a_{n} + 8 = (a_{n} + 2)(a_{n}^{2} + 3 a_{n} + 4)$$

Observamos que el factor $a_{n}^{2} + 3 a_{n} + 4$ coincide con el denominador del término general de nuestra suma. A partir de esta identidad, consideremos la diferencia telescópica:

$$\frac{1}{a_{n} + 2} - \frac{2}{a_{n+1} + 2} = \frac{1}{a_{n} + 2} - \frac{2}{(a_{n} + 2)(a_{n}^{2} + 3 a_{n} + 4)}$$

Poniendo ambos términos bajo un denominador común:

$$\frac{1}{a_{n} + 2} - \frac{2}{a_{n+1} + 2} = \frac{a_{n}^{2} + 3 a_{n} + 4 - 2}{(a_{n} + 2)(a_{n}^{2} + 3 a_{n} + 4)} = \frac{a_{n}^{2} + 3 a_{n} + 2}{(a_{n} + 2)(a_{n}^{2} + 3 a_{n} + 4)}$$

Factorizando el numerador como $a_{n}^{2} + 3 a_{n} + 2 = (a_{n} + 1)(a_{n} + 2)$ y simplificando el factor $(a_{n} + 2)$ (dado que $a_n > 0$ para todo $n \geq 0$):

$$\frac{1}{a_{n} + 2} - \frac{2}{a_{n+1} + 2} = \frac{a_{n} + 1}{a_{n}^{2} + 3 a_{n} + 4}$$

Multiplicando ambos lados por $2^{n}$, obtenemos el término general de la serie:

$$\frac{2^{n}(a_{n} + 1)}{a_{n}^{2} + 3 a_{n} + 4} = \frac{2^{n}}{a_{n} + 2} - \frac{2^{n+1}}{a_{n+1} + 2}$$

Al sumar desde $n = 0$ hasta $N$, la suma se vuelve telescópica:

$$\sum_{n=0}^{N} \frac{2^{n}(a_{n} + 1)}{a_{n}^{2} + 3 a_{n} + 4} = \frac{1}{a_{0} + 2} - \frac{2^{N+1}}{a_{N+1} + 2}$$

Dado que $a_0 = 2024$ y $a_{n+1} > a_n^3$, la sucesión $a_n$ crece de manera superexponencial (mucho más rápido que $2^n$), por lo que:

$$\lim_{N \to \infty} \frac{2^{N+1}}{a_{N+1} + 2} = 0$$

Por lo tanto, el valor de la serie infinita es:

$$\sum_{n=0}^{\infty} \frac{2^{n}(a_{n} + 1)}{a_{n}^{2} + 3 a_{n} + 4} = \frac{1}{a_{0} + 2} = \frac{1}{2024 + 2} = \frac{1}{2026}$$

\boxed{\frac{1}{2026}}