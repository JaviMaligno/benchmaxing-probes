## Solución

**Reescritura.** Como $\frac{3150}{k+0.5} = \frac{6300}{2k+1}$, con la sustitución $m = 2k+1$ la suma recorre todos los impares $m$ desde $-2399$ hasta $2401$:

$$S = \sum_{\substack{m \text{ impar} \\ -2399 \le m \le 2401}} \left\lfloor \frac{6300}{m} \right\rfloor$$

**Emparejamiento $m \leftrightarrow -m$.** Los impares de $1$ a $2399$ (son $1200$ valores) se emparejan con sus negativos, y queda suelto el término $m = 2401$.

Para cada par, uso la identidad $\lfloor x \rfloor + \lfloor -x \rfloor = 0$ si $x \in \mathbb{Z}$, y $-1$ en caso contrario. Por lo tanto cada impar $m \in [1, 2399]$ aporta:
- $0$ si $m \mid 6300$,
- $-1$ si $m \nmid 6300$.

**Divisores impares de 6300.** Como $6300 = 2^2 \cdot 3^2 \cdot 5^2 \cdot 7$, sus divisores impares son los divisores de $3^2 \cdot 5^2 \cdot 7 = 1575$, que son $(2+1)(2+1)(1+1) = 18$. Todos son $\le 1575 < 2399$, así que los $18$ cuentan.

Contribución de los pares: $-(1200 - 18) = -1182$.

**Término restante.** Para $m = 2401 = 7^4$:
$$\left\lfloor \frac{6300}{2401} \right\rfloor = \lfloor 2.624\ldots \rfloor = 2$$

**Total.**
$$S = -1182 + 2 = -1180$$

$$\boxed{-1180}$$