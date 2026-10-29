## Planteamiento

Como 2027 es primo y $z \neq 1$, $z$ es una raíz primitiva de orden 2027. Por tanto, cuando $k$ recorre $1, 2, \dots, 2027$, las potencias $z^k$ recorren **todas** las raíces 2027-ésimas de la unidad (incluyendo $z^{2027}=1$).

La suma buscada es entonces
$$S = \sum_{w^{2027}=1} \frac{1}{1+w}.$$

## Cálculo

Sea $f(x) = x^n - 1 = \prod_w (x-w)$ con $n = 2027$. Derivando logarítmicamente:
$$\sum_w \frac{1}{c-w} = \frac{f'(c)}{f(c)}.$$

Como $n$ es impar, $-1$ no es raíz de $f$, así que podemos evaluar en $c = -1$:
$$\sum_w \frac{1}{-1-w} = \frac{n(-1)^{n-1}}{(-1)^n - 1} = \frac{n}{-2} = -\frac{n}{2}.$$

Y como $\dfrac{1}{1+w} = -\dfrac{1}{-1-w}$:
$$S = \frac{n}{2} = \frac{2027}{2}.$$

## Verificación con $n=3$

Raíces $1, \omega, \omega^2$: usando $1+\omega = -\omega^2$ y $1+\omega^2 = -\omega$,
$$\tfrac12 - \tfrac{1}{\omega^2} - \tfrac{1}{\omega} = \tfrac12 - (\omega + \omega^2) = \tfrac12 + 1 = \tfrac32 = \tfrac n2. \checkmark$$

$$\boxed{\dfrac{2027}{2}}$$