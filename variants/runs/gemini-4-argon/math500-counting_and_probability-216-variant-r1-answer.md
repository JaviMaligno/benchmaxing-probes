Para determinar de cuántas maneras podemos formar un grupo de trabajo de 5 miembros con al menos un ingeniero y al menos un diseñador, podemos usar el método del complemento: calculamos el número total de formas de elegir a 5 miembros cualesquiera y luego restamos los casos que no cumplen con la condición (es decir, los grupos formados únicamente por ingenieros o únicamente por diseñadores).

1. **Número total de formas de elegir 5 miembros de un total de 15 personas (9 ingenieros + 6 diseñadores):**
   $$\binom{15}{5} = \frac{15 \times 14 \times 13 \times 12 \times 11}{5 \times 4 \times 3 \times 2 \times 1} = 3003$$

2. **Número de formas de elegir solo ingenieros (5 ingenieros y 0 diseñadores):**
   $$\binom{9}{5} = \frac{9 \times 8 \times 7 \times 6}{4 \times 3 \times 2 \times 1} = 126$$

3. **Número de formas de elegir solo diseñadores (0 ingenieros y 5 diseñadores):**
   $$\binom{6}{5} = 6$$

4. **Restamos los casos no válidos del total:**
   $$3003 - 126 - 6 = 2871$$

\boxed{2871}