## Planteamiento

El truco está en encontrar el cambio de variable adecuado. Observemos el factor del denominador y probemos con el desplazamiento $u_n = b_n + 3$:

$$(b+3)(b^2+4b+6) = b^3+7b^2+18b+18 = b_{n+1}+3$$

Es decir, la recursión se factoriza exactamente:

$$u_{n+1} = u_n\,(b_n^2+4b_n+6), \qquad u_n = b_n+3$$

## Telescopaje

De aquí, $b_n^2+4b_n+6 = u_{n+1}/u_n$, así que el término general es

$$t_n = \frac{3^n(b_n+1)}{b_n^2+4b_n+6} = \frac{3^n\,u_n\,(u_n-2)}{u_{n+1}}$$

usando $b_n+1 = u_n-2$.

Ahora la clave: escribiendo $b_n^2+4b_n+6 = u_n^2-2u_n+3$ se obtiene

$$u_{n+1}-3u_n = u_n(u_n^2-2u_n+3) - 3u_n = u_n^2(u_n-2)$$

Por lo tanto

$$\frac{3^n}{u_n}-\frac{3^{n+1}}{u_{n+1}} = \frac{3^n(u_{n+1}-3u_n)}{u_nu_{n+1}} = \frac{3^n\,u_n(u_n-2)}{u_{n+1}} = t_n$$

La serie es exactamente telescópica.

## Convergencia y valor

Como $u_{n+1}\sim u_n^3$ con $u_0 = 2028$, la cola $3^n/u_n \to 0$ de forma doblemente exponencial. Entonces

$$\sum_{n=0}^{\infty} t_n = \frac{3^0}{u_0} - \lim_{N\to\infty}\frac{3^{N}}{u_{N}} = \frac{1}{u_0} = \frac{1}{2025+3}$$

$$\boxed{\dfrac{1}{2028}}$$