**Planteamiento.** Un octaedro regular tiene sus 6 vértices en 3 pares de vértices opuestos. Colocándolo con vértices en $(\pm a,0,0)$, $(0,\pm a,0)$, $(0,0,\pm a)$ y tomando $Q=(x,y,z)$, la distancia al vértice $(a,0,0)$ cumple:

$$d^2 = |Q|^2 + a^2 - 2ax, \qquad d'^2 = |Q|^2 + a^2 + 2ax \text{ (vértice opuesto)}$$

Por lo tanto, para **cada par de vértices opuestos**:

$$d^2 + d'^2 = 2|Q|^2 + 2a^2 = \text{constante}$$

**Aplicación.** Los cuadrados de las distancias conocidas son $16, 64, 100, 121, 169$. Busco emparejarlas de modo que dos pares tengan la misma suma:

$$16 + 169 = 185, \qquad 64 + 121 = 185 \checkmark$$

Es decir, los pares $(4,13)$ y $(8,11)$ corresponden a vértices opuestos, y la distancia $10$ queda emparejada con la desconocida $d$:

$$d^2 + 100 = 185 \implies d^2 = 85$$

$$\boxed{\sqrt{85}}$$