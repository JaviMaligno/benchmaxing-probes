## Razonamiento

**Paso 1: tratar cada partido como un bloque.**
Como todos los miembros de cada partido deben sentarse juntos, los tres grupos (Verdes, Liberales, independiente) forman tres bloques contiguos alrededor de la mesa.

**Paso 2: ordenar los bloques en círculo.**
Al haber 3 bloques y considerar equivalentes las rotaciones, el número de ordenaciones circulares es:

$$(3-1)! = 2! = 2$$

(Las reflexiones **no** se consideran equivalentes, pues solo se identifican rotaciones.)

**Paso 3: ordenar dentro de cada bloque.**
- Verdes: $6! = 720$
- Liberales: $4! = 24$
- Independiente: $1! = 1$

**Paso 4: multiplicar.**

$$2 \times 720 \times 24 \times 1 = 34{,}560$$

No hay sobreconteo adicional, ya que los bloques tienen tamaños distintos y cualquier rotación no trivial de una configuración ya quedó descartada al fijar las posiciones relativas de los bloques.

$$\boxed{34560}$$