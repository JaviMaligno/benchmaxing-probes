Para encontrar el radio de la esfera buscada, ubiquemos el cubo de lado $4$ en un sistema de coordenadas tridimensional centrado en el origen $(0,0,0)$, de modo que el cubo ocupe la región $[-2, 2]^3$.

Las ocho esferas de radio $1$ (diámetro $2$) deben colocarse dentro del cubo de lado $4$. Dado que el lado del cubo es exactamente el doble del diámetro de cada esfera, la única forma de acomodar las ocho esferas sin que se superpongan es ubicar una en cada uno de los ocho octantes. Así, los centros de las ocho esferas se encuentran en los puntos:
$$(\pm 1, \pm 1, \pm 1)$$

En esta configuración, la distancia entre los centros de dos esferas adyacentes (que difieren en una sola coordenada) es $2$, lo cual es igual a la suma de sus radios ($1 + 1 = 2$). Por lo tanto, cada esfera es externamente tangente a exactamente otras tres esferas, cumpliendo la condición del problema.

Buscamos una esfera de radio $r$ que sea externamente tangente a las ocho esferas de radio $1$. Para que sea tangente a todas ellas, la distancia desde su centro hasta cada uno de los ocho puntos $(\pm 1, \pm 1, \pm 1)$ debe ser igual a $r + 1$.

El único punto equidistante a los ocho vértices $(\pm 1, \pm 1, \pm 1)$ es el origen $(0,0,0)$. Calculamos la distancia $d$ desde el origen hasta cualquiera de estos centros:
$$d = \sqrt{(\pm 1)^2 + (\pm 1)^2 + (\pm 1)^2} = \sqrt{1 + 1 + 1} = \sqrt{3}$$

Como la esfera central de radio $r$ y cada esfera de radio $1$ son externamente tangentes, la distancia entre sus centros es la suma de sus radios:
$$r + 1 = \sqrt{3}$$

Despejando $r$, obtenemos:
$$r = \sqrt{3} - 1$$

(Dado que $r = \sqrt{3} - 1 \approx 0.732 < 2$, esta esfera queda completamente contenida dentro del cubo).

\boxed{\sqrt{3}-1}