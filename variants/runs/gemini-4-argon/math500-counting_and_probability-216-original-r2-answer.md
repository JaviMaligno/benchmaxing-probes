Para encontrar el número de formas de formar un subcomité de 5 miembros con al menos un miembro de cada partido, podemos calcular primero el número total de formas de elegir 5 miembros sin restricciones y luego restar los casos en los que todos los miembros pertenecen a un solo partido.

1. **Número total de subcomités posibles:**
   En total hay $8 + 6 = 14$ miembros. El número de formas de elegir 5 miembros de un grupo de 14 es:
   $$\binom{14}{5} = \frac{14 \times 13 \times 12 \times 11 \times 10}{5 \times 4 \times 3 \times 2 \times 1} = 2002$$

2. **Subcomités formados únicamente por republicanos (0 demócratas):**
   El número de formas de elegir los 5 miembros de entre los 8 republicanos es:
   $$\binom{8}{5} = \frac{8 \times 7 \times 6}{3 \times 2 \times 1} = 56$$

3. **Subcomités formados únicamente por demócratas (0 republicanos):**
   El número de formas de elegir los 5 miembros de entre los 6 demócratas es:
   $$\binom{6}{5} = 6$$

4. **Subcomités con al menos un miembro de cada partido:**
   Restamos los casos no válidos del total de combinaciones posibles:
   $$2002 - 56 - 6 = 1940$$

\boxed{1940}