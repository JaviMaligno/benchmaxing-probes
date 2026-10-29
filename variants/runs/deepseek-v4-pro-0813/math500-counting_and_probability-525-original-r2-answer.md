Vamos a razonar con cuidado.

Primero, al colocar a 7 personas alrededor de una mesa redonda, consideramos los arreglos salvo rotaciones. Podemos fijar a una persona como referencia y ordenar a las otras 6 en los asientos restantes. Hay \(6!\) arreglos totales.

Sin embargo, el requisito es que Pierre, Rosa y Thomas no se sienten junto a ninguno de los otros dos. Es decir, entre ellos debe haber al menos otra persona.

Una forma clara de contarlo es la siguiente:

1. Fijamos a las otras 4 personas alrededor de la mesa redonda. Como en una mesa redonda las rotaciones se consideran iguales, el número de formas de sentar a estas 4 personas es \((4-1)! = 3!\).

2. Estas 4 personas crean 4 huecos entre ellas (los espacios alrededor de la mesa). Queremos colocar a Pierre, Rosa y Thomas en estos huecos, con la condición de que no haya dos de ellos en el mismo hueco. Como hay 4 huecos y deben ocuparse 3 de ellos con una persona cada uno, el número de formas de elegir los huecos es \(\binom{4}{3}\).

3. Una vez elegidos los 3 huecos, distribuimos a Pierre, Rosa y Thomas en ellos. Hay \(3!\) órdenes posibles.

Entonces, el número de arreglos es:

\[
3! \cdot \binom{4}{3} \cdot 3! = 6 \cdot 4 \cdot 6 = 144.
\]

Por lo tanto, la respuesta es:

\[
\boxed{144}
\]