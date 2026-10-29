Para resolver este problema, primero sentamos a las 4 personas que no tienen restricción y luego colocamos a Pierre, Rosa y Thomas en los huecos entre ellas.

**Paso 1: Sentar a las otras 4 personas.**
Alrededor de una mesa redonda, donde las rotaciones se consideran iguales, 4 personas pueden sentarse de $(4-1)! = 3! = 6$ maneras.

**Paso 2: Colocar a Pierre, Rosa y Thomas en los huecos.**
Entre las 4 personas ya sentadas quedan exactamente 4 huecos (uno entre cada par de vecinos consecutivos). Para que ninguno de los tres esté junto a otro de ellos, cada uno debe ocupar un hueco distinto, y en cada hueco solo puede ir una persona (si dos compartieran un hueco, quedarían adyacentes entre sí).

Elegimos 3 de los 4 huecos y asignamos a las tres personas en orden:
$$4 \times 3 \times 2 = 24 \text{ maneras.}$$

**Paso 3: Multiplicar.**
$$6 \times 24 = 144.$$

Verificación de la condición: al estar cada uno de los tres en un hueco distinto, sus vecinos son siempre personas del grupo de 4, así que la restricción se cumple en todos los casos contados, y todo arreglo válido surge exactamente una vez de esta construcción.

$$\boxed{144}$$