Para encontrar el número de asignaciones posibles $N$, definimos $c$, $v$ y $s$ como el número de jugadores que eligieron chocolate, vainilla y fresa, respectivamente.

Según las condiciones del problema, dado que hay 9 jugadores en total y al menos uno eligió cada sabor:
1. $c + v + s = 9$
2. $c > v > s \ge 1$

Buscamos todas las ternas de números enteros $(c, v, s)$ que cumplen estas condiciones:

- **Caso 1: $s = 1$**
  Tenemos $c + v = 8$ con $c > v > 1$. Las soluciones posibles para $(c, v)$ son $(6, 2)$ y $(5, 3)$, lo que nos da las ternas:
  - $(c, v, s) = (6, 2, 1)$
  - $(c, v, s) = (5, 3, 1)$

- **Caso 2: $s = 2$**
  Tenemos $c + v = 7$ con $c > v > 2$. La única solución posible para $(c, v)$ es $(4, 3)$, lo que nos da la terna:
  - $(c, v, s) = (4, 3, 2)$

- **Caso 3: $s \ge 3$**
  El valor mínimo posible para la suma sería $3 + 4 + 5 = 12 > 9$, por lo que no hay soluciones en este caso.

Como los 9 jugadores son distintos, el número de formas de asignar los sabores para una terna dada $(c, v, s)$ viene dado por el coeficiente multinomial $\frac{9!}{c! \, v! \, s!}$. Calculamos este valor para cada una de las tres ternas:

1. Para $(6, 2, 1)$:
   $$\frac{9!}{6! \, 2! \, 1!} = \frac{9 \times 8 \times 7}{2 \times 1} = 252$$

2. Para $(5, 3, 1)$:
   $$\frac{9!}{5! \, 3! \, 1!} = \frac{9 \times 8 \times 7 \times 6}{6 \times 1} = 504$$

3. Para $(4, 3, 2)$:
   $$\frac{9!}{4! \, 3! \, 2!} = \frac{9 \times 8 \times 7 \times 6 \times 5}{6 \times 2} = 1260$$

Sumamos los resultados de todos los casos para obtener $N$:
$$N = 252 + 504 + 1260 = 2016$$

Finalmente, calculamos el residuo cuando $N = 2016$ se divide entre $1000$:
$$2016 \equiv 16 \pmod{1000}$$

\boxed{16}