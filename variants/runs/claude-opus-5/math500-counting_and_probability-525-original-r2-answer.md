## Planteamiento

Primero sentamos a las 4 personas que no son Pierre, Rosa ni Thomas. Como las rotaciones se consideran iguales, estas 4 personas se pueden colocar de

$$(4-1)! = 3! = 6 \text{ maneras}$$

## Colocación de los tres restantes

Las 4 personas ya sentadas crean exactamente **4 huecos** entre ellas (uno entre cada par de vecinos consecutivos). Para que ninguno de los tres (Pierre, Rosa, Thomas) quede junto a otro, cada uno debe ocupar un hueco distinto:

- Elegir 3 de los 4 huecos: $\binom{4}{3} = 4$
- Asignar las tres personas a esos huecos: $3! = 6$

## Total

$$6 \times 4 \times 6 = 144$$

\boxed{144}