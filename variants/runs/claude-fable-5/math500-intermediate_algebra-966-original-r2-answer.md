Aplico la desigualdad AM-GM, dividiendo los términos de forma que el producto resultante sea una potencia de $xyz$.

**Paso 1: Dividir los términos.** Escribo la expresión como suma de cuatro términos:
$$x^4 + 4y^2 + 4z^4 = x^4 + 2y^2 + 2y^2 + 4z^4.$$

Esta división se elige para que los exponentes de $x$, $y$, $z$ en el producto queden iguales.

**Paso 2: Aplicar AM-GM a los cuatro términos.**
$$x^4 + 2y^2 + 2y^2 + 4z^4 \ge 4\sqrt[4]{x^4 \cdot 2y^2 \cdot 2y^2 \cdot 4z^4} = 4\sqrt[4]{16\,x^4 y^4 z^4}.$$

**Paso 3: Usar la restricción.** Como $xyz = 2$, se tiene $x^4y^4z^4 = (xyz)^4 = 16$, así que
$$4\sqrt[4]{16 \cdot 16} = 4\sqrt[4]{256} = 4 \cdot 4 = 16.$$

**Paso 4: Verificar que la igualdad es alcanzable.** La igualdad en AM-GM requiere $x^4 = 2y^2 = 4z^4$. De ahí $y = x^2/\sqrt{2}$ y $z = x/\sqrt{2}$. Sustituyendo en $xyz = 2$:
$$x \cdot \frac{x^2}{\sqrt 2} \cdot \frac{x}{\sqrt 2} = \frac{x^4}{2} = 2 \implies x^4 = 4 \implies x = \sqrt 2,\ y = \sqrt 2,\ z = 1.$$

Comprobación: $x^4 + 4y^2 + 4z^4 = 4 + 8 + 4 = 16$, y $xyz = \sqrt2\cdot\sqrt2\cdot 1 = 2$. ✓

$$\boxed{16}$$