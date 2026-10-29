## Planteamiento

Sea $P(x)=(x^2-1)(x^2-2)(x^2-3)(x^2-4)$, de grado $8$. Multiplicando la ecuación por $P(x)$:

$$N(x) = (2010x-4)\,P(x),$$

donde
$$N(x)=\sum_{k=1}^{4} k\prod_{j\neq k}(x^2-j)$$
tiene grado $6$.

## El polinomio resultante

La ecuación equivale a
$$Q(x) = N(x) - (2010x-4)P(x) = 0.$$

Con $y=x^2$ se ve que $P(x)=y^4-10y^3+\cdots = x^8-10x^6+\cdots$, es decir **no tiene término en $x^7$**. Entonces

$$(2010x-4)P(x) = 2010x^9 - 4x^8 - 20100x^7+\cdots$$

Como $N(x)$ solo tiene grado $6$, no afecta a los coeficientes de $x^9$ ni de $x^8$:

$$Q(x) = -2010x^9 + 4x^8 + \cdots$$

## Verificación de raíces espurias

Hay que comprobar que ninguna raíz de $Q$ sea un polo. Si $x^2=k$, solo sobrevive un término de $N$; por ejemplo para $x^2=1$:
$$N = 1\cdot(1-2)(1-3)(1-4) = -6 \neq 0,$$
y análogamente para $k=2,3,4$ (se obtienen $2\cdot 1\cdot(-1)(-2)=4$, $3\cdot 2\cdot 1\cdot(-1)=-6$, $4\cdot 3\cdot 2\cdot 1=24$). Luego $Q(\pm\sqrt{k})\neq 0$ y las $9$ raíces de $Q$ son soluciones genuinas.

## Suma por Vieta

$$\text{Suma} = -\frac{4}{-2010} = \frac{4}{2010} = \frac{2}{1005}.$$

$$\boxed{\dfrac{2}{1005}}$$