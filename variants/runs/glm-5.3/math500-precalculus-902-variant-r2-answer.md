## Planteamiento

Coloco el octaedro regular con vértices en $(\pm a,0,0)$, $(0,\pm a,0)$, $(0,0,\pm a)$. Sea $Q=(x,y,z)$ con $r^2=x^2+y^2+z^2$.

**Identidad clave:** la distancia al cuadrado a $(a,0,0)$ es $r^2+a^2-2ax$, y a $(-a,0,0)$ es $r^2+a^2+2ax$. Su suma es $2(r^2+a^2)$, igual para **cada** par de vértices opuestos.

Por lo tanto, las tres parejas de vértices opuestos tienen **la misma suma de distancias al cuadrado**.

## Aplicación

Distancias conocidas: 4, 8, 10, 11, 13 → cuadrados: 16, 64, 100, 121, 169.

El vértice desconocido es opuesto a una de las cinco distancias conocidas $p$; las cuatro restantes deben formar dos parejas con sumas de cuadrados iguales.

- Si $p=10$: quedan 16, 64, 121, 169, y observo $16+169 = 185 = 64+121$. ✓

Entonces la suma común por pareja es $S=185$, formada por $(4,13)$ y $(8,11)$. La pareja restante es $(10, d)$:

$$d^2 + 10^2 = 185 \implies d^2 = 85 \implies d = \sqrt{85}$$

(Los otros casos no dan particiciones con sumas iguales, o dan suma total impar.)

\boxed{\sqrt{85}}