# Solución

**Paso 1: Identificar la condición de validez.**

La función es
$$f(x)=\frac{1}{|x^2+3x-4|+|x^2+9x+20|}.$$

Una fracción solo está definida cuando su denominador es distinto de cero. Los valores de $x$ fuera del dominio son aquellos donde
$$|x^2+3x-4|+|x^2+9x+20|=0.$$

**Paso 2: Usar la positividad del valor absoluto.**

Una suma de valores absolutos es cero si y solo si **cada término es cero simultáneamente**. Por lo tanto, debemos buscar los $x$ que satisfagan al mismo tiempo:
$$x^2+3x-4=0 \quad\text{y}\quad x^2+9x+20=0.$$

**Paso 3: Factorizar cada polinomio.**

$$x^2+3x-4=(x+4)(x-1)=0 \implies x=-4 \;\text{ o }\; x=1.$$

$$x^2+9x+20=(x+5)(x+4)=0 \implies x=-5 \;\text{ o }\; x=-4.$$

**Paso 4: Intersecar las soluciones.**

El único valor común a ambas listas es $x=-4$.

**Paso 5: Verificar.**

- En $x=-4$: $\quad(-4)^2+3(-4)-4 = 16-12-4 = 0$ ✓ y $\quad(-4)^2+9(-4)+20 = 16-36+20 = 0$ ✓. El denominador es $|0|+|0|=0$, así que $f$ no está definida.
- En $x=1$: el segundo término es $1+9+20=30 \neq 0$, el denominador vale $30$.
- En $x=-5$: el primer término es $25-15-4=6 \neq 0$, el denominador vale $6$.

Por lo tanto, el único valor excluido del dominio es $x=-4$.

$$\boxed{x=-4}$$