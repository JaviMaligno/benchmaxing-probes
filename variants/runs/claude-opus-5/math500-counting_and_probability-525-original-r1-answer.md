## Planteamiento

Como las rotaciones se consideran iguales, conviene colocar primero a las otras 4 personas y luego insertar a Pierre, Rosa y Thomas en los huecos.

**Paso 1: sentar a las 4 personas restantes.**
Alrededor de la mesa redonda, 4 personas se pueden ordenar de
$$(4-1)! = 3! = 6 \text{ maneras.}$$
Esto fija el "marco" de la mesa y elimina la simetría rotacional.

**Paso 2: ubicar a Pierre, Rosa y Thomas.**
Las 4 personas ya sentadas generan 4 espacios entre ellas (uno entre cada par de vecinos consecutivos). Si dos de los tres nombrados fueran al mismo espacio quedarían juntos, así que cada uno debe ir en un espacio distinto.

- Elegir 3 de los 4 espacios: $\binom{4}{3} = 4$
- Asignar a Pierre, Rosa y Thomas a esos espacios: $3! = 6$

Esto da $4 \cdot 6 = 24$ maneras.

**Paso 3: multiplicar.**
$$6 \cdot 24 = 144$$

**Verificación rápida:** cada espacio recibe a lo sumo una de las tres personas, por lo que entre dos cualesquiera de ellas siempre queda al menos una de las otras cuatro. No hay casos repetidos ni omitidos.

\boxed{144}