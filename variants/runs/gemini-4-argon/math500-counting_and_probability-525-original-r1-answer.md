Para resolver este problema paso a paso:

1. **Sentar a las otras $4$ personas primero:** 
   De las $7$ personas en total, dejamos aparte a Pierre, Rosa y Thomas, y sentamos primero a las $4$ personas restantes alrededor de la mesa redonda. Dado que las disposiciones que son rotaciones entre sí se consideran iguales, el número de formas de sentar a estas $4$ personas en círculo es:
   $$(4 - 1)! = 3! = 6$$

2. **Ubicar los espacios disponibles:**
   Una vez que estas $4$ personas están sentadas alrededor de la mesa, se forman exactamente $4$ espacios entre cada par de personas adyacentes.

3. **Colocar a Pierre, Rosa y Thomas:**
   Para garantizar que ninguna pareja entre Pierre, Rosa y Thomas se siente junta, cada una de estas $3$ personas debe colocarse en un espacio diferente de los $4$ espacios disponibles.
   - La primera persona tiene $4$ opciones de espacio.
   - La segunda persona tiene $3$ opciones restantes.
   - La tercera persona tiene $2$ opciones restantes.
   
   Esto nos da un total de:
   $$4 \times 3 \times 2 = 24 \text{ formas}$$

4. **Calcular el total de disposiciones:**
   Multiplicamos el número de formas de sentar a las primeras $4$ personas por el número de formas de ubicar a Pierre, Rosa y Thomas en los espacios:
   $$6 \times 24 = 144$$

\boxed{144}