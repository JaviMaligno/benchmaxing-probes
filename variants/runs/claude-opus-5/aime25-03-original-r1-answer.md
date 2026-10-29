## Planteamiento

Buscamos ternas $(c, v, s)$ con $c + v + s = 9$, $c > v > s \ge 1$:

- $s=1, v=2, c=6$
- $s=1, v=3, c=5$
- $s=2, v=3, c=4$

(Los demás casos fallan: $(4,4,1)$ y $(3,3,3)$ no son estrictos, $(7,1,1)$ incumple $v>s$.)

## Conteo

Para cada terna, el número de asignaciones a 9 jugadores distintos es el coeficiente multinomial:

$$\frac{9!}{6!\,2!\,1!} = 252$$
$$\frac{9!}{5!\,3!\,1!} = 504$$
$$\frac{9!}{4!\,3!\,2!} = 1260$$

Total: $N = 252 + 504 + 1260 = 2016$.

El resto al dividir entre 1000 es $16$.

\boxed{16}