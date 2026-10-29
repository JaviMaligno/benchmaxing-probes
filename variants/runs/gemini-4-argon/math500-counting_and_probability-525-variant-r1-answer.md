Para determinar de cuántas maneras pueden sentarse las $8$ personas alrededor de una mesa redonda de modo que ninguna pareja entre Amara, Bastien y Celine se siente en asientos contiguos, podemos seguir estos pasos:

1. **Sentar primero a las demás personas:**
   De las $8$ personas en total, dejamos aparte a Amara, Bastien y Celine, lo que nos deja con $5$ personas sin restricciones. El número de maneras de sentar a estas $5$ personas alrededor de una mesa circular (considerando iguales las rotaciones) es:
   $$(5 - 1)! = 4! = 24$$

2. **Ubicar a Amara, Bastien y Celine en los espacios disponibles:**
   Una vez que las primeras $5$ personas están sentadas alrededor de la mesa, quedan exactamente $5$ espacios vacíos (uno entre cada par de personas contiguas). Para garantizar que ninguna pareja entre Amara, Bastien y Celine quede junta, cada una de estas $3$ personas debe ocupar un espacio distinto entre los $5$ disponibles.
   - Para Amara hay $5$ espacios posibles.
   - Para Bastien quedan $4$ espacios posibles.
   - Para Celine quedan $3$ espacios posibles.

   El número de formas de asignar estos lugares es:
   $$5 \times 4 \times 3 = 60$$

3. **Calcular el total de disposiciones:**
   Multiplicamos el número de formas de sentar a las primeras $5$ personas por el número de formas de ubicar a las $3$ personas restantes:
   $$24 \times 60 = 1440$$

\boxed{1440}