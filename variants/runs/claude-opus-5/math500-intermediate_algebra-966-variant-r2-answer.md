## Solución

**Paso 1.** Agrupamos los términos extremos con AM‑GM:
$$a^4 + 9c^4 \ge 2\sqrt{9a^4c^4} = 6a^2c^2.$$

**Paso 2.** Ahora aplicamos AM‑GM a lo que queda:
$$6a^2c^2 + 6b^2 \ge 2\sqrt{36a^2b^2c^2} = 12abc = 12\cdot 3 = 36.$$

**Paso 3.** Verificamos la igualdad. Se requiere $a^4 = 9c^4$ (es decir $a^2 = 3c^2$) y $a^2c^2 = b^2$. De $abc=3$ con $b = ac$ se obtiene $a^2c^2 = 3$, luego $3c^4 = 3$, así que $c = 1$, $a = \sqrt3$, $b = \sqrt3$.

Comprobación: $a^4 + 6b^2 + 9c^4 = 9 + 18 + 9 = 36$.

El mínimo se alcanza, por lo tanto es efectivamente el valor buscado.

\boxed{36}