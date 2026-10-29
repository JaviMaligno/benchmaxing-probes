## Planteamiento

Primero cuento el total y luego resto los casos prohibidos mediante inclusión-exclusión.

**Total de arreglos circulares de 7 personas:** $(7-1)! = 720$.

## Inclusión-exclusión sobre los paresproblemáticos

Sean los pares de {Pierre, Rosa, Thomas}: hay $\binom{3}{2}=3$ pares. Llamo $A_i$ al evento "el par $i$ se sienta junto".

**Casos con un par específico junto:** trato ese par como un bloque. Hay entonces 6 unidades alrededor de la mesa: $(6-1)! \cdot 2 = 240$.

**Casos con dos pares específicos juntos:** dos pares cualesquiera comparten siempre una persona (p. ej. P–R y R–T), así que forman un bloque de 3 personas con la persona compartida en el medio: $2$ orientaciones. Con 5 unidades alrededor de la mesa: $(5-1)! \cdot 2 = 48$.

**Los tres pares juntos:** imposible, porque cada persona solo tiene dos vecinos y no puede formarse un triángulo: $0$.

## Cálculo

$$\text{casos con algún par junto} = 3 \cdot 240 - 3 \cdot 48 + 0 = 720 - 144 = 576$$

$$\text{casos válidos} = 720 - 576 = 144$$

## Verificación (conteo directo)

Siento primero a las 4 personas restantes alrededor de la mesa: $(4-1)! = 6$ maneras. Ellas crean $4$ huecos; elijo $3$ de ellos para Pierre, Rosa y Thomas en orden: $\binom{4}{3}\cdot 3! = 24$. Total: $6 \cdot 24 = 144$. ✓

\boxed{144}