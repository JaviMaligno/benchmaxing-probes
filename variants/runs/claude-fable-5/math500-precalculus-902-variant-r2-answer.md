## Solución

**Propiedad clave.** Coloquemos el octaedro regular con centro en el origen y vértices en $(\pm a,0,0)$, $(0,\pm a,0)$, $(0,0,\pm a)$. Para un punto cualquiera $Q=(x,y,z)$, la suma de los cuadrados de las distancias a un **par de vértices opuestos** es siempre la misma. Por ejemplo, para el par $(\pm a,0,0)$:

$$|Q-(a,0,0)|^2+|Q-(-a,0,0)|^2 = 2(x^2+y^2+z^2)+2a^2,$$

y lo mismo se obtiene para los otros dos pares. Es decir, los seis vértices se agrupan en tres pares opuestos con

$$d_1^2+d_2^2 \;=\; d_3^2+d_4^2 \;=\; d_5^2+d_6^2.$$

**Aplicación.** Los cuadrados de las distancias conocidas son $16,\,64,\,100,\,121,\,169$. Buscamos dos pares con la misma suma:

$$16+169 = 185, \qquad 64+121 = 185.$$

Entonces $4$ y $13$ corresponden a un par opuesto, y $8$ y $11$ a otro. El vértice restante es el opuesto al que está a distancia $10$, así que

$$100 + x^2 = 185 \quad\Longrightarrow\quad x^2 = 85 \quad\Longrightarrow\quad x = \sqrt{85}.$$

$$\boxed{\sqrt{85}}$$