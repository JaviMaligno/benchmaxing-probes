## Planteamiento

Como $a_n = 2$ y todas las raíces $r_1,\dots,r_n$ son enteras y distintas:

$$f(x) = 2(x-r_1)(x-r_2)\cdots(x-r_n)$$

**Condición del término constante:**
$$a_0 = f(0) = 2(-1)^n r_1r_2\cdots r_n = 66 \implies |r_1r_2\cdots r_n| = 33$$

**Coeficiente buscado:** por las fórmulas de Vieta, $a_{n-1} = -2(r_1+\cdots+r_n)$, luego

$$|a_{n-1}| = 2\left|\sum r_i\right|$$

## Minimizar la suma

Las raíces deben ser divisores de $33$: pertenecen a $\{\pm1,\pm3,\pm11,\pm33\}$, y el producto de sus valores absolutos debe ser $33$. Los únicos casos son:

- **$\{\pm33\}$**, con posible $1$ y/o $-1$ añadidos: sumas $\pm32,\pm33,\pm34$.
- **$\{\pm3\}\cup\{\pm11\}$**, con posible $1$ y/o $-1$: las sumas base son $14,\,8,\,-8,\,-14$, que al añadir $+1$, $-1$ o ambos se desplazan en $+1$, $-1$ o $0$.

El mínimo de $\left|\sum r_i\right|$ se alcanza en $-8+1 = -7$ (o simétricamente $8-1=7$), es decir $7$.

## Verificación

Tomando las raíces $1, 3, -11$ (distintas y enteras):

$$f(x) = 2(x-1)(x-3)(x+11) = 2(x^3 + 7x^2 - 41x + 33) = 2x^3 + 14x^2 - 82x + 66$$

Se cumple $a_n = 2$, $a_0 = 66$, y $|a_{n-1}| = 14 = 2\cdot 7$.

Como $\left|\sum r_i\right| \ge 7$ siempre, el valor mínimo es:

\boxed{14}