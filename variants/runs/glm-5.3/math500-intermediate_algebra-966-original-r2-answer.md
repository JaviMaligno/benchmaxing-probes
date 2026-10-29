## Planteamiento

Queremos minimizar $x^4 + 4y^2 + 4z^4$ con $x, y, z > 0$ y $xyz = 2$.

Hacemos el cambio de variables $u = x^4$, $v = y^2$, $w = z^4$ (todas positivas). La restricción se transforma así:
$$(xyz)^4 = x^4 y^4 z^4 = u \cdot v^2 \cdot w = 2^4 = 16.$$

El objetivo queda $u + 4v + 4w$.

## Aplicación de AM-GM

Escribimos el objetivo como suma de cuatro términos:
$$u + 4v + 4w = u + 2v + 2v + 4w.$$

Por la desigualdad AM-GM:
$$u + 2v + 2v + 4w \ge 4\sqrt[4]{u \cdot 2v \cdot 2v \cdot 4w} = 4\sqrt[4]{16\, u v^2 w} = 4\sqrt[4]{16 \cdot 16} = 4\sqrt[4]{256} = 16.$$

Usamos que $uv^2w = 16$ por la restricción. Por lo tanto, el objetivo es siempre $\ge 16$.

## Verificación de que se alcanza

La igualdad en AM-GM ocurre cuando $u = 2v = 2v = 4w$, es decir:
$$x^4 = 2y^2 = 4z^4.$$

De $x^4 = 2y^2$ y $y^2 = 2z^4$ (que sale de $2v = 4w$), junto con $uv^2w = 16$:
$$u\, v^2\, w = (2v)\cdot v^2 \cdot \tfrac{v}{2} = v^4 = 16 \implies v = 2.$$

Entonces:
- $y^2 = 2 \implies y = \sqrt{2}$
- $x^4 = 4 \implies x = \sqrt{2}$
- $z^4 = 1 \implies z = 1$

Comprobación de la restricción: $xyz = \sqrt{2}\cdot\sqrt{2}\cdot 1 = 2$. ✓

Valor del objetivo: $x^4 + 4y^2 + 4z^4 = 4 + 8 + 4 = 16$. ✓

## Conclusión

El mínimo de $x^4 + 4y^2 + 4z^4$ sujeto a $xyz = 2$ es $16$.

$$\boxed{16}$$