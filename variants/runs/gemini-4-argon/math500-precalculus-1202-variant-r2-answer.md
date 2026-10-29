Para encontrar el polinomio cúbico del cual $x$ es raíz, definimos los ángulos:
$$\alpha = \arccos x, \quad \beta = \arccos 2x, \quad \gamma = \arccos 4x$$

A partir de estas definiciones, tenemos que $\cos \alpha = x$, $\cos \beta = 2x$ y $\cos \gamma = 4x$. La ecuación dada en el problema se puede reescribir como:
$$\alpha + \beta + \gamma = \pi \implies \alpha + \beta = \pi - \gamma$$

Aplicando la función coseno en ambos lados de la igualdad:
$$\cos(\alpha + \beta) = \cos(\pi - \gamma)$$

Utilizando la identidad para el coseno de la suma de dos ángulos y el hecho de que $\cos(\pi - \gamma) = -\cos \gamma$, obtenemos:
$$\cos \alpha \cos \beta - \sin \alpha \sin \beta = -\cos \gamma$$

Reorganizamos los términos para aislar el producto de los senos y elevamos ambos miembros al cuadrado:
$$\cos \alpha \cos \beta + \cos \gamma = \sin \alpha \sin \beta$$
$$(\cos \alpha \cos \beta + \cos \gamma)^2 = \sin^2 \alpha \sin^2 \beta$$

Usando la identidad pitagórica $\sin^2 \theta = 1 - \cos^2 \theta$, desarrollamos ambos lados:
$$\cos^2 \alpha \cos^2 \beta + 2 \cos \alpha \cos \beta \cos \gamma + \cos^2 \gamma = (1 - \cos^2 \alpha)(1 - \cos^2 \beta)$$
$$\cos^2 \alpha \cos^2 \beta + 2 \cos \alpha \cos \beta \cos \gamma + \cos^2 \gamma = 1 - \cos^2 \alpha - \cos^2 \beta + \cos^2 \alpha \cos^2 \beta$$

Cancelando $\cos^2 \alpha \cos^2 \beta$ en ambos lados y agrupando los términos, llegamos a la identidad clásica para tres ángulos que suman $\pi$:
$$\cos^2 \alpha + \cos^2 \beta + \cos^2 \gamma + 2 \cos \alpha \cos \beta \cos \gamma = 1$$

Sustituimos $\cos \alpha = x$, $\cos \beta = 2x$ y $\cos \gamma = 4x$ en la relación anterior:
$$x^2 + (2x)^2 + (4x)^2 + 2(x)(2x)(4x) = 1$$
$$x^2 + 4x^2 + 16x^2 + 16x^3 = 1$$
$$16x^3 + 21x^2 - 1 = 0$$

Para asegurarnos de que este polinomio genera el menor valor posible de $|a| + |b| + |c| + |d|$, verificamos que sus coeficientes $(a=16, b=21, c=0, d=-1)$ son coprimos entre sí ($\gcd(16, 21, 0, -1) = 1$). Además, al aplicar el cambio $y = 1/x$, obtenemos $y^3 - 21y - 16 = 0$, el cual no tiene raíces enteras divisoras de $16$ ($\pm 1, \pm 2, \pm 4, \pm 8, \pm 16$), por lo que el polinomio es irreducible sobre $\mathbb{Q}$ y cualquier otro polinomio cúbico con coeficientes enteros que tenga a $x$ como raíz debe ser un múltiplo entero de $16x^3 + 21x^2 - 1$.

Por lo tanto, el valor mínimo posible de $|a| + |b| + |c| + |d|$ es:
$$|16| + |21| + |0| + |-1| = 16 + 21 + 0 + 1 = 38$$

\boxed{38}