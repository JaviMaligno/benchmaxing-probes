Este es un problema clásico de conjuntos. Vamos a resolverlo paso a paso.

**Datos:**
- Total de estudiantes: 390
- Ninguno de los tres: 20
- Solo cálculo (C), física (F) y química (Q): 20 toman las tres
- Toman cálculo: 200
- El doble toman química que física
- 80 toman cálculo y química
- 80 toman física y química
- 35 toman física y cálculo

**Paso 1: Estudiantes que toman al menos una materia**
```
390 - 20 = 370
```

**Paso 2: Definimos variables**
Sea \( x \) el número de estudiantes que toman química. Entonces física es \( x/2 \).

**Paso 3: Fórmula de inclusión-exclusión**

El total en al menos una materia es:

\[
|C \cup F \cup Q| = |C| + |F| + |Q| - |C \cap F| - |C \cap Q| - |F \cap Q| + |C \cap F \cap Q|
\]

Sustituyendo:

\[
370 = 200 + \frac{x}{2} + x - 35 - 80 - 80 + 20
\]

**Paso 4: Simplificar**

\[
370 = 200 + 1.5x - 175 + 20
\]
\[
370 = 1.5x + 45
\]
\[
325 = 1.5x
\]
\[
x = \frac{325}{1.5} = \frac{650}{3} \approx 216.67
\]

Esto da un número no entero, lo que sugiere que hay un error en mis suposiciones. Volvamos a plantear.

---

**Corrección:** La relación «el doble toman química que física» significa que \( |Q| = 2|F| \), es decir, \( |F| = |Q|/2 \).

Volvamos a usar la fórmula, pero con la definición correcta: sea \( y = |F| \), entonces \( |Q| = 2y \).

\[
370 = 200 + y + 2y - 35 - 80 - 80 + 20
\]
\[
370 = 3y + 25
\]
\[
345 = 3y
\]
\[
y = 115
\]

**Paso 5: Verificación**

- Física: 115
- Química: 230
- Cálculo: 200

Aplicando inclusión-exclusión:

\[
200 + 115 + 230 - 35 - 80 - 80 + 20 = 545 - 175 = 370
\]

✓ Correcto.

**Respuesta: 115 estudiantes toman física.**

\boxed{115}