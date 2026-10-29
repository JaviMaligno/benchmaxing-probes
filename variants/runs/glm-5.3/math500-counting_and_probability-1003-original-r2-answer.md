# Resolución paso a paso

## Paso 1: Plantear las probabilidades del dado

Sean:
- $p$ = probabilidad de la cara $F$ (con $p > \tfrac16$)
- $q$ = probabilidad de la cara opuesta a $F$ (con $q < \tfrac16$)
- Las otras 4 caras tienen probabilidad $\tfrac16$ cada una.

Como la suma total es 1:
$$p + q + 4\cdot\frac16 = 1 \implies p + q = \frac13$$

## Paso 2: Probabilidad de obtener suma 7

Las parejas ordenadas que suman 7 son $(1,6),(6,1),(2,5),(5,2),(3,4),(4,3)$.

Las parejas de caras opuestas del dado son $\{1,6\}$, $\{2,5\}$, $\{3,4\}$. Solo una de ellas es la pareja sesgada $\{F,\, 7-F\}$; las otras dos son "justas".

- Cada pareja justa contribuye: $\frac16\cdot\frac16 + \frac16\cdot\frac16 = \frac{2}{36} = \frac{1}{18}$
- Las dos parejas justas aportan: $\frac{2}{18} = \frac19$
- La pareja sesgada aporta: $pq + qp = 2pq$

Entonces:
$$\frac19 + 2pq = \frac{47}{288}$$

## Paso 3: Resolver para $pq$

$$2pq = \frac{47}{288} - \frac{32}{288} = \frac{15}{288} \implies pq = \frac{15}{576} = \frac{5}{192}$$

## Paso 4: Encontrar $p$ y $q$

Con $p+q = \frac13$ y $pq = \frac{5}{192}$, resolvemos la ecuación cuadrática:
$$t^2 - \frac13 t + \frac{5}{192} = 0$$

Discriminante:
$$\Delta = \frac19 - \frac{20}{192} = \frac{64}{576} - \frac{60}{576} = \frac{4}{576} = \frac{1}{144}$$

$$t = \frac{\frac13 \pm \frac{1}{12}}{2} \implies t = \frac{5}{24} \quad \text{o} \quad t = \frac18$$

## Paso 5: Verificación

- $\frac{5}{24} > \frac{4}{24} = \frac16$ ✓ (esta es $p$)
- $\frac18 = \frac{3}{24} < \frac16$ ✓ (esta es $q$)
- Comprobación: $\frac19 + 2\cdot\frac{5}{24}\cdot\frac18 = \frac{32}{288} + \frac{15}{288} = \frac{47}{288}$ ✓

Por lo tanto $p = \frac{m}{n} = \frac{5}{24}$, con $\gcd(5,24)=1$, así que:
$$m+n = 5 + 24 = \boxed{29}$$