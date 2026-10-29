## Planteamiento

Como todas las raíces son enteras y distintas, y $a_n = 2$, el polinomio se factoriza como
$$f(x) = 2(x - r_1)(x - r_2)\cdots(x - r_n).$$

**Condición del término constante:** $a_0 = 2(-1)^n r_1 r_2 \cdots r_n = 66$, de modo que
$$r_1 r_2 \cdots r_n = \pm 33.$$

Como el producto de las raíces es $\pm 33$ y todas son enteras, cada raíz debe ser un divisor de 33: es decir, pertenece a $\{\pm 1, \pm 3, \pm 11, \pm 33\}$.

**Condición del coeficiente buscado:** $a_{n-1} = -2(r_1 + r_2 + \cdots + r_n)$, así que
$$|a_{n-1}| = 2\,\big|\textstyle\sum r_i\big|.$$

## Minimizar la suma

Para que $|{\prod r_i}| = 33 = 3 \cdot 11$, el conjunto de raíces (distintas) debe contener:
- exactamente uno de $\pm 3$ y uno de $\pm 11$ (y opcionalmente $1$ y/o $-1$), **o**
- uno de $\pm 33$ (y opcionalmente $1$ y/o $-1$).

Revisemos las sumas posibles:
- Con $\pm 33$: la mejor suma es $|33 - 1| = 32$. Muy grande.
- Con $\pm 3$ y $\pm 11$ sin unos: $|\pm 3 \pm 11| \in \{8, 14\}$.
- Con $\pm 3$, $\pm 11$ y ambos $1, -1$: los unos se cancelan, suma $\in \{8, 14\}$.
- Con $\pm 3$, $\pm 11$ y un solo $\pm 1$: $|\pm 1 \pm 3 \pm 11| \in \{7, 9, 13, 15\}$.

El mínimo es $7$, logrado por ejemplo con las raíces $\{1, 3, -11\}$:
$$f(x) = 2(x-1)(x-3)(x+11), \qquad a_0 = 2(-1)(-3)(11) = 66 \checkmark$$
$$a_{n-1} = -2(1 + 3 - 11) = 14.$$

Como el producto de raíces es impar, todas las raíces son impares y ninguna configuración da suma menor que 7.

$$\boxed{14}$$