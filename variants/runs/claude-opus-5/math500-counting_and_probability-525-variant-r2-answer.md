## Planteamiento

Como las rotaciones se consideran iguales, conviene **fijar primero a las 5 personas restantes** y luego colocar a Amara, Bastien y Celine en los huecos.

**Paso 1: sentar a las otras 5 personas**

Alrededor de una mesa redonda, 5 personas se pueden ordenar de
$$(5-1)! = 4! = 24 \text{ maneras.}$$

Al fijar estas 5 posiciones, la simetría rotacional ya queda eliminada.

**Paso 2: identificar los huecos**

Estas 5 personas, dispuestas en círculo, generan exactamente **5 huecos** (uno entre cada par consecutivo).

**Paso 3: colocar a los 3 restantes**

Si dos de los tres estuvieran en el mismo hueco, quedarían adyacentes. Por tanto cada uno debe ir en un hueco distinto, y a lo más uno por hueco. Esto garantiza automáticamente que ningún par de ellos sea vecino.

- Elegir 3 huecos de los 5: $\binom{5}{3} = 10$
- Asignar a Amara, Bastien y Celine a esos huecos: $3! = 6$

$$10 \cdot 6 = 60$$

**Paso 4: multiplicar**

$$24 \cdot 60 = 1440$$

\boxed{1440}