## Planteamiento

**Paso 1: Sentar a las otras 5 personas.**
Fijamos primero a las 5 personas que no son Amara, Bastien ni Celine. Al ser una mesa redonda con rotaciones equivalentes, estas 5 personas se pueden ordenar de

$$(5-1)! = 4! = 24 \text{ maneras.}$$

Esto fija además el marco de referencia (elimina las rotaciones), así que el resto del conteo es lineal.

**Paso 2: Colocar a los 3 restantes en los huecos.**
Las 5 personas ya sentadas crean exactamente **5 huecos** entre personas consecutivas. Si ponemos a Amara, Bastien y Celine en huecos *distintos*, entonces cada uno queda rodeado por dos de las otras 5 personas, por lo que ningún par de ellos queda adyacente. Recíprocamente, si dos de ellos comparten un hueco, quedan juntos.

Entonces hay que elegir 3 huecos de 5 y asignar a las tres personas:

$$\binom{5}{3} \cdot 3! = 10 \cdot 6 = 60 = P(5,3).$$

**Paso 3: Multiplicar.**

$$24 \times 60 = 1440.$$

**Verificación rápida (por complemento):** total sin restricción $= 7! = 5040$. Casos con al menos dos de ellos juntos: pares juntos $3\cdot 2\cdot 6! = 4320$; los tres juntos (contados con inclusión-exclusión) $3!\cdot 5! = 720$ para el bloque de tres, y cada configuración de los tres juntos se cuenta dos veces en la suma de pares. Así, con al menos dos adyacentes $= 4320 - 2\cdot 720 + 720 = 3600$, y $5040 - 3600 = 1440$. ✓

\boxed{1440}