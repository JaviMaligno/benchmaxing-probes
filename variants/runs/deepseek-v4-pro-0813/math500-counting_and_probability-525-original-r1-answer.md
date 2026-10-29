Voy a contar los casos.

**1. Total con las 7 personas.**

En una mesa redonda, 7 personas se sientan de \((7-1)! = 6! = 720\) maneras.

**2. Casos en que Pierre y Rosa están juntos.**

Los trato como un bloque: tendríamos 6 elementos (el bloque más las otras 5 personas), es decir \((6-1)! = 5! = 120\). Dentro del bloque, P y R pueden intercambiarse: \(2!\), así que \(120 \cdot 2 = 240\).

Por simetría, son 240 casos para Pierre–Rosa, 240 para Pierre–Thomas y 240 para Rosa–Thomas.

**3. Casos en que los tres están juntos consecutivamente.**

Trato a P, R y T como un bloque: 5 elementos, es decir \(4! = 24\). Dentro del bloque, pueden permutarse de \(3! = 6\) formas, así que \(24 \cdot 6 = 144\).

**4. Casos con dos de los tres juntos, pero no los tres juntos.**

Para cada pareja (por ejemplo, P y R juntos, sin incluir a T):

- Bloque P–R más T más las otras 4 personas: 6 elementos, \(5!\) ordenaciones, y \(2!\) interno: \(120 \cdot 2 = 240\).
- De estos, quitamos los casos en que T queda pegado al bloque, es decir los tres juntos. Contando sobre una línea circular: los tres juntos con el bloque P–R y T pueden estar en dos posiciones relativas, \(2!\) interno del bloque, y \(4!\) para los restantes, lo que da \(2 \cdot 2 \cdot 24 = 96\).
- Entonces, casos con P–R juntos y T separado de ellos: \(240 - 96 = 144\).

**5. Unión de los casos prohibidos.**

Por inclusión-exclusión:

\[
240 + 240 + 240 - 144 - 144 - 144 + 144
\]

Las tres intersecciones de “dos juntos” ya excluyen a la tercera persona; al restarlas eliminamos los casos de tres juntos, pero los quitamos tres veces. Como en realidad los tres juntos son 144, aplicamos la fórmula estándar:

\[
3 \cdot 240 - 3 \cdot 144 + 144 = 720 - 432 + 144 = 432.
\]

**6. Casos válidos.**

\[
720 - 432 = 288.
\]

Por lo tanto, el número de maneras es:

\[
\boxed{288}
\]