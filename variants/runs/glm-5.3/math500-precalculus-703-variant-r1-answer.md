## Razonamiento

**Paso 1: Identificar el polinomio.**

La suma alterna
$$w^{10} - w^9 + w^8 - \cdots - w + 1$$
es una serie geométrica con razón $-w$ y 11 términos:
$$(1-(-w)^{11}) = 1 + w^{11} \quad\text{dividida entre}\quad 1-(-w) = 1+w.$$

Es decir:
$$w^{10} - w^9 + \cdots - w + 1 = \frac{w^{11}+1}{w+1}.$$

**Paso 2: Resolver $w^{11} = -1$.**

Como $|w^{11}| = 1$, toda raíz cumple $|w| = 1$, es decir $\rho = 1$. Escribiendo $w = e^{i\varphi}$:
$$11\varphi \equiv \pi \pmod{2\pi} \implies \varphi = \frac{(2k+1)\pi}{11}, \quad k = 0, 1, \dots, 10.$$

**Paso 3: Excluir $w = -1$.**

El valor $k=5$ da $\varphi = \frac{11\pi}{11} = \pi$, es decir $w = -1$, que anula el denominador $w+1$ y no es raíz del polinomio original (sustituyendo $w=-1$ se obtiene $11 \neq 0$). Hay que excluirlo.

**Paso 4: Sumar los valores de $\varphi$ en $[0, 2\pi)$.**

Los valores restantes corresponden a los impares
$$1, 3, 5, 7, 9, \; 13, 15, 17, 19, 21,$$
(es decir, todos los impares de 1 a 21 salvo el 11). Su suma es:
$$\underbrace{(1+3+\cdots+21)}_{=11^2=121} - 11 = 110.$$

Por lo tanto:
$$\sum \varphi = \frac{110\pi}{11} = 10\pi.$$

**Verificación:** La suma de las 11 raíces de $w^{11}+1$ es 0; quitando $-1$ (que "aporta" el ángulo $\pi$... en suma de exponentes), la suma de ángulos de las 10 raíces es $\frac{121\pi}{11} - \pi = 10\pi$. ✓

$$\boxed{10\pi}$$