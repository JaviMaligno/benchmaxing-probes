## Planteamiento

Sea $P(x)=\prod_{k=1}^{4}(x^2-k)$. Multiplicando la ecuación por $P(x)$:

$$\underbrace{\sum_{k=1}^{4} k\prod_{j\neq k}(x^2-j)}_{Q(x)} = (2022x-4)P(x)$$

es decir, la ecuación polinómica $(2022x-4)P(x)-Q(x)=0$.

## Grados y coeficientes

- $Q(x)$ es un polinomio en $x^2$ de grado 3, o sea grado 6 en $x$: no afecta a los coeficientes de $x^9$ ni $x^8$.
- $P(x)=x^8-10x^6+\cdots$ (solo potencias pares), luego
$$(2022x-4)P(x)=2022x^9-4x^8+\cdots$$

Así, el polinomio total tiene grado 9, con coeficiente principal $2022$ y coeficiente de $x^8$ igual a $-4$.

## Raíces extrañas

Si $x^2=k$ para algún $k\in\{1,2,3,4\}$, entonces $P(x)=0$ pero $Q(x)=k\prod_{j\neq k}(k-j)\neq 0$, por lo que esos valores no son raíces: no se introdujeron soluciones espurias y las 9 raíces son todas válidas.

## Suma (Vieta)

$$\sum x_i = -\frac{-4}{2022}=\frac{4}{2022}=\frac{2}{1011}$$

\boxed{\dfrac{2}{1011}}