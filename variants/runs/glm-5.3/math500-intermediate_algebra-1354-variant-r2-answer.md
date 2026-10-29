# Resolución

**Paso 1: Identificar la estructura.**
Como $z^{2027} = 1$ y $z \neq 1$, veamos qué orden tiene $z$. El orden de $z$ divide a $2027$, que es primo (lo verifiqué probando divisibilidad por todos los primos hasta $\sqrt{2027}\approx 45$). Como el orden no es $1$, debe ser exactamente $2027$. Entonces $z$ es una raíz primitiva, y las potencias $z, z^2, \dots, z^{2027}$ recorren **todas** las raíces $2027$-ésimas de la unidad, cada una una sola vez.

Por lo tanto la suma es
$$S = \sum_{w^{2027} = 1} \frac{1}{1+w}.$$

**Paso 2: Verificar que nada se anula.**
Un denominador $1+w = 0$ exigiría $w = -1$, pero $(-1)^{2027} = -1 \neq 1$ (2027 es impar), así que $-1$ **no** es raíz $2027$-ésima. Todos los términos están bien definidos.

**Paso 3: Emparejar $w$ con $w^{-1}$.**
Si $w \neq 1$, su inversa $w^{-1}$ también es raíz, y es distinta de $w$: si $w = w^{-1}$, entonces $w^2 = 1$, lo que obligaría a $w = \pm 1$, y ya descartamos ambos casos. Cada pareja aporta:
$$\frac{1}{1+w} + \frac{1}{1+w^{-1}} = \frac{1}{1+w} + \frac{w}{w+1} = \frac{1+w}{1+w} = 1.$$

**Paso 4: Contar.**
Hay $2026$ raíces no triviales, que forman $1013$ parejas, cada una sumando $1$. La raíz restante es $w = 1$, que aporta $\frac{1}{1+1} = \frac{1}{2}$.

$$S = 1013 \cdot 1 + \frac{1}{2} = \frac{2027}{2}.$$

**Comprobación rápida con un caso análogo:** para exponente $3$ (también primo impar), $\frac{1}{1+z}+\frac{1}{1+z^2}+\frac{1}{1+z^3} = 1 + \frac12 = \frac32$, y en efecto $\frac{3}{2}$. El patrón se confirma.

$$\boxed{\dfrac{2027}{2}}$$