## Razonamiento

Buscamos aplicar AM-GM de modo que el producto de los términos sea potencia de $xyz$.

**Elección de la partición:** dividimos $4y^2$ en dos partes iguales para igualar los exponentes:

$$x^4 + 4y^2 + 4z^4 = x^4 + 2y^2 + 2y^2 + 4z^4$$

**Producto de los cuatro términos:**

$$x^4 \cdot 2y^2 \cdot 2y^2 \cdot 4z^4 = 16\,x^4y^4z^4 = 16(xyz)^4 = 16 \cdot 2^4 = 256$$

**AM-GM con cuatro términos:**

$$\frac{x^4 + 2y^2 + 2y^2 + 4z^4}{4} \ge \sqrt[4]{256} = 4$$

por lo que $x^4 + 4y^2 + 4z^4 \ge 16$.

**Verificación de la igualdad:** se requiere $x^4 = 2y^2 = 4z^4$. Tomando el valor común igual a $4$:

- $x^4 = 4 \Rightarrow x = \sqrt{2}$
- $2y^2 = 4 \Rightarrow y = \sqrt{2}$
- $4z^4 = 4 \Rightarrow z = 1$

Restricción: $xyz = \sqrt{2}\cdot\sqrt{2}\cdot 1 = 2$ ✓

Valor: $4 + 8 + 4 = 16$ ✓

El mínimo se alcanza efectivamente, así que la cota es óptima.

$$\boxed{16}$$