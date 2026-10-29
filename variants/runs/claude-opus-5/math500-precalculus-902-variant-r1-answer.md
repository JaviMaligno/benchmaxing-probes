## Razonamiento

En un octaedro regular, los seis vértices se pueden situar en $(\pm a,0,0)$, $(0,\pm a,0)$, $(0,0,\pm a)$, es decir, forman tres pares de vértices opuestos.

Para un punto $Q=(x,y,z)$ cualquiera y un par opuesto $\pm a\,e_i$:

$$|Q - a e_i|^2 + |Q + a e_i|^2 = 2|Q|^2 + 2a^2$$

Este valor no depende de cuál de los tres ejes se tome. Por tanto, **la suma de los cuadrados de las distancias a dos vértices opuestos es la misma para los tres pares**.

Los cuadrados de las distancias conocidas son:
$$16,\quad 64,\quad 100,\quad 121,\quad 169$$

Hay que emparejarlos de modo que dos pares tengan igual suma (y el sobrante se empareje con la distancia desconocida $d$). Buscando:

$$16 + 169 = 185, \qquad 64 + 121 = 185$$

Es la única coincidencia posible entre los pares disponibles. Queda libre el $100$, así que:

$$100 + d^2 = 185 \;\Longrightarrow\; d^2 = 85 \;\Longrightarrow\; d = \sqrt{85}$$

(Aproximadamente $9{,}22$, valor consistente: con $2|Q|^2+2a^2=185$ existe efectivamente una configuración válida.)

$$\boxed{\sqrt{85}}$$