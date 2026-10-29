## Planteamiento

Buscamos minimizar $x^4 + 4y^2 + 4z^4$ sujeto a $xyz = 2$.

**Reparto de términos para AM-GM.** Queremos que el producto de los términos dependa solo de $xyz$, es decir, que los exponentes de $x$, $y$, $z$ coincidan. Si tomamos $a$ copias de $x^4$, $b$ de $y^2$ y $c$ de $z^4$, necesitamos $4a = 2b = 4c$; con $a = c = 1$ resulta $b = 2$.

Por eso partimos el término central en dos mitades:
$$x^4 + 4y^2 + 4z^4 = x^4 + 2y^2 + 2y^2 + 4z^4.$$

**Aplicación de AM-GM** a estos cuatro términos positivos:
$$x^4 + 2y^2 + 2y^2 + 4z^4 \ge 4\sqrt[4]{x^4 \cdot 2y^2 \cdot 2y^2 \cdot 4z^4} = 4\sqrt[4]{16\,x^4y^4z^4} = 8\,xyz.$$

Como $xyz = 2$:
$$x^4 + 4y^2 + 4z^4 \ge 8 \cdot 2 = 16.$$

## Verificación de la igualdad

La igualdad requiere $x^4 = 2y^2 = 4z^4$. De $x^4 = 4z^4$ sale $x = \sqrt{2}\,z$, y de $2y^2 = 4z^4$ sale $y = \sqrt{2}\,z^2$. Sustituyendo en la restricción:
$$xyz = \sqrt{2}z \cdot \sqrt{2}z^2 \cdot z = 2z^4 = 2 \implies z = 1.$$

Luego $x = \sqrt{2}$, $y = \sqrt{2}$, $z = 1$, que cumple $xyz = 2$, y el valor es $4 + 8 + 4 = 16$. La cota es alcanzable.

\boxed{16}