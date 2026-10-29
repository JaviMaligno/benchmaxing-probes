Voy a resolverlo con el principio de inclusión-exclusión.

**Datos:**
- Total de estudiantes: 390, de los cuales 20 no toman ninguna materia, así que 370 toman al menos una.
- Cálculo: $|C| = 200$
- Química: $|Q| = 2|P|$ (el doble que física)
- $|C \cap Q| = 80$, $|P \cap Q| = 80$, $|P \cap C| = 35$
- $|C \cap P \cap Q| = 20$

**Inclusión-exclusión:**

$$|C \cup P \cup Q| = |C| + |P| + |Q| - |C \cap P| - |C \cap Q| - |P \cap Q| + |C \cap P \cap Q|$$

Sustituyendo, con $|P| = x$ y $|Q| = 2x$:

$$370 = 200 + x + 2x - 35 - 80 - 80 + 20$$

$$370 = 25 + 3x$$

$$3x = 345 \implies x = 115$$

**Verificación:** física = 115, química = 230. Entonces $200 + 115 + 230 - 35 - 80 - 80 + 20 = 370$. ✓

$$\boxed{115}$$