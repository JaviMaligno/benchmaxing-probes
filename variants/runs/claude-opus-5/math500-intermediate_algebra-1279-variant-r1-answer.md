## Planteamiento

Sea $P(x)=\prod_{k=1}^{4}(x^2-k)$, de grado 8 y con **solo potencias pares**:
$$P(x)=x^8-10x^6+35x^4-50x^2+24.$$

Al multiplicar la ecuación por $P(x)$:
$$N(x)=(2022x-4)P(x),\qquad N(x)=\sum_{k=1}^{4}k\prod_{j\neq k}(x^2-j).$$

El numerador $N(x)$ tiene grado 6 y también solo potencias pares.

## Polinomio resultante

$$Q(x)=(2022x-4)P(x)-N(x)=0.$$

- Coeficiente de $x^9$: proviene solo de $2022x\cdot x^8$, es $2022$.
- Coeficiente de $x^8$: proviene solo de $-4\cdot x^8$, es $-4$ (ni $2022x\cdot P$ aporta grado 8, porque $P$ es par, ni $N$ llega a grado 8).

Las raíces de $Q$ son exactamente las raíces de la ecuación original: si $x^2=k$, entonces $Q(x)=-N(x)=-k\prod_{j\neq k}(k-j)\neq 0$, así que no hay raíces espurias ni cancelaciones, y el grado es exactamente 9.

## Suma de raíces

Por Vieta:
$$\sum x_i=-\frac{-4}{2022}=\frac{4}{2022}=\frac{2}{1011}.$$

\boxed{\dfrac{2}{1011}}