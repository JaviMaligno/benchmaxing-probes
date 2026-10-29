Para hallar el número de asignaciones de sabores a los $10$ miembros del club de ajedrez, sean $m$, $b$ y $k$ el número de miembros que eligieron mango, banana y kiwi, respectivamente. 

Las condiciones del problema establecen que:
1. $m + b + k = 10$
2. $m > b > k \ge 1$

Buscamos todas las ternas de enteros $(m, b, k)$ que satisfacen ambas condiciones:

- **Si $k = 1$:** Entonces $m + b = 9$ con $m > b > 1$. Las opciones para $(m, b, k)$ son:
  - $(7, 2, 1)$
  - $(6, 3, 1)$
  - $(5, 4, 1)$

- **Si $k = 2$:** Entonces $m + b = 8$ con $m > b > 2$. La única opción para $(m, b, k)$ es:
  - $(5, 3, 2)$

- **Si $k \ge 3$:** La suma mínima posible sería $3 + 4 + 5 = 12 > 10$, por lo que no hay más soluciones.

Dado que los $10$ miembros son distinguibles, para cada terna $(m, b, k)$ el número de asignaciones posibles está dado por el coeficiente multinomial $\frac{10!}{m!\,b!\,k!}$:

1. Para $(7, 2, 1)$:
   $$\frac{10!}{7!\,2!\,1!} = \frac{10 \times 9 \times 8}{2} = 360$$

2. Para $(6, 3, 1)$:
   $$\frac{10!}{6!\,3!\,1!} = \frac{10 \times 9 \times 8 \times 7}{6} = 840$$

3. Para $(5, 4, 1)$:
   $$\frac{10!}{5!\,4!\,1!} = \frac{10 \times 9 \times 8 \times 7 \times 6}{24} = 1260$$

4. Para $(5, 3, 2)$:
   $$\frac{10!}{5!\,3!\,2!} = \frac{10 \times 9 \times 8 \times 7 \times 6}{6 \times 2} = 2520$$

Sumando todos los casos obtenemos el valor total de $N$:
$$N = 360 + 840 + 1260 + 2520 = 4980$$

Finalmente, calculamos el residuo cuando $N$ se divide por $1000$:
$$4980 \equiv 980 \pmod{1000}$$

\boxed{980}