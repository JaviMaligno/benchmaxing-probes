## Planteamiento

Sea $h$ la altura de la caverna. Las alturas de las cuatro puntas son:

- Estalactitas: $h-18$ y $h-34$
- Estalagmitas: $25$ y $47$

## Emparejamiento de diagonales

En un cuadrado, las diagonales se bisecan, así que la suma de las ordenadas de los dos vértices opuestos es la misma para ambas diagonales (igual a $2y_{\text{centro}}$). Probamos los tres emparejamientos:

- $\{h-18,\, 25\}$ y $\{h-34,\, 47\}$: $h+7 = h+13$ → imposible.
- $\{h-18,\, 47\}$ y $\{h-34,\, 25\}$: $h+29 = h-9$ → imposible.
- $\{h-18,\, h-34\}$ y $\{25,\, 47\}$: $2h-52 = 72 \Rightarrow h = 62$.

## Verificación

Con $h=62$ las ordenadas son $44,\,28$ (una diagonal) y $25,\,47$ (la otra), con centro en $y=36$. Tomando $p,q$ como los desplazamientos horizontales desde el centro, las semidiagonales son $a=(p,8)$ y $b=(q,-11)$. Las condiciones de cuadrado (perpendicularidad e igual longitud) dan:

$$pq = 88, \qquad p^2 - q^2 = 57$$

De aquí $p^2 - \dfrac{7744}{p^2} = 57 \Rightarrow p^2 = 121$, es decir $p=11$, $q=8$.

Entonces $|a|^2 = 121+64 = 185 = 64+121 = |b|^2$ ✓. El cuadrado existe (lado $\sqrt{370}$), y las cuatro puntas $44,\,28,\,25,\,47$ están dentro del intervalo $(0,62)$.

\boxed{62}