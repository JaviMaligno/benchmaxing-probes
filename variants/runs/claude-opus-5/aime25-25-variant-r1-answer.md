## Planteamiento

Una configuración es una cadena binaria de longitud 17 con nueve 1 (ocupados) y ocho 0 (vacíos). La condición «ningún invitado está sentado junto a dos otros invitados» significa que ningún asiento ocupado tiene ambos vecinos ocupados, es decir: **no puede aparecer el bloque `111`**.

## Conteo

Colocamos los 8 asientos vacíos, que generan 9 huecos (incluidos los extremos). Si $x_i$ es el número de ocupados en el hueco $i$, hay que contar

$$x_1+\cdots+x_9=9,\qquad 0\le x_i\le 2$$

(cada bloque de ocupados consecutivos debe tener a lo sumo 2 asientos).

Esto es el coeficiente de $z^9$ en $(1+z+z^2)^9=\left(\frac{1-z^3}{1-z}\right)^9$:

$$N=\sum_{k\ge 0}(-1)^k\binom{9}{k}\binom{17-3k}{8}$$

- $k=0:\ \binom{17}{8}=24310$
- $k=1:\ -9\binom{14}{8}=-9\cdot 3003=-27027$
- $k=2:\ +36\binom{11}{8}=36\cdot 165=5940$
- $k=3:\ -84\binom{8}{8}=-84$

$$N=24310-27027+5940-84=3139$$

## Resultado

$$3139 \equiv 139 \pmod{1000}$$

\boxed{139}