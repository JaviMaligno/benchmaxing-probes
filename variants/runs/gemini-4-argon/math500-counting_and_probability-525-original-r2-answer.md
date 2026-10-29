Para resolver este problema paso a paso, podemos separar a las $7$ personas en dos grupos: las $3$ personas que no pueden sentarse juntas (Pierre, Rosa y Thomas) y las otras $4$ personas sin restricciones.

**Paso 1: Sentar a las $4$ personas sin restricciones.**
Primero sentamos a las otras $4$ personas alrededor de la mesa redonda. Como las rotaciones se consideran iguales, el número de formas de organizar a $n$ personas en un círculo es $(n-1)!$. Para estas $4$ personas, hay:
$$(4 - 1)! = 3! = 6 \text{ formas.}$$

**Paso 2: Ubicar a Pierre, Rosa y Thomas.**
Una vez que las $4$ personas están sentadas, se forman $4$ espacios vacíos entre ellas alrededor de la mesa. Para asegurarnos de que ninguno de los tres (Pierre, Rosa y Thomas) se siente junto a otro, debemos colocar a cada uno en un espacio diferente.

Como las $4$ personas ya sentadas son distintas, los $4$ espacios entre ellas también son distinguibles:
- Hay $4$ opciones de espacio para Pierre.
- Quedan $3$ opciones de espacio para Rosa.
- Quedan $2$ opciones de espacio para Thomas.

Por lo tanto, el número de formas de ubicar a Pierre, Rosa y Thomas en los espacios es:
$$4 \times 3 \times 2 = 24 \text{ formas.}$$

**Paso 3: Calcular el total de combinaciones.**
Multiplicamos las formas de sentar al primer grupo por las formas de ubicar al segundo grupo:
$$6 \times 24 = 144$$

\boxed{144}