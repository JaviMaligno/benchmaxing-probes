Para encontrar el polinomio cúbico cuya raíz es $x$, definamos primero los ángulos:
$$\alpha = \arccos x, \quad \beta = \arccos 2x, \quad \gamma = \arccos 4x.$$

De acuerdo con el enunciado, tenemos que:
$$\alpha + \beta + \gamma = \pi \implies \alpha + \beta = \pi - \gamma.$$

Aplicando la función coseno en ambos lados de la ecuación:
$$\cos(\alpha + \beta) = \cos(\pi - \gamma).$$

Utilizando la identidad para el coseno de la suma de dos ángulos y el hecho de que $\cos(\pi - \gamma) = -\cos \gamma$, obtenemos:
$$\cos \alpha \cos \beta - \sin \alpha \sin \beta = -\cos \gamma,$$
lo cual se puede reescribir como:
$$\cos \alpha \cos \beta + \cos \gamma = \sin \alpha \sin \beta.$$

Elevando al cuadrado ambos lados de la ecuación:
$$(\cos \alpha \cos \beta + \cos \gamma)^2 = \sin^2 \alpha \sin^2 \beta.$$

Usando la identidad pitagórica $\sin^2 \theta = 1 - \cos^2 \theta$:
$$\cos^2 \alpha \cos^2 \beta + 2\cos \alpha \cos \beta \cos \gamma + \cos^2 \gamma = (1 - \cos^2 \alpha)(1 - \cos^2 \beta).$$

Desarrollando el lado derecho:
$$\cos^2 \alpha \cos^2 \beta + 2\cos \alpha \cos \beta \cos \gamma + \cos^2 \gamma = 1 - \cos^2 \alpha - \cos^2 \beta + \cos^2 \alpha \cos^2 \beta.$$

Restando $\cos^2 \alpha \cos^2 \beta$ en ambos lados y agrupando los términos:
$$\cos^2 \alpha + \cos^2 \beta + \cos^2 \gamma + 2\cos \alpha \cos \beta \cos \gamma - 1 = 0.$$

Sustituyendo $\cos \alpha = x$, $\cos \beta = 2x$ y $\cos \gamma = 4x$:
$$x^2 + (2x)^2 + (4x)^2 + 2(x)(2x)(4x) - 1 = 0$$
$$x^2 + 4x^2 + 16x^2 + 16x^3 - 1 = 0$$
$$16x^3 + 21x^2 - 1 = 0.$$

Por el teorema de las raíces racionales, las posibles raíces racionales de $16x^3 + 21x^2 - 1 = 0$ son de la forma $\pm \frac{1}{2^k}$ para $k \in \{0, 1, 2, 3, 4\}$. Al evaluar cada una de ellas, se comprueba que ninguna anula el polinomio, por lo que $16x^3 + 21x^2 - 1$ es irreducible sobre $\mathbb{Q}$.

Como $\text{mcd}(16, 21, 0, -1) = 1$, los coeficientes enteros que minimizan la suma de sus valores absolutos corresponden a $a = 16$, $b = 21$, $c = 0$ y $d = -1$ (o sus opuestos). Por lo tanto, el menor valor posible de $|a| + |b| + |c| + |d|$ es:
$$|16| + |21| + |0| + |-1| = 16 + 21 + 0 + 1 = 38.$$

\boxed{38}