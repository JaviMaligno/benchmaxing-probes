## Desarrollo paso a paso

**Paso 1. Aplicar Vieta a la primera condición.**

El polinomio $x^{2}+ax+b$ tiene raíces $b$ y $c$, por lo tanto:

$$b + c = -a \qquad \text{(suma de raíces)}$$
$$bc = b \qquad \text{(producto de raíces)}$$

**Paso 2. Despejar $c$.**

Como $b \neq 0$, dividimos $bc = b$ entre $b$:

$$c = 1$$

**Paso 3. Usar la segunda condición.**

El polinomio $x^{2}+cx+a$ tiene a $7$ como raíz:

$$49 + 7c + a = 0 \implies a = -49 - 7c$$

Sustituyendo $c = 1$:

$$a = -49 - 7 = -56$$

**Paso 4. Calcular $b$.**

De $b + c = -a$:

$$b = -a - c = -(-56) - 1 = 55$$

**Verificación.** Con $(a,b,c) = (-56,\,55,\,1)$:

- $x^{2}-56x+55 = (x-1)(x-55)$ → raíces $55$ y $1$, es decir, $b$ y $c$. ✓
- $x^{2}+x-56 = (x-7)(x+8)$ → raíz $7$. ✓

Todos los valores son reales no nulos. ✓

## Respuesta

$$\boxed{55}$$