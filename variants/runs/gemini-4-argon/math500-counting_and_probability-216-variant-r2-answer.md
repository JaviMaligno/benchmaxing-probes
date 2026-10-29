Para encontrar el número de formas de formar un equipo de trabajo de 5 miembros con al menos un ingeniero y al menos un diseñador, podemos calcular el número total de formas de elegir 5 miembros sin restricciones y restar los casos que no cumplen la condición (es decir, cuando todos son ingenieros o todos son diseñadores).

1. **Número total de personas en el consejo:**
   Hay 9 ingenieros y 6 diseñadores, lo que da un total de $9 + 6 = 15$ personas.

2. **Número total de formas de elegir 5 miembros de 15:**
   $$\binom{15}{5} = \frac{15 \times 14 \times 13 \times 12 \times 11}{5 \times 4 \times 3 \times 2 \times 1} = 3003$$

3. **Casos no válidos:**
   - **Todos los miembros son ingenieros (0 diseñadores):** Elegimos los 5 miembros únicamente entre los 9 ingenieros.
     $$\binom{9}{5} = \frac{9 \times 8 \times 7 \times 6}{4 \times 3 \times 2 \times 1} = 126$$
   - **Todos los miembros son diseñadores (0 ingenieros):** Elegimos los 5 miembros únicamente entre los 6 diseñadores.
     $$\binom{6}{5} = 6$$

4. **Casos válidos (al menos un ingeniero y al menos un diseñador):**
   Restamos los casos no válidos del total:
   $$3003 - 126 - 6 = 2871$$

\boxed{2871}