Para encontrar el número de formas en que podemos formar un subcomité de 5 miembros con al menos un miembro de cada partido, podemos usar el método del complemento: calculamos el número total de formas de elegir 5 miembros sin restricciones y luego restamos los casos en los que todos los miembros pertenecen a un solo partido.

1. **Número total de miembros en el comité:**
   Hay 8 republicanos y 6 demócratas, lo que da un total de $8 + 6 = 14$ miembros.

2. **Número total de subcomités posibles de 5 miembros (sin restricciones):**
   $$\binom{14}{5} = \frac{14 \times 13 \times 12 \times 11 \times 10}{5 \times 4 \times 3 \times 2 \times 1} = 2002$$

3. **Subcomités formados únicamente por republicanos (5 republicanos y 0 demócratas):**
   $$\binom{8}{5} = \frac{8 \times 7 \times 6}{3 \times 2 \times 1} = 56$$

4. **Subcomités formados únicamente por demócratas (0 republicanos y 5 demócratas):**
   $$\binom{6}{5} = 6$$

5. **Subcomités con al menos un miembro de cada partido:**
   Restamos los casos no válidos del total:
   $$2002 - 56 - 6 = 1940$$

\boxed{1940}