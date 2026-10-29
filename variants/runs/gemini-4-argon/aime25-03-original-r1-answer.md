Para encontrar el número de asignaciones diferentes de sabores a los jugadores, denotemos por $c$, $v$ y $s$ el número de jugadores que eligieron chocolate, vainilla y fresa (strawberry), respectivamente.

Dado que hay $9$ jugadores y cada uno elige exactamente un sabor, tenemos que:
$$c + v + s = 9$$

Además, el problema establece que al menos un jugador eligió cada sabor y que el número de jugadores que eligió chocolate es mayor que el de vainilla, que a su vez es mayor que el de fresa. Esto nos da la condición:
$$c > v > s \ge 1$$

Buscamos todas las ternas de números enteros $(c, v, s)$ que cumplen estas condiciones:

1. **Si $s = 1$:** Tenemos $c + v = 8$ con $c > v \ge 2$.
   - Si $v = 2$, entonces $c = 6$, lo que nos da la terna $(6, 2, 1)$.
   - Si $v = 3$, entonces $c = 5$, lo que nos da la terna $(5, 3, 1)$.
   - Si $v \ge 4$, entonces $c \le 4$, lo cual no cumple $c > v$.

2. **Si $s = 2$:** Tenemos $c + v = 7$ con $c > v \ge 3$.
   - Si $v = 3$, entonces $c = 4$, lo que nos da la terna $(4, 3, 2)$.
   - Si $v \ge 4$, entonces $c \le 3$, lo cual no cumple $c > v$.

3. **Si $s \ge 3$:** El valor mínimo posible para la suma sería $3 + 4 + 5 = 12 > 9$, por lo que no hay más soluciones.

Para cada terna $(c, v, s)$, el número de formas de asignar los sabores a los $9$ jugadores distintos está dado por el coeficiente multinomial $\frac{9!}{c!\,v!\,s!}$:

- Para $(6, 2, 1)$:
  $$\frac{9!}{6!\,2!\,1!} = \frac{9 \times 8 \times 7}{2 \times 1} = 252$$

- Para $(5, 3, 1)$:
  $$\frac{9!}{5!\,3!\,1!} = \frac{9 \times 8 \times 7 \times 6}{6 \times 1} = 504$$

- Para $(4, 3, 2)$:
  $$\frac{9!}{4!\,3!\,2!} = \frac{9 \times 8 \times 7 \times 6 \times 5}{6 \times 2} = 1260$$

Sumando todos los casos posibles obtenemos el valor total de $N$:
$$N = 252 + 504 + 1260 = 2016$$

Finalmente, calculamos el residuo cuando $N$ se divide entre $1000$:
$$2016 \equiv 16 \pmod{1000}$$

\boxed{16}