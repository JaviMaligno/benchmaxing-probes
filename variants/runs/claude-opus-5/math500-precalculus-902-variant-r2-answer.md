## Razonamiento

En un octaedro regular los vértices forman tres pares de vértices opuestos. Sea el centro $O$ y el semi-diagonal $a$; los pares opuestos son $\pm a\mathbf{e}_i$.

Para cualquier punto $Q$ con vector posición $\mathbf{q}$ respecto al centro:

$$|\mathbf{q}-a\mathbf{e}_i|^2+|\mathbf{q}+a\mathbf{e}_i|^2 = 2|\mathbf{q}|^2+2a^2$$

Esto **no depende de $i$**: la suma de los cuadrados de las distancias a dos vértices opuestos es la misma para los tres pares.

Los cuadrados de las distancias conocidas son: $16,\,64,\,100,\,121,\,169$, más $x^2$.

Hay que repartirlos en tres pares con igual suma. Buscando entre los conocidos:

$$16+169=185,\qquad 64+121=185$$

Esta es la única coincidencia posible (se verifican todas las demás combinaciones: $16+121=137$, $16+100=116$, $64+100=164$, $100+121=221$, $100+169=269$, $121+169=290$, $16+64=80$, y ninguna admite complemento válido).

Queda entonces el $100$ emparejado con $x^2$:

$$100+x^2=185 \implies x^2=85 \implies x=\sqrt{85}$$

(Coherente: $\sqrt{85}\approx 9.22$.)

$$\boxed{\sqrt{85}}$$