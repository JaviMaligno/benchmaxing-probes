## Planteamiento

**Paso 1: El orden de $z$.**
El número $2027$ es primo (no tiene divisores hasta $\sqrt{2027}\approx 45$). Como $z^{2027}=1$ y $z\neq 1$, el orden de $z$ es un divisor de $2027$ distinto de $1$, es decir, exactamente $2027$. Por lo tanto $z$ es una **raíz primitiva** de la unidad de orden $2027$.

**Paso 2: Las potencias recorren todas las raíces.**
Como $z$ es primitiva, las potencias
$$z,\ z^2,\ z^3,\ \dots,\ z^{2027}$$
recorren **exactamente una vez** cada una de las $2027$ raíces de la unidad. Así que la suma pedida es
$$S=\sum_{w^{2027}=1}\frac{1}{1+w}.$$

**Paso 3: Emparejamiento.**
Las raíces son $w=1$ junto con los demás elementos del grupo. Como $2027$ es impar, si $w\neq 1$ es raíz, entonces $w\neq w^{-1}$ (solo $1$ y $-1$ satisfacen $w^2=1$, y $-1$ no lo es). Así las $2026$ raíces restantes forman $1013$ pares $\{w,\,1/w\}$.

Para cada par:
$$\frac{1}{1+w}+\frac{1}{1+w^{-1}}=\frac{1}{1+w}+\frac{w}{w+1}=\frac{1+w}{1+w}=1.$$

**Paso 4: Total.**
$$S=\underbrace{1013\cdot 1}_{\text{pares}}+\underbrace{\frac{1}{1+1}}_{w=1}=1013+\frac12=\frac{2027}{2}.$$

*(Verificación rápida con $n=3$: raíces $1,\omega,\omega^2$ dan $\frac12+1=\frac32=\frac{n}{2}$, consistente.)*

$$\boxed{\frac{2027}{2}}$$