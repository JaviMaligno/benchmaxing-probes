Para determinar de cuántas maneras se pueden sentar $8$ personas alrededor de una mesa redonda de modo que ningún par de las $3$ personas (Amara, Bastien y Celine) se siente junto, podemos resolver el problema por pasos ubicando primero al resto de las personas:

1. **Sentar a las otras $5$ personas:**
   Primero sentamos a las $5$ personas restantes alrededor de la mesa redonda. Dado que las rotaciones se consideran iguales, el número de maneras de organizar a estas $5$ personas en círculo es:
   $$(5 - 1)! = 4! = 24$$

2. **Ubicar a Amara, Bastien y Celine en los espacios disponibles:**
   Una vez que las $5$ personas están sentadas, se forman exactamente $5$ espacios (huecos) entre ellas alrededor de la mesa. Para garantizar que Amara, Bastien y Celine no se sienten en asientos contiguos, debemos colocar a cada una de estas $3$ personas en un espacio diferente.
   - Para Amara hay $5$ espacios posibles.
   - Para Bastien quedan $4$ espacios posibles.
   - Para Celine quedan $3$ espacios posibles.

   El número de maneras de ubicar a las $3$ personas en estos espacios es:
   $$5 \times 4 \times 3 = 60$$

3. **Calcular el total de disposiciones:**
   Multiplicamos las formas de sentar a las primeras $5$ personas por las formas de ubicar a las $3$ restantes:
   $$24 \times 60 = 1440$$

\boxed{1440}