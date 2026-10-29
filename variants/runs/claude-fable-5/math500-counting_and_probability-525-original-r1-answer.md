Para resolverlo, coloco primero a las 4 personas restantes y luego inserto a Pierre, Rosa y Thomas en los huecos.

**Paso 1: Sentar a las otras 4 personas.**
Como las rotaciones se consideran iguales, las 4 personas que no tienen restricción se pueden sentar alrededor de la mesa de $(4-1)! = 3! = 6$ maneras.

**Paso 2: Contar los huecos disponibles.**
Estas 4 personas crean exactamente $4$ huecos entre ellas. Si Pierre, Rosa y Thomas ocupan huecos distintos (a lo sumo una persona por hueco), queda garantizado que ninguno de los tres se sienta junto a otro de los tres, porque siempre habrá al menos una de las otras 4 personas entre ellos.

**Paso 3: Ubicar a Pierre, Rosa y Thomas.**
Hay que elegir 3 de los 4 huecos y asignar a las tres personas en orden, es decir:
$$P(4,3) = 4 \times 3 \times 2 = 24 \text{ maneras.}$$

**Paso 4: Multiplicar.**
$$6 \times 24 = 144.$$

**Verificación rápida:** el total sin restricciones es $6! = 720$, y es razonable que al prohibir adyacencias entre 3 de las 7 personas quede una fracción (un quinto) de los casos.

$$\boxed{144}$$