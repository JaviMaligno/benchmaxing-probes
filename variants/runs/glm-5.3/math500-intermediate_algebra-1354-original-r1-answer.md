# Planteamiento

Como $\omega^{1997}=1$ y $\omega \neq 1$, y dado que $1997$ es primo, $\omega$ es una raíz primitiva de la unidad de orden $1997$. Los valores $\omega, \omega^2, \dots, \omega^{1997}$ recorren **todas** las raíces 1997-ésimas de la unidad, cada una exactamente una vez (con $\omega^{1997}=1$ incluida). Así que la suma es

$$S = \sum_{\zeta^{1997}=1} \frac{1}{1+\zeta}.$$

Ningún denominador se anula: si $\zeta = -1$, entonces $(-1)^{1997} = -1 \neq 1$, así que $-1$ no es raíz.

# Agrupamiento por pares

Como $1997$ es impar, cada raíz $\zeta \neq 1$ es distinta de su inversa $\zeta^{-1}$ (pues $\zeta = \zeta^{-1}$ exigiría $\zeta^2 = 1$, es decir $\zeta = \pm 1$). Entonces las $1996$ raíces restantes forman $998$ pares $\{\zeta, \zeta^{-1}\}$, y cada par contribuye:

$$\frac{1}{1+\zeta} + \frac{1}{1+\zeta^{-1}} = \frac{1}{1+\zeta} + \frac{\zeta}{\zeta+1} = \frac{1+\zeta}{1+\zeta} = 1.$$

La raíz $\zeta = 1$ (que aparece cuando $k=1997$) aporta $\frac{1}{1+1} = \frac{1}{2}$.

Por lo tanto:

$$S = \underbrace{998}_{998 \text{ pares}} + \frac{1}{2} = \frac{1997}{2}.$$

# Verificación (método alternativo)

Si $\eta = -\zeta$, entonces $\eta$ recorre las raíces de $R(x) = x^{1997}+1$, y

$$S = \sum_{\eta^{1997}=-1} \frac{1}{1-\eta} = \frac{R'(1)}{R(1)} = \frac{1997 \cdot 1^{1996}}{2} = \frac{1997}{2}. \checkmark$$

$$\boxed{\dfrac{1997}{2}}$$