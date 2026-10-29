Para encontrar el número de asignaciones posibles $N$, llamemos $m$, $b$ y $k$ al número de miembros que eligieron mango, banana y kiwi, respectivamente.

De acuerdo con el problema, se deben cumplir las siguientes condiciones:
1. $m + b + k = 10$
2. $m > b > k \ge 1$

Primero, determinamos todas las ternas de números enteros $(m, b, k)$ que satisfacen estas condiciones:
- **Si $k = 1$:** entonces $m + b = 9$ con $m > b \ge 2$. Las opciones posibles para $(m, b, k)$ son:
  - $(7, 2, 1)$
  - $(6, 3, 1)$
  - $(5, 4, 1)$
- **Si $k = 2$:** entonces $m + b = 8$ con $m > b \ge 3$. La única opción posible es:
  - $(5, 3, 2)$
- **Si $k \ge 3$:** entonces $b \ge 4$ y $m \ge 5$, por lo que $m + b + k \ge 12$, lo cual excede el total de $10$ miembros.

Ahora, dado que los $10$ miembros del club son distinguibles, el número de maneras de asignar los sabores para una terna fija $(m, b, k)$ viene dado por el coeficiente multinomial $\frac{10!}{m!\,b!\,k!}$:

1. Para $(7, 2, 1)$:
   $$\frac{10!}{7!\,2!\,1!} = \frac{10 \times 9 \times 8}{2} = 360$$

2. Para $(6, 3, 1)$:
   $$\frac{10!}{6!\,3!\,1!} = \frac{10 \times 9 \times 8 \times 7}{6} = 840$$

3. Para $(5, 4, 1)$:
   $$\frac{10!}{5!\,4!\,1!} = \frac{10 \times 9 \times 8 \times 7 \times 6}{24} = 1260$$

4. Para $(5, 3, 2)$:
   $$\frac{10!}{5!\,3!\,2!} = \frac{10 \times 9 \times 8 \times 7 \times 6}{6 \times 2} = 2520$$

Sumamos todos los casos posibles para hallar $N$:
$$N = 360 + 840 + 1260 + 2520 = 4980$$

Finalmente, calculamos el residuo cuando $N$ se divide por $1000$:
$$4980 \equiv 980 \pmod{1000}$$

\boxed{980}