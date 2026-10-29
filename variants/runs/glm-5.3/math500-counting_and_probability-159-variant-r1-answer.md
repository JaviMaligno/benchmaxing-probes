## Planteamiento

**Paso 1: Agrupar por bloques.**
Como cada partido debe sentarse junto, tratamos a cada grupo como un solo "bloque":
- Bloque G (verdes): 6 personas
- Bloque L (liberales): 4 personas
- Bloque I (independiente): 1 persona

Esto da 3 objetos que hay que acomodar alrededor de una mesa circular.

**Paso 2: Ordenar los bloques en círculo.**
El número de maneras de acomodar 3 objetos distintos en círculo, donde las rotaciones son equivalentes, es:
$$(3-1)! = 2! = 2$$

**Paso 3: Ordenar dentro de cada bloque.**
Los bloques ocupan asientos consecutivos, así que dentro de cada bloque el orden es lineal:
- Verdes: $6! = 720$ maneras
- Liberales: $4! = 24$ maneras
- Independiente: $1$ manera

**Paso 4: Multiplicar.**
$$2 \times 6! \times 4! = 2 \times 720 \times 24 = 34\,560$$

\boxed{34560}