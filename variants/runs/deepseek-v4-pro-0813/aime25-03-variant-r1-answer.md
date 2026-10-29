Sea $m$, $b$, $k$ el número de miembros que eligen mango, banana y kiwi, respectivamente. Las condiciones son:

- $m + b + k = 10$
- $m > b > k \ge 1$

Como $k \ge 1$ y $b > k$, entonces $b \ge 2$ y $m \ge 3$.

Enumeremos las ternas posibles $(m, b, k)$:

- $k = 1$: $b \ge 2$, $m > b$, y $m + b = 9$.
  - $b = 2 \Rightarrow m = 7$ → $(7,2,1)$
  - $b = 3 \Rightarrow m = 6$ → $(6,3,1)$
  - $b = 4 \Rightarrow m = 5$ → $(5,4,1)$
  - $b = 5 \Rightarrow m = 4$, pero $m > b$ falla.
- $k = 2$: $b \ge 3$, $m > b$, y $m + b = 8$.
  - $b = 3 \Rightarrow m = 5$ → $(5,3,2)$
  - $b = 4 \Rightarrow m = 4$, falla $m > b$.
- $k = 3$: $b \ge 4$, $m + b = 7$, $m > b$ → $m \ge 5$, $b \ge 4$ da suma $\ge 9 > 7$. No hay.

Las ternas válidas son:
$$(7,2,1),\ (6,3,1),\ (5,4,1),\ (5,3,2)$$

Los miembros son distinguibles, así que el número de asignaciones para una terna es el coeficiente multinomial:
$$\frac{10!}{m!\, b!\, k!}$$

Calculamos:

- $\frac{10!}{7!\,2!\,1!} = \frac{10 \cdot 9}{2} = 45$
- $\frac{10!}{6!\,3!\,1!} = \frac{10 \cdot 9 \cdot 8 \cdot 7}{3!} \cdot \frac1{1!} = 840$
- $\frac{10!}{5!\,4!\,1!} = \frac{10 \cdot 9 \cdot 8 \cdot 7 \cdot 6}{4! \cdot 1!} = 1260$
- $\frac{10!}{5!\,3!\,2!} = \frac{10 \cdot 9 \cdot 8 \cdot 7 \cdot 6}{3! \cdot 2!} = 2520$

Portanto,
$$N = 45 + 840 + 1260 + 2520 = 4665$$

El resto al dividir por $1000$ es $4665 - 4000 = 665$.

$$\boxed{665}$$